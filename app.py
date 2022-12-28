from multiprocessing import freeze_support

from src.grpc_server import serve


if __name__ == "__main__":
    freeze_support()
    serve()
