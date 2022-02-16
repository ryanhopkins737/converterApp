from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from fileTypes import *

window = Tk()
window.eval('tk::PlaceWindow . center')
window.title("File Converter")
icon = window.iconbitmap(r'C:\Users\ryan.hopkins\PycharmProjects\converterApp\spanner.ico')

bigPaddings = {'padx': 60, 'pady': 30}
smallPaddings = {'padx': 5, 'pady': 5}


def UploadFile(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)




title = ttk.Label(window, text="File Converter", font=("Helvetica", 30))
title.grid(column=0, row=0, columnspan=2, **bigPaddings)

il = ttk.Label(window, text="Input File Type: ", font=("Helvetica", 15))
il.grid(column=0, row=1, sticky=E, **smallPaddings)

itype = ttk.Combobox(window, width=15, values=file)
itype.grid(column=1, row=1, sticky=W, **smallPaddings)

ol = ttk.Label(window, text="Output File Type: ", font=("Helvetica", 15))
ol.grid(column=0, row=2, sticky=E, **smallPaddings)

otype = ttk.Combobox(window, width=15, values=file)
otype.grid(column=1, row=2, sticky=W, **smallPaddings)

filel = ttk.Label(window, text="Input File Path: ", font=("Helvetica", 15))
filel.grid(column=0, row=3, sticky=E, **smallPaddings)

iFilePath = ttk.Entry(window, width=35, font=("Helvetica", 15))
iFilePath.grid(column=1, row=3, sticky=W, **smallPaddings)

cButton = ttk.Button(window, text="Convert", width=20)
cButton.grid(column=1, row=1, sticky=E, **smallPaddings)

fuButton = ttk.Button(window, text='Upload File', command=lambda:UploadFile(), width=20)
fuButton.grid(column=1, row=2, sticky=E, **smallPaddings)

fdButton = ttk.Button(window, text='Download File', width=20)
fdButton.grid(column=1, row=2, **smallPaddings)

if __name__ == "__main__":
    window.mainloop()
