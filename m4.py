import tkinter as tk
from tkinter.ttk import *
import datetime
import pytz


LARGE_FONT= ("Verdana", 12)
timezones = ["US/Alaska", "US/Aleutian", "US/Arizona", "US/Central", "US/East-Indiana", "US/Eastern", "US/Hawaii", "US/Indiana-Starke", "US/Michigan", "US/Mountain", "US/Pacific", "US/Samoa"]


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)


    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="(>°-°)> Home <(°_°'<)", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="-> TimeZone", command=lambda: controller.show_frame(PageOne))
        button.pack()
        button2 = tk.Button(self, text="-> UploadScript", command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Select your timezone, please", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="-> UploadScript", command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        select_timezone_label = Label(self, text="Please select a timezone.")
        list_var = tk.Variable(value=timezones)
        select_timezone_listbox = tk.Listbox(self, listvariable=list_var, height=1)

        liste = Combobox(self)
        liste['values']= (timezones, "Text")
        liste.current(1) #index de l'élément sélectionné

        select_timezone_button = Button(self, text="Timezone")
        time_label = Label(self, text="")

        select_timezone_label.pack()
        select_timezone_listbox.pack()
        select_timezone_button.pack()
        time_label.pack()



    def get_timezone_time(e, args):
        select_timezone_listbox = args[0]
        time_label = args[1]
        selection_index = select_timezone_listbox.curselection()
        selected_timezone = select_timezone_listbox.get(selection_index)
    
        now_time = datetime.datetime.now()
        tz_time = now_time.astimezone(pytz.timezone(selected_timezone))
        tz_formatted = tz_time.strftime("%H:%M:%S")
        time_label.configure({"text": f"The time in {selected_timezone} is {tz_formatted}."})
        time_label.update()



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Select the script for automation, please", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        


app = SeaofBTCapp()
app.title("PassCron Automation Scripts")

window_width = 450
window_height = 300
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
center_x = int((screen_width - window_width)/2)
center_y = int((screen_height - window_height)/2)
app.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")



app.mainloop()