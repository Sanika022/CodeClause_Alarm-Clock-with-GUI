from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer
from datetime import datetime
from time import sleep
from threading import Thread

#color
bg_color="#82cafa" #sky blue

#root
window = Tk()
window.title("ALARM CLOCK WITH GUI")
window.iconbitmap('clock.ico')
window.geometry("700x500")
window.configure(bg=bg_color)

#frame
frame_body = Frame(window, width=2000, height=300, bg = bg_color)
frame_body.grid(row=0 , column=0)

#configuring frame body
img = Image.open('icon.jpg')
img.resize((190,190))
img = ImageTk.PhotoImage(img)

app_img= Label(frame_body, height=100, image=img, bg= "#000000")
app_img.place(x=10, y=10)

#Labeling for Alarm Clock
name = Label(frame_body, text = "ALARM CLOCK", height=1, font=('Ivy 40 bold'), bg= bg_color)
name.place(x=200, y=10)

#Describing Hour 
hour = Label(frame_body, text = "Hour", height=1, font=('Ivy 15 bold'), bg= bg_color)
hour.place(x=100, y=150)
c_hour = Combobox(frame_body, width=5, font=('arial 15'))
c_hour['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
c_hour.current(00)
c_hour.place(x=100, y=180)

#Describing Minutes
min = Label(frame_body, text = "Minutes", height=1, font=('Ivy 15 bold'), bg= bg_color)
min.place(x=200, y=150)
c_min = Combobox(frame_body, width=5, font=('arial 15'))
c_min['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "58", "59", "60")
c_min.current(00)
c_min.place(x=200, y=180)

#Describing Seconds 
sec = Label(frame_body, text = "Seconds", height=1, font=('Ivy 15 bold'), bg= bg_color)
sec.place(x=300, y=150)
c_sec = Combobox(frame_body, width=5, font=('arial 15'))
c_sec['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "58", "59", "60")
c_sec.current(00)
c_sec.place(x=300, y=180)

#Describing Period
period = Label(frame_body, text = "Period", height=1, font=('Ivy 15 bold'), bg= bg_color)
period.place(x=400, y=150)
c_period = Combobox(frame_body, width=5, font=('arial 15'))
c_period['values'] = ("AM", "PM")
c_period.current(00)
c_period.place(x=400, y=180)

def set_alarm():
    t = Thread(target=alarm)
    t.start()

def stop_alarm():
    print('Stop Alarm: ', selected.get())
    mixer.music.stop()

selected = IntVar()

r1 = Radiobutton(frame_body, text="Set Alarm", font=('arial 10 bold'), value= 1, bg= bg_color, command=set_alarm, variable=selected)
r1.place(x=200, y=270)

def sound_alarm():
    mixer.music.load('Audio.mp3')
    mixer.music.play()
    selected.set(0)

    r2 = Radiobutton(frame_body, text="Stop Alarm", font=('arial 10 bold'), value= 2, bg= bg_color, command=stop_alarm, variable=selected)
    r2.place(x=300, y=270)

def alarm():
    while True:
        control = selected.get()
        print(control) 

        alarm_hour = c_hour.get()
        alarm_min = c_min.get()
        alarm_sec = c_sec.get()
        alarm_period = c_period.get()
        alarm_period = str(alarm_period).upper()
        

        now = datetime.now()

        hour = now.strftime("%I")
        min = now.strftime("%M")
        sec = now.strftime("%S")
        period = now.strftime("%p")

        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_min == min:
                        if alarm_sec == sec:
                            print("Time to get up!")
                            sound_alarm()
        sleep(1)

#t = Thread(target=alarm)
#t.start()
mixer.init()


window.mainloop()

