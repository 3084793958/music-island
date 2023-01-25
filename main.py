import os
import sys
import time
import linecache
from PyQt5 import QtCore,QtMultimedia
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class MI(QWidget):
    def __init__(self, parent=None):
        super(MI, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|Qt.SubWindow)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowTitle('music island')
        self.setWindowIcon(QIcon('files/image/musicrun.gif'))
        self.repaint()
        self.initPall()
        self.update()
        self.about()
        self.movie_frame=0
        self.sp.movie.frame=0
        self.nx.movie.frame=0
        self.bc.movie.frame=0
        self.sp.movie.gif=0
        self.music_list=0
        self.hint=False
        self.dock_d=0
        self.bn=False
        self.fileslist=[]
        self.move(QApplication.desktop().width()/2-100,10)
        self.time_id = self.startTimer(1)
        self.mouse=self.cursor()
        self.setAcceptDrops(True)
        self.play_check=QtMultimedia.QMediaPlayer()
        self.play_music=QtMultimedia.QMediaPlayer()
        self.play_music.stateChanged.connect(self.do_mediaplayer_statechanged)
        self.play_check.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile((QtCore.QDir.current().absoluteFilePath('files/sound/check.mp3')))))
        self.QSlider1()
        self.QSlider2()
        self.QSlider3()
        for x in range(int(linecache.getline('files/data/list.txt',1).replace('\n', ''))):
            self.fileslist.append(linecache.getline('files/data/list.txt',x+2).replace('\n', ''))
        if int(linecache.getline('files/data/list.txt',1))>0:
            self.play_music.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile((QtCore.QDir.current().absoluteFilePath(self.fileslist[0])))))
            self.music_list=1
    def initPall(self):
        icons=os.path.join('files/image/musicrun.gif')
        exit=os.path.join('files/image/exit.svg')
        tab=os.path.join('files/image/setting.svg')
        tab_button = QAction((linecache.getline('files/data/main.txt',1)), self, triggered=self.dark)
        tab_button.setIcon(QIcon(tab))
        quit_button = QAction((linecache.getline('files/data/main.txt',2)), self, triggered=self.quit)
        quit_button.setIcon(QIcon(exit))
        show = QAction((linecache.getline('files/data/main.txt',3)), self, triggered=self.showmain)
        show.setIcon(QIcon('files/image/hidden.svg'))
        hint = QAction((linecache.getline('files/data/main.txt',4)), self, triggered=self.hintmain)
        hint.setIcon(QIcon('files/image/hint.svg'))
        about_i = QAction((linecache.getline('files/data/main.txt',5)), self, triggered=self.show_about)
        about_i.setIcon(QIcon('files/image/about.svg'))
        self.tray_menu = QMenu(self)
        self.tray_menu.addAction(about_i)
        self.tray_menu.addAction(tab_button)
        self.tray_menu.addAction(show)
        self.tray_menu.addAction(hint)
        self.tray_menu.addAction(quit_button)
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(icons))
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.show()
    def quit(self):
        os.system('echo "'+str(len(self.fileslist))+'\n'+str(self.fileslist).replace('[', '').replace(']', '').replace('[', '').replace("'", "").replace(", ", "\n")+'"'+' > files/data/list.txt')
        self.close()
        sys.exit()
    def update(self):
        self.image = QLabel(self)
        self.movie = QMovie("files/image/dock.gif")
        self.image.setMovie(self.movie)
        self.movie.start()
        self.movie.setScaledSize(QSize(200, 50))
        self.resize(200,50)
        self.image.resize(200,50)
        self.movie.stop()
        self.movie.start()
        self.movie.stop()
        self.movie.jumpToFrame(0)
        self.sp=QLabel(self)
        self.sp.movie = QMovie("files/image/start.gif")
        self.sp.setMovie(self.sp.movie)
        self.sp.movie.start()
        self.sp.movie.setScaledSize(QSize(35, 35))
        self.sp.resize(35,35)
        self.sp.move(80,8)
        self.sp.movie.stop()
        self.sp.movie.start()
        self.sp.movie.stop()
        self.sp.movie.jumpToFrame(0)
        self.nx=QLabel(self)
        self.nx.movie = QMovie("files/image/next.gif")
        self.nx.setMovie(self.nx.movie)
        self.nx.movie.start()
        self.nx.movie.setScaledSize(QSize(20, 20))
        self.nx.resize(20,20)
        self.nx.move(120,15)
        self.nx.movie.stop()
        self.nx.movie.start()
        self.nx.movie.stop()
        self.nx.movie.jumpToFrame(0)
        self.bc=QLabel(self)
        self.bc.movie = QMovie("files/image/back.gif")
        self.bc.setMovie(self.bc.movie)
        self.bc.movie.start()
        self.bc.movie.setScaledSize(QSize(20, 20))
        self.bc.resize(20,20)
        self.bc.move(55,15)
        self.bc.movie.stop()
        self.bc.movie.start()
        self.bc.movie.stop()
        self.bc.movie.jumpToFrame(0)
        self.mu=QLabel(self)
        self.mu.movie = QMovie("files/image/musicstop.gif")
        self.mu.setMovie(self.mu.movie)
        self.mu.movie.start()
        self.mu.movie.setScaledSize(QSize(30, 30))
        self.mu.resize(30,30)
        self.mu.move(20,10)
        self.so=QLabel(self)
        self.so.movie = QMovie("files/image/sound.gif")
        self.so.setMovie(self.so.movie)
        self.so.movie.start()
        self.so.movie.setScaledSize(QSize(30, 30))
        self.so.resize(30,30)
        self.so.move(150,10)
        self.so.movie.stop()
        self.so.movie.start()
        self.so.movie.stop()
        self.so.movie.jumpToFrame(0)
        self.so.movie.setCacheMode(QMovie.CacheAll)
    def dark(self):
        if self.movie_frame==0:
            self.movie.start()
            self.movie.jumpToFrame(1)
            self.movie.stop()
            self.movie_frame=1
        else:
            self.movie.start()
            self.movie.jumpToFrame(0)
            self.movie.stop()
            self.movie_frame=0
    def showmain(self):
        self.play_check.play()
        if self.windowOpacity()<0.05:
            self.showNormal()
            self.activateWindow()
            for x in range(2000):
                time.sleep(0.0001)
                self.setWindowOpacity(x/2000)
    def hintmain(self):
        self.play_check.play()
        if self.windowOpacity()>0.95:
            for x in range(2000):
                time.sleep(0.0001)
                self.setWindowOpacity(1- x/2000)
            self.showMinimized()
    def mousePressEvent(self, event):
        if self.QS1.isActiveWindow()==False:
            self.QS1.setWindowOpacity(0)
            self.QS1.showMinimized()
        if self.QS2.isActiveWindow()==False:
            self.QS2.setWindowOpacity(0)
            self.QS2.showMinimized()
        if self.QS3.isActiveWindow()==False:
            self.QS3.setWindowOpacity(0)
            self.QS3.showMinimized()
        if self.about.isActiveWindow()==False:
            self.about.showMinimized()
        if event.button() == Qt.LeftButton:
            self.play_check.play()
            self.left_mouse = True
            if self.pos().x()+self.sp.pos().x()-self.mouse.pos().x()>-35*self.QS3.value()/100 and self.pos().x()+self.sp.pos().x()-self.mouse.pos().x()<0 and self.pos().y()+self.sp.pos().y()-self.mouse.pos().y()>-35*self.QS3.value()/100 and self.pos().y()+self.sp.pos().y()-self.mouse.pos().y()<0 and len(self.fileslist)!=0:
                if self.sp.movie.gif==0:
                    self.sp.movie = QMovie("files/image/stop.gif")
                    self.mu.movie = QMovie("files/image/musicrun.gif")
                    self.sp.movie.gif=1
                    self.play_music.play()
                else:
                    self.sp.movie = QMovie("files/image/start.gif")
                    self.mu.movie = QMovie("files/image/musicstop.gif")
                    self.sp.movie.gif=0
                    self.play_music.pause()
                self.sp.setMovie(self.sp.movie)
                self.sp.movie.setScaledSize(QSize(35*self.QS3.value()/100, 35*self.QS3.value()/100))
                self.mu.setMovie(self.mu.movie)
                self.mu.movie.setScaledSize(QSize(30*self.QS3.value()/100, 30*self.QS3.value()/100))
                self.sp.movie.start()
                self.sp.movie.stop()
                self.mu.movie.start()
            if self.pos().x()+self.nx.pos().x()-self.mouse.pos().x()>-20*self.QS3.value()/100 and self.pos().x()+self.nx.pos().x()-self.mouse.pos().x()<0 and self.pos().y()+self.nx.pos().y()-self.mouse.pos().y()>-20*self.QS3.value()/100 and self.pos().y()+self.nx.pos().y()-self.mouse.pos().y()<0 and len(self.fileslist)!=0:
                self.bn=True
                if self.music_list==len(self.fileslist):
                    self.music_list=1
                else:
                    self.music_list+=1
                self.play_music.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile((QtCore.QDir.current().absoluteFilePath(self.fileslist[self.music_list-1])))))
                self.play_music.stop()
                self.bn=False
            if self.pos().x()+self.bc.pos().x()-self.mouse.pos().x()>-20*self.QS3.value()/100 and self.pos().x()+self.bc.pos().x()-self.mouse.pos().x()<0 and self.pos().y()+self.bc.pos().y()-self.mouse.pos().y()>-20*self.QS3.value()/100 and self.pos().y()+self.bc.pos().y()-self.mouse.pos().y()<0 and len(self.fileslist)!=0:
                self.bn=True
                if self.music_list==1:
                    self.music_list=len(self.fileslist)
                else:
                    self.music_list-=1
                self.play_music.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile((QtCore.QDir.current().absoluteFilePath(self.fileslist[self.music_list-1])))))
                self.play_music.stop()
                self.bn=False
            if self.pos().x()+self.so.pos().x()-self.mouse.pos().x()>-30*self.QS3.value()/100 and self.pos().x()+self.so.pos().x()-self.mouse.pos().x()<0 and self.pos().y()+self.so.pos().y()-self.mouse.pos().y()>-30*self.QS3.value()/100 and self.pos().y()+self.so.pos().y()-self.mouse.pos().y()<0:
                if self.QS1.isActiveWindow()==True:
                    self.QS1.setWindowOpacity(0)
                else:
                    self.QS1.activateWindow()
                    self.QS2.setWindowOpacity(0)
                    self.QS3.setWindowOpacity(0)
                    self.QS1.showNormal()
                    self.QS1.setWindowOpacity(1)
            if self.pos().x()+self.mu.pos().x()-self.mouse.pos().x()>-30*self.QS3.value()/100 and self.pos().x()+self.mu.pos().x()-self.mouse.pos().x()<0 and self.pos().y()+self.mu.pos().y()-self.mouse.pos().y()>-30*self.QS3.value()/100 and self.pos().y()+self.mu.pos().y()-self.mouse.pos().y()<0:
                if self.QS2.isActiveWindow()==True:
                    self.QS2.setWindowOpacity(0)
                else:
                    self.QS2.activateWindow()
                    self.QS1.setWindowOpacity(0)
                    self.QS3.setWindowOpacity(0)
                    self.QS2.showNormal()
                    self.QS2.setWindowOpacity(1)
            if self.hint==True:
                self.hint=False
                self.movie.start()
                if self.dock_d==0:
                    self.movie=QMovie("files/image/dock.gif")
                    self.image.setMovie(self.movie)
                    self.movie.setScaledSize(QSize(200*self.QS3.value()/100,50*self.QS3.value()/100))
                    self.resize(200*self.QS3.value()/100,50*self.QS3.value()/100)
                    self.image.resize(200*self.QS3.value()/100,50*self.QS3.value()/100)
                    self.sp.move(80*self.QS3.value()/100,15*self.QS3.value()/200)
                    self.nx.move(120*self.QS3.value()/100,15*self.QS3.value()/100)
                    self.bc.move(55*self.QS3.value()/100,15*self.QS3.value()/100)
                    self.so.move(150*self.QS3.value()/100,10*self.QS3.value()/100)
                    self.mu.move(20*self.QS3.value()/100,10*self.QS3.value()/100)
                else:
                    self.movie=QMovie("files/image/dock2.gif")
                    self.image.setMovie(self.movie)
                    self.movie.setScaledSize(QSize(50*self.QS3.value()/100,200*self.QS3.value()/100))
                    self.resize(50*self.QS3.value()/100,200*self.QS3.value()/100)
                    self.image.resize(50*self.QS3.value()/100,200*self.QS3.value()/100)
                    self.sp.move(15*self.QS3.value()/200,80*self.QS3.value()/100)
                    self.nx.move(15*self.QS3.value()/100,120*self.QS3.value()/100)
                    self.bc.move(15*self.QS3.value()/100,55*self.QS3.value()/100)
                    self.so.move(10*self.QS3.value()/100,150*self.QS3.value()/100)
                    self.mu.move(10*self.QS3.value()/100,20*self.QS3.value()/100)
                self.movie.stop()
                if self.movie_frame==0:
                    self.movie.start()
                    self.movie.jumpToFrame(1)
                    self.movie.jumpToFrame(0)
                    self.movie.stop()
                else:
                    self.movie.start()
                    self.movie.jumpToFrame(0)
                    self.movie.jumpToFrame(1)
                    self.movie.stop()
        else:
            self.left_mouse = False
            if event.button() == QtCore.Qt.MidButton and self.sp.movie.gif==1 and len(self.fileslist)!=0 and self.hint==False:
                if self.pos().x()+self.mu.pos().x()-self.mouse.pos().x()>-30*self.QS3.value()/100 and self.pos().x()+self.mu.pos().x()-self.mouse.pos().x()<0 and self.pos().y()+self.mu.pos().y()-self.mouse.pos().y()>-30*self.QS3.value()/100 and self.pos().y()+self.mu.pos().y()-self.mouse.pos().y()<0:
                    self.bn=True
                    del self.fileslist[self.music_list-1]
                    if self.music_list==len(self.fileslist)+1:
                        self.music_list-=1
                    if len(self.fileslist)!=0:
                        self.play_music.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile((QtCore.QDir.current().absoluteFilePath(self.fileslist[self.music_list-1])))))
                    else:
                        self.sp.movie = QMovie("files/image/start.gif")
                        self.mu.movie = QMovie("files/image/musicstop.gif")
                        self.sp.movie.gif=0
                        self.sp.setMovie(self.sp.movie)
                        self.sp.movie.setScaledSize(QSize(35*self.QS3.value()/100, 35*self.QS3.value()/100))
                        self.mu.setMovie(self.mu.movie)
                        self.mu.movie.setScaledSize(QSize(30*self.QS3.value()/100, 30*self.QS3.value()/100))
                        self.sp.movie.start()
                        self.sp.movie.stop()
                        self.mu.movie.start()
                    self.play_music.stop()
                    self.bn=False
        self.mouse_pos = event.globalPos() - self.pos()
        event.accept()
    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.left_mouse:
            self.setCursor(QCursor(Qt.OpenHandCursor))
            self.move(event.globalPos() - self.mouse_pos)
        event.accept()
    def mouseReleaseEvent(self, event):
        self.setCursor(QCursor(Qt.ArrowCursor))
        if self.pos().x()==0 and self.hint==False and self.pos().y()>10 and self.pos().y()<QApplication.desktop().height()-10:
            self.hint=True
            self.movie = QMovie("files/image/show.gif")
            self.image.setMovie(self.movie)
            self.movie.setScaledSize(QSize(20, 50))
            self.resize(20,50)
            self.image.resize(20,50)
            self.mu.move(200,50)
            self.move(0,self.pos().y())
            self.movie.start()
        if self.pos().x()==QApplication.desktop().width()-self.size().width() and self.hint==False and self.pos().y()>10 and self.pos().y()<QApplication.desktop().height()-10:
            self.hint=True
            self.movie = QMovie("files/image/show2.gif")
            self.image.setMovie(self.movie)
            self.movie.setScaledSize(QSize(20, 50))
            self.resize(20,50)
            self.image.resize(20,50)
            self.mu.move(200,50)
            self.movie.start()
            self.move(QApplication.desktop().width(),self.pos().y())
    def timerEvent(self,q):
        if self.dock_d==0:
            self.QS1.move(self.pos().x(),self.pos().y()-10)
            self.QS2.move(self.pos().x(),self.pos().y()+50*self.QS3.value()/100)
            self.QS3.move(self.pos().x(),self.pos().y()+65*self.QS3.value()/100)
        else:
            self.QS1.move(self.pos().x(),self.pos().y()-10)
            self.QS2.move(self.pos().x(),self.pos().y()+200*self.QS3.value()/100)
            self.QS3.move(self.pos().x(),self.pos().y()+215*self.QS3.value()/100)
        if self.pos().x()+self.sp.pos().x()-self.mouse.pos().x()>-35*self.QS3.value()/100 and self.pos().x()+self.sp.pos().x()-self.mouse.pos().x()<0 and self.pos().y()+self.sp.pos().y()-self.mouse.pos().y()>-35*self.QS3.value()/100 and self.pos().y()+self.sp.pos().y()-self.mouse.pos().y()<0:
            self.sp.movie.start()
            self.sp.movie.jumpToFrame(1)
            self.sp.movie.stop()
            self.sp.movie.frame=1
        else:
            self.sp.movie.start()
            self.sp.movie.jumpToFrame(0)
            self.sp.movie.stop()
            self.sp.movie.frame=0
        if self.pos().x()+self.nx.pos().x()-self.mouse.pos().x()>-20*self.QS3.value()/100 and self.pos().x()+self.nx.pos().x()-self.mouse.pos().x()<0 and self.pos().y()+self.nx.pos().y()-self.mouse.pos().y()>-20*self.QS3.value()/100 and self.pos().y()+self.nx.pos().y()-self.mouse.pos().y()<0:
            self.nx.movie.start()
            self.nx.movie.jumpToFrame(1)
            self.nx.movie.stop()
            self.nx.movie.frame=1
        else:
            self.nx.movie.start()
            self.nx.movie.jumpToFrame(0)
            self.nx.movie.stop()
            self.nx.movie.frame=0
        if self.pos().x()+self.bc.pos().x()-self.mouse.pos().x()>-20*self.QS3.value()/100 and self.pos().x()+self.bc.pos().x()-self.mouse.pos().x()<0 and self.pos().y()+self.bc.pos().y()-self.mouse.pos().y()>-20*self.QS3.value()/100 and self.pos().y()+self.bc.pos().y()-self.mouse.pos().y()<0:
            self.bc.movie.start()
            self.bc.movie.jumpToFrame(1)
            self.bc.movie.stop()
            self.bc.movie.frame=1
        else:
            self.bc.movie.start()
            self.bc.movie.jumpToFrame(0)
            self.bc.movie.stop()
            self.bc.movie.frame=0
            if abs(self.QS2.value()-self.play_music.position()/(self.play_music.duration()+0.0001)*100)<5:
                self.QS2.setValue(self.play_music.position()/(self.play_music.duration()+0.0001)*100)
                if self.play_music.duration()!=0:
                    if self.play_music.position()/self.play_music.duration()==1:
                        self.QS2.setValue(0)
            else:
                self.play_music.setPosition((self.QS2.value())/100*self.play_music.duration())
    def QSlider1(self):
        self.QS1 = QSlider(Qt.Horizontal)
        self.QS1.setMinimum(0)
        self.QS1.setMaximum(100)
        self.QS1.setSingleStep(10)
        self.QS1.setValue(100)
        self.QS1.setTickPosition(QSlider.TicksBelow)
        self.QS1.setTickInterval(10)
        self.QS1.valueChanged.connect(self.valuechange)
        self.QS1.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|Qt.SubWindow)
        self.QS1.setAutoFillBackground(False)
        self.QS1.setAttribute(Qt.WA_TranslucentBackground, True)
        self.QS1.setWindowTitle((linecache.getline('files/data/main.txt',6)))
        self.QS1.setWindowIcon(QIcon('files/image/musicrun.gif'))
        self.QS1.setWindowOpacity(0)
        self.QS1.show()
    def QSlider2(self):
        self.QS2 = QSlider(Qt.Horizontal)
        self.QS2.setMinimum(0)
        self.QS2.setMaximum(100)
        self.QS2.setSingleStep(1)
        self.QS2.setValue(0)
        self.QS2.setTickPosition(QSlider.TicksBelow)
        self.QS2.setTickInterval(5)
        self.QS2.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|Qt.SubWindow)
        self.QS2.setAutoFillBackground(False)
        self.QS2.setAttribute(Qt.WA_TranslucentBackground, True)
        self.QS2.setWindowTitle((linecache.getline('files/data/main.txt',7)))
        self.QS2.setWindowIcon(QIcon('files/image/musicrun.gif'))
        self.QS2.setWindowOpacity(0)
        self.QS2.show()
    def QSlider3(self):
        self.QS3 = QSlider(Qt.Horizontal)
        self.QS3.setMinimum(50)
        self.QS3.setMaximum(150)
        self.QS3.setSingleStep(10)
        self.QS3.setValue(100)
        self.QS3.setTickPosition(QSlider.TicksBelow)
        self.QS3.setTickInterval(10)
        self.QS3.valueChanged.connect(self.valuechange)
        self.QS3.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|Qt.SubWindow)
        self.QS3.setAutoFillBackground(False)
        self.QS3.setAttribute(Qt.WA_TranslucentBackground, True)
        self.QS3.setWindowTitle((linecache.getline('files/data/main.txt',11)))
        self.QS3.setWindowIcon(QIcon('files/image/musicrun.gif'))
        self.QS3.setWindowOpacity(0)
        self.QS3.show()
    def valuechange(self):
        self.play_check.play()
        if self.QS1.value()>60 or self.QS1.value()==60:
            self.so.movie.start()
            self.so.movie.jumpToFrame(1)
            self.so.movie.stop()
        if not(self.QS1.value()<30) and self.QS1.value()<60:
            self.so.movie.start()
            self.so.movie.jumpToFrame(2)
            self.so.movie.stop()
        if self.QS1.value()>0 and self.QS1.value()<30:
            self.so.movie.start()
            self.so.movie.jumpToFrame(3)
            self.so.movie.stop()
        if self.QS1.value()==0:
            self.so.movie.start()
            self.so.movie.jumpToFrame(4)
            self.so.movie.stop()
        self.play_check.setVolume(self.QS1.value())
        self.play_music.setVolume(self.QS1.value())
        self.movie.start()
        if self.dock_d==0:
            self.movie=QMovie("files/image/dock.gif")
            self.image.setMovie(self.movie)
            self.movie.setScaledSize(QSize(200*self.QS3.value()/100,50*self.QS3.value()/100))
            self.resize(200*self.QS3.value()/100,50*self.QS3.value()/100)
            self.image.resize(200*self.QS3.value()/100,50*self.QS3.value()/100)
            self.sp.move(80*self.QS3.value()/100,15*self.QS3.value()/200)
            self.nx.move(120*self.QS3.value()/100,15*self.QS3.value()/100)
            self.bc.move(55*self.QS3.value()/100,15*self.QS3.value()/100)
            self.so.move(150*self.QS3.value()/100,10*self.QS3.value()/100)
            self.mu.move(20*self.QS3.value()/100,10*self.QS3.value()/100)
        else:
            self.movie=QMovie("files/image/dock2.gif")
            self.image.setMovie(self.movie)
            self.movie.setScaledSize(QSize(50*self.QS3.value()/100,200*self.QS3.value()/100))
            self.resize(50*self.QS3.value()/100,200*self.QS3.value()/100)
            self.image.resize(50*self.QS3.value()/100,200*self.QS3.value()/100)
            self.sp.move(15*self.QS3.value()/200,80*self.QS3.value()/100)
            self.nx.move(15*self.QS3.value()/100,120*self.QS3.value()/100)
            self.bc.move(15*self.QS3.value()/100,55*self.QS3.value()/100)
            self.so.move(10*self.QS3.value()/100,150*self.QS3.value()/100)
            self.mu.move(10*self.QS3.value()/100,20*self.QS3.value()/100)
        self.movie.stop()
        if self.movie_frame==0:
            self.movie.start()
            self.movie.jumpToFrame(1)
            self.movie.jumpToFrame(0)
            self.movie.stop()
        else:
            self.movie.start()
            self.movie.jumpToFrame(0)
            self.movie.jumpToFrame(1)
            self.movie.stop()
        self.sp.resize(35*self.QS3.value()/100,35*self.QS3.value()/100)
        self.sp.movie.setScaledSize(QSize(35*self.QS3.value()/100,35*self.QS3.value()/100))
        self.nx.resize(20*self.QS3.value()/100,20*self.QS3.value()/100)
        self.nx.movie.setScaledSize(QSize(20*self.QS3.value()/100,20*self.QS3.value()/100))
        self.bc.resize(20*self.QS3.value()/100,20*self.QS3.value()/100)
        self.bc.movie.setScaledSize(QSize(20*self.QS3.value()/100,20*self.QS3.value()/100))
        self.mu.resize(30*self.QS3.value()/100,30*self.QS3.value()/100)
        self.mu.movie.setScaledSize(QSize(30*self.QS3.value()/100,30*self.QS3.value()/100))
        self.so.resize(30*self.QS3.value()/100,30*self.QS3.value()/100)
        self.so.movie.setScaledSize(QSize(30*self.QS3.value()/100,30*self.QS3.value()/100))
        self.sp.movie.start()
        self.sp.movie.jumpToFrame(0)
        self.sp.movie.stop()
        self.nx.movie.start()
        self.nx.movie.jumpToFrame(0)
        self.nx.movie.stop()
        self.bc.movie.start()
        self.bc.movie.jumpToFrame(0)
        self.bc.movie.stop()
        self.so.movie.start()
        self.so.movie.jumpToFrame(0)
        self.so.movie.jumpToFrame(2)
        if self.QS1.value()>60 or self.QS1.value()==60:
            self.so.movie.jumpToFrame(1)
        if not(self.QS1.value()<30) and self.QS1.value()<60:
            self.so.movie.jumpToFrame(2)
        if self.QS1.value()>0 and self.QS1.value()<30:
            self.so.movie.jumpToFrame(3)
        if self.QS1.value()==0:
            self.so.movie.jumpToFrame(4)
        self.so.movie.stop()
        self.mu.movie.jumpToNextFrame()
    def about(self):
        self.about=QWidget()
        self.about.showMinimized()
        self.about.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.about.setWindowTitle((linecache.getline('files/data/main.txt',5)))
        self.about.setWindowIcon(QIcon('files/image/musicrun.gif'))
        self.about.setFixedSize(550,200)
        self.about.text1=QLabel(self.about)
        self.about.text1.setStyleSheet("font-size:20px;")
        self.about.text1.setText("music-island\n"+(linecache.getline('files/data/main.txt',8)).strip()+":deepin20.8\n"+(linecache.getline('files/data/main.txt',9)).strip()+":")
        self.about.text2=QLabel(self.about)
        self.about.text2.setStyleSheet("font-size:15px;")
        self.about.text2.move(0,100)
        self.about.text2.setText("github:https://github.com/3084793958/music-island.git\n"+"githubfast:https://githubfast.com/3084793958/music-island.git\n"+"gitlab:https://gitlab.com/3084793958/music-island.git")
        self.about.show()
    def show_about(self):
        self.play_check.play()
        self.about.showNormal()
        self.about.activateWindow()
    def dragEnterEvent(self,event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    def dropEvent(self, event):
        urls=[u for u in event.mimeData().urls()]
        for url in urls:
            if os.path.splitext(url.path()[1:])[1] in ['.mp3', '.au', '.midi', '.ogg', '.ra', '.ram', '.wav']:
                if len(self.fileslist)==0:
                    self.fileslist.append("/"+url.path()[1:])
                    self.play_music.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile((QtCore.QDir.current().absoluteFilePath(self.fileslist[0])))))
                    self.music_list=1
                else:
                    self.fileslist.append("/"+url.path()[1:])
        if self.music_list>len(self.fileslist):
            if len(self.fileslist)==0:
                self.music_list=0
            else:
                self.music_list=1
    def do_mediaplayer_statechanged(self, state):
        if state == QtMultimedia.QMediaPlayer.StoppedState:
            if len(self.fileslist)==0:
                if self.bn==False:
                    self.sp.movie = QMovie("files/image/start.gif")
                    self.mu.movie = QMovie("files/image/musicstop.gif")
                    self.sp.movie.gif=0
                    self.sp.setMovie(self.sp.movie)
                    self.sp.movie.setScaledSize(QSize(35*self.QS3.value()/100, 35*self.QS3.value()/100))
                    self.mu.setMovie(self.mu.movie)
                    self.mu.movie.setScaledSize(QSize(30*self.QS3.value()/100, 30*self.QS3.value()/100))
                    self.sp.movie.start()
                    self.sp.movie.stop()
                    self.mu.movie.start()
            else:
                if self.bn==False:
                    if self.music_list==len(self.fileslist):
                        self.music_list=1
                    else:
                        self.music_list+=1
                self.play_music.setMedia(QtMultimedia.QMediaContent(QUrl.fromLocalFile((QtCore.QDir.current().absoluteFilePath(self.fileslist[self.music_list-1])))))
                self.QS2.setValue(0)
                self.play_music.setPosition(0)
                if self.sp.movie.gif==1:
                    self.play_music.play()
    def contextMenuEvent(self, event):
        if self.hint==False:
            menu = QMenu(self)
            about_m = menu.addAction((linecache.getline('files/data/main.txt',5)))
            size_m = menu.addAction((linecache.getline('files/data/main.txt',11)))
            dock_c = menu.addAction((linecache.getline('files/data/main.txt',10)))
            hide = menu.addAction((linecache.getline('files/data/main.txt',4)))
            quitapp = menu.addAction((linecache.getline('files/data/main.txt',2)))
            action = menu.exec_(self.mapToGlobal(event.pos()))
            if action == quitapp:
                self.quit()
            if action == hide:
                self.play_check.play()
                if self.windowOpacity()>0.95:
                    for x in range(2000):
                        time.sleep(0.0001)
                        self.setWindowOpacity(1- x/2000)
                    self.showMinimized()
                    self.QS1.showMinimized()
                    self.QS2.showMinimized()
                    self.QS3.showMinimized()
            if action == about_m:
                self.show_about()
            if action == size_m:
                if self.QS3.isActiveWindow()==True:
                    self.QS3.setWindowOpacity(0)
                else:
                    self.QS3.activateWindow()
                    self.QS1.setWindowOpacity(0)
                    self.QS2.setWindowOpacity(0)
                    self.QS3.showNormal()
                    self.QS3.setWindowOpacity(1)
            if action == dock_c:
                if self.dock_d==0:
                    self.dock_d=1
                else:
                    self.dock_d=0
                self.movie.start()
                if self.dock_d==0:
                    self.movie=QMovie("files/image/dock.gif")
                    self.image.setMovie(self.movie)
                    self.movie.setScaledSize(QSize(200*self.QS3.value()/100,50*self.QS3.value()/100))
                    self.resize(200*self.QS3.value()/100,50*self.QS3.value()/100)
                    self.image.resize(200*self.QS3.value()/100,50*self.QS3.value()/100)
                    self.sp.move(80*self.QS3.value()/100,15*self.QS3.value()/200)
                    self.nx.move(120*self.QS3.value()/100,15*self.QS3.value()/100)
                    self.bc.move(55*self.QS3.value()/100,15*self.QS3.value()/100)
                    self.so.move(150*self.QS3.value()/100,10*self.QS3.value()/100)
                    self.mu.move(20*self.QS3.value()/100,10*self.QS3.value()/100)
                else:
                    self.movie=QMovie("files/image/dock2.gif")
                    self.image.setMovie(self.movie)
                    self.movie.setScaledSize(QSize(50*self.QS3.value()/100,200*self.QS3.value()/100))
                    self.resize(50*self.QS3.value()/100,200*self.QS3.value()/100)
                    self.image.resize(50*self.QS3.value()/100,200*self.QS3.value()/100)
                    self.sp.move(15*self.QS3.value()/200,80*self.QS3.value()/100)
                    self.nx.move(15*self.QS3.value()/100,120*self.QS3.value()/100)
                    self.bc.move(15*self.QS3.value()/100,55*self.QS3.value()/100)
                    self.so.move(10*self.QS3.value()/100,150*self.QS3.value()/100)
                    self.mu.move(10*self.QS3.value()/100,20*self.QS3.value()/100)
                self.movie.stop()
                if self.movie_frame==0:
                    self.movie.start()
                    self.movie.jumpToFrame(1)
                    self.movie.jumpToFrame(0)
                    self.movie.stop()
                else:
                    self.movie.start()
                    self.movie.jumpToFrame(0)
                    self.movie.jumpToFrame(1)
                    self.movie.stop()
if __name__=='__main__':
    app = QApplication(sys.argv)
    desktop_helper = MI()
    desktop_helper.show()
    sys.exit(app.exec_())
