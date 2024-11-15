from tkinter import *
from random import choice,randint,shuffle
from tkinter.ttk import Notebook


timer = None
    # window
root = Tk()
root.title("Hot Roll")
root.geometry("550x450")
root.config(bg="white")
root.resizable(False,False)

    # images
image_dice_one = PhotoImage(file="images/one.png")
image_dice_two = PhotoImage(file="images/two.png")
image_dice_three = PhotoImage(file="images/three.png")
image_dice_four = PhotoImage(file="images/four.png")
image_dice_five = PhotoImage(file="images/five.png")
image_dice_six = PhotoImage(file="images/six.png")
image_list = [image_dice_one,image_dice_two,image_dice_three,
              image_dice_four,image_dice_five,image_dice_six]

    # Frame
menu = Notebook()
menu.grid(row=1,column=1)

main_page = Frame(menu)
main_page.grid(row=1,column=2)
menu.add(main_page,text="Dice_six")
main_page.config(bg="white")

    # fun
def finish_program():
    root.destroy()

def test():
    # roll_dice(randint(2,5))
    pass

def roll_dice():
    canvas.itemconfig(canvas_image, image=choice(image_list))
    pass
    # global timer
    # if count >0:
    #     print("roll")
    #     timer = root.after(150,roll_dice,count-1)
    # else:
    #     print("cancel")
    #     root.after_cancel(timer)
    # for i in image_list:
    #     print(i)
    #     canvas.itemconfig(canvas_image, image=i)




    #canvas
canvas = Canvas(master=main_page,width=400,height=400,
                highlightthickness=0,bg='black')
canvas_image = canvas.create_image(0, 0, anchor="nw", image=choice(image_list))
canvas.grid(row=1,column=2, rowspan=3)


    # buttons root_window
button_roll = Button(master=main_page,text="Rool",command=roll_dice,width=15,height=3)
button_roll.grid(row=1,column=1,padx=15)
button_setings = Button(master=main_page,text="Setings",command=test,width=15,height=3)
button_setings.grid(row=2,column=1,padx=15)
button_exit = Button(master=main_page,text="exit",command=root.destroy,width=15,height=3)
button_exit.grid(row=3,column=1,padx=15)





mainloop()