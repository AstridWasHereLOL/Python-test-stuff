from tkinter import *
from plyer import notification

ws = Tk()
ws.title("Really Cool Program.py")
ws.geometry('400x300')
ws['bg'] = 'lightgray'

def printValue():
    pname = player_name.get()
    #Label(ws, text=f'{pname}, Registered!', pady=20, bg='lightgray').pack()
    notification.notify(
    title = 'Recieved Message',
    message = pname,
    app_icon = "IMG_8635.ico",
    timeout = 10,
)


player_name = Entry(ws)
player_name.pack(pady=30)

Button(
    ws,
    bg="white",
    text="Send to Notification", 
    padx=10, 
    pady=5,
    command=printValue
    ).pack()

ws.mainloop()