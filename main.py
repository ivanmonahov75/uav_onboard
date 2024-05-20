import comm
import cv2
import socket
import numpy as  np
if __name__ == '__main__':
    img = cv2.imread('img_new.jpg')
    img = cv2.imencode('.jpg', img)[1]
    while 1:
        socket_client = socket.socket()
        socket_client.connect(('192.168.1.58', 8080))
        socket_client.send(int.to_bytes(len(img), 4, 'little'))
        socket_client.send(img.tobytes())