# -*- This python file uses the following encoding : utf-8 -*-
import os.path
from datetime import datetime


from PySide6.QtWidgets import QWidget, QFrame, QLabel, QPushButton, QSizePolicy, QHBoxLayout, QVBoxLayout, QSpacerItem, \
    QGridLayout, QSlider
from PySide6.QtGui import QFont, QCursor    
from PySide6.QtCore import QSize, Qt, QRect

from message import Message
import utils


class Bubble(QWidget):

    STRING_FORMAT_TIME = "%H:%M"

    def __init__(self, message: Message, position: str):
        QWidget.__init__(self)

        self.message = message
        self.position = position
        self.on_left = self.position == "left"

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

        elif self.message_kind == "document":
            self.show_document_bubble()

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

        # Labels container
        # self.bubble_frame = QWidget(self)
        # self.bubble_frame.setStyleSheet(u"background-color:rgba(255,255,255,0.1);")
        # self.bubble_frame.setMinimumSize(QSize(100, 71))
        # self.bubble_frame.setMaximumSize(QSize(316, 120))
        # self.bubble_frame.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)


        # Bubble : background
        self.bubble = QFrame(self)
        self.bubble.setMaximumWidth(316)
        self.bubble.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)

        left_style = u"border-radius:20px;border-top-left-radius:8px;background-color: rgb(40, 40, 43);"
        right_style = u"border-radius:20px;border-top-right-radius:8px;background-color: rgb(14, 14, 15);"

        if self.on_left:
            # self.bubble.move(17, 17)
            self.bubble.setStyleSheet(left_style)
        else:
            # self.bubble.move(-17, -17)
            self.bubble.setStyleSheet(right_style)

        # Message Label
        self.message_label = QLabel(self.bubble)
        self.message_label.setObjectName(u"message_label")
        self.message_label.setFont(font12)
        self.message_label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.message_label.setWordWrap(True)
        self.message_label.setTextInteractionFlags(
            Qt.LinksAccessibleByKeyboard | Qt.LinksAccessibleByMouse | Qt.TextBrowserInteraction | Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse)
        self.message_label.setText(self.message_body)

        if self.on_left:
            self.message_label.setStyleSheet(u"QLabel{color: #ccc;background-color:transparent;}")
        else:
            self.message_label.setStyleSheet(u"QLabel{color: #eee;background-color:transparent;}")

        # Add message label and time
        self.create_time_label(self.bubble, self.message_label)

        # Add frame on the widget
        self.add_widget(self.bubble)

    def create_small_decorators(self, widget):
        # Small decoration frames
        self.frame = QFrame(widget)
        if self.on_left:
            self.frame.setGeometry(QRect(10, 10, 14, 14))
            self.frame.setStyleSheet(u"background-color: rgba(40, 40, 43, 0.7);border-radius:7px;")
        else:
            self.frame.setGeometry(QRect(134, 8, 14, 14))
            self.frame.setStyleSheet(u"background-color: rgba(14, 14, 15, 0.7);border-radius:7px;")

        self.frame_2 = QFrame(widget)
        if self.on_left:
            self.frame_2.setGeometry(QRect(5, 4, 8, 8))
            self.frame_2.setStyleSheet(u"background-color: rgb(40, 40, 43);border-radius:4px;")
        else:
            self.frame_2.setGeometry(QRect(145, 2, 8, 8))
            self.frame_2.setStyleSheet(u"background-color: rgb(14, 14, 15);border-radius:4px;")

    def add_widget(self, widget):
        # Show small decorators
        # self.create_small_decorators(widget)

        # Add time on the widget

        # Add the bubble container on the main widget
        self.horizontalLayout_11 = QHBoxLayout(self)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.spacer = QSpacerItem(500, 2, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        if self.on_left:
            self.horizontalLayout_11.addWidget(widget)
            self.horizontalLayout_11.addItem(self.spacer)
        else:
            self.horizontalLayout_11.addItem(self.spacer)
            self.horizontalLayout_11.addWidget(widget)

    def create_time_label(self, parent, time_buddy):
        font7 = QFont()
        font7.setPointSize(7)

        font8 = QFont()
        font8.setPointSize(8)

        # Time label
        self.time_label = QLabel(parent)
        self.time_label.setFixedSize(QSize(31, 14))
        self.time_label.setFont(font8)
        self.time_label.setStyleSheet(u"QLabel{color:#555;border-radius:7px;}")
        self.time_label.setText(self.message_time)

        self.time_label_layout = QHBoxLayout()
        self.time_label_layout.setSpacing(3)

        self.time_label_spacer = QSpacerItem(41, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.time_label_layout.addItem(self.time_label_spacer)
        self.time_label_layout.addWidget(self.time_label)

        if not self.on_left:
            self.ticks = QLabel(parent)
            self.ticks.setFixedSize(QSize(24, 14))
            self.ticks.setFont(font7)
            self.ticks.setStyleSheet(u"image: url(:/cils/cils/cil-check-circle-green.png);\n"
                                     "background-color:rgba(255,255,255,0.1);border-radius:7px;padding:1px;")
            self.time_label_layout.addWidget(self.ticks)

        self.verticalLayout_22 = QVBoxLayout(parent)
        self.verticalLayout_22.setSpacing(2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")

        if self.message_kind == "text":
            self.verticalLayout_22.setContentsMargins(12, 6, 12, 0)
        else:
            self.verticalLayout_22.setContentsMargins(2, 2, 2, 0)

        self.verticalLayout_22.addWidget(time_buddy)
        self.verticalLayout_22.addLayout(self.time_label_layout)


    def show_voice_bubble(self):
        # self.voice_bubble_frame = QFrame(self)
        # self.voice_bubble_frame.setObjectName(u"voice_bubble_frame")
        # self.voice_bubble_frame.setFixedSize(QSize(320, 111))


        self.voice_bubble = QFrame(self)
        self.voice_bubble.setObjectName(u"frame_12")
        self.voice_bubble.setGeometry(QRect(17, 17, 304, 91))
        self.voice_bubble.setMaximumSize(QSize(304, 16777215))
        self.voice_bubble.setStyleSheet(u"	border-radius:10px;\n"
                                    "	border-top-left-radius:8px;\n"
                                    "	background-color: rgb(40, 40, 43);\n"
                                    "")

        self.arv_bubble = QFrame(self.voice_bubble)
        self.arv_bubble.setObjectName(u"arv_bubble")
        self.arv_bubble.setMinimumSize(QSize(300, 70))
        self.arv_bubble.setMaximumSize(QSize(300, 70))
        self.arv_bubble.setStyleSheet(u"QFrame{\n"
                                      "	background-color:#88FFFFFF;\n"
                                      "	border-radius:10px;\n"
                                      "\n"
                                      "}")


        self.title = QLabel(self.arv_bubble)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(52, 3, 241, 20))
        self.title.setStyleSheet(u"QLabel{	background:#44FFFFFF;color:#000;}")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setTextInteractionFlags(Qt.TextSelectableByMouse)

        path = self.message_body
        filename = os.path.splitext(os.path.basename(path))[0] + ".arv"
        self.title.setText(filename)
        self.title.setObjectName(f"path|{path}")


        self.elapsed_time = QLabel(self.arv_bubble)
        self.elapsed_time.setObjectName(u"elapsed_time")
        self.elapsed_time.setGeometry(QRect(52, 49, 51, 16))
        self.elapsed_time.setStyleSheet(u"QLabel{\n"
                                        "	background:#44FFFFFF;\n"
                                        "    color:#333;\n"
                                        "	border-radius:8px;\n"
                                        "}")
        self.elapsed_time.setAlignment(Qt.AlignCenter)
        self.elapsed_time.setText("00:00")

        self.total_time = QLabel(self.arv_bubble)
        self.total_time.setObjectName(u"total_time")
        self.total_time.setGeometry(QRect(241, 49, 51, 16))
        self.total_time.setStyleSheet(u"QLabel{\n"
                                      "	background:#44FFFFFF;\n"
                                      "    color:#333;\n"
                                      "	border-radius:8px;\n"
                                      "}")
        self.total_time.setAlignment(Qt.AlignCenter)
        self.total_time.setText("--:--")

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

        # Add message label and time
        self.create_time_label(self.voice_bubble, self.arv_bubble)

        # Add frame on the widget
        self.add_widget(self.voice_bubble)

    def show_document_bubble(self):

        # self.document_bubble_frame = QFrame(self)
        # self.document_bubble_frame.setObjectName(u"document_bubble_frame")
        # self.document_bubble_frame.setGeometry(QRect(380, 180, 201, 101))
        # self.document_bubble_frame.setMinimumSize(QSize(201, 101))

        self.document_bubble = QFrame(self)
        self.document_bubble.setObjectName(u"document_bubble")
        self.document_bubble.setGeometry(QRect(17, 17, 181, 71))
        self.document_bubble.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.document_bubble.setStyleSheet(u"border-radius:10px;border-top-left-radius:8px;\n"
                                           "	background-color: rgb(40, 40, 43);")

        self.document = QFrame(self.document_bubble)
        self.document.setObjectName(u"document")
        self.document.setStyleSheet(u".QFrame{\n"
                                    "	background-color:#88FFFFFF;\n"
                                    "	border-radius:10px;\n"
                                    "\n"
                                    "}")
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
        # self.document_title.setWordWrap(True)

        self.document_title_size_layout.addWidget(self.document_title)

        self.document_size = QLabel(self.document)
        self.document_size.setObjectName(u"document_size")
        self.document_size.setStyleSheet(u"QLabel{\n"
                                         "	background:transparent;\n"
                                         "    color:#333;\n"
                                         "}")
        self.document_size.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.document_size.setTextInteractionFlags(Qt.TextSelectableByMouse)
        size = round((os.path.getsize(path) / 1024 / 1024), 2)
        self.document_size.setText(f"{size} Mb")

        self.document_title_size_layout.addWidget(self.document_size)

        self.horizontalLayout_23.addLayout(self.document_title_size_layout)

        # Add message label and time
        self.create_time_label(self.document_bubble, self.document)

        # Add frame on the widget
        self.add_widget(self.document_bubble)

    def show_image_bubble(self):
        font10 = QFont()
        font10.setBold(False)

        self.image_bubble = QFrame(self)
        self.image_bubble.setObjectName(u"image_bubble")
        self.image_bubble.setGeometry(QRect(17, 17, 191, 201))
        self.image_bubble.setStyleSheet(u"	border-radius:10px;\n"
                                        "	border-top-left-radius:8px;\n"
                                        "	background-color: rgb(40, 40, 43);\n"
                                        "")

        self.image = QLabel(self.image_bubble)
        self.image.setObjectName(u"image")
        self.image.setMinimumSize(QSize(180, 180))
        self.image.setMaximumSize(QSize(16777215, 180))
        self.image.setFont(font10)
        self.image.setStyleSheet(u"QLabel{\n"
                                 "	border-radius:10px;\n"
                                 "	border-image: url(:/icons/icons/test.jpg);\n"
                                 "	color:#000;\n"
                                 "	padding:2px;\n"
                                 "\n"
                                 "}")
        self.image.setText(u"<p><span style=\" color:#848484;\">1.2Mb</span> • Image.ext</p>")
        self.image.setAlignment(Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)
        self.image.setTextInteractionFlags(Qt.TextSelectableByMouse)

        # Add message label and time
        self.create_time_label(self.image_bubble, self.image)

        # Add frame on the widget
        self.add_widget(self.image_bubble)