import tkinter as tk
from tkinter import messagebox


#Saving the Data
def save():
    website_text = website.get()
    email_text = email_username.get()
    password_text = password.get()

    if website_text == "" or email_text == "" or password_text == "":
        messagebox.showinfo(title="Warning!", message="There are empty fields.")
    else:    
        is_yes = messagebox.askokcancel(title="Confirmation", message=f"This data will be saved to data.txt:\nWebsite: {website_text}\nEmail/Username: {email_text}\nPassword: {password_text}")    

        if is_yes == True:
            with open("./data.txt", "a") as file:
                file.write(f"{website_text} | {email_text} | {password_text}\n")
                website.delete(0, tk.END)
                email_username.delete(0, tk.END)
                password.delete(0, tk.END)


#Window
window = tk.Tk()
window.title("Password Saver")
window.config(padx=50, pady=50, bg="#EEEEEE")
window.resizable(False, False)

#Canvas
canvas = tk.Canvas(height=200, width=200, bg="#EEEEEE", highlightthickness=0)
img = tk.PhotoImage(file="./lock.png")
canvas.create_image(100,100, image=img)

canvas.grid(row=0, column=1)

#Labels
label1 = tk.Label(text="Website:", font=("Arial", 11), bg="#EEEEEE", fg="#222831")
label2 = tk.Label(text="Email/Username:", font=("Arial", 11), bg="#EEEEEE", fg="#222831")
label3 = tk.Label(text="Password:", font=("Arial", 11), bg="#EEEEEE", fg="#222831")

label1.grid(row=1, column=0)
label2.grid(row=2, column=0)
label3.grid(row=3, column=0)

#Entries
website = tk.Entry(width=35)
website.focus()
email_username = tk.Entry(width=35)
password = tk.Entry(width=34)

website.grid(row=1, column=1, columnspan=2)
email_username.grid(row=2, column=1, columnspan=2)
password.grid(row=3, column=1)

#Buttons
button = tk.Button(text="Add", width=30, bg="#76ABAE", fg="#222831", command=save)

button.grid(row=4, column=1, columnspan=2)





window.mainloop()