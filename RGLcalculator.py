import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Plant Calculator")

type_var = tk.StringVar()

type_label = tk.Label(root, text="Select plant type:", font=("Arial", 20))
type_label.pack(padx=20, pady=10)

type_box = ttk.Combobox(root, textvariable=type_var, font=("Arial", 20))
type_box['values'] = ["Photoperiod (Seasonal)", "Day-Neutral (Autoflower)"]
type_box.current(0)
type_box.pack(padx=20, pady=10)

stage_label = tk.Label(root, text="Select stage:", font=("Arial", 20))
stage_label.pack(padx=20, pady=10)

stage_box = ttk.Combobox(root, font=("Arial", 20))
stage_box['values'] = ["Propagation", "Early Growth", "Mid Growth", "Pre-Bloom", "Blooming"]
stage_box.current(0)
stage_box.pack(padx=20, pady=10)

potsize_label = tk.Label(root, text="Select pot size (L)", font=("Arial", 20))
potsize_label.pack()
potsize_entry = tk.Entry(root, font=("Arial", 20))
potsize_entry.pack(padx=20, pady=10)

# multipliers
stage_multipliers = {
    "Early Growth": 0.02,
    "Mid Growth": 0.05,
    "Pre-Bloom": 0.07,
    "Blooming": 0.05,
}

watering_interval_days = {
    "Early Growth": 5,
    "Mid Growth": 4,
    "Pre-Bloom": 3,
    "Blooming": 4,
}

calculate_result = tk.Label(root, text="", font=("Arial", 20))
calculate_result.pack()

calculate_potresult = tk.Label(root, text="", font=("Arial", 20))
calculate_potresult.pack()

def calculate():
    stage = stage_box.get()
    plant_type = type_var.get()
    pot_input = potsize_entry.get()

    # Topf input validation
    if not pot_input.replace('.', '', 1).isdigit():
        calculate_potresult.config(text="Please enter a valid numeric pot volume.")
        return

    pot_size = float(pot_input)

    # Climate output
    if stage == "Propagation":
        calculate_result.config(
            text="Humidity between 80–90%\n"
                 "Day temperature between 25–26°C\n"
                 "Night temperature between 23–24°C\n"
                 "No watering required."
        )
        calculate_potresult.config(text="")
        return

    elif stage in stage_multipliers:
        climate_settings = {
            "Early Growth": ((65, 70), (20, 25), (15, 20)),
            "Mid Growth": ((40, 70), (22, 28), (18, 23)),
            "Pre-Bloom": ((40, 50), (20, 26), (20, 26)),
            "Blooming": ((30, 40), (18, 24), (14, 28)),
        }

        humidity, temp_day, temp_night = climate_settings[stage]
        calculate_result.config(
            text=f"Humidity between {humidity[0]}–{humidity[1]}%\n"
                 f"Day temperature between {temp_day[0]}–{temp_day[1]}°C\n"
                 f"Night temperature between {temp_night[0]}–{temp_night[1]}°C"
        )

        # Topf-Größe regeln
        if plant_type == "Photoperiod (Seasonal)" and not (0.5 <= pot_size <= 22):
            calculate_potresult.config(text="Pot size must be 0.5–22L for Photoperiod.")
            return
        if plant_type == "Day-Neutral (Autoflower)" and not (0.5 <= pot_size <= 15):
            calculate_potresult.config(text="Pot size must be 0.5–15L for Day-Neutral (Autoflower).")
            return

        # Wasserverbrauch-Rechner
        multiplier = stage_multipliers[stage]
        interval = watering_interval_days[stage]
        water_per_watering = pot_size * multiplier
        total_7 = round(water_per_watering * (7 // interval), 2)
        total_14 = round(water_per_watering * (14 // interval), 2)

        calculate_potresult.config(
            text=f"~{water_per_watering:.2f} L per watering.\n"
                 f"Total over 7d: {total_7} L\n"
                 f"Total over 14d: {total_14} L"
        )

    else:
        calculate_result.config(text="Invalid stage.")
        calculate_potresult.config(text="")

calculate_button = tk.Button(root, text="Calculate Ideal Conditions", command=calculate, font=("Arial", 20))
calculate_button.pack(padx=20, pady=10)

root.mainloop()
