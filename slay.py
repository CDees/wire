from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

import base64
import socket
import threading

class rsa_layer:
    def __init__(self):
        random_generator = Random.new().read
        self.private_key = RSA.generate(1024, random_generator)
        self.public_key = self.private_key.publickey().exportKey("PEM")


class recv(threading.Thread):
    def __init__(self, hostname, port, rsa_class, wire_class, slay_class):
        threading.Thread.__init__(self)

        self.hostname = hostname
        self.port = int(port)
        self.rsa_class = rsa_class
        self.wire_class = wire_class
        self.slay_class = slay_class


    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.hostname, self.port))
        self.socket.listen(1)

        connection, address = self.socket.accept()              #waiting for connection ... connect page
        self.capture_public_key = connection.recv(1024)

        while True:
            packet = connection.recv(1024)
            if len(packet) > 0:
                decrypted_packet = self.rsa_class.private_key.decrypt(packet)
                decoded_packet = base64.b64decode(decrypted_packet)

                self.wire_class.wire_text_browser.append(decoded_packet)
                self.slay_class.slay_text_browser.append(str(packet))

class send(threading.Thread):
    def __init__(self, hostname, port, rsa_class, recv_class, wire_class, slay_class):
        threading.Thread.__init__(self)

        self.hostname = hostname
        self.port = int(port)
        self.rsa_class = rsa_class
        self.recv_class = recv_class
        self.wire_class = wire_class
        self.slay_class = slay_class

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.hostname, int(self.port)))
        self.socket.sendall(self.rsa_class.public_key)


    def session_key(self, key):
        self.imported_public_key = RSA.importKey(key)

    def send_message(self):
        packet = self.wire_class.wire_home_message.text()
        encoded_packet = base64.b64encode(packet)
        encrypted_packet = self.imported_public_key.encrypt(encoded_packet, 32)[0]
        self.socket.sendall(str(encrypted_packet))

        self.wire_class.wire_text_browser.append(packet)
        self.slay_class.slay_text_browser.append(str(encrypted_packet))
