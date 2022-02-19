##########





from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, 
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QStyleFactory,
        QVBoxLayout, QTextBrowser, QLineEdit, QPushButton)


class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)
        self.originalPalette = QApplication.palette()
        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())   
        styleLabel = QLabel("&be tartib url, token:, username, passwordeto vared kon ")
        self.defaultPushButton = QPushButton(self)    
        styleLabel.setBuddy(styleComboBox)
        self.useStylePaletteCheckBox = QCheckBox("&Use style's standard palette")
        self.useStylePaletteCheckBox.setChecked(True)
        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createBottomLeftTabWidget()
        self.createBottomRightGroupBox()       
        styleComboBox.activated[str].connect(self.changeStyle)
        self.useStylePaletteCheckBox.toggled.connect(self.changePalette)        
        topLayout = QHBoxLayout()
        topLayout.addWidget(styleLabel)
        url = QLineEdit()
        topLayout.addWidget(url)
        token = QLineEdit()
        topLayout.addWidget(token)  
        username = QLineEdit()
        topLayout.addWidget(username)
        password = QLineEdit()
        topLayout.addWidget(password)
        topLayout.addWidget(styleComboBox)
        topLayout.addStretch(1)
        topLayout.addWidget(self.useStylePaletteCheckBox)       
        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomLeftTabWidget, 2, 0)
        mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)   
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)
        self.setWindowTitle("Styles")
        self.changeStyle('Windows')

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        self.changePalette()
        
    def changePalette(self):
        if (self.useStylePaletteCheckBox.isChecked()):
            QApplication.setPalette(QApplication.style().standardPalette())
        else:
            QApplication.setPalette(self.originalPalette)

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Group 1")

        text_browser = QTextBrowser()
        layout = QVBoxLayout()

        layout = QVBoxLayout()
        layout.addWidget(text_browser)
        self.topLeftGroupBox.setLayout(layout)       
           
    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Group 2")
        text_browser = QTextBrowser()
        layout = QVBoxLayout()
        layout = QVBoxLayout()
        layout.addWidget(text_browser)
        self.topRightGroupBox.setLayout(layout)
    
    def createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget = QGroupBox("Group 4")      
        text_browser = QTextBrowser()
        layout = QVBoxLayout()
        layout = QVBoxLayout()
        layout.addWidget(text_browser)
        self.bottomLeftTabWidget.setLayout(layout)

    def createBottomRightGroupBox(self,text=None):
        self.bottomRightGroupBox = QGroupBox("Group 3")       
        text_browser = QTextBrowser()
        layout = QVBoxLayout()
        layout = QVBoxLayout()
        layout.addWidget(text_browser)
        self.bottomRightGroupBox.setLayout(layout)
      
        
        




if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_()) 




