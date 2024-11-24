from tkinter import *
from tkinter import ttk 
from tkinter import scrolledtext 

root = Tk()
root.title("Binary Decoder by MD.Bayazid")
root.geometry("1000x600")
root.resizable(False , False)
tabmanager = ttk.Notebook(root)

#functions 

def encode():
    b = ''
    text = asciiIn.get(1.0,END)
    if not text =="\n":
        for char in text:
            d = ord(char )
            e = format(d , '08b')
            b = b+' '+e
        print(b)
        binaryout.delete(1.0 , END)
        binaryout.insert(1.0 , b[1:])
    else:
        binaryout.delete(1.0 , END)
        binaryout.insert(1.0 , "please enter a text to encode!")




def decode():
    
    text = binaryIn.get(1.0 , END)
    if not text =="\n":
        print(text)
        codes = text.split()
        t = ""
        for code in codes:
            asciiCode = int(code , 2 )
            char = chr(asciiCode)
            t = t+char
        print(t)
        asciiout.delete(1.0 , END)
        asciiout.insert(1.0 , t)
    else:
        asciiout.delete(1.0 , END)
        asciiout.insert(1.0 , "please enter a binary code  to encode!")


tab1 = ttk.Frame(tabmanager)
tab2 = ttk.Frame(tabmanager)
tabmanager.add(tab1 , text="Decoder")
tabmanager.add(tab2 , text="Encoder" )
tabmanager.pack(padx=10 , pady=10)



lf = ttk.LabelFrame(tab1  , text="Binary Code")
lf.pack(padx  = 10 , pady = 10)

binaryIn = scrolledtext.ScrolledText(lf ,width = 800 , height = 10 , wrap = "word" , font=(10))
binaryIn.pack(padx  = 10 , pady = 10)

btnd = ttk.Button(tab1 , text = "Decode" ,width = 100 , command=decode)
btnd.pack()

lf2 = ttk.LabelFrame(tab1 , text="Decoded Text")
lf2.pack(padx=10 , pady=10)


asciiout = scrolledtext.ScrolledText(lf2 ,width = 800, height=15 ,font=(10) , wrap = "word" )
asciiout.pack(padx=10 , pady=10)



lf = ttk.LabelFrame(tab2  , text="Ascii Code")
lf.pack(padx  = 10 , pady = 10)

asciiIn = scrolledtext.ScrolledText(lf ,width = 800 , height = 10 , wrap = "word", font=(10))
asciiIn.pack(padx  = 10 , pady = 10)

btn1e = ttk.Button(tab2 , text = "Encode" ,width = 100 , command=encode )
btn1e.pack()

lf2 = ttk.LabelFrame(tab2 , text="Encoded Text")
lf2.pack(padx=10 , pady=10)


binaryout = scrolledtext.ScrolledText(lf2 ,width = 800, height=15 ,font=(10) , wrap = "word" )
binaryout.pack(padx=10 , pady=10)





root.mainloop()