from tkinter import *
from tkinter import messagebox
import pyperclip

# check shift value input.continue with encryption/decryption if input is in this list
SH_VALUES=["0","1","2","3","4","5","6","7","8","9","10","11","12"]

#list of letters
LETTERS=["a","b","c","d",
         "e","f","g","h",
         "i","j","k","l",
         "m","n","o","p",
         "q","r","s","t",
         "u","v","w","x",
         "y","z",
         "a", "b", "c", "d",
         "e", "f", "g", "h",
         "i", "j", "k", "l",
         "m", "n", "o", "p",
         "q", "r", "s", "t",
         "u", "v", "w", "x",
         "y", "z"]
#list of numbers
NUMBERS=["1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9"]


def encrypt():
    '''encrypt function. opens a messagebox with the final message as well as copy to clipboard'''
    direction="encrypt"
    encoded_message=[]
    shift_value = value_inside.get()
    if shift_value in SH_VALUES:
        shift_value=int(value_inside.get())
    else:
        messagebox.showerror(f"A problem appeared", message=f"{shift_value} is not available as a shift value option.\nPlease try again")
        return None
    msg=str(msg_entry.get().lower())
    print(msg)
    for letter in msg:
        if letter==" ":
            encoded_message.append(" ")
        elif letter in LETTERS:
            new_letter_index=LETTERS.index(letter) + shift_value
            encoded_message.append(LETTERS[new_letter_index])
        elif letter in NUMBERS:
            new_index=NUMBERS.index(letter) + shift_value
            encoded_message.append(NUMBERS[new_index])
    print(encoded_message)
    #this for loop is used to get rid of any spaces added after the message
    for i,char in enumerate(encoded_message):
        if char==" " and i==len(encoded_message):
            encoded_message.remove(char)
    final_msg="".join(encoded_message)
    messagebox.showinfo(title=f"{direction.title()}ed message", message=final_msg)
    msg=""
    #copies result to clipboard
    pyperclip.copy(final_msg)
    msg_entry.delete(0,END)


def decrypt():
    '''decrypt function. opens a messagebox with the final message as well as copy to clipboard'''

    direction = "decrypt"
    encoded_message = []
    shift_value = value_inside.get()
    if shift_value in SH_VALUES:
        shift_value = int(value_inside.get())
    else:
        messagebox.showerror(f"A problem appeared", message=f"{shift_value} is not available as a shift value option.\nPlease try again")
        return None
    msg = str(msg_entry.get().lower())
    #checks in message. adds space where space exists otherwise adds the encrypted letter or number
    for letter in msg:
        if letter == " ":
            encoded_message.append(" ")
        elif letter in LETTERS:
            new_letter_index = LETTERS.index(letter) - shift_value
            encoded_message.append(LETTERS[new_letter_index])
        elif letter in NUMBERS:
            new_num_in = NUMBERS.index(letter) - shift_value
            encoded_message.append(NUMBERS[new_num_in])
    print(encoded_message)
    #this next for loop exists to get rid of any spaces added after the entire message
    for i,char in enumerate(encoded_message):
        if char==" " and i==len(encoded_message):
            encoded_message.remove(char)
    final_msg="".join(encoded_message)

    messagebox.showinfo(title=f"{direction.title()}ed message", message=final_msg)
    #copies result to clipboard
    pyperclip.copy(final_msg)
    #empties the message entry widget
    msg_entry.delete(0,END)
numbers=[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
window=Tk()

window.title("Caesar Cipher")
canvas=Canvas(width=512,height=512)
img=PhotoImage(file="caesar_cipher.png")
canvas.create_image(256,256,image=img)
canvas.grid(row=1,column=2)

shift_val_lbl=Label(text="Shift the text by: ")
shift_val_lbl.grid(row=3,column=1)
value_inside=StringVar()
shift_val_opt=OptionMenu(window,value_inside,1,2,3,4,5,6,7,8,9,10,11,12)
shift_val_opt.grid(row=3,column=2)

encr_but=Button(text="Encrypt",highlightthickness=0,command=encrypt)
decr_but=Button(text="Decrypt",highlightthickness=0,command=decrypt)
encr_but.grid(column=5,row=4)
decr_but.grid(column=5,row=2)
msg_entry=Entry(width=50)
msg_entry.grid(row=4,column=2)
window.mainloop()