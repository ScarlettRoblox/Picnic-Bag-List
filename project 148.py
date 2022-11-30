from tkinter import *
import random

root=Tk()
root.title("Picnic Bag List")
root.geometry("400x400")


list1 = [" Bottle", "Tiffin/Snacks", "Hand Sanitizer","Tissues","First Aid Kit"]
print(list1)
def random_number():
    random_no = random.randint(0, 4)
    
    print(random_no)
    random_item_for_picnic= list1[random_no]
    print("Picnic Bag :" + random_item_for_picnic)
    
btn=Button(root,text="Picnic Bag",command = random_number)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop