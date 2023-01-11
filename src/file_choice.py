'''
link:
https://pythonru.com/uroki/dialogovye-vsplyvajushhie-okna-tkinter-9
This code write for project box_distributor:
https://github.com/Ni3nayka/box_distributor
Egor Bakay <egor_bakay@inbox.ru>
may 2022
'''

import tkinter.filedialog as fd

def file_choice():
    #filetypes = (("exel", "*.xlsx *.xls"),
    filetypes = (("wav", "*.wav"),
                    ("Любой", "*"))
    filename = fd.askopenfilename(title="Открыть файл", initialdir="/",
                                    filetypes=filetypes)
    
    return filename

if __name__=="__main__": 
    print(file_choice())