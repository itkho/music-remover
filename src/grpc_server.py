import grpc
from concurrent import futures
from time import sleep
from protobuf import moubah_pb2
from protobuf import moubah_pb2_grpc


class MusicRemoverServicer(moubah_pb2_grpc.MusicRemoverServicer):
    def RemoveMusic(self, request, context):
        print(request)
        print("START")
        print("request.input_path", request.input_path)
        sleep(3)
        print("END")
        return moubah_pb2.GenericResponse(succeeded=True)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    moubah_pb2_grpc.add_MusicRemoverServicer_to_server(MusicRemoverServicer(), server)
    # TODO: use specific port
    server.add_insecure_port('localhost:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()