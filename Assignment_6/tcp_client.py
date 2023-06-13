import socket
import json


class TCPclient():
    def __init__(self, sms):
        self.target_ip = 'localhost'
        self.target_port = 9998
        self.input_checking(sms)

    def client_runner(self):

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.target_ip, self.target_port))

        # client.send(self.client_sms)
        #
        #     received_from_server = client.recv(4096)
        #
        #     recv_sms = received_from_server.decode("utf-8")
        #
        #     print("$:", recv_sms)
        #
        #     client.close()
        return client  # to send and received data

    def input_checking(self, sms):
        if sms == "gad":
            self.get_all_data(sms)

        elif sms == "login":
            self.login(sms)

        elif sms == "reg":
            self.register(sms)
        else:
            print("Invalid Option")

    def get_all_data(self, sms):
        client = self.client_runner()
        sms = bytes(sms, "utf-8")
        client.send(sms)
        received_from_server = client.recv(4096)
        # print(received_from_server.decode("utf-8"))

        dict_data: dict = json.loads(received_from_server.decode("utf-8"))
        print(type(dict_data))
        print(dict_data)
        client.close()

    def login(self, info):
        try:
            print("This is login Form")
            l_email = input("Enter your email to login:")
            l_pass = input("Enter your password to login:")

            client = self.client_runner()
            sms = info + ' ' + l_email + ' ' + l_pass  # login email password
            sms = bytes(sms, "utf-8")
            client.send(sms)
            received_from_server = client.recv(4096)
            print(received_from_server.decode("utf-8"))
            client.close()

        except Exception as err:
            print(err)

    def register(self, info):

        print("This is registration option ")
        try:
            r_name = input("Please Enter Your Name to Register :")
            r_email = input("Please Enter Email to Register :")
            r_password = input("Please Enter Password to Register :")
            r_phone = input("Please Enter Phone number to Register :")

            client = self.client_runner()
            cmd = info + ' ' + r_name + ' ' + r_email + ' ' + r_password + ' ' + r_phone
            cmd = bytes(cmd, 'utf_8')
            client.send(cmd)

            received_from_server = client.recv(4096)
            received_data = received_from_server.decode('utf-8')

            if received_data == "success":
                print("Registration Success!")
                self.login("login")
            else:
                print(received_data)
                self.register(info)
            client.close()

        except Exception as err:
            print(err)


if __name__ == "__main__":
    while True:
        sms = input("Enter some data to send:")
        tcp_client = TCPclient(sms)
