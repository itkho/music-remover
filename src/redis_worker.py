from typing import Optional
import redis
import json

from src.dto.chunk_request import ChunkRequestDTO

class RedisWorker:
    def __init__(self) -> None:
        self.redis = redis.Redis(username="backend", password="password")

    def pop_from_queue(self, queue_name: str, timeout: Optional[int] = None) -> ChunkRequestDTO:
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
            return ChunkRequestDTO(**json.loads(data.decode("utf-8")))

    def publish_to_channel(self, channel_name: str, chunk_request: ChunkRequestDTO) -> None:
        self.redis.publish(channel_name, json.dumps(chunk_request.__dict__))
