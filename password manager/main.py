from tkinter import *
from tkinter import messagebox
import password_generator
import json
def save():
    website = website_entry.get()
    mail = mail_entry.get()
    password  = password_entry.get()
    new_data = {website:{
        "email":mail,
        "password":password,
    }}
    if len(website)==0 or len(mail)==0 or password == 0:
        messagebox.showerror(title="Error",message="Please enter the details")
    else:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)    
        else:    
                data.update(new_data)
                with open("data.json","w") as data_file:
                    json.dump(data,data_file,indent=4) 
                
        finally:
                website_entry.delete(0,END)
                mail_entry.delete(0,END)
                password_entry.delete(0,END)
                messagebox.showinfo(title="Successful",message="The details are updated successfully")
def password_gen():
    password_entry.delete(0,END)
    password = password_generator.password_generator()
    password_entry.insert(0,password)

def find():
    website = website_entry.get()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
         messagebox.showerror(title="Error",message="Data file is Empty")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email : {email}\nPassword : {password}")
        else:
             messagebox.showerror(title=website,message="Data not exist")
              

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image= logo_img)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
mail_label = Label(text="Email/Username:")
mail_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

website_entry = Entry(width=28)
website_entry.grid(row=1,column=1)
website_entry.focus()
mail_entry = Entry(width=46)
mail_entry.grid(row=2,column=1,columnspan=2)
password_entry = Entry(width=28)
password_entry.grid(row=3,column=1)

generate_btn = Button(text="Generate Password",command=password_gen)
generate_btn.grid(row=3,column=2)
add_btn = Button(text="Add",width=37,command=save)
add_btn.grid(row=4,column=1,columnspan=2)
search_btn = Button(text="Search",width=14,command=find)
search_btn.grid(row=1,column=2)






window.mainloop()
