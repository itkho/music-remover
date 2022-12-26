from typing import TYPE_CHECKING
from src.redis_worker import RedisWorker

if TYPE_CHECKING:
    from src.dto.chunk_request import ChunkRequestDTO


redis_worker = RedisWorker()


def handle_audio_request(chunk_request: "ChunkRequestDTO"):
    # TODO: see if it's still true ⬇️
    # The import has to be local to avoid infinite loop on frozen app
    from src.libs.spleeter import Spleeter
    
    print(chunk_request.input_path)
    Spleeter.remove_music(
        audio_path=chunk_request.input_path,
        output_path=chunk_request.output_path,
        remove_original=chunk_request.remove_original
    )
    redis_worker.publish_to_channel("audio-chunk:done", chunk_request)


def main():
    while True:
        if chunk_request := redis_worker.pop_from_queue(queue_name="audio-chunk:todo:priority-high"):
            print("handle_audio_request HIGH")
            handle_audio_request(chunk_request)
        else:
            if chunk_request := redis_worker.pop_from_queue(queue_name="audio-chunk:todo:priority-low", timeout=1):
                print("handle_audio_request LOW")
                handle_audio_request(chunk_request)
