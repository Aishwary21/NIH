import tkinter as tk
from tkinter import *
from link_search.open_site import open_link

if __name__ == "__main__":
    
    top = tk.Tk()
    top.title(string="Data Scrap")
    top.geometry("300x300")
    e1=tk.Label(top, 
            text="No. of Tweets :"
            )
    e1.place(relx = 0.11,
                 rely = 0.4
            )
    B1=tk.Button(top,
                text = "Save Data",
                command=open_link
                ).place(x=150,y=200)
    # B2=tk.Button(top,
    #           text="Show Data",
    #           command=
    #           ).place(x=80,y=200)
    
    top.mainloop()
