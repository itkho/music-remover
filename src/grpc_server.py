import static_ffmpeg
static_ffmpeg.add_paths()

from time import sleep
import json
import os
import grpc
from concurrent import futures

import moubah_pb2
import moubah_pb2_grpc

from src.logger import logging


class MusicRemoverServicer(moubah_pb2_grpc.MusicRemoverServicer):
    def GetProcess(self, request, context):
        return moubah_pb2.Process(id=os.getpid())

    def Ping(self, request, context):
        return moubah_pb2.GenericResponse(succeeded=True)

    def RemoveMusic(self, request, context):
        logging.info(f"Get request for: {request.input_path}")
        # TODO: see if it's still true ⬇️
        # The import has to be local to avoid infinite loop on frozen app
        from src.libs.spleeter import Spleeter
        
        try:
            # TODO: remove the WARNING logs from tensorflow
            Spleeter.remove_music(
                audio_path=request.input_path,
                output_path=request.output_path,
                remove_original=request.remove_original
            )
        except Exception as exc:
            logging.exception("Exception when removing the music")
            return moubah_pb2.GenericResponse(succeeded=False, error=str(exc))
        else:
            logging.debug(f"Done with: {request.input_path}")
            return moubah_pb2.GenericResponse(succeeded=True)


def serve(host: str, port: int):
    # Spleeter's libs are imported here, before running the gRPC server because it takes time to load
    logging.info("Importing libraries...")
    from src.libs.spleeter import Spleeter
    logging.info("Libraries imported!")
    
    # with open("../config.json") as config_file:
    #     config = json.load(config_file)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    moubah_pb2_grpc.add_MusicRemoverServicer_to_server(MusicRemoverServicer(), server)
    server.add_insecure_port(f"{host}:{port}")
    server.start()
    logging.info("Server running...")
    server.wait_for_termination()
