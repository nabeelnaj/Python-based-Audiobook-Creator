"""import pyttsx3
import pypdf2
from tkinter.filedialog import *

book=askopenfilename()
pdfreader=pypdf2.PdfFileReader(book)
pages=pdfreader.numPages

for num in range(0,pages):
page=pdfreader.getPage(num)
text=page.extractText()
player=pyttsx3.init()
player.say(text)
player.runAndWait()
"""

import pyttsx3
import pypdf
from tkinter.filedialog import askopenfilename

# 1. Select the file
book = askopenfilename()

if book:
    # 2. Open the PDF
    reader = pypdf.PdfReader(book)
    pages = len(reader.pages)
    
    # 3. Initialize the speaker ONCE (outside the loop)
    player = pyttsx3.init()

    # 4. Loop through pages
    for num in range(pages):
        page = reader.pages[num]
        text = page.extract_text()
        
        if text:
            print(f"Reading page {num + 1}...")
            player.say(text)
            player.runAndWait()

