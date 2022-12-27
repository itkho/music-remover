from typing import Optional
import redis
import json

from dto.audio_request import AudioRequestDTO

class RedisWorker:
    def __init__(self) -> None:
        self.redis = redis.Redis(username="backend", password="password")

    def pop_from_queue(self, queue_name: str, timeout: Optional[int] = None) -> AudioRequestDTO:
        """
        "timeout" in seconds (0 for infinite wait)
        """
        if timeout is None:
            data = self.redis.rpop(queue_name)
            if not data:
                return
        else:
            res = self.redis.brpop(queue_name, timeout=timeout)
            if not res:
                return
            _, data = res
        if data:
            return AudioRequestDTO(**json.loads(data.decode("utf-8")))

    def publish_to_channel(self, channel_name: str, audio_request: AudioRequestDTO) -> None:
        self.redis.publish(channel_name, json.dumps(audio_request.__dict__))
