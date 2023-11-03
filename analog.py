import tkinter as tk
from datetime import datetime
import math
import pytz

# Create a Tkinter window
window = tk.Tk()
window.title("Scalable Analog Clock - Indian Time Zone")

# Dropdown menu for selecting time zone
timezone_var = tk.StringVar()
timezones = ["Asia/Kolkata", "America/New_York", "Europe/London", "Australia/Sydney",
    "Asia/Tokyo", "Africa/Cairo", "America/Los_Angeles", "America/Chicago",
    "America/Denver", "America/Phoenix", "America/Anchorage", "America/Adak",
     "Africa/Lagos", "Africa/Johannesburg",
    "Asia/Shanghai", "Asia/Dubai", "Asia/Seoul", "Asia/Hong_Kong", "Europe/Moscow",
    "Europe/Berlin", "Europe/Paris"]
timezone_var.set("Asia/Kolkata")  # Default to Indian Time Zone

timezone_label = tk.Label(window, text="Select Time Zone:")
timezone_label.pack()
timezone_dropdown = tk.OptionMenu(window, timezone_var, *timezones)
timezone_dropdown.pack()

# Create a variable to track the AM/PM display
am_pm_var = tk.IntVar()
am_pm_var.set(0)  # Default to not displaying AM/PM

# Checkbox to display AM/PM
am_pm_check = tk.Checkbutton(window, text="Display AM/PM", variable=am_pm_var)
am_pm_check.pack()

# Dropdown menu for selecting clock face color
clock_face_color_var = tk.StringVar()
clock_face_colors = ["black", "yellow", "pink", "skyblue", "orange"]
clock_face_color_var.set("black")  # Default clock face color

clock_face_color_label = tk.Label(window, text="Select Clock Face Color:")
clock_face_color_label.pack()
clock_face_color_dropdown = tk.OptionMenu(window, clock_face_color_var, *clock_face_colors)
clock_face_color_dropdown.pack()

# Background color for the clock face
background_color_var = tk.StringVar()
background_colors = ["white", "lightgray", "lightblue", "lightpink", "black","brown"]
background_color_var.set("white")  # Default background color

background_color_label = tk.Label(window, text="Select Background Color:")
background_color_label.pack()
background_color_dropdown = tk.OptionMenu(window, background_color_var, *background_colors)
background_color_dropdown.pack()

# Numbers color inside the clock face
numbers_color_var = tk.StringVar()
numbers_colors = ["white", "black", "red", "blue","brown","pink"]
numbers_color_var.set("white")  # Default numbers color

numbers_color_label = tk.Label(window, text="Select Numbers Color:")
numbers_color_label.pack()
numbers_color_dropdown = tk.OptionMenu(window, numbers_color_var, *numbers_colors)
numbers_color_dropdown.pack()

# Define the clock's size and center
canvas = tk.Canvas(window, width=600, height=400, bg=background_color_var.get())
canvas.pack(expand=True, fill=tk.BOTH)

# Function to update the clock
# ... (previous code) ...

def update_clock():
    canvas.delete("all")

    # Get the current time based on the selected time zone
    selected_timezone = timezone_var.get()
    tz = pytz.timezone(selected_timezone)
    current_time = datetime.now(tz)
    if am_pm_var.get():
        current_time_str = current_time.strftime("%I:%M:%S %p")
    else:
        current_time_str = current_time.strftime("%H:%M:%S")
    current_day_str = current_time.strftime("%A")

    # Get the clock face color, background color, and numbers color
    clock_face_color = clock_face_color_var.get()
    background_color = background_color_var.get()
    numbers_color = numbers_color_var.get()

    # Calculate the size based on the window size
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    clock_radius = min(canvas_width, canvas_height) / 2 - 20

    # Draw clock face
    canvas.create_oval(canvas_width / 2 - clock_radius, canvas_height / 2 - clock_radius,
                       canvas_width / 2 + clock_radius, canvas_height / 2 + clock_radius,
                       fill=clock_face_color, outline="white", width=4)

    # Draw numbers on the clock face
    for i in range(1, 13):
        angle = math.radians(30 * i)
        x = canvas_width / 2 + clock_radius * 0.85 * math.sin(angle)
        y = canvas_height / 2 - clock_radius * 0.85 * math.cos(angle)
        canvas.create_text(x, y, text=str(i), font=("Helvetica", 14), fill=numbers_color)

    # Draw time below the clock
    canvas.create_text(canvas_width / 2, canvas_height / 2 + clock_radius + 10, text=current_time_str,
                       font=("Helvetica", 16), fill=numbers_color)

    # Draw the day above the clock
    canvas.create_text(canvas_width / 2, canvas_height / 2 - clock_radius - 10, text=current_day_str,
                       font=("Helvetica", 16), fill=numbers_color)

    # Draw clock hands
    second = current_time.second
    minute = current_time.minute
    hour = current_time.hour

    second_angle = math.radians(6 * second)
    minute_angle = math.radians(6 * (minute + second / 60))
    hour_angle = math.radians(30 * (hour + minute / 60))

    # Second hand
    canvas.create_line(canvas_width / 2, canvas_height / 2,
                       canvas_width / 2 + clock_radius * 0.8 * math.sin(second_angle),
                       canvas_height / 2 - clock_radius * 0.8 * math.cos(second_angle), fill="red", width=2)

    # Minute hand
    canvas.create_line(canvas_width / 2, canvas_height / 2,
                       canvas_width / 2 + clock_radius * 0.7 * math.sin(minute_angle),
                       canvas_height / 2 - clock_radius * 0.7 * math.cos(minute_angle), fill="blue", width=4)

    # Hour hand
    canvas.create_line(canvas_width / 2, canvas_height / 2,
                       canvas_width / 2 + clock_radius * 0.6 * math.sin(hour_angle),
                       canvas_height / 2 - clock_radius * 0.6 * math.cos(hour_angle), fill="green", width=6)

    # Set the background color
    canvas.configure(bg=background_color)

    window.after(1000, update_clock)

update_clock()
window.mainloop()
