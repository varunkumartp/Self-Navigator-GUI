#!/usr/bin/env python

import tkinter as tk
import subprocess
from tkinter.constants import CENTER, FALSE, E, N, W
import rospy
from std_msgs.msg import Int16
import roslib; roslib.load_manifest('rviz_python_tutorial')
import sys
## Finally import the RViz bindings themselves.
import rviz


def getRes():
    cmd = ['xrandr']
    cmd2 = ['grep', '*']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(cmd2, stdin=p.stdout, stdout=subprocess.PIPE)
    p.stdout.close()
    resolution_string, junk = p2.communicate()
    resolution = resolution_string.split()[0]
    resolution = resolution.decode("utf-8")
    width, height = resolution.split('x')
    return int(width), int(height)

class login_page():
    def __init__(self, root):
        self.root = root
        self.root.update_idletasks()
        self.root.geometry(str(w)+'x'+str(h)+'+'+str(int((screen_w-w)/2))+'+'+str(int((screen_h-h)/2)))
        self.root.resizable(FALSE, FALSE)
        self.root.title('Self-Navigating Bot')
        self.root.config(background="#090909")
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        # self.frame = rviz.VisualizationFrame()

        tk.Label(self.root, text='SELF-NAVIGATING BOT', bg='#090909', foreground='#ffffff', font=("Times New Roman",25,"bold")).place(relx=0.5, rely=0.1, anchor=CENTER)
        tk.Label(self.root, text='Username : ', background='#090909', foreground='#ffffff', font=("Times New Roman",18,"bold")).place(relx=0.5, rely=0.4, anchor=E)
        tk.Label(self.root, text='Password : ', background='#090909', foreground='#ffffff', font=("Times New Roman",18,"bold")).place(relx=0.5, rely=0.5, anchor=E)
        
        tk.Entry(self.root, textvariable=self.username, width=20).place(relx=0.5, rely=0.4, anchor=W)
        tk.Entry(self.root, textvariable=self.password, width=20, show='*').place(relx=0.5, rely=0.5, anchor=W)

        tk.Button(self.root, text='Enter', background='#ffffff', foreground='#000000', height=1, width=5, command=self.verify).place(relx=0.5, rely=0.6, anchor=CENTER)
        tk.Button(self.root, text='Exit',  background='#ffffff', foreground='#000000', height=1, width=5, command=self.quit).place(relx=0.5, rely=0.9, anchor=CENTER)

    def verify(self):
        if self.username.get() == 'q' and self.password.get() == 'q':
            second = tk.Toplevel(self.root)
            self.root.withdraw()
            a = selection_page(second,self.root)
        else:
            tk.Label(self.root, text='Incorrect username or password', background='#090909', foreground='#ff0000', font=('Times New Roman', 15)).place(relx=0.5, rely=0.7, anchor=CENTER)

    def quit(self):
        self.root.destroy()
        exit()

class selection_page():
    def __init__(self, second, root):
        self.second = second
        self.root = root
        self.second.update_idletasks()
        self.second.geometry(str(w)+'x'+str(h)+'+'+str(int((screen_w-w)/2))+'+'+str(int((screen_h-h)/2)))
        self.second.resizable(FALSE, FALSE)
        self.second.title('Self-Navigating Bot')
        self.second.config(background="#090909")

        tk.Label(self.second, text='Navigator Mode', background='#090909', foreground='#ffffff', font=('Times New Roman', 25, 'bold')).place(relx=0.5, rely=0.1, anchor=CENTER)
        tk.Button(self.second, text='Back', background='#ffffff', foreground='#000000', height=1, width=5, command=self.back).place(relx=0.1, rely=0.9, anchor=CENTER)
        tk.Button(self.second, text='Exit', background='#ffffff', foreground='#000000', height=1, width=5, command=self.quit).place(relx=0.9, rely=0.9, anchor=CENTER)

        self.auto = tk.Button(self.second, text='Autonomous Navigation',                          background='#ffffff', foreground='#000000', height=1, width=40, command=self.AUTO).place(relx=0.5, rely=0.5, anchor=CENTER)
        self.slam = tk.Button(self.second, text='Simultaneous Mapping and Localization',          background='#ffffff', foreground='#000000', height=1, width=40, command=self.SLAM).place(relx=0.5, rely=0.3, anchor=CENTER)
        self.sman = tk.Button(self.second, text='Simultaneous Mapping and Autonomous Navigation', background='#ffffff', foreground='#000000', height=1, width=40, command=self.SMAN).place(relx=0.5, rely=0.7, anchor=CENTER)
        
    def back(self):
        self.second.withdraw()
        self.root.update()
        self.root.deiconify()

    def quit(self):
        self.root.destroy()
        exit()

    def SLAM(self):
        slam = tk.Toplevel(self.second)
        self.second.withdraw()
        a = manual(slam,self.second, True)

    def SMAN(self):
        slam = tk.Toplevel(self.second)
        self.second.withdraw()
        a = manual(slam,self.second, False)

    def AUTO(self):
        pass

class manual():
    def __init__(self, second, root, mode):
        self.second = second
        self.root = root
        self.mode = mode
        self.second.update_idletasks()
        self.second.geometry(str(w)+'x'+str(h)+'+'+str(int((screen_w-w)/2))+'+'+str(int((screen_h-h)/2)))
        self.second.resizable(FALSE, FALSE)
        self.second.title('Self-Navigating Bot')
        self.second.config(background="#090909")
        self.stat=' '

        tk.Label(self.second, text='Navigator Mode', background='#090909', foreground='#ffffff', font=('Times New Roman', 25, 'bold')).place(relx=0.5, rely=0.1, anchor=CENTER)
        
        tk.Button(self.second, text='Back', background='#ffffff', foreground='#000000', height=1, width=5, command=self.back).place(relx=0.1, rely=0.9, anchor=CENTER)
        tk.Button(self.second, text='Exit', background='#ffffff', foreground='#000000', height=1, width=5, command=self.quit).place(relx=0.9, rely=0.9, anchor=CENTER)

        self.button = tk.Button(self.second, text='Start',background='#ffffff', foreground='#000000', height=1, width=5, command=self.start, activebackground='#00ff00').place(relx=0.5, rely=0.9, anchor=CENTER)
        
    def start(self):
        self.detail = tk.Label(self.second, text='i: Forward      k: Backward      j: Left      l: Right      other keys: Stop', background='#090909', foreground='#ffffff', font=('Times New Roman', 15)).place(relx=0.5, rely=0.95, anchor=N)
        self.button = tk.Button(self.second, text='Stop', background='#ffffff', foreground='#000000', height=1, width=5, command=self.stop,  activebackground='#ff0000').place(relx=0.5, rely=0.9, anchor=CENTER)
        self.second.bind('<KeyPress>', self.getKey)

    def stop(self):
        self.detail = tk.Label(self.second, text='i: Forward      k: Backward      j: Left      l: Right      other keys: Stop', background='#090909', foreground='#090909', font=('Times New Roman', 15)).place(relx=0.5, rely=0.95, anchor=N)
        self.button = tk.Button(self.second, text='Start',background='#ffffff', foreground='#000000', height=1, width=5, command=self.start, activebackground='#00ff00').place(relx=0.5, rely=0.9, anchor=CENTER)
        self.second.unbind('<KeyPress>')

    def send(self, l, r):
        lwheel.publish(l)
        rwheel.publish(r)

    def getKey(self,event):
        if self.stat != event.char:
            if event.char == 'i':
                self.send(128, 128)
            elif event.char == 'j':
                self.send(-128, 128)
            elif event.char == 'l':
                self.send(128, -128)
            elif event.char == 'k':
                self.send(-128, -128)
            else:
                self.send(0, 0)
            self.stat = event.char

    def back(self):
        self.second.withdraw()
        self.root.update()
        self.root.deiconify()

    def quit(self):
        self.root.destroy()
        exit()

if __name__ == '__main__':
    rospy.init_node("Navigator_GUI")
    nodename = rospy.get_name()
    rospy.loginfo("-I- %s started" % nodename)
    
    lwheel = rospy.Publisher("motors/pwm/lwheel", Int16, queue_size=10)
    rwheel = rospy.Publisher("motors/pwm/rwheel", Int16, queue_size=10)
    
    screen_w, screen_h = getRes()
    h = 650
    w = 1000
    
    window = tk.Tk()
    login_page(window)
    window.mainloop()