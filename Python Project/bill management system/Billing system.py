from tkinter import *

# Initialize the main window
root = Tk()
root.geometry("1000x500")
root.title("Bill Management System")
root.resizable(False, False)
root.configure(bg="#2c3e50")  # Dark background for the main window

def reset():
    entry_samosa.delete(0, END)
    entry_Chicken_Roll.delete(0, END)
    entry_Vegetable_Roll.delete(0, END)
    entry_Fries.delete(0, END)
    entry_Chicken_Biryani.delete(0, END)
    entry_Mutton_Biryani.delete(0, END)
    entry_Chicken_Burger.delete(0, END)
    Total_Bill.set("")

def total():
    try:
        a1 = int(Samosa.get())
    except ValueError:
        a1 = 0

    try:
        a2 = int(ChickenRoll.get())
    except ValueError:
        a2 = 0

    try:
        a3 = int(VegetableRoll.get())
    except ValueError:
        a3 = 0

    try:
        a4 = int(Fries.get())
    except ValueError:
        a4 = 0

    try:
        a5 = int(ChickenBiryani.get())
    except ValueError:
        a5 = 0

    try:
        a6 = int(MuttonBiryani.get())
    except ValueError:
        a6 = 0

    try:
        a7 = int(ChickenBurger.get())
    except ValueError:
        a7 = 0

    # Define the cost of each item per quantity
    c1 = 30 * a1
    c2 = 60 * a2
    c3 = 40 * a3
    c4 = 100 * a4
    c5 = 180 * a5
    c6 = 250 * a6
    c7 = 270 * a7

    total_cost = c1 + c2 + c3 + c4 + c5 + c6 + c7
    total_bill = f"Rs {total_cost:.2f}"
    Total_Bill.set(total_bill)

    lbl_total = Label(f2, font=('aria', 20, 'bold'), text="Total", width=16, fg="white", bg="#34495e")
    lbl_total.place(x=0, y=50)

    entry_total = Entry(f2, font=('aria', 20, 'bold'), textvariable=Total_Bill, bd=6, width=15, bg="#1abc9c", fg="white")
    entry_total.place(x=20, y=100)

# Header Label
Label(root, text="Bill Management", bg="#e74c3c", fg="white", font=("calibri", 33, "bold"), width="300", height="2").pack()

# Menu card
f = Frame(root, bg="#3498db", highlightbackground="black", highlightthickness=1, width=300, height=370)
f.place(x=10, y=118)  # for menu card

Label(f, text="Menu", font=("Gabriola", 40, "bold"), fg="white", bg="#3498db").place(x=80, y=0)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Samosa....30 Rs", fg="white", bg="#3498db").place(x=10, y=80)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Chicken Roll......60 Rs", fg="white", bg="#3498db").place(x=10, y=110)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Vegetable Roll...40 Rs", fg="white", bg="#3498db").place(x=10, y=140)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Fries.......100 Rs", fg="white", bg="#3498db").place(x=10, y=170)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Chicken Biryani...180 Rs", fg="white", bg="#3498db").place(x=10, y=200)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Mutton Biryani...250 Rs", fg="white", bg="#3498db").place(x=10, y=230)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Chicken Burger...270 Rs", fg="white", bg="#3498db").place(x=10, y=260)

# BILL frame
f2 = Frame(root, bg="#ecf0f1", highlightbackground="black", highlightthickness=1, width=300, height=370)
f2.place(x=690, y=118)

Bill = Label(f2, text="Bill", font=('calibri', 20, 'bold'), bg="#ecf0f1", fg="#2c3e50")
Bill.place(x=120, y=10)

# Entry Frame
f1 = Frame(root, bd=5, height=370, width=300, relief=RAISED, bg="#2c3e50")
f1.pack()

Samosa = StringVar()
ChickenRoll = StringVar()
VegetableRoll = StringVar()
Fries = StringVar()
ChickenBiryani = StringVar()
MuttonBiryani = StringVar()
ChickenBurger = StringVar()
Total_Bill = StringVar()

# Labels and Entries with improved styling
lbl_samosa = Label(f1, font=("arial", 20, "bold"), text="Samosa", width=12, fg="#ecf0f1", bg="#2c3e50")
lbl_samosa.grid(row=1, column=0)
entry_samosa = Entry(f1, font=("arial", 20, "bold"), textvariable=Samosa, bd=6, width=8, bg="#1abc9c", fg="white")
entry_samosa.grid(row=1, column=1)

lbl_Chicken_Roll = Label(f1, font=("arial", 20, "bold"), text="Chicken Roll", width=12, fg="#ecf0f1", bg="#2c3e50")
lbl_Chicken_Roll.grid(row=2, column=0)
entry_Chicken_Roll = Entry(f1, font=("arial", 20, "bold"), textvariable=ChickenRoll, bd=6, width=8, bg="#1abc9c", fg="white")
entry_Chicken_Roll.grid(row=2, column=1)

lbl_Vegetable_Roll = Label(f1, font=("arial", 20, "bold"), text="Vegetable Roll", width=12, fg="#ecf0f1", bg="#2c3e50")
lbl_Vegetable_Roll.grid(row=3, column=0)
entry_Vegetable_Roll = Entry(f1, font=("arial", 20, "bold"), textvariable=VegetableRoll, bd=6, width=8, bg="#1abc9c", fg="white")
entry_Vegetable_Roll.grid(row=3, column=1)

lbl_Fries = Label(f1, font=("arial", 20, "bold"), text="Fries", width=12, fg="#ecf0f1", bg="#2c3e50")
lbl_Fries.grid(row=4, column=0)
entry_Fries = Entry(f1, font=("arial", 20, "bold"), textvariable=Fries, bd=6, width=8, bg="#1abc9c", fg="white")
entry_Fries.grid(row=4, column=1)

lbl_Chicken_Biryani = Label(f1, font=("arial", 20, "bold"), text="Chicken Biryani", width=12, fg="#ecf0f1", bg="#2c3e50")
lbl_Chicken_Biryani.grid(row=5, column=0)
entry_Chicken_Biryani = Entry(f1, font=("arial", 20, "bold"), textvariable=ChickenBiryani, bd=6, width=8, bg="#1abc9c", fg="white")
entry_Chicken_Biryani.grid(row=5, column=1)

lbl_Mutton_Biryani = Label(f1, font=("arial", 20, "bold"), text="Mutton Biryani", width=12, fg="#ecf0f1", bg="#2c3e50")
lbl_Mutton_Biryani.grid(row=6, column=0)
entry_Mutton_Biryani = Entry(f1, font=("arial", 20, "bold"), textvariable=MuttonBiryani, bd=6, width=8, bg="#1abc9c", fg="white")
entry_Mutton_Biryani.grid(row=6, column=1)

lbl_Chicken_Burger = Label(f1, font=("arial", 20, "bold"), text="Chicken Burger", width=12, fg="#ecf0f1", bg="#2c3e50")
lbl_Chicken_Burger.grid(row=7, column=0)
entry_Chicken_Burger = Entry(f1, font=("arial", 20, "bold"), textvariable=ChickenBurger, bd=6, width=8, bg="#1abc9c", fg="white")
entry_Chicken_Burger.grid(row=7, column=1)
# Total Button with new styling
btn_total = Button(root, font=("calibri", 20, "bold"), text="Total", padx=1 ,pady=1, bg="#e74c3c", fg="white", command=total)
btn_total.place(x=8, y=10)

# Reset Button with new styling
btn_reset = Button(root, font=("calibri", 20, "bold"), text="Reset", padx=1, pady=1, bg="#e74c3c", fg="white", command=reset)
btn_reset.place(x=900, y=10)

# Ensure the Total button is on top
btn_total.lift()

root.mainloop()
