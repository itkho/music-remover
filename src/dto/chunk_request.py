from dataclasses import dataclass

@dataclass
class ChunkRequestDTO:
    input_path: str
    output_path: str
    remove_original: bool