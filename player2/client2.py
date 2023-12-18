from threading import Thread
from queue import Queue
from socket import *
import cv2
import struct
import numpy as np
from server2 import display_frames


# 定义客户端
class Client:
    def __init__(self, Host, Port, Buf_size):
        # 创建相关socket对象
        self.host = Host
        self.port = Port
        self.buf_size = Buf_size
        self.client_socket = None

        # 缓冲区队列
        self.frame_queue_send = Queue()
        self.frame_queue_rec = Queue()
        # 错误提醒文字
        self.error_text = "Error: "

        self.send_thread = None
        self.rec_thread = None

        self.off = False
        # send_thread.start()

        self.num1 = 0
        self.num2 = 0

    def connect(self):  # socket连接并且开启线程
        self.client_socket.connect((self.host, self.port))

    def send_thread_start(self):
        self.send_thread = Thread(target = self.send_message, daemon = True)
        self.send_thread.start()

    def rec_thread_start(self):
        self.rec_thread = Thread(target = self.receive_message, daemon = True)
        self.rec_thread.start()

    def creat_socket(self):  # 创建socket变量
        self.client_socket = socket(AF_INET, SOCK_STREAM)

    def send_message(self):  # 处理视频传输的函数
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
                self.client_socket.sendall(struct.pack('!I', frame_size))

                # 发送视频帧到服务器
                self.client_socket.sendall(jpeg_data)
                self.num1 += 1
                print(self.num1)
                print('已成功发送一帧')

                if self.off:
                    break

            except Exception as e:
                print('send_message', self.error_text, e)
                break

    def receive_message(self):
        while True:
            try:
                # 首先接收长度信息（4个字节）
                length = self.client_socket.recv(4)
                if not length:
                    break
                frame_length = struct.unpack('!I', length)[0]

                data = b''
                while len(data) < frame_length:
                    # 根据长度信息接收整个帧
                    packet = self.client_socket.recv(self.buf_size)
                    self.num2 += 1
                    print(self.num2)
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

                if self.off:
                    break

            except Exception as e:
                print('receive_message', self.error_text, e)
                break

            # finally:
            #     # 关闭客户端连接
            #     self.client_socket.close()
            #     print("Connection closed.")


if __name__ == '__main__':
    # 服务器地址

    send = Client('192.168.43.133', 1900, 60000)
    send.creat_socket()
    send.connect()
    send.send_thread_start()
    send.rec_thread_start()

    display_thread = Thread(target = display_frames, args = (send.frame_queue_rec, 'client'), daemon = True)
    display_thread.start()
    # # 启动视频传输线程
    # send_thread = Thread(target = send.send_frame)
    # send_thread.start()

    # 打开摄像头
    cap = cv2.VideoCapture(0)

    # 循环读取摄像头视频帧
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)  # 反转画面
        # 将视频帧添加到缓冲区队列
        send.frame_queue_send.put(frame)

        # 显示视频帧
        cv2.imshow("Video", frame)

        # 按q键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 关闭摄像头和客户端连接
    cap.release()
    cv2.destroyAllWindows()
    send.client_socket.close()
