import sys
from UI.ui_player1 import *
from client2 import *
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QImage, QPixmap
import cv2

'''
目前功能：实现摄像头拍摄能在ui窗口上播放,并且传给服务器，服务器再传回视频并在ui上播放
目前问题：停止后再次开启会无响应，客户端会主动断开
'''


# 注意此处所选的父类要和刚开始创建的一样
class MainWindow(QWidget):
    def __init__(self, host, port, buf_size):
        super().__init__()
        self.ui = Ui_app()
        self.ui.setupUi(self)
        self.ui.set_text('欢迎进入路况智能识别系统')  # 文本提示框设置

        self.host = host
        self.port = port
        self.buf_size = buf_size

        self.camera = cv2.VideoCapture(0)  # 打开摄像头
        self.timer = QTimer()

        self.ui.button1.clicked.connect(self.start_app)
        self.ui.button2.clicked.connect(self.stop_app)

        # self.client = None
        self.client = Client(self.host, self.port, self.buf_size)

    def update_frame(self):
        ret, frame = self.camera.read()  # 读取摄像头画面
        if ret:
            flipped_frame = cv2.flip(frame, 1)  # 反转画面

            # 进行画面传送
            self.client.frame_queue_send.put(flipped_frame)
            frame1 = self.client.frame_queue_rec.get()
            # 将OpenCV图像转换为PyQt图像
            qt_image = frame_trans(flipped_frame)
            qt_image1 = frame_trans(frame1)
            # 在QLabel上显示图像
            self.ui.vedio_label1.setPixmap(QPixmap.fromImage(qt_image))
            self.ui.vedio_label2.setPixmap(QPixmap.fromImage(qt_image1))

    def start_app(self):
        # self.client = Client(self.host, self.port, self.buf_size)
        self.client.off = False
        self.client.creat_socket()  # 每次开始都会启动新的socket还有发送的线程
        self.client.connect()
        self.client.send_thread_start()
        self.client.rec_thread_start()

        self.timer.start(10)  # 更新帧率为每秒30帧
        self.timer.timeout.connect(self.update_frame)
        self.ui.set_text('正在进行路况识别')

    def stop_app(self):
        self.camera.release()
        self.timer.stop()
        self.timer.timeout.disconnect(self.update_frame())
        self.ui.vedio_label1.clear()  # 清空标签上显示的图像
        self.ui.vedio_label2.clear()  # 清空标签上显示的图像
        self.client.client_socket.close()
        self.client.off = True
        self.ui.set_text('系统已关闭')


def frame_trans(fra):#将图像帧转换为能在ui上显示
    rgb_image = cv2.cvtColor(fra, cv2.COLOR_BGR2RGB)
    h, w, ch = rgb_image.shape
    bytes_per_line = ch * w
    qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
    return qt_image


if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = MainWindow('192.168.43.133', 1900, 60000)
    player.show()
    sys.exit(app.exec_())
