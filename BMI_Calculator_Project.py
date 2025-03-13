from tkinter import *
from tkinter import ttk

# Colors 
color0 = "#444466"  # black
color1 = "#feffff"  # white
color2 = "#6856FF"  # blue

window = Tk()
window.title('BMI Calculator')
window.geometry('295x300')  
window.resizable(height=False, width=False)
window.configure(bg=color1)

# Frames
top_frame = Frame(window, width=295, height=50, bg=color1, pady=0, padx=0)
top_frame.grid(row=0, column=0)

down_frame = Frame(window, width=295, height=250, bg=color1, pady=0, padx=0)
down_frame.grid(row=1, column=0)

# App Title
app_name = Label(top_frame, text="BMI CALCULATOR", width=23, height=1, padx=0, anchor="center", 
                 font=("Ivy 16 bold"), bg=color1, fg=color0)
app_name.place(x=0, y=2)

# Blue line below the title
app_line = Label(top_frame, text="", width=400, height=1, padx=0, anchor="center", 
                 font=("Arial 1"), bg=color2, fg=color0)
app_line.place(x=0, y=35)

# Function to calculate BMI
def calculate():
    try:
        weight = float(e_weight.get())
        height = float(e_height.get()) / 100  # Convert cm to meters
        result = weight / (height ** 2)

        if result < 18.5:
            category = "Underweight"
        elif 18.5 <= result < 24.9:
            category = "Normal"
        elif 25 <= result < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        # Update result labels
        l_result.config(text="{:.2f}".format(result))  # Numeric BMI value
        l_result_text.config(text=f"Your BMI is: {category}")  # BMI category

    except ValueError:
        l_result_text.config(text="Please enter valid numbers!")


# Input fields for weight
l_weight = Label(down_frame, text="Enter your weight (kg):", height=1, padx=0, anchor="w",
                 font=("Ivy 10 bold"), bg=color1, fg=color0)
l_weight.grid(row=0, column=0, columnspan=1, pady=10, padx=10, sticky="w")

e_weight = Entry(down_frame, width=10, font=("Ivy 10 bold"), justify="center", relief="solid")
e_weight.grid(row=0, column=1, columnspan=1, pady=10, padx=10)

# Input fields for height
l_height = Label(down_frame, text="Enter your height (cm):", height=1, padx=0, anchor="w",
                 font=("Ivy 10 bold"), bg=color1, fg=color0)
l_height.grid(row=1, column=0, columnspan=1, pady=10, padx=10, sticky="w")

e_height = Entry(down_frame, width=10, font=("Ivy 10 bold"), justify="center", relief="solid")
e_height.grid(row=1, column=1, columnspan=1, pady=10, padx=10)

# Display BMI result
l_result = Label(down_frame, width=8, text="----", height=1, padx=6, pady=6, 
                 relief="flat", anchor="center", font=("Ivy 24 bold"), bg=color2, fg=color1)
l_result.grid(row=2, column=0, columnspan=2, pady=10)

# Display BMI category
l_result_text = Label(down_frame, width=37, text="", height=1, padx=6, pady=6, 
                      relief="flat", anchor="center", font=("Ivy 10 bold"), bg=color1, fg=color0)
l_result_text.grid(row=3, column=0, columnspan=2, pady=5)

# Calculate button (Inside `down_frame`)

b_calculate = Button(down_frame, text="Calculate", width=30, height=1, 
                     bg=color2, fg=color2,  # Blue background, white text
                     font=("Ivy 10 bold"), anchor="center", command=calculate)
b_calculate.grid(row=4, column=0, columnspan=2, pady=15)

window.mainloop()

