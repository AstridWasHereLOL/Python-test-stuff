from pypresence import Presence
import time
from tkinter import *
from plyer import notification

if __name__ == '__main__':
    def readyCallback(current_user):
        print('Our user: {}'.format(current_user))

    def disconnectedCallback(codeno, codemsg):
        print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
            codeno, codemsg
        ))

    def errorCallback(errno, errmsg):
        print('An error occurred! Error {}: {}'.format(
            errno, errmsg
        ))
        
    # Note: 'event_name': callback
    callbacks = {
        'ready': readyCallback,
        'disconnected': disconnectedCallback,
        'error': errorCallback,
    }


app = Tk()
app.title("Custom Discord RPC via Tkinter")
#app.geometry('400x300')
#app['bg'] = 'lightgray'

def startRPC():
    appID = appIDe.get()
    wantTS = wantTSint.get()
    #print("\nYour Application ID is " + str(appID) + "!")
    appDetails = appDetailse.get()
    appState = appStatee.get()
    Limage = Limagee.get()
    Simage = Simagee.get()
    RPC = Presence(appID, pipe=0, loop=None, handler=None)
    if int(wantTS) == 1:
        RPC.connect()
        RPC.update(state=appState)
        RPC.update(details=appDetails)
        RPC.update(large_image=Limage)
        RPC.update(small_image=Simage)
        #RPC.update(large_text=LimageTEXT)
        #RPC.update(small_text=SimageTEXT)
        #RPC.update(start=time.time())
        notification.notify(
        title = 'Discord RPC Control',
        message = "Discord RPC successfully started!",
        app_icon = "app.ico",
        timeout = 10,
        )
    else:
        RPC.connect()
        RPC.update(state=appState)
        RPC.update(details=appDetails)
        RPC.update(large_image=Limage)
        RPC.update(small_image=Simage)
        #RPC.update(large_text=LimageTEXT)
        #RPC.update(small_text=SimageTEXT)
        notification.notify(
        title = 'Discord RPC Control',
        message = "Discord RPC successfully started!",
        app_icon = "app.ico",
        timeout = 10,
        )

def stopRPC():
    appID = appIDe.get()
    RPC = Presence(appID)
    RPC.connect()
    RPC.clear()
    RPC.close()
    notification.notify(
    title = 'Discord RPC Control',
    message = "Discord RPC successfully stopped!",
    app_icon = "app.ico",
    timeout = 10,
    )
    

#app ID
appIDlabelText=StringVar()
appIDlabelText.set("Enter the Application ID")
appIDlabelDir=Label(app, textvariable=appIDlabelText, height=2,width=20)
appIDlabelDir.grid(row=1,column=1)

appIDe=Entry(app,width=25)
appIDe.grid(row=1,column=3)

#timestamp
wantTSlabelText=StringVar()
wantTSlabelText.set("Do you want a timestamp?")
wantTSlabelDir=Label(app, textvariable=wantTSlabelText, height=2,width=20)
wantTSlabelDir.grid(row=8,column=1)

wantTSint = IntVar()
wantTSe = Checkbutton(app,variable=wantTSint, onvalue=1, offvalue=0)
wantTSe.grid(row=8,column=3)

#details line
appDetailslabelText=StringVar()
appDetailslabelText.set("What will be the Details?")
appDetailslabelDir=Label(app, textvariable=appDetailslabelText, height=2,width=20)
appDetailslabelDir.grid(row=2,column=1)


appDetailse=Entry(app,width=25)
appDetailse.grid(row=2,column=3)

#state line
appStatelabelText=StringVar()
appStatelabelText.set("What will be the State?")
appStatelabelDir=Label(app, textvariable=appStatelabelText, height=2,width=20)
appStatelabelDir.grid(row=3,column=1)


appStatee=Entry(app,width=25)
appStatee.grid(row=3,column=3)

#large image line
LimagelabelText=StringVar()
LimagelabelText.set("What is the Large image?")
LimagelabelDir=Label(app, textvariable=LimagelabelText, height=2,width=20)
LimagelabelDir.grid(row=4,column=1)


Limagee=Entry(app,width=25)
Limagee.grid(row=4,column=3)

#small image line
SimagelabelText=StringVar()
SimagelabelText.set("What is the Small image?")
SimagelabelDir=Label(app, textvariable=SimagelabelText, height=2,width=20)
SimagelabelDir.grid(row=5,column=1)


Simagee=Entry(app,width=25)
Simagee.grid(row=5,column=3)

Button(
    app,
    bg="white",
    text="Start RPC", 
    padx=10, 
    pady=5,
    command=startRPC,
    ).grid(row=9,column=2)

Button(
    app,
    bg="white",
    text="Stop RPC", 
    padx=10, 
    pady=5,
    command=stopRPC,
    ).grid(row=10,column=2)

app.mainloop()