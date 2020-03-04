from PyQt4 import QtGui, QtCore 
from morse import Ui_Dialog as morse
import time
import sys
try:
    import winsound
except ImportError:
    print("sie verwenden kein Windowssystem")
    
    
    
class MeinDialog(QtGui.QDialog, morse): 
    def __init__(self): 
        QtGui.QDialog.__init__(self) 
        self.setupUi(self)
        
        self.a = 0
        self.b = 0
        self.text=''
        self.morsetext=''
        self.fromMorse = True
        
        self.CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
                     'D': '-..',    'E': '.',      'F': '..-.',
                     'G': '--.',    'H': '....',   'I': '..',
                     'J': '.---',   'K': '-.-',    'L': '.-..',
                     'M': '--',     'N': '-.',     'O': '---',
                     'P': '.--.',   'Q': '--.-',   'R': '.-.',
                     'S': '...',    'T': '-',      'U': '..-',
                     'V': '...-',   'W': '.--',    'X': '-..-',
                     'Y': '-.--',   'Z': '--..',

                  '0': '-----',  '1': '.----',  '2': '..---',
                  '3': '...--',  '4': '....-',  '5': '.....',
                  '6': '-....',  '7': '--...',  '8': '---..',
                  '9': '----.',  ' ': '|' ,     '\n': '.......',
                  '!': '---.',   '?': '..--..', ':': '---...',
                  '.': '.-.-.-', ',': '--..--', '@': '.--.-.',
                  '"': '.-..-.', '/': '-..-.',  '-': '-....-',
                  '=': '-...-',  "'": '.----.'   
        }
        self.CODE_REVERSED = {value:key for key,value in self.CODE.items()}
        



        
        self.connect(self.Bsignal,QtCore.SIGNAL("pressed()"), self.timeon) 
        self.connect(self.Bsignal,QtCore.SIGNAL("released()"), self.write) 
        self.connect(self.Btranslate,QtCore.SIGNAL("clicked()"), self.translate) 
        self.connect(self.Bclear,QtCore.SIGNAL("clicked()"), self.cleart) 
        self.connect(self.pushButton,QtCore.SIGNAL("clicked()"), self.toggletranslate) 

    
  
    
    def toggletranslate(self):
        if self.fromMorse:
            self.fromMorse = False
            self.label.setText("to Morse")
        else:
            self.fromMorse = True
            self.label.setText("from Morse")
    
    def cleart(self):
        self.text = ''
        self.morsetext = ''
        
    def timeon(self):
        self.a=time.time()
        
        self.b=self.a - self.b
        
        if self.b > 0.5:
            self.text+= ' '
        if self.b > 1.5:
            self.text+= ' | '
        
    def write(self):
        self.b=time.time()
        self.b = self.b-self.a
        
        if self.b > 0.2:
            self.text+= '-'
        else:
            self.text+='.'
        
        self.textEdit.setText(self.text)
        
        self.b=time.time()
    
    def translate(self):
        def to_morse(self,s):
            return ' '.join(self.CODE.get(i.upper()) for i in s)
        def from_morse(self,s):
            return ''.join(self.CODE_REVERSED.get(i) for i in s.split())
            
        if self.fromMorse:
            text = str(self.textEdit.toPlainText())
            self.textEdit.setText(from_morse(self,text))
            self.text=''
        else:
            text = str(self.textEdit.toPlainText())
            self.textEdit.setText(to_morse(self,text))
            self.text=''


app = QtGui.QApplication(sys.argv) 
dialog = MeinDialog() 
dialog.show() 
sys.exit(app.exec_())

