"""IMAGE EDITOR"""
from PIL import Image, ImageEnhance, ImageFilter
import os


print ("Hello! Welcome to the mini-app")
print("what you have to do is to put in the 'imgs' folder your pics")
print("And edit the pics inside automatically to the parameters below")


path = './imgs'
pathOut = '/editedImgs'


for filename in os.listdir(path):
    #Setting up the open img construction
    img = Image.open(f"{path}/{filename}")
    #the pics editing settings are below:

    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_editedSHARPEN-Black.jpg')