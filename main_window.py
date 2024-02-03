# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QImage

import requests
from functools import partial
from pytube import YouTube

from artist_window import Ui_ArtistWindow
from song_window import Ui_SongWindow
from scroll import Ui_Form
from sql1 import Songs, Artists, Lyrics, lyrics, artists, songs, ArtistInfo, session, song_urls


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(616, 499)
        MainWindow.setSizeIncrement(QtCore.QSize(5, 4))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("background-color: rgb(83, 83, 255);\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.search_line = QtWidgets.QLineEdit(self.centralwidget)
        self.search_line.setGeometry(QtCore.QRect(210, 100, 141, 31))
        self.search_line.textChanged.connect(self.filter)
        self.search_line.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.102, y1:0.153, x2:0.915, y2:0.988409, stop:0 rgba(255, 23, 18, 255), stop:1 rgba(255, 212, 122, 255));\n"
"padding: 3px;\n"
"")
        self.search_line.setText("")
        self.search_line.setMaxLength(23234)
        self.search_line.setObjectName("search_line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 110, 37);\n"
"font-weight: 600;\n"
"font-size: 30px;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(470, 50, 71, 31))
        self.checkBox.stateChanged.connect(self.filter)
        self.checkBox.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"padding: 5px;\n"
"border-radius: 4px;")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(470, 90, 70, 31))
        self.checkBox_2.stateChanged.connect(self.filter)
        self.checkBox_2.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"padding: 5px;\n"
"border-radius: 4px;\n"
"width: fit-content;")
        self.checkBox_2.setObjectName("checkBox_2")
        self.scrollArea_genre = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_genre.setGeometry(QtCore.QRect(10, 140, 80, 121))
        self.scrollArea_genre.setStyleSheet("background-color: rgb(75, 255, 48);")
        self.scrollArea_genre.setWidgetResizable(True)
        self.scrollArea_genre.setObjectName("scrollArea_genre")
        self.scrollArea_genre.setVisible(False)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 99, 119))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.innerWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.innerWidget.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.innerWidget.setObjectName("innerWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.innerWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 61, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout1.setObjectName("verticalLayout1")
        self.gridLayout.addWidget(self.innerWidget, 0, 0, 1, 1)
        self.scrollArea_genre.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_country = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_country.setGeometry(QtCore.QRect(10, 320, 80, 121))
        self.scrollArea_country.setStyleSheet("background-color: rgb(75, 255, 48);")
        self.scrollArea_country.setWidgetResizable(True)
        self.scrollArea_country.setObjectName("scrollArea_country")
        self.scrollArea_country.setVisible(False)
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 99, 119))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.innerWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.innerWidget_2.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.innerWidget_2.setObjectName("innerWidget_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.innerWidget_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 61, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout1_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout1_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout1_2.setObjectName("verticalLayout1_2")
        self.gridLayout_2.addWidget(self.innerWidget_2, 0, 0, 1, 1)
        self.scrollArea_country.setWidget(self.scrollAreaWidgetContents_2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 81, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 280, 81, 20))
        self.label_3.setObjectName("label_3")
        self.checkBox_filter = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_filter.setGeometry(QtCore.QRect(30, 50, 61, 31))
        self.checkBox_filter.setStyleSheet("font: 75 12pt \"Gadugi\";\n"
"background-color: rgb(255, 202, 8);\n"
"padding: 5px;\n"
"border-radius:5px;")
        self.checkBox_filter.setObjectName("checkBox_filter")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 616, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.genres = []
        self.countries = []

        for song in songs:
            if song.song_genre not in self.genres:
                self.genres.append(song.song_genre)

        for artist in artists:
            if artist.country not in self.countries:
                self.countries.append(artist.country)

        self.genre_checks = []
        self.country_checks = []

        for i in self.genres:
            text = i
            check_box = QtWidgets.QCheckBox(text)
            check_box.setFixedHeight(20)
            check_box.setStyleSheet("background-color: rgb(233, 100, 122); font-size: 10px")
            check_box.stateChanged.connect(self.filter)
            self.verticalLayout1.addWidget(check_box)
            self.genre_checks.append(check_box)
        self.innerWidget.setLayout(self.verticalLayout1)
        self.innerWidget.setStyleSheet('padding-left: 5px;')


        for i in self.countries:
            text = i
            check_box = QtWidgets.QCheckBox(text)
            check_box.setFixedHeight(20)
            check_box.setStyleSheet("background-color: rgb(233, 100, 122); font-size: 10px")
            check_box.stateChanged.connect(self.filter)
            self.verticalLayout1_2.addWidget(check_box)
            self.country_checks.append(check_box)
        self.innerWidget_2.setLayout(self.verticalLayout1_2)
        self.innerWidget_2.setStyleSheet('padding-left: 5px;')

        self.song_labels = []
        self.artist_labels = []

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.scroll_area()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music app"))
        self.search_line.setPlaceholderText(_translate("MainWindow", "Search: "))
        self.label.setText(_translate("MainWindow", "Music app"))
        self.checkBox.setText(_translate("MainWindow", "artists"))
        self.checkBox_2.setText(_translate("MainWindow", "songs"))
        self.label_2.setText(_translate("MainWindow", "filter by genre"))
        self.label_3.setText(_translate("MainWindow", "filter by country"))
        self.checkBox_filter.setText(_translate("MainWindow", "filter"))
        self.checkBox_filter.stateChanged.connect(self.filter)



    def show_artist_window(self, artist: Artists):
        self.artist_window = QtWidgets.QMainWindow()
        self.image_url = artist.get_info().artist_photo
        self.image = QImage()
        self.image.loadFromData(requests.get(self.image_url).content)

        self.pixmap = QPixmap(self.image)
        size = QSize(100, 100)
        resized = self.pixmap.scaled(size)
        self.ui = Ui_ArtistWindow()
        self.ui.setupUi(self.artist_window)
        self.ui.photo_label.setPixmap(resized)
        self.artist_window.show()
        self.ui.label_date.setText(self.ui.label_date.text() + str(artist.birth_date))
        self.ui.label_country.setText(self.ui.label_country.text() + artist.country)
        self.ui.labe_listeners.setText(self.ui.labe_listeners.text() + str(artist.monthly_listeners))
        if artist.last_name:
            self.artist_window.setWindowTitle(artist.first_name + artist.last_name)
            self.ui.label_artist.setText(f'{self.ui.label_artist.text()} {artist.first_name} {artist.last_name}')
        else:
            self.artist_window.setWindowTitle(artist.first_name)
            self.ui.label_artist.setText(f'{self.ui.label_artist.text()} {artist.first_name}')
        self.ui.info_text.setText(artist.get_info().content)
        self.ui.info_text.setStyleSheet('color: black;')

    def show_song_window(self, song: Songs):
        self.song_window = QtWidgets.QMainWindow()
        self.ui = Ui_SongWindow()
        self.ui.setupUi(self.song_window)
        self.song_window.show()
        self.song_window.setWindowTitle(song.song_name)
        self.ui.labelArtist.setText(f'{self.ui.labelArtist.text()} '
                                    f'{song.get_artist().first_name} {song.get_artist().last_name}')
        self.ui.label_name.setText(self.ui.label_name.text()+song.song_name)
        self.ui.label_genre.setText(self.ui.label_genre.text()+song.song_genre)
        self.ui.label_likes.setText(self.ui.label_likes.text()+str(song.youtube_likes))
        if song.get_lyrics():
            self.ui.lyrics_text.setText(song.get_lyrics().lyric)

    def scroll_area(self):
        self.scroll = QtWidgets.QScrollArea(MainWindow)
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet('background-color:green;')
        self.scroll.setGeometry(100, 150, 400, 300)

        self.scroll_widget = QtWidgets.QWidget()
        self.scroll.setWidget(self.scroll_widget)
        self.scroll_widget.setStyleSheet('background-color:blue;')

        self.scroll_layout = QtWidgets.QVBoxLayout()

        for artist in Artists.get_all():
            card = QtWidgets.QLabel()
            horizontal = QtWidgets.QHBoxLayout()
            card.setLayout(horizontal)
            card.setFixedHeight(70)
            card.setStyleSheet('background-color: gold;')
            name_label = QtWidgets.QLabel()
            button_info = QtWidgets.QPushButton('info')
            button_info.clicked.connect(partial(self.show_artist_window, artist))

            button_songs = QtWidgets.QPushButton('songs')
            button_songs.clicked.connect(partial(self.artist_song, artist))

            if artist.last_name:
                label_text = f"{artist.first_name} {artist.last_name}"
            else:
                label_text = f"{artist.first_name}"
            name_label.setText(label_text)

            name_label.setStyleSheet('''
            background-color: pink; border: 2px solid blue;
            padding: 3px;
            ''')
            horizontal.addWidget(name_label)
            horizontal.addWidget(button_info)
            horizontal.addWidget(button_songs)
            self.scroll_layout.addWidget(card)
            card.setVisible(False)
            self.artist_labels.append(card)


        self.scroll_widget.setLayout(self.scroll_layout)

        for song in songs:
            card = QtWidgets.QLabel()
            horizontal = QtWidgets.QHBoxLayout()
            vertical = QtWidgets.QVBoxLayout()
            vertical_label = QtWidgets.QLabel()
            vertical_label.setLayout(vertical)
            card.setLayout(horizontal)
            card.setFixedHeight(70)
            card.setStyleSheet('background-color: gold;')

            name_label = QtWidgets.QLabel()
            button_info = QtWidgets.QPushButton('info')
            button_info.clicked.connect(partial(self.show_song_window, song))

            button_play = QtWidgets.QPushButton('play')
            button_play.setFixedHeight(27)
            button_play.setStyleSheet('background-color: orange;')
            button_download = QtWidgets.QPushButton('download')
            button_download.setFixedHeight(27)
            button_download.setStyleSheet('background-color: darkred;')
            button_download.clicked.connect(partial(self.download_song, song.get_url().url))

            vertical.addWidget(button_play)
            vertical.addWidget(button_download)

            label_text = f"{song.song_name}"
            name_label.setText(label_text)

            name_label.setStyleSheet('''
                        background-color: pink; border: 2px solid blue;
                        padding: 3px;
                        ''')
            horizontal.addWidget(name_label)

            horizontal.addWidget(button_info)
            horizontal.addWidget(vertical_label)
            self.scroll_layout.addWidget(card)
            self.song_labels.append(card)

    def artist_song(self, artist: Artists):
        self.artists_songs = QtWidgets.QWidget()
        self.ui_scroll = Ui_Form()
        self.ui_scroll.setupUi(self.artists_songs)
        self.artists_songs.show()

        for song in artist.get_all_songs():
            card = QtWidgets.QLabel()
            horizontal = QtWidgets.QHBoxLayout()
            vertical = QtWidgets.QVBoxLayout()
            vertical_label = QtWidgets.QLabel()
            vertical_label.setLayout(vertical)
            card.setLayout(horizontal)
            card.setFixedHeight(70)
            card.setStyleSheet('background-color: gold;')

            name_label = QtWidgets.QLabel()
            button_info = QtWidgets.QPushButton('info')
            button_info.clicked.connect(partial(self.show_song_window, song))

            button_play = QtWidgets.QPushButton('play')
            button_play.setFixedHeight(27)
            button_play.setStyleSheet('background-color: orange;')
            button_download = QtWidgets.QPushButton('download')
            button_download.setFixedHeight(27)
            button_download.setStyleSheet('background-color: darkred;')
            button_download.clicked.connect(partial(self.download_song, song.get_url().url))

            vertical.addWidget(button_play)
            vertical.addWidget(button_download)

            label_text = f"{song.song_name}"
            name_label.setText(label_text)

            name_label.setStyleSheet('''
                        background-color: pink; border: 2px solid blue;
                        padding: 3px;
                        ''')
            horizontal.addWidget(name_label)

            horizontal.addWidget(button_info)
            horizontal.addWidget(vertical_label)
            self.ui_scroll.verticalLayout1.addWidget(card)

    def filter(self):
        text = self.search_line.text()

        if self.checkBox.isChecked() or self.checkBox_filter.isChecked():
            for i in range(len(artists)):
                if artists[i].last_name:
                    full_name = f'{artists[i].first_name.lower()} {artists[i].last_name.lower()}'
                else:
                    full_name =artists[i].first_name.lower()
                if text == '':
                    self.artist_labels[i].show()
                elif full_name.startswith(text.lower()) and text != '':
                    self.artist_labels[i].show()
                    self.scroll_layout.update()

                else:
                    self.artist_labels[i].setVisible(False)
        else:
            for i in range(len(artists)):
                self.artist_labels[i].setVisible(False)

        if self.checkBox_2.isChecked():
            for i in range(len(songs)):
                if text == '':
                    self.song_labels[i].show()
                elif songs[i].song_name.lower().startswith(text.lower()) and text != '':
                    self.song_labels[i].show()
                    self.scroll_layout.update()

                else:
                    self.song_labels[i].setVisible(False)
        else:
            for i in range(len(songs)):
                self.song_labels[i].setVisible(False)

        if self.checkBox_filter.isChecked():
            self.scrollArea_genre.show()
            self.scrollArea_country.show()


            for i in range(len(self.genres)):
                if self.genre_checks[i].isChecked():
                    for j in range(len(songs)):
                        if (songs[j].song_genre == self.genre_checks[i].text() and
                                songs[j].song_name.lower().startswith(text.lower())):
                            self.song_labels[j].show()
                else:
                    for j in range(len(songs)):
                        if songs[j].song_genre == self.genre_checks[i].text():
                            self.song_labels[j].setVisible(False)

            for i in range(len(self.countries)):
                if self.country_checks[i].isChecked():
                    for j in range(len(artists)):
                        if (artists[j].country == self.country_checks[i].text() and
                                artists[j].first_name.lower().startswith(text.lower())):
                            self.artist_labels[j].show()
                else:
                    for j in range(len(artists)):
                        if (artists[j].country == self.country_checks[i].text()):
                            self.artist_labels[j].setVisible(False)
                        # else:
                        #     self.artist_labels[j].setVisible(False)



        else:
            self.scrollArea_genre.setVisible(False)
            self.scrollArea_country.setVisible(False)



    def download_song(self, song_url):
        url = song_url
        video = YouTube(url)
        stream = video.streams.filter(only_audio=True).first()
        stream.download(filename=f'{video.title}.mp3')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
