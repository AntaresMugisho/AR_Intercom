
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

from resources import img_rc
import utils

from ui.main_window import Ui_MainWindow

class ChatFunctions(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def show_user_widget(self, user, online: bool = False):
        """
        Load users conversation list from users who are registered in database
        """
        uuid = user.get_uuid()
        name = user.get_user_name()
        profile_picture_path = user.get_image_path()

        font1 = QFont()
        font1.setPointSize(10)

        # FRAME FOR ONE CLIENT
        self.client_info = QFrame(self.ui.chat_list_widget)
        self.client_info.setObjectName(f"{uuid}")
        self.client_info.setMinimumSize(QSize(271, 61))
        self.client_info.setMaximumSize(QSize(271, 61))
        self.client_info.setCursor(QCursor(Qt.PointingHandCursor))
        self.client_info.setStyleSheet(u"QFrame{\n"
                                       "	border-radius:8px;\n"
                                       "	background-color: rgba(50, 50, 50, 50);\n"
                                       "}\n"
                                       "\n"
                                       "QFrame:hover{\n"
                                       "	background-color: rgba(50, 50, 50, 255);\n"
                                       "}\n"
                                       "")
        self.client_info.setFrameShape(QFrame.Box)
        self.client_info.setFrameShadow(QFrame.Plain)
        self.client_info.setLineWidth(1)

        last_index = self.ui.chat_list_layout.count() - 1
        self.ui.chat_list_layout.insertWidget(last_index, self.client_info,
                                             Qt.AlignmentFlag.AlignCenter, Qt.AlignmentFlag.AlignTop)

        print(last_index)

        # PROFILE PICTURE
        self.client_picture = QLabel(self.client_info)
        self.client_picture.setObjectName(u"client_picture")
        self.client_picture.setGeometry(QRect(3, 3, 56, 56))
        self.client_picture.setStyleSheet("border-radius:28px;border:none;")

        # Create rounded pixmap
        rounded_pixmap = utils.create_rounded_image(profile_picture_path, self.client_picture.width())
        self.client_picture.setPixmap(rounded_pixmap)
        self.client_picture.setScaledContents(True)

        # ONLINE TOAST
        self.online_toast = QLabel(self.client_info)
        self.online_toast.setObjectName(f"{uuid}_toast")
        self.online_toast.setGeometry(QRect(47, 41, 12, 12))
        self.online_toast.setStyleSheet(u"QLabel{\n"
                                        "	border-radius:6px;\n"
                                        "	border:2px solid rgb(20,20,20);\n"
                                        "	background-color: #00ff00;	\n"
                                        "}")
        self.online_toast.setFrameShadow(QFrame.Raised)
        if not online:
            self.online_toast.hide()

        # NAME
        self.client_name = QPushButton(self.client_info)
        self.client_name.setObjectName(f"{uuid}")
        self.client_name.setGeometry(QRect(70, 6, 131, 31))
        font4 = QFont()
        font4.setPointSize(12)
        self.client_name.setFont(font4)
        self.client_name.setStyleSheet(u"QLabel{\n"
                                       "	background-color:none;\n"
                                       "	color: white;\n"
                                       "}")
        self.client_name.setText(name)
        self.client_name.clicked.connect(self.show_conversation)

        # LAST MESSAGE
        self.last_message = QLabel(self.client_info)
        self.last_message.setObjectName(u"last_message")
        self.last_message.setGeometry(QRect(70, 36, 131, 20))
        self.last_message.setFont(font1)
        self.last_message.setStyleSheet(u"QLabel{\n"
                                        "	background-color:transparent;\n"
                                        "	color:rgba(255, 255, 255, 0.5);\n"
                                        "}")


        # MESSAGE COUNTER
        self.messege_number = QLabel(self.client_info)
        self.messege_number.setObjectName(f"{uuid}_counter")
        self.messege_number.setGeometry(QRect(213, 23, 30, 20))
        self.messege_number.setText("1")
        font5 = QFont()
        font5.setPointSize(8)
        self.messege_number.setFont(font5)
        self.messege_number.setStyleSheet(u"QLabel{\n"
                                          "	background-color:transparent;\n"
                                          "	color:rgba(255, 255, 255, 0.6);\n"
                                          "\n"
                                          "}")
        self.messege_number.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        # self.message_number.hide()

        # ENVELOP ICON
        self.envelop_msg = QFrame(self.client_info)
        self.envelop_msg.setObjectName(u"envelop_msg")
        self.envelop_msg.setGeometry(QRect(247, 27, 12, 12))
        self.envelop_msg.setStyleSheet(u"QFrame{\n"
                                       "	background-color:transparent;\n"
                                       "	image: url(:/cils/cils/cil-envelope-closed.png);\n"
                                       "	border:none;}")

    def show_conversation(self):
        pass