from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QRadioButton, QCheckBox, QStyle
from PyQt5.QtCore import QThread, pyqtSignal, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtWidgets, uic
from datetime import datetime
from time import sleep
import sys, os
class ConvertThread(QThread):  
    data_downloaded = pyqtSignal(object)
    def __init__(self):
        QThread.__init__(self)
    def run(self):
        while True: 
            t = datetime.now()
            time_collection = t.hour, t.minute, t.second
            self.data_downloaded.emit(f'{time_collection}')
            sleep(0.1)
class mainwindowUI(QMainWindow):
    def __init__(self, parent=None):
        super(mainwindowUI, self).__init__(parent)
        uic.loadUi('UI/mainwindow.ui', self)
        self.loadUIelements()
        self.startClock()
        self.show()
    def loadUIelements(self):
        self.binHour1 = '0'
        self.binHour2 = '0'
        self.binMinute1 = '0'
        self.binMinute2 = '0'
        self.binSecond1 = '0'
        self.binSecond2 = '0'
        # COL, ROW
        self.Hour01 = self.findChild(QLabel, 'Hour01')
        self.Hour02 = self.findChild(QLabel, 'Hour02')
        self.Hour11 = self.findChild(QLabel, 'Hour11')
        self.Hour12 = self.findChild(QLabel, 'Hour12')
        self.Hour13 = self.findChild(QLabel, 'Hour13')
        self.Hour14 = self.findChild(QLabel, 'Hour14')
        
        self.lblHour1 = self.findChild(QLabel, 'lblHour1')
        self.lblHour2 = self.findChild(QLabel, 'lblHour2')
        
        self.Minute01 = self.findChild(QLabel, 'Minute01')
        self.Minute02 = self.findChild(QLabel, 'Minute02')
        self.Minute03 = self.findChild(QLabel, 'Minute03')
        self.Minute11 = self.findChild(QLabel, 'Minute11')
        self.Minute12 = self.findChild(QLabel, 'Minute12')
        self.Minute13 = self.findChild(QLabel, 'Minute13')
        self.Minute14 = self.findChild(QLabel, 'Minute14')
        
        self.lblMinute1 = self.findChild(QLabel, 'lblMinute1')
        self.lblMinute2 = self.findChild(QLabel, 'lblMinute2')
        
        self.Second01 = self.findChild(QLabel, 'Second01')
        self.Second02 = self.findChild(QLabel, 'Second02')
        self.Second03 = self.findChild(QLabel, 'Second03')
        self.Second11 = self.findChild(QLabel, 'Second11')
        self.Second12 = self.findChild(QLabel, 'Second12')
        self.Second13 = self.findChild(QLabel, 'Second13')
        self.Second14 = self.findChild(QLabel, 'Second14')
        
        self.lblSecond1 = self.findChild(QLabel, 'lblSecond1')
        self.lblSecond2 = self.findChild(QLabel, 'lblSecond2')

        self.line_8 = self.findChild(QLabel, 'line_8')
        self.line_9 = self.findChild(QLabel, 'line_9')

        self.grplbl1 = self.findChild(QLabel,'grplbl1')
        self.grplbl2 = self.findChild(QLabel,'grplbl2')
        self.grplbl4 = self.findChild(QLabel,'grplbl4')
        self.grplbl8 = self.findChild(QLabel,'grplbl8')
        
        self.radText = self.findChild(QRadioButton,'radText')
        self.radImg = self.findChild(QRadioButton,'radImg')
        self.chkLabel = self.findChild(QCheckBox,'chkLabel')
        self.chkVal = self.findChild(QCheckBox,'chkVal')
        
    def startClock(self):
        self.threads = []
        converter = ConvertThread()
        converter.data_downloaded.connect(self.on_data_ready)
        self.threads.append(converter)
        converter.start()
    def on_data_ready(self, text):
        try:
            self.setWindowTitle(f'{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}')
            # text = '12, 57, 9'
            text = text.replace('(','')
            text = text.replace(')','')
            text = text.replace(' ', '')
            text = text.split(',')
            if self.chkLabel.isChecked():
                self.lblHour1.setHidden(False)
                self.lblHour2.setHidden(False)
                self.lblMinute1.setHidden(False)
                self.lblMinute2.setHidden(False)
                self.lblSecond1.setHidden(False)
                self.lblSecond2.setHidden(False)
                self.line_8.setHidden(False)
                self.line_9.setHidden(False)
                if len(text[0]) == 1: self.lblHour1.setText('0'); self.lblHour2.setText(text[0])
                else: self.lblHour1.setText(text[0][0]); self.lblHour2.setText(text[0][1])
                if len(text[1]) == 1: self.lblMinute1.setText('0'); self.lblMinute2.setText(text[1])
                else: self.lblMinute1.setText(text[1][0]); self.lblMinute2.setText(text[1][1])
                if len(text[2]) == 1: self.lblSecond1.setText('0'); self.lblSecond2.setText(text[2])
                else: self.lblSecond1.setText(text[2][0]); self.lblSecond2.setText(text[2][1])
                self.grplbl1.setText('1')
                self.grplbl2.setText('2')
                self.grplbl4.setText('4')
                self.grplbl8.setText('8')
            else:
                self.grplbl1.setText(' ')
                self.grplbl2.setText(' ')
                self.grplbl4.setText(' ')
                self.grplbl8.setText(' ')
                self.lblHour1.setHidden(True)
                self.lblHour2.setHidden(True)
                self.lblMinute1.setHidden(True)
                self.lblMinute2.setHidden(True)
                self.lblSecond1.setHidden(True)
                self.lblSecond2.setHidden(True)
                self.line_8.setHidden(True)
                self.line_9.setHidden(True)
            if len(text[0]) == 1: self.binHour2 = "%04d" % int(bin(int(text[0][0]))[2:])
            else: self.binHour1 = "%02d" % int(bin(int(text[0][0]))[2:]); self.binHour2 = "%04d" % int(bin(int(text[0][1]))[2:])
            if len(text[1]) == 1: self.binMinute2 = "%04d" % int(bin(int(text[1][0]))[2:])
            else: self.binMinute1 = "%03d" % int(bin(int(text[1][0]))[2:]); self.binMinute2 = "%04d" % int(bin(int(text[1][1]))[2:])
            if len(text[2]) == 1: self.binSecond2 = "%04d" % int(bin(int(text[2][0]))[2:])
            else: self.binSecond1 = "%03d" % int(bin(int(text[2][0]))[2:]); self.binSecond2 = "%04d" % int(bin(int(text[2][1]))[2:])
            # binHour = "%03d" % int(bin(int(text[2]))[2:])
            # binMinute = "%07d" % int(bin(int(text[2]))[2:])
            # binSecond = "%07d" % int(bin(int(text[2]))[2:])

            if self.radText.isChecked():
                if self.chkVal.isChecked():
                    if not len(text[0]) == 1: self.Hour01.setText('1' if self.binHour1[1] == '1' else '0'); self.Hour02.setText('2' if self.binHour1[0] == '1' else '0')
                    else: self.Hour01.setText('0'); self.Hour02.setText('0')
                    self.Hour11.setText('1' if self.binHour2[3] == '1' else '0')
                    self.Hour12.setText('2' if self.binHour2[2] == '1' else '0')
                    self.Hour13.setText('4' if self.binHour2[1] == '1' else '0')
                    self.Hour14.setText('8' if self.binHour2[0] == '1' else '0')
                    
                    if not len(text[1]) == 1: self.Minute01.setText('1' if self.binMinute1[2] == '1' else '0'); self.Minute02.setText('2' if self.binMinute1[1] == '1' else '0'); self.Minute03.setText('4' if self.binMinute1[0] == '1' else '0')
                    else: self.Minute01.setText('0'); self.Minute02.setText('0'); self.Minute03.setText('0')
                    self.Minute11.setText('1' if self.binMinute2[3] == '1' else '0')
                    self.Minute12.setText('2' if self.binMinute2[2] == '1' else '0')
                    self.Minute13.setText('4' if self.binMinute2[1] == '1' else '0')
                    self.Minute14.setText('8' if self.binMinute2[0] == '1' else '0')
                    
                    if not len(text[2]) == 1: self.Second01.setText('1' if self.binSecond1[2] == '1' else '0'); self.Second02.setText('2' if self.binSecond1[1] == '1' else '0'); self.Second03.setText('4' if self.binSecond1[0] == '1' else '0')
                    else: self.Second01.setText('0'); self.Second02.setText('0'); self.Second03.setText('0')
                    self.Second11.setText('1' if self.binSecond2[3] == '1' else '0')
                    self.Second12.setText('2' if self.binSecond2[2] == '1' else '0')
                    self.Second13.setText('4' if self.binSecond2[1] == '1' else '0')
                    self.Second14.setText('8' if self.binSecond2[0] == '1' else '0')
                else:
                    if not len(text[0]) == 1: self.Hour01.setText(self.binHour1[1]); self.Hour02.setText(self.binHour1[0])
                    else: self.Hour01.setText('0'); self.Hour02.setText('0')
                    self.Hour11.setText(self.binHour2[3])
                    self.Hour12.setText(self.binHour2[2])
                    self.Hour13.setText(self.binHour2[1])
                    self.Hour14.setText(self.binHour2[0])
                    
                    if not len(text[1]) == 1: self.Minute01.setText(self.binMinute1[2]); self.Minute02.setText(self.binMinute1[1]); self.Minute03.setText(self.binMinute1[0])
                    else: self.Minute01.setText('0'); self.Minute02.setText('0'); self.Minute03.setText('0')
                    self.Minute11.setText(self.binMinute2[3])
                    self.Minute12.setText(self.binMinute2[2])
                    self.Minute13.setText(self.binMinute2[1])
                    self.Minute14.setText(self.binMinute2[0])
                    
                    if not len(text[2]) == 1: self.Second01.setText(self.binSecond1[2]); self.Second02.setText(self.binSecond1[1]); self.Second03.setText(self.binSecond1[0])
                    else: self.Second01.setText('0'); self.Second02.setText('0'); self.Second03.setText('0')
                    self.Second11.setText(self.binSecond2[3])
                    self.Second12.setText(self.binSecond2[2])
                    self.Second13.setText(self.binSecond2[1])
                    self.Second14.setText(self.binSecond2[0])
            if self.radImg.isChecked():
                self.chkVal.setEnabled(False)
                noIcon = QIcon(self.style().standardIcon(getattr(QStyle, 'SP_DialogNoButton')))
                noPixmap = QPixmap(noIcon.pixmap(QSize(32,32)))
                yesIcon = QIcon(self.style().standardIcon(getattr(QStyle, 'SP_DialogYesButton')))
                yesPixmap = QPixmap(yesIcon.pixmap(QSize(32,32)))
                if not len(text[0]) == 1: self.Hour01.setPixmap(yesPixmap if self.binHour1[1] == '1' else noPixmap); self.Hour02.setPixmap(yesPixmap if self.binHour1[0] == '1' else noPixmap)
                else: self.Hour01.setPixmap(noPixmap); self.Hour02.setPixmap(noPixmap)
                self.Hour11.setPixmap(yesPixmap if self.binHour2[3] == '1' else noPixmap)
                self.Hour12.setPixmap(yesPixmap if self.binHour2[2] == '1' else noPixmap)
                self.Hour13.setPixmap(yesPixmap if self.binHour2[1] == '1' else noPixmap)
                self.Hour14.setPixmap(yesPixmap if self.binHour2[0] == '1' else noPixmap)
                
                if not len(text[1]) == 1: self.Minute01.setPixmap(yesPixmap if self.binMinute1[2] == '1' else noPixmap); self.Minute02.setPixmap(yesPixmap if self.binMinute1[1] == '1' else noPixmap); self.Minute03.setPixmap(yesPixmap if self.binMinute1[0] == '1' else noPixmap)
                else: self.Minute01.setPixmap(noPixmap); self.Minute02.setPixmap(noPixmap); self.Minute03.setPixmap(noPixmap)
                self.Minute11.setPixmap(yesPixmap if self.binMinute2[3] == '1' else noPixmap)
                self.Minute12.setPixmap(yesPixmap if self.binMinute2[2] == '1' else noPixmap)
                self.Minute13.setPixmap(yesPixmap if self.binMinute2[1] == '1' else noPixmap)
                self.Minute14.setPixmap(yesPixmap if self.binMinute2[0] == '1' else noPixmap)
                
                if not len(text[2]) == 1: self.Second01.setPixmap(yesPixmap if self.binSecond1[2] == '1' else noPixmap); self.Second02.setPixmap(yesPixmap if self.binSecond1[1] == '1' else noPixmap); self.Second03.setPixmap(yesPixmap if self.binSecond1[0] == '1' else noPixmap)
                else: self.Second01.setPixmap(noPixmap); self.Second02.setPixmap(noPixmap); self.Second03.setPixmap(noPixmap)
                self.Second11.setPixmap(yesPixmap if self.binSecond2[3] == '1' else noPixmap)
                self.Second12.setPixmap(yesPixmap if self.binSecond2[2] == '1' else noPixmap)
                self.Second13.setPixmap(yesPixmap if self.binSecond2[1] == '1' else noPixmap)
                self.Second14.setPixmap(yesPixmap if self.binSecond2[0] == '1' else noPixmap)
            else:
                self.chkVal.setEnabled(True)
                if not self.radText.isChecked(): self.chkVal.setChecked(False)
            # for i, j in enumerate(binHour):
                # print(j)
            # print(binMinute)
            # print(binSecond)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainwindowUI()
    app.exec_()
