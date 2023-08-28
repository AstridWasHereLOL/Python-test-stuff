#from tkinter import *
#from plyer import notification
import DiscordRPC
import time

print("Go to Discord's Dev portal before continuing! https://discord.com/developers/applications")

appID = int(input("What's your Discord Application ID? "))

wantTS = input("\nDo you want a timestamp? (Y/N) ")

#print("\nYour Application ID is " + str(appID) + "!")

appDetails = input("Type to enter the Details line! (top text!) ")
appState = input("Type to enter the State line! (the line under Details!) ")
Limage = input("Large image key? (this is case sensitive!) ")
Simage = input("Small image key? (this is also case sensitive!) ")

print("\nRemember! CTRL + C to terminate! (Windows, Linux, and Mac!)")

rpc = DiscordRPC.RPC.Set_ID(app_id=appID)
if wantTS.lower() == "y":
    rpc.set_activity(
      state=appState,
      details=appDetails,
      large_image=Limage,
      small_image=Simage,
      timestamp=time.time()
    )
#elif wantTS == "y":
#     rpc.set_activity(
#      state=appState,
#      details=appDetails,
#      large_image=Limage,
#      small_image=Simage,
#      timestamp=time.time()
#    )
else:
     rpc.set_activity(
      state=appState,
      details=appDetails,
      large_image=Limage,
      small_image=Simage
    )

rpc.run()