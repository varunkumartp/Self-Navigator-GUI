#!/usr/bin/env python


from gui_to_motors import gui_to_motors as teleop
import PyQt5.QtWidgets as qt
import PyQt5.QtGui as gui
import PyQt5.QtCore as core
import roslib; roslib.load_manifest('rviz_python_tutorial')
import rospkg
import rviz

class MainWindow(qt.QMainWindow):
    def __init__(self):
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
        self.username.setStyleSheet('background-color: #ffffff')
        self.username.setGeometry(610,250,150,25)

        # Password field
        self.password = qt.QLineEdit(self)
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
        self.exit = qt.QPushButton('Exit', self, clicked = lambda: self.quit())
        self.exit.setStyleSheet('background-color: #ffffff')
        self.exit.move(core.QPoint(int(w/2),600)-self.exit.frameGeometry().center())

    def Enter(self):
        if self.username.text() == '' and self.password.text() == '':
            self.wlabel.setHidden(True)
            widget.setCurrentIndex(widget.currentIndex()+1)
            widget.setWindowTitle('Main Menu')
        else:
            self.wlabel.setHidden(False)
            
    def quit(self):
        app.quit()


class second(qt.QMainWindow):
    def __init__(self):
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
        self.sman = qt.QPushButton('Simultaneous Mapping and Autonomous Navigation', self, clicked = lambda: self.viz('Simultaneous Mapping and Autonomous Navigation', 1))
        self.sman.setStyleSheet('background-color: #ffffff')
        self.sman.setFixedSize(350,30)
        self.sman.move(core.QPoint(int(w/2),425)-self.sman.frameGeometry().center())

    def viz(self, title, index):
        widget.setCurrentIndex(widget.currentIndex()+index)
        widget.setWindowTitle(title)
        
    def keyReleaseEvent(self, event):
        if event.key() == 16777219:
            self.viz('Login Page', -1)


class SLAM(qt.QWidget):
    def __init__(self):
        super().__init__()
        self.stat = ' '
        self.tele = teleop()
        self.setStyleSheet('background-color: #414141')

        # save button
        self.save = qt.QPushButton('Save Map', self, clicked = lambda: self.save_())
        self.save.setStyleSheet('background-color: #00ff00')
        self.save.setFixedSize(100,30)

        # final layout
        layout = qt.QVBoxLayout()
        layout.addWidget(Myviz().getviz())
        layout.addWidget(self.save, alignment=core.Qt.AlignCenter | core.Qt.AlignVCenter)
        Widget = qt.QWidget(self)
        Widget.setFixedSize(w, h)
        Widget.move(core.QPoint(int(w/2),325)-Widget.frameGeometry().center())
        Widget.setLayout(layout)

    def keyPressEvent(self, event):
        print(event.key())
        if event.key() != self.stat:
            self.stat = event.key()
            self.tele.getcommands(event.key())
            
    def keyReleaseEvent(self, event):
        if event.key() and not event.isAutoRepeat():
            self.stat = ' '
            self.tele.getcommands(' ')
        if event.key() == 16777219:
            widget.setCurrentIndex(widget.currentIndex()-1)
            widget.setWindowTitle('Main Menu')

    def save_(self):
        print('map saved')

class AUTO(qt.QWidget):
    def __init__(self):
        super().__init__()

        # final layout
        layout = qt.QVBoxLayout()
        layout.addWidget(Myviz().getviz())
        Widget = qt.QWidget(self)
        Widget.setFixedSize(w, h)
        Widget.move(core.QPoint(int(w/2),325)-Widget.frameGeometry().center())
        Widget.setLayout(layout)

    def keyReleaseEvent(self, event):
        if event.key() == 16777219:
            widget.setCurrentIndex(widget.currentIndex()-2)
            widget.setWindowTitle('Main Menu')

class Myviz():
    def __init__(self):
        reader = rviz.bindings.YamlConfigReader()
        config = rviz.bindings.Config()
        reader.readFile( config, rospack.get_path('navigator_gui')+"/rviz/robot_mapping.rviz" )
        self.frame = rviz.bindings.VisualizationFrame()
        self.frame.setSplashPath( "" )
        self.frame.initialize()
        self.frame.load( config )
        self.frame.setStatusBar( None )
        self.frame.setMenuBar(None)
    
    def getviz(self):
        return self.frame
        

if __name__ == '__main__':     
    w = 1200
    h = 650
    rospack = rospkg.RosPack()
    app = qt.QApplication([])
    widget = qt.QStackedWidget()

    widget.setFixedSize(w, h)
    widget.setStyleSheet('background-color: #414141')
    widget.move(qt.QDesktopWidget().availableGeometry().center()-widget.frameGeometry().center())
    

    login_page = MainWindow()
    main_menu = second()
    slam_menu = SLAM()
    auto_menu = AUTO()

    widget.addWidget(login_page)
    widget.addWidget(main_menu)
    widget.addWidget(slam_menu)
    widget.addWidget(auto_menu)

    widget.show()

    app.exec_()     
        
