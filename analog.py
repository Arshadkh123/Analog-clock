import tkinter as tk
from datetime import datetime
import math
import pytz

# Create a Tkinter window
window = tk.Tk()
window.title("Analog Clock - Indian Time Zone")

# Dropdown menu for selecting time zone
timezone_var = tk.StringVar()
timezones = ["Asia/Kolkata", "America/New_York", "Europe/London", "Australia/Sydney","Asia/Tokyo", "Africa/Cairo"]
timezone_var.set("Asia/Kolkata")  # Default to Indian Time Zone

timezone_label = tk.Label(window, text="Select Time Zone:")
timezone_label.pack()
timezone_dropdown = tk.OptionMenu(window, timezone_var, *timezones)
timezone_dropdown.pack()

# Define the clock's size and center
canvas = tk.Canvas(window, width=400, height=400, bg="black")
canvas.pack()

# Function to update the clock
def update_clock():
    canvas.delete("all")

    # Get the current time based on the selected time zone
    selected_timezone = timezone_var.get()
    tz = pytz.timezone(selected_timezone)
    current_time = datetime.now(tz)
    current_time_str = current_time.strftime("%H:%M:%S")
    current_day_str = current_time.strftime("%A")

    # Draw clock face
    canvas.create_oval(50, 50, 350, 350, fill="black", outline="white", width=2)

    # Draw numbers on the clock face
    for i in range(1, 13):
        angle = math.radians(360 / 12 * i)
        x = 200 + 140 * math.sin(angle)
        y = 200 - 140 * math.cos(angle)
        canvas.create_text(x, y, text=str(i), font=("Helvetica", 12), fill="white")

    canvas.create_text(200, 30, text=current_time_str, font=("Helvetica", 16), fill="white")
    canvas.create_text(200, 370, text=current_day_str, font=("Helvetica", 12), fill="white")

    # Draw clock hands
    second = current_time.second
    minute = current_time.minute
    hour = current_time.hour

    second_angle = math.radians(6 * second)
    minute_angle = math.radians(6 * (minute + second / 60))
    hour_angle = math.radians(30 * (hour + minute / 60))

    # Second hand
    canvas.create_line(200, 200, 200 + 70 * math.sin(second_angle), 200 - 70 * math.cos(second_angle), fill="red", width=2)

    # Minute hand
    canvas.create_line(200, 200, 200 + 60 * math.sin(minute_angle), 200 - 60 * math.cos(minute_angle), fill="blue", width=4)

    # Hour hand
    canvas.create_line(200, 200, 200 + 50 * math.sin(hour_angle), 200 - 50 * math.cos(hour_angle), fill="green", width=6)

    window.after(1000, update_clock)

update_clock()
window.mainloop()
