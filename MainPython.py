import tkinter as tk
import time

window = tk.Tk()

window.title(".DUM Translator (No Procceses)")

Regular = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
BruhDum = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "9", "8", "7", "6", "5", "4", "3", "2", "1"]


def trans():
  window.title(".DUM Translator (Translating...)")
  time.sleep(0.5)
  text_to_translate = text_box.get('1.0', 'end-1c').lower()
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
  text_to_translate = text_box.get('1.0', 'end-1c').lower()
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
  text_box.insert("1.0", finaltrans)
  window.title(".DUM Translator (No Procceses)")

text_box = tk.Text()
button = tk.Button(window, text="Translate", command=trans)
button2 = tk.Button(window, text="Untranslate", command=Untrans)

text_box.pack()
button.pack()
button2.pack()




print(text_box.get('1.0', 'end-1c'))
window.mainloop()

