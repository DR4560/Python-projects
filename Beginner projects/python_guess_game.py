""" PYTHON GUESS SIMPLE GAME WITHOUT GRAPHIC UI"""
from PIL.ImImagePlugin import number
import os
from PIL import Image
from datetime import datetime
img_path = (r"C:\Users\System-Pc\Desktop\flower1.jpg")

#Lets also back the gift


def compare_guess_number(value):
    value_ = value
    user_name = input("Hello! Lets first guess a number?:) Tell me your name, please")
    print('Hello' + user_name)
    try:
        guess = int(input(f"Dear {user_name}, guess a number, is less then 10 but more then 0: "))
        if guess > 10 or guess < 1:
            raise ValueError("Its too far..MORE then 0 and LESS then 10")
            print("Try one more time!")
        elif guess > value_:
            print(f"Dear {user_name}, you are almost there! But my number is a little less")
        elif guess < value_:
            print("Take a little higher, you can!")
                if guess < value_:
                    print("Little more higher")
                else:
                    print("You are going right")
        else:
             print("Good job! Its a right answer! Check your Desktop, there are some gift!")
             return True
        return False

    except ValueError as ve:
       print(ve)

# creating a image object (main image)
im1 = Image.open(img_path)

# save a image using extension
im1 = im1.save("YourGift.jpg")#geek?



curr_datetime = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
splitted_path = os.path.splitext(img_path)
modified_picture_path = splitted_path[0] +
curr_datetime + splitted_path[1]
img.save(modified_picture_path)
# Open an image file


img = Image.open(img_path)
img.show()  # Display the image

while True:
    if compare_guess_number(4):
        break



#links:
#https://www.geeksforgeeks.org/python-pil-save-file-with-datetime-as-name/?ref=oin_asr1
#https://www.youtube.com/watch?v=_Izc-544tS4&ab_channel=rorymulcahey