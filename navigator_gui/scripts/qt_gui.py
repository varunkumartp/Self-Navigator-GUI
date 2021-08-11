#!/usr/bin/env python

import os
import rviz
import signal
import rospkg
import subprocess
import PyQt5.QtGui as gui
import PyQt5.QtCore as core
import PyQt5.QtWidgets as qt
from teleop import teleop

#############################################################
class LoginPage(qt.QMainWindow):
#############################################################

    #############################################################
    def __init__(self):
    #############################################################
        super().__init__()
        widget.setWindowTitle('Login Page')
    
        # Main Window Title
        self.label = qt.QLabel('SELF-NAVIGATING BOT',self)
        self.label.setFont(gui.QFont('Times New Roman', 25, weight=gui.QFont.Bold))
        self.label.setStyleSheet('color: #ffffff')
        self.label.adjustSize()
        self.label.setAlignment(core.Qt.AlignCenter | core.Qt.AlignVCenter)
        self.label.move(core.QPoint(int(w/2),66)-self.label.frameGeometry().center())
        
        # Username label
        self.user = qt.QLabel('Username', self)
        self.user.setFont(gui.QFont('Times New Roman', 20))
        self.user.setStyleSheet('color: #ffffff')
        self.user.adjustSize()
        self.user.setAlignment(core.Qt.AlignRight | core.Qt.AlignVCenter)
        self.user.setGeometry(490,250,100,25)
        
        # Password Label
        self.pswd = qt.QLabel('Password', self)
        self.pswd.setFont(gui.QFont('Times New Roman', 20))
        self.pswd.setStyleSheet('color: #ffffff')
        self.pswd.adjustSize()
        self.pswd.setAlignment(core.Qt.AlignRight | core.Qt.AlignVCenter)
        self.pswd.setGeometry(490,290,100,25)
        
        # Username field
        self.username = qt.QLineEdit(self)
        self.username.setText('Self-Navigating Bot')
        self.username.setStyleSheet('background-color: #ffffff')
        self.username.setGeometry(610,250,150,25)

        # Password field
        self.password = qt.QLineEdit(self)
        self.password.setText('navigator')
        self.password.setEchoMode(qt.QLineEdit.Password)
        self.password.setStyleSheet('background-color: #ffffff')
        self.password.setGeometry(610,290,150,25)

        # Enter button
        self.enter = qt.QPushButton('Enter', self, clicked = lambda: self.Enter())
        self.enter.setStyleSheet('background-color: #ffffff')
        self.enter.move(core.QPoint(int(w/2),360)-self.enter.frameGeometry().center())
        
        # Wrong credentials label
        self.wlabel = qt.QLabel('Wrong username or password', self)
        self.wlabel.setFont(gui.QFont('Times New Roman', 15, weight=gui.QFont.Bold))
        self.wlabel.setStyleSheet('color: #ff0000')
        self.wlabel.adjustSize()
        self.wlabel.setAlignment(core.Qt.AlignCenter | core.Qt.AlignVCenter)
        self.wlabel.move(core.QPoint(int(w/2),500)-self.wlabel.frameGeometry().center())
        self.wlabel.setHidden(True)

        # Exit button
        self.exit = qt.QPushButton('Exit', self, clicked = lambda: app.quit())
        self.exit.setStyleSheet('background-color: #ff0000')
        self.exit.move(core.QPoint(int(w/2),600)-self.exit.frameGeometry().center())

    #############################################################
    def Enter(self):
    #############################################################
        if self.username.text() == 'Self-Navigating Bot' and self.password.text() == 'navigator':
            self.wlabel.setHidden(True)
            widget.setCurrentIndex(widget.currentIndex()+1)
            widget.setWindowTitle('Main Menu')
        else:
            self.wlabel.setHidden(False)


#############################################################
class MainMenu(qt.QMainWindow):
#############################################################

    #############################################################
    def __init__(self):
    #############################################################
        super().__init__()

        # Main Window Title
        self.label = qt.QLabel('SELECT NAVIGATOR MODE',self)
        self.label.setFont(gui.QFont('Times New Roman', 25, weight=gui.QFont.Bold))
        self.label.setStyleSheet('color: #ffffff')
        self.label.adjustSize()
        self.label.setAlignment(core.Qt.AlignCenter | core.Qt.AlignVCenter)
        self.label.move(core.QPoint(int(w/2),66)-self.label.frameGeometry().center())

        # slam Button
        self.slam = qt.QPushButton('Simultaneous Mapping and Localization', self, clicked = lambda: self.viz('Simultaneous Mapping and Localization', 1))
        self.slam.setStyleSheet('background-color: #ffffff')
        self.slam.setFixedSize(350,30)
        self.slam.move(core.QPoint(int(w/2),225)-self.slam.frameGeometry().center())

        # auto Button
        self.auto = qt.QPushButton('Autonomous Navigation', self, clicked = lambda: self.viz('Autonomous Navigation', 2))
        self.auto.setStyleSheet('background-color: #ffffff')
        self.auto.setFixedSize(350,30)
        self.auto.move(core.QPoint(int(w/2),325)-self.auto.frameGeometry().center())

        # sman Button
        self.sman = qt.QPushButton('Simultaneous Mapping and Autonomous Navigation', self, clicked = lambda: self.viz('Simultaneous Mapping and Autonomous Navigation', 3))
        self.sman.setStyleSheet('background-color: #ffffff')
        self.sman.setFixedSize(350,30)
        self.sman.move(core.QPoint(int(w/2),425)-self.sman.frameGeometry().center())

    #############################################################
    def keyReleaseEvent(self, event):
    #############################################################
        if event.key() == 16777219:
            self.viz('Login Page', -1)
    
    #############################################################
    def viz(self, title, index):
    #############################################################
        widget.setCurrentIndex(widget.currentIndex()+index)
        widget.setWindowTitle(title)
        
    
#############################################################
class SLAM(qt.QWidget):
#############################################################

    #############################################################
    def __init__(self):
    #############################################################
        super().__init__()
        self.setStyleSheet('background-color: #353535')

        self.mode = False
        self.stat = ' '
        self.tele = teleop()
        
        # start button
        self.start = qt.QPushButton('Start', self, clicked = lambda: self.start_())
        self.start.setStyleSheet('background-color: #00ff00')
        self.start.setFixedSize(100,30)

        # stop button
        self.stop = qt.QPushButton('Stop', self, clicked = lambda: self.stop_())
        self.stop.setStyleSheet('background-color: #ff0000')
        self.stop.setFixedSize(100,30)
        self.stop.hide()

        # save button
        self.save = qt.QPushButton('Save Map', self, clicked = lambda: os.system('rosrun map_server map_saver -f '+rospack.get_path('navigator_gui')+'/maps/mymap'))
        self.save.setStyleSheet('background-color: #0000ff')
        self.save.setFixedSize(100,30)
        self.save.setEnabled(False)

        # final layout
        button = qt.QHBoxLayout()
        button.addWidget(self.start)
        button.addWidget(self.stop)
        button.addWidget(self.save)
        layout = qt.QVBoxLayout()
        layout.addWidget(Myviz().getviz())
        layout.addLayout(button)
        Widget = qt.QWidget(self)
        Widget.setFixedSize(w, h)
        Widget.move(core.QPoint(int(w/2),325)-Widget.frameGeometry().center())
        Widget.setLayout(layout)

    #############################################################
    def start_(self):
    #############################################################
        self.process = subprocess.Popen(['python', rospack.get_path('navigator_gui')+'/scripts/python_roslaunch.py','0'])
        self.start.hide()
        self.stop.show()
        self.mode = True
        self.save.setEnabled(True)

        
    #############################################################
    def stop_(self):
    #############################################################
        try:
            self.process.send_signal(signal.SIGTERM)
            self.process.wait()
            self.process.kill()
            self.process.wait()
            self.mode = False
        finally:
            self.process.terminate()
            self.start.show()
            self.stop.hide()
            self.save.setEnabled(False)


    #############################################################
    def keyPressEvent(self, event):
    #############################################################
        print(event.key())
        if event.key() != self.stat and self.mode:
            self.stat = event.key()
            self.tele.getcommands(event.key())
            
    #############################################################
    def keyReleaseEvent(self, event):
    #############################################################
        if event.key() and not event.isAutoRepeat() and self.mode:
            self.stat = ' '
            self.tele.getcommands(' ')
        if event.key() == 16777219:
            widget.setCurrentIndex(widget.currentIndex()-1)
            widget.setWindowTitle('Main Menu')

#############################################################
class SMAN(qt.QWidget):
#############################################################

    #############################################################
    def __init__(self):
    #############################################################
        super().__init__()
        self.setStyleSheet('background-color: #353535')

        self.mode = False
        self.stat = ' '
        self.tele = teleop()
        
        # start button
        self.start = qt.QPushButton('Start', self, clicked = lambda: self.start_())
        self.start.setStyleSheet('background-color: #00ff00')
        self.start.setFixedSize(100,30)

        # stop button
        self.stop = qt.QPushButton('Stop', self, clicked = lambda: self.stop_())
        self.stop.setStyleSheet('background-color: #ff0000')
        self.stop.setFixedSize(100,30)
        self.stop.hide()

        # save button
        self.save = qt.QPushButton('Save Map', self, clicked = lambda: os.system('rosrun map_server map_saver -f '+rospack.get_path('navigator_gui')+'/maps/mymap'))
        self.save.setStyleSheet('background-color: #0000ff')
        self.save.setFixedSize(100,30)
        self.save.setEnabled(False)

        # final layout
        button = qt.QHBoxLayout()
        button.addWidget(self.start)
        button.addWidget(self.stop)
        button.addWidget(self.save)
        layout = qt.QVBoxLayout()
        layout.addWidget(Myviz().getviz())
        layout.addLayout(button)
        Widget = qt.QWidget(self)
        Widget.setFixedSize(w, h)
        Widget.move(core.QPoint(int(w/2),325)-Widget.frameGeometry().center())
        Widget.setLayout(layout)

    #############################################################
    def start_(self):
    #############################################################
        self.process = subprocess.Popen(['python', rospack.get_path('navigator_gui')+'/scripts/python_roslaunch.py','2'])
        self.start.hide()
        self.stop.show()
        self.mode = True
        self.save.setEnabled(True)
        
    #############################################################
    def stop_(self):
    #############################################################
        try:
            self.process.send_signal(signal.SIGTERM)
            self.process.wait()
            self.process.kill()
            self.process.wait()
            self.mode = False
        finally:
            self.process.terminate()
            self.start.show()
            self.stop.hide()
            self.save.setEnabled(False)

    #############################################################
    def keyPressEvent(self, event):
    #############################################################
        print(event.key())
        if event.key() != self.stat and self.mode:
            self.stat = event.key()
            self.tele.getcommands(event.key())
            
    #############################################################
    def keyReleaseEvent(self, event):
    #############################################################
        if event.key() and not event.isAutoRepeat() and self.mode:
            self.stat = ' '
            self.tele.getcommands(' ')
        if event.key() == 16777219:
            widget.setCurrentIndex(widget.currentIndex()-3)
            widget.setWindowTitle('Main Menu')


#############################################################
class AUTO(qt.QWidget):
#############################################################

    #############################################################
    def __init__(self):
    #############################################################
        super().__init__()
        self.setStyleSheet('background-color: #353535')

        # start button
        self.start = qt.QPushButton('Start', self, clicked = lambda: self.start_())
        self.start.setStyleSheet('background-color: #00ff00')
        self.start.setFixedSize(100,30)

        # start button
        self.stop = qt.QPushButton('Stop', self, clicked = lambda: self.stop_())
        self.stop.setStyleSheet('background-color: #ff0000')
        self.stop.setFixedSize(100,30)
        self.stop.hide()
        
        # final layout
        layout = qt.QVBoxLayout()
        layout.addWidget(Myviz().getviz())
        layout.addWidget(self.stop, alignment=core.Qt.AlignCenter | core.Qt.AlignVCenter)
        layout.addWidget(self.start, alignment=core.Qt.AlignCenter | core.Qt.AlignVCenter)
        Widget = qt.QWidget(self)
        Widget.setFixedSize(w, h)
        Widget.move(core.QPoint(int(w/2),325)-Widget.frameGeometry().center())
        Widget.setLayout(layout)

    #############################################################
    def keyReleaseEvent(self, event):
    #############################################################
        if event.key() == 16777219:
            widget.setCurrentIndex(widget.currentIndex()-2)
            widget.setWindowTitle('Main Menu')
    
    #############################################################
    def start_(self):
    #############################################################
        self.process = subprocess.Popen(['python', rospack.get_path('navigator_gui')+'/scripts/python_roslaunch.py','1'])
        self.start.hide()
        self.stop.show()

    #############################################################
    def stop_(self):
    #############################################################
        try:
            self.process.send_signal(signal.SIGTERM)
            self.process.wait()
            self.process.kill()
            self.process.wait()
        finally:
            self.process.terminate()
        self.stop.hide()
        self.start.show()
    
#############################################################
class Myviz():
#############################################################

    #############################################################
    def __init__(self):
    #############################################################
        reader = rviz.bindings.YamlConfigReader()
        config = rviz.bindings.Config()
        reader.readFile( config, rospack.get_path('navigator_gui')+"/rviz/robot_mapping.rviz" )
        self.frame = rviz.bindings.VisualizationFrame()
        self.frame.setSplashPath( "" )
        self.frame.initialize()
        self.frame.load( config )
        self.frame.setStatusBar( None )
        self.frame.setMenuBar(None)
        self.frame.setHideButtonVisibility(False)
    
    #############################################################
    def getviz(self):
    #############################################################
        return self.frame

#############################################################
#############################################################
if __name__ == '__main__':     
    w, h = 1200, 650
    rospack = rospkg.RosPack()
    app = qt.QApplication([])
    widget = qt.QStackedWidget()

    widget.setFixedSize(w, h)
    widget.setStyleSheet('background-color: #353535')
    widget.move(qt.QDesktopWidget().availableGeometry().center()-widget.frameGeometry().center())
    

    login_page = LoginPage()
    main_menu = MainMenu()
    slam_menu = SLAM()
    auto_menu = AUTO()
    sman_menu = SMAN()

    widget.addWidget(login_page)
    widget.addWidget(main_menu)
    widget.addWidget(slam_menu)
    widget.addWidget(auto_menu)
    widget.addWidget(sman_menu)
    widget.show()

    app.exec_()     
        
