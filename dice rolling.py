import tkinter
from PIL import Image, ImageTk
import random

# فانکشن انتخاب و نمایش تصادفی تاس ها
def rolling_dice():
    image_dice = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # آپدیت کردن
    label_dice.configure(image=image_dice)
    # نمایش دادن
    label_dice.image = image_dice


root = tkinter.Tk()
root.geometry('400x400')
root.title('Dice Rolling')

# وارد کردن عکس های مربوط به تاس
dice = ['die1.png', 'die2.png', 'die3.png',
        'die4.png', 'die5.png', 'die6.png']
# انتخاب عدد 6 برای نمایش اولیه تاس
image_dice = ImageTk.PhotoImage(
    Image.open('die6.PNG'))

# ساخت یک لیبل برای نمایش دادن عکس ها
label_dice = tkinter.Label(root, image=image_dice)
label_dice.image = image_dice
label_dice.pack(expand=True)

# کلید مربوط به ریختن تاس
button = tkinter.Button(root, text='Roll the Dice',fg='brown', command=rolling_dice)
button.pack(expand=True)
root.mainloop()