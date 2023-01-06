import argparse
from src.logger import logging, init_logger
from multiprocessing import freeze_support

from src.grpc_server import serve


if __name__ == "__main__":
    freeze_support()

    parser = argparse.ArgumentParser(
        prog = "Music remover",
        description = "Remove the music from an audio file",
        epilog = "Run a gRPC server on 'host' and 'port' given, then process one by one the audio files"
    )
    parser.add_argument("--host", help="Host name", required=True)
    parser.add_argument("--port", help="Port number", required=True)
    parser.add_argument("--log_path", help="Logfile's path", default="music-remover.log", required=False)
    parser.add_argument("--log_level", help="Level of logs info", choices=list(logging._levelToName.values()), default="INFO", required=False)
    args = parser.parse_args()

    init_logger(log_path=args.log_path, log_level=args.log_level)

    serve(host=args.host, port=args.port)
