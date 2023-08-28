# what the fuck do i do
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from plyer import notification

# declare the window
window = Tk()
window.geometry("300x150")
window.title("Very Cool program.py")
window.configure(bg='lightgray')

# a label??????
label = tk.Label(
    text="my brudda"
)

# an entry?????????????????
entry = tk.Entry()

# a button???????????????????????????? oh hell naw!!!!
button = tk.Button(
    text="submit dat shit!!"
)

label.pack()
entry.pack()
button.pack()

window.mainloop()


#notification.notify(
#    title = 'testing',
#    message = 'message',
#    app_icon = None,
#    timeout = 10,
#)