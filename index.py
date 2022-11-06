
from PIL import Image
import random, os

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

#region menu
asciiName = """ ::::::::  :::        ::::::::::: :::::::::  :::::::::  :::::::::: :::::::::
:+:    :+: :+:            :+:     :+:    :+: :+:    :+: :+:        :+:    :+:
+:+        +:+            +:+     +:+    +:+ +:+    +:+ +:+        +:+    +:+
+#++:++#++ +#+            +#+     +#++:++#+  +#++:++#+  +#++:++#   +#++:++#:
       +#+ +#+            +#+     +#+        +#+        +#+        +#+    +#+
#+#    #+# #+#            #+#     #+#        #+#        #+#        #+#    #+#
 ########  ########## ########### ###        ###        ########## ###    ###
                             Roblox image slipper\n"""

def menu(a):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(asciiName)
    return input(f'{a}: ')
#endregion

file = menu("Image file").replace("\"", "")

img = Image.open(file)

if menu("Resize? (y/n)") == "y":
    size = menu("Size (x,y): ").split(",")
    img = img.resize((int(size[0]),int(size[1])))

#region methods
# Make images with alphas from 150 to 255
def alphasMethod():
    count = 0
    for a in range(150,256):
        count += 1
        rgba = img.convert("RGBA")
        datas = rgba.getdata()

        newData = []
        for item in datas:
            newData.append((item[0], item[1], item[2], a))

        rgba.putdata(newData)
        rgba.save(f'{folder}/{a}.png', "PNG")

# Random color on a random pixel
def randomColorMethod(count,intensity):
    for a in range(0,count):
        rgba = img.convert("RGBA")
        datas = rgba.getdata()

        newData = []

        for item in datas:
            newData.append(item)

        # Picks random pixel to replace
        ran = random.randint(0,int(len(newData)))
        # Sets the color
        newData[ran]=(
            random.randint(0,intensity),
            random.randint(0,intensity),
            random.randint(0,intensity), 0)
        print(ran,newData[ran])
        rgba.putdata(newData)
        rgba.save(f'{folder}/{a+1}.png', "PNG")

# Add static to image
def staticMethod(count,intensity):
    for a in range(0,count):
        rgba = img.convert("RGBA")
        datas = rgba.getdata()
        newData = []

        for item in datas:
            newData.append((
                item[0] + random.randint(0,intensity),
                item[1] + random.randint(0,intensity),
                item[2] + random.randint(0,intensity), item[3]))
        print(a)
        rgba.putdata(newData)
        rgba.save(f'{folder}/{a+1}.png', "PNG")
#endregion

choice = menu("Choose method\n\n1. Alphas\n2. Random color\n3. Static\n\nChoice")
if choice == "1":
    alphasMethod()
elif choice == "2":
    randomColorMethod(int(menu("How many images?")),int(menu("How much intensity? (1-255)")))
elif choice == "3":
    staticMethod(int(menu("How many images?")),int(menu("How much intensity? (1-255)")))
else:
    print("Invalid choice")