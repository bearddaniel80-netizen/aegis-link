from dataclasses import dataclass, field

@dataclass
class FileArtifact:
    output_file: str = ""
    content: list[str] = field(default_factory=list)
    binary: bool = False