# -*- This python file uses the following encoding : utf-8 -*-
import os.path
from datetime import datetime

from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QWidget, QFrame, QLabel, QPushButton, QSizePolicy, QHBoxLayout, QVBoxLayout, QSpacerItem, \
    QGridLayout, QSlider
from PySide6.QtGui import QFont, QCursor, QPixmap, QImage, QScreen
from PySide6.QtCore import QSize, Qt, QRect, QUrl, Signal

from message import Message
import utils


class Bubble(QFrame):
    playButtonClicked = Signal(object)
    STRING_FORMAT_TIME = "%H:%M"

    def __init__(self, message: Message, position: str):
        QFrame.__init__(self)

        self.message = message
        self.position = position
        self.on_left = self.position == "left"

        self.left_style = u".QFrame{border-radius:20px;border-top-left-radius:8px;background-color: rgb(40, 40, 43);}"
        self.right_style = u".QFrame{border-radius:20px;border-top-right-radius:8px;background-color: rgb(14, 14, 15)};"

        self.message_kind = self.message.get_kind()
        self.message_body = self.message.get_body()
        self.message_time = datetime.strftime(self.message.get_created_at(), self.STRING_FORMAT_TIME)
        self.message_received = self.message.get_status()

        self.show_bubble()

    def show_bubble(self):
        if self.message_kind == "text":
            self.show_text_bubble()

        elif self.message_kind == "voice":
            self.show_voice_bubble()

        elif self.message_kind == "image":
            self.show_image_bubble()
            pass

        elif self.message_kind == "document":
            self.show_document_bubble()
            pass
        elif self.message_kind == "video":
            pass

        elif self.message_kind == "audio":
            pass

    def show_text_bubble(self):
        """
        Create text message bubble
        """

        font12 = QFont()
        font12.setPointSize(12)

        # Bubble : background
        self.bubble = QFrame(self)

        # Message Label
        self.message_label = QLabel(self.bubble)
        self.message_label.setObjectName(u"message_label")
        self.message_label.setFont(font12)
        self.message_label.setWordWrap(True)
        self.message_label.setTextInteractionFlags(
            Qt.LinksAccessibleByKeyboard | Qt.LinksAccessibleByMouse | Qt.TextBrowserInteraction | Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse)
        self.message_label.setText(self.message_body)

        label_width = self.message_label.fontMetrics().boundingRect(self.message_label.text()).width()
        self.message_label.setMaximumWidth(400)
        if label_width > self.message_label.maximumWidth():
            self.message_label.setMinimumWidth(self.message_label.maximumWidth())

        if self.on_left:
            self.message_label.setStyleSheet(u"QLabel{color: #ccc;background-color:transparent;padding:4px 4px 0px;}")
        else:
            self.message_label.setStyleSheet(u"QLabel{color: #eee;background-color:transparent;padding:4px 4px 0px;}")

        # Add message label and time
        self.create_time_label(self.bubble, self.message_label)

        # Render the widget

        self.render_bubble(self.bubble)


    def render_bubble(self, bubble):

        size_hint = bubble.sizeHint() + QSize(12, 12)
        self.setMinimumSize(size_hint)
        self.setMaximumSize(size_hint)

        # Small decoration frames
        self.large_ellipse = QFrame(self)
        self.small_ellipse = QFrame(self)

        if self.on_left:
            self.small_ellipse.setGeometry(QRect(0, 0, 8, 8))
            self.small_ellipse.setStyleSheet(u"background-color: rgb(40, 40, 43);border-radius:4px;")
            self.large_ellipse.setGeometry(QRect(5, 6, 14, 14))
            self.large_ellipse.setStyleSheet(u"background-color: rgba(40, 40, 43, 0.7);border-radius:7px;")

            bubble.move(12, 12)
            bubble.setStyleSheet(self.left_style)
        else:
            bubble_width = self.width()

            self.small_ellipse.setGeometry(QRect(bubble_width - 8, 0, 8, 8))
            self.small_ellipse.setStyleSheet(u"background-color: rgb(14, 14, 15);border-radius:4px;")
            self.large_ellipse.setGeometry(QRect(bubble_width - 14 - 5, 6, 14, 14))
            self.large_ellipse.setStyleSheet(u"background-color: rgba(14, 14, 15, 0.7);border-radius:7px;")
            bubble.move(0, 12)
            bubble.setStyleSheet(self.right_style)

        return self

    def create_time_label(self, bubble_widget, message_widget):
        font7 = QFont()
        font7.setPointSize(7)

        font8 = QFont()
        font8.setPointSize(8)

        # Time label
        self.time_label = QLabel()
        self.time_label.setFixedSize(QSize(31, 14))
        self.time_label.setFont(font8)
        self.time_label.setStyleSheet(u"QLabel{color:#555;border-radius:7px;}")
        self.time_label.setText(self.message_time)

        self.time_label_layout = QHBoxLayout()
        self.time_label_layout.setContentsMargins(4, 0, 6, 2)
        self.time_label_layout.setSpacing(3)

        self.time_label_spacer = QSpacerItem(41, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.time_label_layout.addItem(self.time_label_spacer)
        self.time_label_layout.addWidget(self.time_label)

        if not self.on_left:
            self.ticks = QPushButton()
            self.ticks.setFixedSize(QSize(24, 14))
            self.ticks.setFont(font7)
            self.ticks.setStyleSheet(u"image: url(:/cils/cils/cil-check-circle-green.png);"
                                     "background-color:rgba(255,255,255,0.1);border-radius:7px;padding:1px;")
            self.time_label_layout.addWidget(self.ticks)
            if not self.message_received :
                self.ticks.setObjectName(f"error_{self.message.get_id()}")

        self.vertical_layout = QVBoxLayout(bubble_widget)
        self.vertical_layout.setSpacing(2)
        self.vertical_layout.setObjectName(u"verticalLayout_22")

        self.vertical_layout.setContentsMargins(2, 2, 2, 0)

        self.vertical_layout.addWidget(message_widget)
        self.vertical_layout.addLayout(self.time_label_layout)


    def show_voice_bubble(self):

        # Bubble background
        self.voice_bubble = QFrame(self)
        self.voice_bubble.setFixedSize(304, 96)

        # Frame
        self.arv_bubble = QFrame(self.voice_bubble)
        self.arv_bubble.setObjectName(u"arv_bubble")
        self.arv_bubble.setFixedSize(QSize(300, 70))
        self.arv_bubble.setStyleSheet(u"QFrame{background-color:#88FFFFFF;border-radius:10px;}")

        # Voice note title
        path = self.message_body
        filename = os.path.splitext(os.path.basename(path))[0] + ".arv"

        self.title = QLabel(self.arv_bubble)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(52, 3, 241, 20))
        self.title.setStyleSheet(u"QLabel{	background:#44FFFFFF;color:#000;}")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.title.setText(filename)
        self.title.setObjectName(f"path|{path}")

        # Time indicators
        self.elapsed_time = QLabel(self.arv_bubble)
        self.elapsed_time.setObjectName(u"elapsed_time")
        self.elapsed_time.setGeometry(QRect(52, 49, 51, 16))
        self.elapsed_time.setStyleSheet(u"QLabel{background:#44FFFFFF;color:#333;border-radius:8px;}")
        self.elapsed_time.setAlignment(Qt.AlignCenter)
        self.elapsed_time.setText("00:00")

        self.total_time = QLabel(self.arv_bubble)
        self.total_time.setObjectName(u"total_time")
        self.total_time.setGeometry(QRect(241, 49, 51, 16))
        self.total_time.setStyleSheet(u"QLabel{background:#44FFFFFF;color:#333;border-radius:8px;}")
        self.total_time.setAlignment(Qt.AlignCenter)
        self.total_time.setText("--:--")

        # Slider -> progress bar
        self.slider = QSlider(self.arv_bubble)
        self.slider.setObjectName(u"slider")
        self.slider.setGeometry(QRect(52, 30, 241, 12))
        self.slider.setStyleSheet(u"""QSlider{
            background:none;}
    
        QSlider::groove:horizontal{ 
            height:4px;
            border:none;}
        
        QSlider::handle:horizontal{
            height:12px;
            width:12px;
            border-radius:6px;
            margin:-4px 0px -4px 0px;
            background-color: rgba(0, 121, 215, 255);}
            
        QSlider::handle:hover{
            background-color: rgba(0, 52, 93, 255);}
        
        QSlider::handle:pressed{
            background-color: rgba(0, 121, 215, 255);}
        
        QSlider::add-page:horizontal{
            background-color:#55FFFFFF;}
        
        QSlider::sub-page:horizontal{
            background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
            stop:0 rgba(0, 52, 93, 255), stop:1 rgba(0, 121, 215, 255));}""")

        self.slider.setMaximum(100)
        self.slider.setValue(0)
        self.slider.setOrientation(Qt.Horizontal)

        self.play_button = QPushButton(self.arv_bubble)
        # self.play_button.setObjectName(u"play_button")
        self.play_button.setGeometry(QRect(7, 16, 41, 41))
        self.play_button.setStyleSheet(u"QPushButton{\n"
                                       "	background-image: url(:/cils/cils/cil-media-play.png);\n"
                                       "	background-repeat: no-repeat;\n"
                                       "	background-position:center;\n"
                                       "	border-radius:6px;\n"
                                       "	border:none;\n"
                                       "}\n"
                                       "QPushButton::hover{\n"
                                       "    border:1px inset rgba(255, 255, 255, 0.6);\n"
                                       "}\n"
                                       "        \n"
                                       "QPushButton::pressed{\n"
                                       "     border:2px inset rgba(255, 255, 255, 1);\n"
                                       "}")


        self.play_button.clicked.connect(self.play)

        # Add message label and time
        self.create_time_label(self.voice_bubble, self.arv_bubble)

        # Add frame on the widget
        self.render_bubble(self.voice_bubble)

    def play(self):
        btn = self.sender()
        self.playButtonClicked.emit(btn)

    def show_document_bubble(self):

        self.document_bubble = QFrame(self)
        self.document_bubble.setObjectName(u"document_bubble")
        self.document_bubble.setGeometry(0, 0, 181, 71)
        self.document_bubble.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.document = QFrame(self.document_bubble)
        self.document.setObjectName(u"document")
        self.document.setStyleSheet(u".QFrame{background-color:#88FFFFFF;border-radius:10px;}")
        self.horizontalLayout_23 = QHBoxLayout(self.document)
        self.horizontalLayout_23.setSpacing(6)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(9, 6, 9, 6)
        self.document_icon = QLabel(self.document)
        self.document_icon.setObjectName(u"document_icon")
        self.document_icon.setMinimumSize(QSize(40, 50))
        self.document_icon.setMaximumSize(QSize(40, 50))
        font9 = QFont()
        font9.setPointSize(6)
        font9.setBold(True)
        self.document_icon.setFont(font9)
        self.document_icon.setStyleSheet(u"QLabel{background-color: #bbb;border-radius:4px;color:#000;"
                                         "image: url(:/cils/cils/blacks/cil-file.png);}")
        self.document_icon.setAlignment(Qt.AlignCenter)
        self.document_icon.setTextInteractionFlags(Qt.TextSelectableByMouse)

        path = self.message_body
        extension = os.path.splitext(path)[1][1:]
        self.document_icon.setText(extension.upper())

        self.horizontalLayout_23.addWidget(self.document_icon)

        self.document_title_size_layout = QVBoxLayout()
        self.document_title_size_layout.setSpacing(0)
        self.document_title_size_layout.setObjectName(u"document_title_size_layout")

        self.document_title = QLabel(self.document)
        self.document_title.setObjectName(u"document_title")
        font6 = QFont()
        font6.setBold(True)
        self.document_title.setFont(font6)
        self.document_title.setStyleSheet(u"QLabel{\n"
                                          "    color:#000;\n"
                                          "background-color:transparent;\n"
                                          "}")
        self.document_title.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.document_title.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.document_title.setText(os.path.basename(path))

        self.document_title_size_layout.addWidget(self.document_title)

        self.document_size = QLabel(self.document)
        self.document_size.setObjectName(u"document_size")
        self.document_size.setStyleSheet(u"QLabel{background:transparent;color:#333;}")
        self.document_size.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.document_size.setTextInteractionFlags(Qt.TextSelectableByMouse)
        size = round((os.path.getsize(path) / 1024 / 1024), 2)
        self.document_size.setText(f"{size} Mb")

        self.document_title_size_layout.addWidget(self.document_size)

        self.horizontalLayout_23.addLayout(self.document_title_size_layout)

        # Add message label and time
        self.create_time_label(self.document_bubble, self.document)

        # Add frame on the widget
        self.render_bubble(self.document_bubble)

    def show_image_bubble(self):
        font10 = QFont()
        font10.setBold(False)

        # Collect image metadata
        path = self.message.get_body()
        filename = os.path.basename(path)
        size = round((os.path.getsize(path) / 1024 / 1024), 2)  # Size in Mb

        image = QImage(path).scaledToWidth(280)
        pixmap = utils.create_rounded_image(path, image.width(), image.height(), radius=10)

        # Global bubble
        self.image_bubble = QFrame(self)
        self.image_bubble.setObjectName(u"image_bubble")
        self.image_bubble.setGeometry(QRect(17, 17, image.width(), image.height()))
        # self.image_bubble.setMaximumWidth(image.width())

        # Label displaying image
        self.image = QLabel(self.image_bubble)
        self.image.setFont(font10)
        self.image.setStyleSheet(f"border-radius:10px;color:#000;padding:2px;")
        self.image.setPixmap(pixmap)
        self.image.setScaledContents(True)

        # Label displaying image name and size
        self.image_info = QLabel(self.image_bubble)
        self.image_info.setGeometry(QRect(9, 6, 270, 20))
        self.image_info.setStyleSheet(u"background-color:transparent;")
        self.image_info.setText(f"<p><span style='color:#848484;'>{size} Mb</span> • {filename}</p>")
        self.image_info.setTextInteractionFlags(Qt.TextSelectableByMouse)

        # Add message label and time
        self.create_time_label(self.image_bubble, self.image)

        # Add frame on the widget
        self.render_bubble(self.image_bubble)

    def show_video_bubble(self):
        # Collect image metadata
        path = self.message.get_body()
        filename = os.path.basename(path)
        size = round((os.path.getsize(path) / 1024 / 1024), 2)

        # Global bubble
        self.video_bubble = QFrame(self)
        self.video_bubble.setObjectName(u"image_bubble")
        self.video_bubble.setGeometry(QRect(17, 17, 191, 201))
        self.video_bubble.setMaximumWidth(280)
        if self.on_left:
            self.video_bubble.setStyleSheet(self.left_style)
        else:
            self.video_bubble.setStyleSheet(self.right_style)

        self.video = QVideoWidget()
        self.video.setMinimumSize(280, 160)
        self.video.setMaximumSize(280, 160)
        self.video.setStyleSheet(u"border-radius:10px;")
        self.video.setFullScreen(True)

        self.audio_output = QAudioOutput()

        self.player = QMediaPlayer()
        self.player.setSource(QUrl.fromLocalFile(path))
        self.player.setVideoOutput(self.video)
        self.player.setAudioOutput(self.audio_output)
        # self.player.play()


        # Add message label and time
        self.create_time_label(self.video_bubble, self.video)

        # Add frame on the widget
        self.render_bubble()

    def show_audio_bubble(self):
        pass