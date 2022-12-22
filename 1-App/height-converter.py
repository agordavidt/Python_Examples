import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Height Converter")

# Create a label to prompt the user to enter their height
label = tk.Label(window, text="Enter your height:")
label.pack()

# Create a text entry box for the user to input their height
height_entry = tk.Entry(window)
height_entry.pack()

# Create a label to display the result of the conversion
result_label = tk.Label(window, text="")
result_label.pack()

# Function to convert the height
def convert_height():
    # Get the user's input
    height = height_entry.get()
    # Convert the input to a float
    height = float(height)
    # Determine which unit of measurement the user entered
    if unit.get() == "cm":
        # convert the height to inches
        height_in_inches = height / 2.54
        # Display the result
        result_label.config(text=f"{height} cm is equal to {height_in_inches:.2f} inches")
    elif unit.get() == "in":
        # Convert the height to centimeters
        height_in_cm = height * 2.54
        # Displary the result
        result_label.config(text=f"{height} inches is equal to {height_in_cm:.2f} cm")
    elif unit.get() == "m":
        # Convert the height to inches
        height_in_inches = height * 100 / 2.54
        # Display the result
        result_label.config(text=f"{height} meters is equal to {height_in_inches:.2f} inches")

# Create a radio button to allow the user to selct the unit of measurement for their height
unit = tk.StringVar()
unit.set("cm") # default value

# Create radio buttons for each unit of measurement
cm_radio = tk.Radiobutton(window, text="cm", variable=unit, value="cm")
cm_radio.pack()
in_radio = tk.Radiobutton(window, text="in", variable=unit, value="in")
in_radio.pack()
m_radio = tk.Radiobutton(window, text="m", variable=unit, value="m")
m_radio.pack()

# Create a buton to initiate the conversion
convert_button = tk.Button(window, text="Convert", command=convert_height)
convert_button.pack()



window.mainloop()









