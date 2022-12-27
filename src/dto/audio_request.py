from dataclasses import dataclass

@dataclass
class AudioRequestDTO:
    input_path: str
    output_path: str
    remove_original: bool