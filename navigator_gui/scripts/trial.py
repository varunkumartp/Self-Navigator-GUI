#!/usr/bin/env python

## BEGIN_TUTORIAL
##
## Imports
## ^^^^^^^
##
## First we start with the standard ros Python import line:
import roslib; roslib.load_manifest('rviz_python_tutorial')
import rospkg
## Then load sys to get sys.argv.
import sys

import PyQt5.QtWidgets as qt
import rviz

class MyViz( qt.QMainWindow ):
    def __init__(self):
        super().__init__()
        self.frame = rviz.bindings.VisualizationFrame()
        self.frame.setSplashPath('')
        self.frame.initialize()
        self.frame.load( config )
        self.frame.setStatusBar( None )
        self.frame.setHideButtonVisibility( False )
        layout = qt.QVBoxLayout()
        layout.addWidget(self.frame)
        widget = qt.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = qt.QApplication( sys.argv )
    rospack = rospkg.RosPack()
    reader = rviz.bindings.YamlConfigReader()
    config = rviz.bindings.Config()
    reader.readFile( config, rospack.get_path('navigator_gui')+"/rviz/robot_mapping.rviz" )
    myviz = MyViz()
    myviz.resize( 1000, 650 )
    myviz.show()

    app.exec_()