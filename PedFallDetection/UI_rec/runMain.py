# -*- coding: utf-8 -*-
"""

"""
import os
import warnings
from PedFallRecing import PedFall_MainWindow
from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    # 忽略警告
    # os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
    # warnings.filterwarnings(action='ignore')

    app = QApplication(argv)

    win = PedFall_MainWindow()
    win.showTime()
    exit(app.exec_())
