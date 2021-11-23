# Reading PDF file using Tkinter and Py TTS
import pyttsx3
import PyPDF2
from tkinter.filedialog import *             # Import everything from Tkinter

file = askopenfilename()                     # Popup to select pdf file of your choice
pdfread = PyPDF2.PdfFileReader(file)         # Read file
total_pages = pdfread.numPages               # Calculating total number of pages in PDF

for num in range(0, total_pages):
    page = pdfread.getPage(num)
    new_voice_rate = 125                     # Increase/Decrease value to change speed
    text = page.extractText()
    player = pyttsx3.init()
    voices = player.getProperty('voices')
    for voice in voices:                           # Changing Voices
        player.setProperty('voice', voice.id)
        player.setProperty('rate', new_voice_rate)
        player.say(text)
        player.runAndWait()

# Ctrl F2 to discontinue
