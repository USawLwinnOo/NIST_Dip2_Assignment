import socket


class TCPserver():
    def __init__(self):
        self.server_ip = 'localhost'
        self.server_port = 9998
        self.toSave = {}

    def main(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.server_ip, self.server_port))
        server.listen()
        print("Server listen on port:{} and ip {}".format(self.server_port, self.server_ip))
        try:
            while True:
                client, address = server.accept()
                print("Accepted Connection from - {} : {} ".format(address[0], address[1]))
                self.handle_client(client)
        except Exception as err:
            print(err)

    def handle_client(self, client_socket):
        with client_socket as sock:
            from_client = sock.recv(1024)
            received_data = from_client.decode("utf-8")

            try:
                if received_data == "gad":
                    print("All Data in Server")
                    print("*****************\n", self.toSave)
                    print("*****************")

                else:
                    print("Received Data From Client:", received_data)
                    self.toSave.update({len(self.toSave): received_data})

            except Exception as err:
                print(err)
            message = "server got it:>" + received_data
            to_send = bytes(message, 'utf-8')
            sock.send(to_send)


if __name__ == '__main__':
    tcpserver = TCPserver()
    tcpserver.main()
