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
       # self.iconbitmap('Alarm_Clock.ico')
        self.time_label=tk.StringVar()
        self.date_label=tk.StringVar()
        self.hour_box=tk.StringVar()
        self.minute_box=tk.StringVar()
        self.second_box=tk.StringVar()

        

#Create Widgets
        self.clocklabel = tk.Label(text="Python Digital Clock", font=Large)
        self.time_tk = tk.Label(self, textvariable=self.time_label, font=Large)
        self.date_tk = tk.Label(self, textvariable=self.date_label, font=Large)
        self.alarmlabel = tk.Label(text="Set an alarm", font=Large)
        self.hourlabel = tk.Label(text="Hour", font=Small)
        self.minutelabel = tk.Label(text="Minute", font=Small)
        self.secondlabel = tk.Label(text="Seconds", font=Small)
        self.hour_box = tk.Spinbox(self,from_= 00, to = 23, width = 5)
        self.minute_box = tk.Spinbox(self,from_= 00, to = 59, width = 5)
        self.second_box = tk.Spinbox(self,from_= 00, to = 59, width = 5)
        self.submit = tk.Button(self, text="Submit", command=self.alarm_clock)
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

        
#Update time label & Date label
    def update_time(self):
            time_seconds = time.localtime()
            date_str = time.strftime("%d-%m-%Y", time_seconds)
            time_str = time.strftime("%H:%M:%S", time_seconds)
            

            self.time_label.set(time_str)
            self.date_label.set(date_str)

            
#Alarm Clock feature
    def alarm_clock(self):
        time_seconds = time.localtime()
        while True:
            H = self.hour_box.get()
            M = self.minute_box.get()
            S = self.second_box.get()

            alarm_time = time.strftime("%H:%M:%S", time_seconds)

    def update_alarm(self):
        time_seconds = time.localtime()
        time_str = time.strftime("%H:%M:%S", time_seconds)
        alarm_time = time.strftime("%H:%M:%S", time_seconds)
        while True:
            if alarm_time == time_str:
                winsound.Beep()

    def alarm_off():
       winsound.stop()
       alarm_time = ""
        
    def close(self):
        self.destroy()
        self.close()










app = app1()
#app.mainloop()
while True: #calls update_time function and loops it
    app.update_time()
    app.update_idletasks()
    app.update()
    time.sleep(0.1)

