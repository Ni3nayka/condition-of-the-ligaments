'''
This code write for project box_distributor:
https://github.com/Ni3nayka/box_distributor
The previous project was taken as the basis of this <SuCCess>:
https://github.com/Ni3nayka/SuCCess
Egor Bakay <egor_bakay@inbox.ru>
july 2022
'''
    
from tkinter import *
from tkinter import messagebox
from time import sleep
from os import path
#import webbrowser

from file_choice import file_choice

class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder=None):
        super().__init__(master)

        if placeholder is not None:
            self.placeholder = placeholder
            self.placeholder_color = 'grey'
            self.default_fg_color = self['fg']

            self.bind("<FocusIn>", self.focus_in)
            self.bind("<FocusOut>", self.focus_out)

            self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def focus_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def focus_out(self, *args):
        if not self.get():
            self.put_placeholder()

class graphics:
    
    def __init__(self,title='SuCCess graphics Debug',comanda_start=0,comanda_example=0):
        self.name = title
        self.window = Tk()
        self.window.title(self.name)
        self.window.geometry('300x150')
        #self.window.resizable(0, 0)

        self.file_path = ""
        self.comanda_start = comanda_start
        if self.comanda_start==0: self.comanda_start = self.plug
        self.comanda_example = comanda_example
        if self.comanda_example==0: self.comanda_example = self.plug

        self.lbl_file = Label(text="")
        self.lbl_file.place(relx=.5, rely=.1, anchor="c")

        self.lbl = Label(text="выберите файл <обзор> и нажмите <старт>")
        self.lbl.place(relx=.5, rely=.2, anchor="c")

        self.start_audio = EntryWithPlaceholder(master=self.window,placeholder="время начала аудио (в милисекундах)")
        self.start_audio.place(relx=.5, rely=.4, anchor="c",height = 25,width = 280)

        self.end_audio = EntryWithPlaceholder(master=self.window,placeholder="время конца аудио (в милисекундах)")
        self.end_audio.place(relx=.5, rely=.6, anchor="c",height = 25,width = 280)
        
        # link_button = Button(text="ссылка", command=self.open_link)
        # link_button.place(relx=.12, rely=.77, anchor="c",height = 40,width = 70)

        # example_button = Button(text="пример", command=self.add_example)
        # example_button.place(relx=.37, rely=.77, anchor="c",height = 40,width = 70)

        file_button = Button(text="обзор", command=self.test_file_path)
        file_button.place(relx=.25, rely=.85, anchor="c",height = 40,width = 145)

        start_button = Button(text="старт", command=self.start_operating)
        start_button.place(relx=.75, rely=.85, anchor="c",height = 40,width = 145)

    def test_file_path(self):
        #self.file_path = "D:/GitHub/_cache/condition-of-the-ligaments/src/test/Соловьева_НВ_1977_14_06_2022_185051_GX010425.wav"
        self.file_path = file_choice()
        self.lbl_file.config(text=self.file_path)
        self.lbl.config(text="нажмите <старт>")
        self.comanda_start(self.file_path,"view")
        #self.message_entry.config(text=self.file_path)

    # def add_example(self):
    #     self.comanda_example()
    #     self.lbl.config(text="пример создан")

    def start_operating(self):
        
        # def test(A):
        #     alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        #     B = A.get().upper()
        #     if B=="": return True
        #     for a in B:
        #         try: alphabet.index(a)
        #         except ValueError: return True
        #     return False

        # if test(self.message_sport_category):
        #     messagebox.showerror("SaveSystem", "столбец разрядов (1) введен неверно")
        #     return
        # if test(self.message_start_rez):
        #     messagebox.showerror("SaveSystem", "первый столбец результатов (2) введен неверно")
        #     return
        # if test(self.message_end_rez):
        #     messagebox.showerror("SaveSystem", "последний столбец результатов (3) введен неверно")
        #     return
        # if not self.message_start_line.get().isdigit(): 
        #     messagebox.showerror("SaveSystem", "первая строка результатов (4) введена неверно")
        #     return
        # if not self.message_end_line.get().isdigit(): 
        #     messagebox.showerror("SaveSystem", "последняя строка результатов (5) введена неверно")
        #     return
        # if test(self.message_rang): 
        #     messagebox.showerror("SaveSystem", "столбец получаемых разрядов (5) введен неверно")
        #     return
        if not path.exists(self.file_path):
            messagebox.showerror("SaveSystem", "по такому пути нет такого файла")
            return
             
        a = self.start_audio.get()
        b = self.end_audio.get()
        try: a = int(a)
        except ValueError: a = None
        try: b = int(b)
        except ValueError: b = None
        print(a,b)

        self.lbl.config(text="файл обрабатывается.....")
        self.window.update()
        self.comanda_start(self.file_path,"operating",a,b)
        #sleep(0.5)
        self.lbl.config(text="файл обрабобтан")
        #print(self.file_path)

    def loop(self):
        self.window.mainloop()

    def plug(self,*arg): # pass
        pass
        #print(self.get_data())
    
        
    

if __name__=="__main__":
    # https://pythonguides.com/python-tkinter-button/    картинка в кнопке
    
    window = graphics()
    window.loop()