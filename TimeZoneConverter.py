import tkinter as tk
from tkinter import ttk
import datetime
import pytz

class TimeZoneConverter(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        timezones = ["US/Alaska", "US/Aleutian", "US/Arizona", "US/Central", "US/East-Indiana", "US/Eastern", "US/Hawaii", "US/Indiana-Starke", "US/Michigan", "US/Mountain", "US/Pacific", "US/Samoa",
                     "Europe/Amsterdam", "Europe/Andorra", "Europe/Astrakhan", "Europe/Athens", "Europe/Belgrade", "Europe/Berlin", "Europe/Bratislava", "Europe/Brussels", "Europe/Bucharest", "Europe/Budapest",
                     "Asia/Kolkata", "Asia/Krasnoyarsk", "Asia/Kuala_Lumpur", "Asia/Kuching", "Asia/Kuwait", "Asia/Macau", "Asia/Magadan", "Asia/Makassar", "Asia/Manila", "Asia/Muscat", "Asia/Nicosia"]
        select_timezone_label = ttk.Label(self, text="Please select a timezone.")
        list_var = tk.Variable(value=timezones)
        select_timezone_listbox = tk.Listbox(self, listvariable=list_var, height=1)

        liste = ttk.Combobox(self)
        liste['values']= (timezones, "Text")
        liste.current(1) #index de l'élément sélectionné
        time_label = ttk.Label(self, text="")

        select_timezone_button = ttk.Button(self, text="Timezone")
        
        select_timezone_label.pack()
        select_timezone_listbox.pack()
        select_timezone_button.pack()
        time_label.pack()

        select_timezone_button.bind("<Button>", lambda e, args=[select_timezone_listbox, time_label]: self.get_timezone_time(e, args))

    def get_timezone_time(self, e, args):
        select_timezone_listbox = args[0]
        time_label = args[1]
        selection_index = select_timezone_listbox.curselection()
        selected_timezone = select_timezone_listbox.get(selection_index)
    
        now_time = datetime.datetime.now()
        tz_time = now_time.astimezone(pytz.timezone(selected_timezone))
        tz_formatted = tz_time.strftime("%H:%M:%S")
        time_label.configure({"text": f"The time in {selected_timezone} is {tz_formatted}."})
        time_label.update()
