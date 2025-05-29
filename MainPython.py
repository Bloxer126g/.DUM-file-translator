import tkinter as tk
from tkinter import filedialog
from tkinter import font as tkFont
import time

filetypes = (
    ('Translatable Files', '*.DUM *.TXT'),
    ('DUM Files', '*.DUM'),
    ('Text Files', '*.TXT'),
)

window = tk.Tk()

def Updatescreen():
  window.Destroy()
  #MsgBox

window.title(".DUM Translator (No Procceses)")


EmojiSize = tkFont.Font(family='Comic Sans MS', size=20, weight='bold')
FailSize = tkFont.Font(size=80, weight="bold", family="Comic Sans MS")
BoxSize = tkFont.Font(size=15, weight="normal", family="Comic Sans MS")

Regular = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "!", ".", "/", ",", "?", "-", "😀", "😢", "🔪", "😭"]
BruhDum = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "9", "8", "7", "6", "5", "4", "3", "2", "1", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ".", "!", ",", "/", "#", "@", "😢", "😀", "🐔", "😆"]


def trans():
  window.title(".DUM Translator (Translating...)")
  time.sleep(0.5)
  text_to_translate = text_box.get('1.0', 'end-1c')
  translation = []
  number = 0
  for char in text_to_translate:
    time.sleep(0.05)
    window.title(".DUM Translator (Translating..."+str(char)+"  i = "+str(number)+")")
    number += 1
    if char not in Regular:
      TransChar = char
    else:
      Index = Regular.index(char)
      TransChar = BruhDum[Index]
    translation.insert(len(translation)+1, TransChar)
  finaltrans = "".join(translation)
  window.title(".DUM Translator (Translation Complete)")
  text_box.delete("1.0","end")
  text_box.insert("1.0", finaltrans)
  window.title(".DUM Translator (No Procceses)")

def Untrans():
  window.title(".DUM Translator (Translating...)")
  time.sleep(0.5)
  text_to_translate = text_box.get('1.0', 'end-1c')
  translation = []
  number = 0
  for char in text_to_translate:
    time.sleep(0.05)
    window.title(".DUM Translator (Translating..."+str(char)+"  i = "+str(number)+")")
    number += 1
    if char not in BruhDum:
      TransChar = char
    else:
      Index = BruhDum.index(char)
      TransChar = Regular[Index]
    translation.insert(len(translation)+1, TransChar)
  finaltrans = "".join(translation)
  window.title(".DUM Translator (Translation Complete)")
  text_box.delete("1.0","end")
  text_box.insert("end", finaltrans)
  window.title(".DUM Translator (No Procceses)")

def file():
  window.title("Select a file")
  filename = tk.filedialog.askopenfilename(
    title='Select a file...',
    filetypes=filetypes,
  )
  print(filename)
  text_box.delete("1.0","end")
  with open(filename) as f:
    text_box.insert("1.0", f.read())
    window.title(filename)

def save():
  window.title("save as a DUM file")
  filename = tk.filedialog.askopenfilename(
    title='Save to a DUM file',
    filetypes=filetypes,
  )
  print(filename)
  with open(filename, "w") as f:
    window.title("[SAVING]"+filename)
    f.write(text_box.get('1.0', 'end-1c'))

def InsertText(Text):
  print("Inserting "+Text)
  text_box.insert("end", Text)


def EmojiMenu():
  emojis = tk.Tk()
  emojis.title("😀")

  happyw = tk.Button(emojis, text="😀", command=lambda: InsertText("😀"))
  sadw = tk.Button(emojis, text="😢", command=lambda: InsertText("😢"))
  knifew = tk.Button(emojis, text="🔪", command=lambda: InsertText("🔪"))
  cryw = tk.Button(emojis, text="😭", command=lambda: InsertText("😭"))

  happyw['font'] = EmojiSize
  sadw['font'] = EmojiSize
  knifew['font'] = EmojiSize
  cryw['font'] = EmojiSize

  happyw.grid(row=1,column=1)
  sadw.grid(row=1,column=2)
  knifew.grid(row=1,column=3)
  cryw.grid(row=1,column=4)

  emojis.mainloop()

def Configuration():
  config = tk.Tk()
  config.title("⚙️")

ButtonsWindow = tk.Tk()
text_box = tk.Text()
button = tk.Button(ButtonsWindow, text="Translate", command=trans)
button2 = tk.Button(ButtonsWindow, text="Untranslate", command=Untrans)
filebtn = tk.Button(ButtonsWindow, text="Select File", command=file)
savebtn = tk.Button(ButtonsWindow, text="Save File", command=save)
emojis = tk.Button(ButtonsWindow, text="Emojis", command=EmojiMenu)
configbtn = tk.Button(ButtonsWindow, text="Settings", command=Configuration)

text_box['font'] = BoxSize

configbtn.grid(row=1, column=0)
text_box.grid(row=2,column=0)
button.grid(row=3,column=0)
button2.grid(row=3,column=1)
filebtn.grid(row=1,column=2)
savebtn.grid(row=1,column=1)
emojis.grid(row=3,column=3)
InsertText("DUM translator update logs: \n        V0.2 BETA\nWhat's New?\n- File select menu to open .DUM and .TXT files\n- Support for translating a few symbols\n- New Emoji Menu (with translations)\nWhat's Changed?\n- New, larger text size for improved visibility (and a nice font!)\n- Capital letters now get translated")


print(text_box.get('1.0', 'end-1c'))
window.mainloop()

