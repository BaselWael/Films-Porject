from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import sys
from os import path
from Quert_Term import query_term
from TorrentData import torrent
import socket
import time
import os
import urllib.request


FORM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),'main.ui'))
class MainApp(QMainWindow,FORM_CLASS):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.UI()
        self.Buttons()

        #self.progress_bar()


    def UI(self):
        self.setWindowTitle("MovieDownload")

    def Buttons(self):
        self.pushButton.clicked.connect(self.CheckMovieButton)
        self.save_location_button.clicked.connect(self.location_button)
        self.pushButton_download.clicked.connect(self.torreentUrlDownload)
        self.pushButton_Checkquality.clicked.connect(self.QualityCheck)

    def CheckMovieButton(self):
        movie_name = self.lineEdit.text()
        data = movie_name
        film_name = query_term(film_name=movie_name).Check()
        data = torrent(film_name=film_name,limit=50).GetFilmNames()
        lst = []
        self.comboBox.clear()
        self.comboBox_Quality.clear()
        for i in data:
            self.comboBox.addItem(i)
        QMessageBox.information(self,"Notice","Please save location first then download")



        QApplication.processEvents()
    def QualityCheck(self):
        Film_name_text = open('Filmname.txt', "w+")
        item = str(self.comboBox.currentText())
        Film_name_text.write(item)
        Film_name_text.close()

        try:
            if self.comboBox.currentIndex != 0:
                quality = torrent(film_name=str(self.comboBox.currentText()), limit=50).GetQuality()
                type = torrent(film_name=str(self.comboBox.currentText()), limit=50).GetType()
                size = torrent(film_name=str(self.comboBox.currentText()), limit=50).GetSize()
                for (qual,typ,siz) in zip(quality,type,size):
                    self.comboBox_Quality.addItem(f"Quality : {qual} ,Type : {typ} ,Size : {siz}")
            else:
                quality = torrent(film_name=self.comboBox.currentText, limit=50).GetQuality()
                #type = torrent(film_name=self.comboBox.currentIndex, limit=50).GetType()
                #size = torrent(film_name=self.comboBox.currentIndex, limit=50).GetSize()
                for qual in quality:
                    self.comboBox_Quality.addItem(f"Quality : {qual}")
        except Exception:
            print("Error")

    def torreentUrlDownload(self):
        '''item = str(self.comboBox.currentText())
        Film_name_text = open('Filmname.txt',"w+")
        Film_name_text.write(item)
        Film_name_text.close()'''
        time.sleep(1)
        quality = torrent(film_name=str(self.comboBox.currentText()), limit=50).GetQuality()
        type = torrent(film_name=str(self.comboBox.currentText()), limit=50).GetType()
        size = torrent(film_name=str(self.comboBox.currentText()), limit=50).GetSize()
        data = str(self.comboBox_Quality.currentText())
        for (qual, typ, siz) in zip(quality, type, size):
            time.sleep(1)
            if qual in data or siz in data:
                TorrentUrl = torrent(film_name=self.comboBox.currentText(),limit=50).GetTorrentUrl(quality=qual,type=typ,size=siz)
                self.size = float(siz.split(" ")[0])
                break
        #location = os.getcwd()
        opener = urllib.request.URLopener()
        opener.addheader('User-Agent', 'Mozilla/5.0')
        filename, headers = opener.retrieve(TorrentUrl,str(self.comboBox.currentText())+'.Torrent')
        filmname = str(self.comboBox.currentText())
        ip_address = '127.0.0.1'
        port = 8080  # The same port as used by the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, port))

        film_name2 = rf"{self.comboBox.currentText()}.Torrent"
        film_name_encode = film_name2.encode()
        s.sendall(film_name_encode)  # sec sending location+filmname
        time.sleep(1)
        self.Calculate_progs_DS_Rem()
        QApplication.processEvents()


    def location_button(self):
        self.save = QFileDialog.getExistingDirectory(self, "Select Download Directory")
        self.lineEdit_2.setText(self.save)
        data = rf"{self.save}"
        os.startfile("ServerTest.exe")
        ip_address ='127.0.0.1'
        port = 8080  # The same port as used by the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, port))
        location_encoding = data.encode()
        s.sendall(location_encoding)  # first sending location
        QApplication.processEvents()

    def download_speed(self): # to put download speed
        try:
            data = ''
            self.speed = self.respone()
            self.label_downloadspeedcurrent.setText(f"{self.speed} k/b")
        except Exception as e:
            print(f"error download speed :  {e}")
        QApplication.processEvents()

    def FileSize(self): # to get file size
        try:
            quality = torrent(film_name=str(self.comboBox.currentText()), limit=50).GetQuality()
            type = torrent(film_name=str(self.comboBox.currentText()), limit=50).GetType()
            size = torrent(film_name=str(self.comboBox.currentText()), limit=50).GetSize()
            data = str(self.comboBox_Quality.currentText())
            for (qual, typ, siz) in zip(quality, type, size):
                time.sleep(1)
                if qual in data or siz in data:
                    TorrentUrl = torrent(film_name=self.comboBox.currentText(), limit=50).GetTorrentUrl(quality=qual,type=typ,size=siz)
                    size = float(siz.split(" ")[0])
                    return size
        except Exception as e:
            return f"error filesize : {e}"

    def Calculate_progs_DS_Rem(self): # to calculate everything
        while True:
            try:
                #time.sleep(1)
                self.progress_bar()
                self.download_speed()
                #self.Remaining()
            except Exception as e:
              print(f"error {e}")
            QApplication.processEvents()
    def progress_bar(self):
        try:
            self.progress = self.respone()
            self.progressBar.setValue(int(float(self.progress)))
        except Exception as e:
            print(f"error progressbar : {e}")
    def downloaded(self):
        return float(self.progress)

    def Remaining(self): # to calculate time of file download
        try:
            progress = self.downloaded() / 100
            size = self.FileSize()
            calc1 = progress*size
            if float(self.speed) == 0:
                result = "infinity"
            else:
                result = str((size-calc1) / float(self.speed))
            self.label_Remaining.setText(result)
        except Exception as e:
            print(f"error remaining : {e}")
        QApplication.processEvents()

    def respone(self): # Respone Data always
        ip_address = "127.0.0.1"
        port = 8080  # The same port as used by the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip_address, port))
        s.listen(5)
        conn, address = s.accept()
        data = conn.recv(1024).decode()
        conn.close()
        return data



def Main_():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    Main_()
