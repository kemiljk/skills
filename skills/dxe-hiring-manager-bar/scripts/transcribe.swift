// Local file transcription using Apple's on-device Speech API (macOS 26+).
// API reference: https://developer.apple.com/documentation/speech/speechanalyzer
import AVFoundation
import Foundation
import Speech

struct Segment: Encodable {
    let start: Double
    let end: Double
    let text: String
}

struct Transcript: Encodable {
    let engine = "Apple SpeechTranscriber"
    let operatingSystem = ProcessInfo.processInfo.operatingSystemVersionString
    let locale: String
    let elapsedSeconds: Double
    let speakerDiarization = false
    let humanAudioVerified = false
    let segments: [Segment]
}

@main struct Transcribe {
    static func main() async throws {
        guard CommandLine.arguments.count == 3 else {
            throw NSError(domain: "Transcribe", code: 1, userInfo: [NSLocalizedDescriptionKey: "Usage: transcribe INPUT_AUDIO OUTPUT_JSON"])
        }
        guard SpeechTranscriber.isAvailable,
              let locale = await SpeechTranscriber.supportedLocale(equivalentTo: Locale(identifier: "en-US")) else {
            throw NSError(domain: "Transcribe", code: 2, userInfo: [NSLocalizedDescriptionKey: "On-device English SpeechTranscriber is unavailable"])
        }
        let started = Date()
        let transcriber = SpeechTranscriber(locale: locale, transcriptionOptions: [], reportingOptions: [], attributeOptions: [.audioTimeRange])
        if let installation = try await AssetInventory.assetInstallationRequest(supporting: [transcriber]) {
            try await installation.downloadAndInstall()
        }
        let collector = Task { () throws -> [Segment] in
            var segments: [Segment] = []
            for try await result in transcriber.results {
                let start = CMTimeGetSeconds(result.range.start)
                let end = CMTimeGetSeconds(CMTimeRangeGetEnd(result.range))
                let text = String(result.text.characters)
                if start.isFinite && end.isFinite && end >= start && !text.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty {
                    segments.append(Segment(start: start, end: end, text: text))
                }
            }
            return segments
        }
        let analyzer = SpeechAnalyzer(modules: [transcriber])
        do {
            let file = try AVAudioFile(forReading: URL(fileURLWithPath: CommandLine.arguments[1]))
            if let lastSample = try await analyzer.analyzeSequence(from: file) {
                try await analyzer.finalizeAndFinish(through: lastSample)
            } else {
                await analyzer.cancelAndFinishNow()
            }
            let segments = try await collector.value
            guard !segments.isEmpty else {
                throw NSError(domain: "Transcribe", code: 3, userInfo: [NSLocalizedDescriptionKey: "No speech segments returned"])
            }
            let transcript = Transcript(locale: locale.identifier, elapsedSeconds: Date().timeIntervalSince(started), segments: segments)
            let encoder = JSONEncoder()
            encoder.outputFormatting = [.prettyPrinted, .sortedKeys, .withoutEscapingSlashes]
            try encoder.encode(transcript).write(to: URL(fileURLWithPath: CommandLine.arguments[2]), options: .atomic)
            print("Transcribed \(segments.count) segments in \(Int(transcript.elapsedSeconds)) seconds")
        } catch {
            collector.cancel()
            await analyzer.cancelAndFinishNow()
            throw error
        }
    }
}
