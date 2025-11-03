from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("Codingal's text editor")
window.geometry("600x500")

def open_file():
    filepath = askopenfilename(
        filetype=[("Text Files", "*.txt"),("All Files", "*.*")]
    )

    if not filepath:
        return
    txt_edit.delete(1.0, END)

    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
    window.title(f"codingal's text editor {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return    
    
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    window.title(f"codingal's text editor {filepath}")

txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0)
btn_save.grid(row=1, column=0)
fr_buttons.grid(row=0, column=0)
txt_edit.grid(row=0, column=1)

window.mainloop()