type Project = { title: string; href: string; summary: string; contribution: string };

export function ProjectCard({ project }: { project: Project }) {
  return (
    <a href={project.href} className="group block border p-6">
      <h2>{project.title}</h2>
      <div className="hidden opacity-0 group-hover:opacity-100 md:block">
        <p>{project.summary}</p>
        <p>My contribution: {project.contribution}</p>
      </div>
      <div className="md:hidden" aria-hidden="true">{project.title}</div>
    </a>
  );
}
