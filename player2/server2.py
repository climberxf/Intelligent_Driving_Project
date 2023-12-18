from threading import Thread
from queue import Queue
from socket import *
import cv2
import numpy as np
import struct


# 定义服务端
class Server:
    def __init__(self, host, port, bufsize):
        self.host = host
        self.port = port
        self.bufsize = bufsize
        self.server_socket = None
        # 缓冲区队列
        self.frame_queue_rec = Queue()
        self.frame_queue_send = Queue()
        # 错误提醒文字
        self.error_text = "Error: "

        self.server_socket = None
        self.rec_thread = None
        self.send_thread = None

    def creat_socket(self):
        # 创建套接字并绑定地址
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))

    def rec_thread_start(self, client_socket, client_address):
        self.rec_thread = Thread(target = self.receive_message, args = (client_socket, client_address), daemon = True)
        self.rec_thread.start()

    def send_thread_start(self, client_socket):
        self.send_thread = Thread(target = self.send_message, args = (client_socket,), daemon = True)
        self.send_thread.start()

    def start(self):
        self.server_socket.listen(5)
        print("Server is running...")

    def receive_message(self, client_socket, client_address):
        # print("Connection from ", client_address)
        while True:
            try:
                # 首先接收长度信息（4个字节）
                length = client_socket.recv(4)
                if not length:
                    break
                frame_length = struct.unpack('!I', length)[0]

                data = b''
                while len(data) < frame_length:
                    # 根据长度信息接收整个帧
                    packet = client_socket.recv(self.bufsize)
                    if not packet:
                        break
                    data += packet

                if not data:
                    break

                # 解码图像帧
                frame = np.frombuffer(data, dtype = np.uint8)
                frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

                if frame is not None:
                    # 将图像帧放入队列
                    self.frame_queue_rec.put(frame)
                    self.frame_queue_send.put(frame)
                print('+1')

            except Exception as e:
                print('receive_message', self.error_text, e)
                break

            # finally:
            #     # 关闭客户端连接
            #     client_socket.close()
            #     print("Connection closed.")

    def send_message(self, client_socket):
        while True:
            try:
                # 从缓冲区队列获取视频帧
                frame = self.frame_queue_send.get()

                # 对视频帧进行JPEG编码
                ret, jpeg = cv2.imencode('.jpg', frame)
                if not ret:
                    continue

                # 获取编码后的帧大小
                jpeg_data = jpeg.tobytes()
                frame_size = len(jpeg_data)

                # 发送帧大小信息
                client_socket.sendall(struct.pack('!I', frame_size))

                # 发送视频帧到服务器
                client_socket.sendall(jpeg_data)
                print('已成功发送一帧')

            except Exception as e:
                print('send_message', self.error_text, e)
                break


def display_frames(frame_queue_rec, name):
    try:
        while True:
            if not frame_queue_rec.empty():
                # 从队列中获取视频帧
                frame = frame_queue_rec.get()
                # 显示视频帧
                cv2.imshow(name, frame)
                # 释放帧队列中的帧
                frame_queue_rec.task_done()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print("Error: ", e)


if __name__ == '__main__':
    # 服务器地址
    HOST = '192.168.43.133'
    PORT = 1900
    # 缓冲区大小
    BUFSIZE = 60000

    # 创建ReceiveInfo对象并启动服务器
    receive_info = Server(HOST, PORT, BUFSIZE)
    receive_info.creat_socket()
    receive_info.start()
    # 启动显示视频帧的线程
    display_thread = Thread(target = display_frames, args = (receive_info.frame_queue_rec, 'Video Stream'),
                            daemon = True)
    display_thread.start()

    try:
        while True:
            # 等待客户端连接
            print('waiting')
            cli_socket, cli_address = receive_info.server_socket.accept()
            # print('已连接')

            # 启动处理客户端连接的线程
            receive_info.rec_thread_start(cli_socket, cli_address)
            receive_info.send_thread_start(cli_socket)

    except KeyboardInterrupt:
        print("Server is shutting down...")
    finally:
        # 关闭服务器
        receive_info.server_socket.close()
        print('服务器已经关闭')
        # 等待显示视频帧的线程结束
        display_thread.join()
