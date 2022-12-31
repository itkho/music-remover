import argparse
from multiprocessing import freeze_support

from src.grpc_server import serve


if __name__ == "__main__":
    freeze_support()
    
    parser = argparse.ArgumentParser(
        prog = "Music remover",
        description = "Remove the music from an audio file",
        epilog = "Run a gRPC server on 'host' and 'port' given, then process one by one the audio files"
    )
    parser.add_argument("-h", "--host", help="Host name", required=True)
    parser.add_argument("-p", "--port", help="Port number", required=True)
    args = parser.parse_args()

    serve(host=args.host, port=args.port)
