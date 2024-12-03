# yeah replet u.s. ka time batayega but agar aap is replit ko apne local computer me use karenge to yeah replit jis computer aap use karenge replit ko waha ka time batayega.
import time
timestamp1=time.strftime('%H:%M:%S%p %a')
print(timestamp1)
currenttime=int(time.strftime("%H"))
min=int(time.strftime("%M"))
clock=time.strftime("%p")
# print(clock)
if currenttime>=4 and currenttime <12 and clock.__eq__("AM"): # 4 to 12
    print("Good Morning!!")
elif currenttime>=12 and currenttime <17 and clock == "PM": # 12 to 5
    print("Good Afternoon!!")
elif currenttime>=17 and (currenttime <=23 and min<=30) and clock == "PM": # 5 to 11 30
    print("Good Evening!!")
else:
    print("Good Night!!") #11 30 to 3 59

if clock.__eq__("AM"):
    print("HEllo")

if clock=="AM":
    print("Yellow")
