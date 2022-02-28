import tkinter
import citi


root= tkinter.Tk()
root.geometry('300x150')
root.resizable(False,False)
root.title('Citiaon Machine')
doi_var= tkinter.StringVar()
doi_label= tkinter.Label(root, text='Name of the article:')
doi_label.pack(fill='x',expand=True)
doi= tkinter.Entry(root, textvariable=doi_var)
doi.pack(fill='x', expand=True)
doi.focus()
def cm():
    txt= doi.get()
    return citi.cA.cmd(txt)

btn= tkinter.Button(root, text='Get', command=cm)
btn.pack(fill='x', expand= True, pady=10)
textbox= tkinter.Text(root)
textbox.pack(fill='x', expand=True)
textbox.insert(tkinter.END, citi.cB())
root.mainloop()
