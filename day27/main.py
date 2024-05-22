from tkinter import *

def button_clicked():
    miles= int(input.get())
    km = miles *1.6
    my_label_km_out.config(text=km)
    my_label_km_out.grid(column=1,row=1)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# input field
input = Entry(width=7)
input.grid(column=1, row=0)
# input.pack()

#label
my_label_miles = Label(text="Miles", font=("Arial", 12, "italic"))
# my_label.pack()
# my_label.place(x=50, y=50)
my_label_miles.grid(column=2,row=0)

my_label_km = Label(text="Km", font=("Arial", 12, "italic"))
my_label_km.grid(column=2,row=1)

my_label_iet = Label(text="is equal to", font=("Arial", 12, "italic"))
my_label_iet.grid(column=0,row=1)

my_label_km_out = Label(text="0", font=("Arial", 12, "italic"))
my_label_km_out.grid(column=1,row=1)
# button
button = Button(text="Calculate", command=button_clicked)
# button.pack()
button.grid(column=1,row=2)




window.mainloop()