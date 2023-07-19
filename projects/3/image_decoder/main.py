import datetime
import os
import random
import numpy as np
import cv2
import sys
from PyQt6.QtCore import QRect, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QCheckBox, QSlider, \
    QComboBox


class Docs:
    # todo image:
    # r - red       (0 - 255)
    # g - green     (0 - 255)
    # b - blue      (0 - 255)
    # a - alpha     (0 - 100)

    # crop - обрезка (пиксели уменьшаются)
    # 1.
    # ... matrix RGB -> manipulate
    #

    # resize - изменение размера полотна, само изображение сохраняется (пиксели уменьшаются)

    # change quality - изменение качества (пиксели не уменьшаются)

    # reverse

    # change color to black and white (grayscale)

    # find face

    # add another image or figure

    # todo video
    # find face(s)

    # data1 = [
    # [1, 2, 3],
    # [1, 2, 3],
    # [1, 2, 3],
    # [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
    # print(data1)
    # print(data1[:len(data1)//2])

    """
    Сжиматель аватарок для облака.

    input(10 files) -> 1920:1080 (100%) = 3.0 mb
    output(10 files) -> 1920*s_param:1080*s_param (100 * q_param%) = 3.0/N mb
    """
    pass


class OpenCv:
    """Обёртка над библиотекой OpenCV."""

    @staticmethod
    def read_image(file_path: str):
        print("file_path: ", file_path)

        # поиск файла
        file = cv2.samples.findFile(file_path)
        # чтение файла в матрицу(BGR==RGB)
        img = cv2.imread(file)
        return img

    @staticmethod
    def shov_image(img: any):
        cv2.imshow(f"Display window{random.randint(1, 10000)}", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def update_image(img: any, path_to_save_images, prefix_to_images, quality_for_save, is_gray, multiply):
        height, width, channels = img.shape  # (1920, 1080, 3)
        before, after = path_to_save_images.split("-")
        new_file_path = f"{before}-{prefix_to_images}{after}"
        if is_gray:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        multiply_val: float = multiply / 100  # 1.0 = 100%
        img = cv2.resize(img, (int(width * multiply_val), int(height * multiply_val)))
        cv2.imwrite(new_file_path, img, [cv2.IMWRITE_JPEG_QUALITY, quality_for_save])

    class Example:
        @staticmethod
        def read_and_show_image():
            img = cv2.imread(cv2.samples.findFile("src/src.jpg"))
            cv2.imshow("Display window", img)
            cv2.waitKey(0)

        @staticmethod
        def crop_image():
            img = cv2.imread(cv2.samples.findFile("src/src.jpg"))
            height, width, channels = img.shape  # (1920, 1080, 3)
            cv2.imshow("Display window", img)
            cv2.imshow("Display window cropped", img[0:height // 2, 0:width // 2])  # y1:y2, x1:x2
            cv2.imshow("Display window cropped2", img[height // 2:height, width // 2:width])  # y1:y2, x1:x2
            cv2.waitKey(0)

        @staticmethod
        def change_to_gray_image():
            img = cv2.imread(cv2.samples.findFile("src/src.jpg"), cv2.IMREAD_GRAYSCALE)  # в оперативной памяти
            # img2 = cv2.imread(path, cv2.IMREAD_COLOR)
            # image_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  # BGR(RGB) -> GRAY
            cv2.imshow("Display window", img)
            cv2.waitKey(0)

        @staticmethod
        def change_to_bw_image():
            img = cv2.imread(cv2.samples.findFile("src/src.jpg"), cv2.IMREAD_GRAYSCALE)  # в оперативной памяти

            contrast = 90
            image = cv2.threshold(img, contrast, 255, cv2.THRESH_BINARY)[1]
            cv2.imshow("Display window", image)
            cv2.waitKey(0)

        @staticmethod
        def change_quality_image():
            img = cv2.imread(cv2.samples.findFile("src/src.jpg"), cv2.IMREAD_COLOR)
            quality = 70
            cv2.imwrite("src/src_avatar.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, quality])

        @staticmethod
        def resize_image():
            img = cv2.imread(cv2.samples.findFile("src/src.jpg"), cv2.IMREAD_COLOR)
            height, width, channels = img.shape  # (1920, 1080, 3)
            multiply: float = 75 / 100  # 1.0 = 100%
            img2 = cv2.resize(img, (int(width * multiply), int(height * multiply)))
            cv2.imshow("Display img", img)
            cv2.imshow("Display img2", img2)
            cv2.waitKey(0)

        @staticmethod
        def find_face_image():
            src = cv2.imread(cv2.samples.findFile("src/avatars/Tom.jpg"), cv2.IMREAD_COLOR)
            # src = cv2.imread(cv2.samples.findFile("src/avatars/img1.jpeg"), cv2.IMREAD_COLOR)
            img = src.copy()
            height, width, channels = img.shape  # (1920, 1080, 3)
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            haar_cascade = cv2.CascadeClassifier('src/cascadeHaare.xml')
            faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=4)

            def one():
                x, y, w, h = faces_rect[0]  # 381 184 416 416
                multiply_h: int = int(240 * (height / 1920))
                multiply_w: int = int(200 * (width / 1920))  # 1280==70 | 1920==100 | 3840==200 |

                y1 = y - multiply_h
                y2 = y + h + multiply_h
                x1 = x - multiply_w
                x2 = x + w + multiply_w
                print(height, width, channels)
                print(multiply_h, multiply_w)
                print(y1, y2, x1, x2)
                cv2.imshow(
                    "cropped",
                    img[y1:y2, x1:x2]
                )  # y1:y2, x1:x2
                cv2.imshow('face', img)
                cv2.imshow('src', src)
                cv2.waitKey(0)

            def many():
                print("старт обработки")
                index = 0
                for (x, y, w, h) in faces_rect:
                    if w < 50 or h < 50:
                        continue
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    index += 1
                    multiply_h: int = int(240 * (height / 1920))
                    multiply_w: int = int(200 * (width / 1920))  # 1280==70 | 1920==100 | 3840==200 |
                    y1 = y - multiply_h
                    y2 = y + h + multiply_h
                    x1 = x - multiply_w
                    x2 = x + w + multiply_w
                    print(height, width, channels)
                    print(multiply_h, multiply_w)
                    print(y1, y2, x1, x2)
                    cv2.imshow(f"cropped {index}", img[y1:y2, x1:x2])  # y1:y2, x1:x2
                # cv2.imshow(f'src {index}', src)
                cv2.imshow(f'face {index}', img)
                cv2.waitKey(0)

            # one()
            many()

        @staticmethod
        def processing_video():
            # speed: float = 1.0
            # speed: float = 0.5
            speed: float = 2.5
            cap: cv2.VideoCapture = cv2.VideoCapture('src/video.mp4')
            haar_cascade = cv2.CascadeClassifier('src/cascadeHaare.xml')
            while cap.isOpened():
                ok, frame = cap.read()  # читает следующий кадр
                if not ok:
                    break
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
                faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
                for (x, y, w, h) in faces_rect:
                    if w < 20 or h < 20:
                        continue
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.imshow('Frame', frame)
                cv2.imshow('thresh', thresh)
                if cv2.waitKey(int(24 / speed)) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()


class Ui:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.setWindowTitle("Сжиматель")
        self.window.setWindowIcon(QIcon("src/media/icon.ico"))
        self.window.setGeometry(QRect(200, 200, 640, 480))
        self.window.setMinimumSize(640, 480)
        self.window.setMaximumSize(3840, 2160)

        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.label_input = QLabel('Путь к файлам: ')
        self.grid.addWidget(self.label_input, 0, 0)
        self.text_input = QLineEdit("src/input")
        self.grid.addWidget(self.text_input, 1, 0)

        self.label_output = QLabel('Место выхода: ')
        self.grid.addWidget(self.label_output, 0, 1)
        self.text_output = QLineEdit("src/output")
        self.grid.addWidget(self.text_output, 1, 1)

        self.label_prefix = QLabel('Префикс: ')
        self.grid.addWidget(self.label_prefix, 0, 2)
        self.text_prefix = QLineEdit("new_")
        self.grid.addWidget(self.text_prefix, 1, 2)

        self.label_prefix = QLabel('Качество: ')
        self.grid.addWidget(self.label_prefix, 0, 3)
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setMinimum(1)
        self.slider.setMaximum(100)
        self.slider.setValue(100)
        self.slider.setTickInterval(1)
        self.grid.addWidget(self.slider, 1, 3)

        self.label_extensions = QLabel('Расширения: ')
        self.grid.addWidget(self.label_extensions, 0, 4)
        self.text_extensions = QLineEdit("jpg, png, jpeg, bmp")
        self.grid.addWidget(self.text_extensions, 1, 4)

        self.label_extensions = QLabel('Превратить в серый?: ')
        self.grid.addWidget(self.label_extensions, 0, 5)
        self.check_box_gray = QCheckBox()
        self.grid.addWidget(self.check_box_gray, 1, 5)

        self.label_extensions = QLabel('Процент от полотна: ')
        self.grid.addWidget(self.label_extensions, 0, 6)
        self.cb = QComboBox()
        self.cb.addItems(["25", "50", "75", "100"])  # # self.cb.addItem("C")
        self.cb.setCurrentIndex(3)
        self.grid.addWidget(self.cb, 1, 6)

        self.button_start = QPushButton('запустить')
        self.button_start.clicked.connect(self.start_processing)
        self.grid.addWidget(self.button_start, 4, 4)

        self.window.setLayout(self.grid)
        self.window.show()
        self.app.exec()

    def start_processing(self):
        print(f"start_processing {datetime.datetime.now()}")

        path_to_read_images: str = str(self.text_input.text())
        path_to_save_images: str = str(self.text_output.text())
        prefix_to_images: str = str(self.text_prefix.text())
        quality_for_save: int = int(self.slider.value())
        is_gray: bool = bool(self.check_box_gray.isChecked())
        valid_extensions: list[str] = [
            x.strip().lower() for x in str(self.text_extensions.text()).strip().replace(".", "").split(",")
        ]
        multiply: int = int(self.cb.currentText())

        for file in os.listdir(path_to_read_images):
            f_name = file.split('.')
            extension = f_name[-1].lower()
            if extension not in valid_extensions:
                continue
            name = ".".join(f_name[:-1]) + f".{extension}"

            img = OpenCv.read_image(os.path.join(path_to_read_images, name))
            OpenCv.update_image(
                img, path_to_save_images + f"\\{name}", prefix_to_images, quality_for_save, is_gray, multiply
            )


if __name__ == "__main__":
    # ui = Ui()
    OpenCv.Example.processing_video()
