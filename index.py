
from PIL import Image
import random, os

file = input("Image file: ").replace("\"", "")
#file = "320.png"
folder = "out"

# checking if the directory 
# exist or not.
if not os.path.exists(folder):
      
    # if the directory is not present 
    # then create it.
    os.makedirs(folder)
else:
    # Clear out the folder of files if it already exists
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

img = Image.open(file)
#img = img.resize((450,450))

# Make images with alphas from 150 to 255
# for a in range(150,256):
#     rgba = img.convert("RGBA")
#     datas = rgba.getdata()
    
#     newData = []
#     for item in datas:
#         newData.append((item[0], item[1], item[2], a))
    
#     rgba.putdata(newData)
#     rgba.save(f'{folder}/{a}.png', "PNG")


# Random color on a random pixel
# for a in range(1,51):
#     rgba = img.convert("RGBA")
#     datas = rgba.getdata()
#
#     newData = []
#
#     for item in datas:
#        newData.append(item)
#
#     # Picks random pixel to replace
#     ran = random.randint(0,int(len(newData)))
#     # Sets the color
#     newData[ran]=(random.randint(0,255), random.randint(0,255), random.randint(0,255), 0)
#     print(ran,newData[ran])
#     rgba.putdata(newData)
#     rgba.save(f'{folder}/{a}.png', "PNG")

# Add static to image
for a in range(1,31):
    rgba = img.convert("RGBA")
    datas = rgba.getdata()
    newData = []

    for item in datas:
       newData.append((
        item[0] + random.randint(0,20),
        item[1] + random.randint(0,20),
        item[2] + random.randint(0,20), item[3]))
    print(a)
    rgba.putdata(newData)
    rgba.save(f'{folder}/{a}.png', "PNG")