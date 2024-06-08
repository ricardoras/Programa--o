from customtkinter import *

app = CTk()
app.geometry('720x720')
app.title('Bot de cadastro')
set_appearance_mode("light")

title = CTkLabel(master=app,text="Bem vindo a Queo!", font=('Arial',20), text_color="#0000ff")
title.place(relx=0.5,rely=0.3,anchor = 'e')

switch = CTkSwitch(master=app, text='Multiuser?')
switch.place(relx=0.5, rely=0.4, anchor='center')      


btn = CTkButton(master=app, text="CLick aqui para login e senha!", corner_radius=32,)
btn.place(relx=0.5, rely=0.5, anchor='center')      

btnCombo = CTkComboBox(master=app ,values=['Solar','Femsa'])
btnCombo.place(relx=0.5, rely=0.7, anchor='center')

app.mainloop()