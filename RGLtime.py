import tkinter as tk
from datetime import datetime
from datetime import timedelta
import time
import json

root = tk.Tk()
root.title("Plant Birthday Tracker")

# Top label
birthday_label = tk.Label(root, text="Please input the birthday of your plant", font=("Arial", 20))
birthday_label.pack(pady=10)

# Frame (Rahmen)
datetime_frame = tk.Frame(root)
datetime_frame.pack(pady=5)
spin_width = 6

year_spinbox = tk.Spinbox(datetime_frame, from_=2025, to=2125, font=("Arial", 18), width=spin_width, justify='center')
month_spinbox = tk.Spinbox(datetime_frame, from_=1, to=12, font=("Arial", 18), width=spin_width, justify='center')
day_spinbox = tk.Spinbox(datetime_frame, from_=1, to=31, font=("Arial", 18), width=spin_width, justify='center')
hour_spinbox = tk.Spinbox(datetime_frame, from_ =0, to=23, font=("Arial", 18), width=spin_width, justify='center')
minute_spinbox = tk.Spinbox(datetime_frame, from_ =0, to=59, font=("Arial", 18), width=spin_width, justify='center')

# Labels
label_font = ("Arial", 14)
label_width = 8

year_label = tk.Label(datetime_frame, text="Year", font=label_font, width=label_width, anchor='center')
month_label = tk.Label(datetime_frame, text="Month", font=label_font, width=label_width, anchor='center')
day_label = tk.Label(datetime_frame, text="Day", font=label_font, width=label_width, anchor='center')
hour_label = tk.Label(datetime_frame, text="Hour", font=label_font, width=label_width, anchor='center')
minute_label = tk.Label(datetime_frame, text="Minute", font=label_font, width=label_width, anchor='center')
# Grid layout



year_spinbox.grid(row=0, column=0, padx=5)
month_spinbox.grid(row=0, column=1, padx=5)
day_spinbox.grid(row=0, column=2, padx=5)
hour_spinbox.grid(row=0, column=3, padx=5)
minute_spinbox.grid(row=0, column=4, padx=5)

year_label.grid(row=1, column=0)
month_label.grid(row=1, column=1)
day_label.grid(row=1, column=2)
hour_label.grid(row=1, column=3)
minute_label.grid(row=1, column=4)

cuttent_time_label = tk.Label(root, text="Please input the current time:", font=("Arial", 20))
cuttent_time_label.pack(pady=10)

current_time_frame = tk.Frame(root)
current_time_frame.pack(pady= 5)

current_year_spinbox = tk.Spinbox(current_time_frame, from_=2025, to=2125, font=("Arial", 18), width=spin_width, justify='center')
current_month_spinbox = tk.Spinbox(current_time_frame, from_=1, to=12, font=("Arial", 18), width=spin_width, justify='center')
current_day_spinbox = tk.Spinbox(current_time_frame, from_=1, to=31, font=("Arial", 18), width=spin_width, justify='center')
current_hour_spinbox = tk.Spinbox(current_time_frame, from_ =0, to=23, font=("Arial", 18), width=spin_width, justify='center')
current_minute_spinbox = tk.Spinbox(current_time_frame, from_ =0, to=59, font=("Arial", 18), width=spin_width, justify='center')

current_year_label = tk.Label(current_time_frame, text="Year", font=label_font, width=label_width, anchor='center')
current_month_label = tk.Label(current_time_frame, text="Month", font=label_font, width=label_width, anchor='center')
current_day_label = tk.Label(current_time_frame, text="Day", font=label_font, width=label_width, anchor='center')
current_hour_label = tk.Label(current_time_frame, text="Hour", font=label_font, width=label_width, anchor='center')
current_minute_label = tk.Label(current_time_frame, text="Minute", font=label_font, width=label_width, anchor='center')


current_year_spinbox.grid(row=0, column=0, padx=5)
current_month_spinbox.grid(row=0, column=1, padx=5)
current_day_spinbox.grid(row=0, column=2, padx=5)
current_hour_spinbox.grid(row=0, column=3, padx=5)
current_minute_spinbox.grid(row=0, column=4, padx=5)

current_year_label.grid(row=1, column=0)
current_month_label.grid(row=1, column=1)
current_day_label.grid(row=1, column=2)
current_hour_label.grid(row=1, column=3)
current_minute_label.grid(row=1, column=4)

# Result label
result_label = tk.Label(root, font=("Arial", 16))
result_label.pack(pady=10)

is_clicked = False

# Calculate function
def calculate_age():
    try:
        global birth_time, current_time, System_time, is_clicked, referenz_monotonic
        referenz_monotonic = time.monotonic()
        birth_time = datetime(
            int(year_spinbox.get()),
            int(month_spinbox.get()),
            int(day_spinbox.get()),
            int(hour_spinbox.get()),
            int(minute_spinbox.get())
        )
        current_time = datetime(
            int(current_year_spinbox.get()),
            int(current_month_spinbox.get()),
            int(current_day_spinbox.get()),
            int(current_hour_spinbox.get()),
            int(current_minute_spinbox.get())
        )
        with open("plant_time.json", "w") as f:
            json.dump({
            "birth_time": birth_time.isoformat(),
            "reference_time": current_time.isoformat(),
            "reference_monotonic": referenz_monotonic
            }, f)
# Wird im dem User/user Ordnerort gespeichert
        plant_age = current_time - birth_time

        if plant_age.days >= 0:
            result_label.config(text=f"🌱 Your plant is {plant_age.days} days old")
            global is_clicked
            is_clicked = True
            System_time = current_time + timedelta(seconds=referenz_monotonic)
            print(f"✅ System time is now: {System_time}")  # 
        else:
            result_label.config(text="⚠️ Invalid date/time entered")

    except ValueError:
        result_label.config(text="⚠️ Invalid date/time entered")



# Knopf
Calculate = tk.Button(root, text="Calculate Birthday", font=("Arial", 16), command=calculate_age)
Calculate.pack(pady=10)

root.mainloop()