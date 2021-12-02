#Python Modules
import tkinter as tk
import winsound
import time

#Fonts
Large = ("Helvetica", 36)
Small = ("Helvetica", 24)


#Main application
class app1(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("app1")
        self.geometry("600x500")
        #self.iconbitmap('Alarm_Clock.ico')
        self.time_label=tk.StringVar()
        self.date_label=tk.StringVar()
        self.hour_box=tk.StringVar()
        self.minute_box=tk.StringVar()
        self.second_box=tk.StringVar()
        self.hourvalue = tk.StringVar()
        self.minutevalue = tk.StringVar()
        self.secondvalue = tk.StringVar()
        self.start_alarm_time = -1
        self.end_alarm_time = -1
        

#Create Widgets
        self.clocklabel = tk.Label(text="Python Digital Clock", font=Large)
        self.time_tk = tk.Label(self, textvariable=self.time_label, font=Large)
        self.date_tk = tk.Label(self, textvariable=self.date_label, font=Large)
        self.alarmlabel = tk.Label(text="Set an alarm", font=Large)
        self.hourlabel = tk.Label(text="Hour", font=Small)
        self.minutelabel = tk.Label(text="Minute", font=Small)
        self.secondlabel = tk.Label(text="Seconds", font=Small)
        self.hour_box = tk.Spinbox(self,from_= 00, to = 23, width = 5, textvariable = self.hourvalue)
        self.minute_box = tk.Spinbox(self,from_= 00, to = 59, width = 5, textvariable = self.minutevalue)
        self.second_box = tk.Spinbox(self,from_= 00, to = 59, width = 5, textvariable = self.secondvalue)
        self.submit = tk.Button(self, text="Submit", command=self.alarm_values)
        self.stop_alarm = tk.Button(self, text="Alarm off", command=self.alarm_off)
        self.quit = tk.Button(self, text="Quit", command=self.close)


#Position Widgets
        self.clocklabel.grid(padx=20, pady=20, row=0, column=0, columnspan=5)
        self.time_tk.grid(padx=1, pady=1, row=1, column=0, columnspan=2)
        self.date_tk.grid(padx=1, pady=1, row=1, column=3)
        self.alarmlabel.grid(padx=20, pady=20, row=2, column=0, columnspan=4)
        self.hourlabel.grid(padx=20, pady=20, row=3, column=1)
        self.minutelabel.grid(padx=20, pady=20, row=3, column=2)
        self.secondlabel.grid(padx=20, pady=20, row=3, column=3)
        self.hour_box.grid(padx=20, pady=20, row=4, column=1)
        self.minute_box.grid(padx=20, pady=20, row=4, column=2)
        self.second_box.grid(padx=20, pady=20, row=4, column=3)
        self.submit.grid(padx=20, pady=20, row=5, column=1)
        self.stop_alarm.grid(padx=20, pady=20, row=5, column=2)
        self.quit.grid(padx=20, pady=20, row=5, column=3)

        
#Clock feature
    def update_time(self):#Update time label & Date label with current time
            
            self.time_seconds = time.localtime()
            date_str = time.strftime("%d-%m-%Y", self.time_seconds)
            time_str = time.strftime("%H:%M:%S", self.time_seconds)
            

            self.time_label.set(time_str)
            self.date_label.set(date_str)


            
#Alarm Clock feature
    def alarm_values(self):#Obtains spinbox values for alarm
        
        # Values from the Spinboxes are taken and stored to be used in self.start_alarm_time .
        H = self.hour_box.get()
        M = self.minute_box.get()
        S = self.second_box.get()

        # self.start_alarm_time is turned into seconds using the fstring with date & time.
        # The alarm will sound between self.alarm_start_time and self.end-alarm_time .
        # The self.end_alarm_time is 30 seconds after the self.alarm_start-time .
        self.start_alarm_time = time.mktime(time.strptime(f"{self.time_seconds.tm_year} {self.time_seconds.tm_mon} {self.time_seconds.tm_mday} {H} {M} {S}", "%Y %m %d %H %M %S"))
        self.end_alarm_time = self.start_alarm_time + 30 



    def alarm_time_up(self):# when the alarm time matches the current time, alarm function is triggered
        
        # time_seconds is turned into seconds using time.mktime .
        # The IF statement checks the self.start_alarm_time seconds against the time_seconds  .
        # If the IF stement is true, self.alarm_sound is called till self.start_alarm_time equals self.end_alarm_time .
        time_seconds = time.mktime(self.time_seconds)
        #print(self.start_alarm_time, self.end_alarm_time, time_seconds)
        if time_seconds >= self.start_alarm_time and time_seconds <= self.end_alarm_time:
            self.start_alarm_time += 2
            #print("Trigger alarm")
            self.alarm_sound()


    def alarm_sound(self):#Triggering the alarm sound
            #print("Alarm sound")
            winsound.Beep(440, 500)

    def alarm_off(self):#Turns off alarm sound and resets spinboxes
       #
       self.start_alarm_time = 0
       self.end_alarm_time = 0
       self.hourvalue.set(value = "0")
       self.minutevalue.set(value = "0")
       self.secondvalue.set(value = "0")

#Program exit
    def close(self):#Closes the program down
        self.destroy()











app = app1()
#app.mainloop()
while True: #calls update_time function and loops it
    app.update_time()
    app.update_idletasks()
    app.update()
    app.alarm_time_up()
    time.sleep(0.1)


