from PIL import Image
import random, os, math

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
            print(f'Failed to delete {file_path}. Reason: {e}')

#region menu
asciiName = """ ::::::::  :::        ::::::::::: :::::::::  :::::::::  :::::::::: :::::::::
:+:    :+: :+:            :+:     :+:    :+: :+:    :+: :+:        :+:    :+:
+:+        +:+            +:+     +:+    +:+ +:+    +:+ +:+        +:+    +:+
+#++:++#++ +#+            +#+     +#++:++#+  +#++:++#+  +#++:++#   +#++:++#:
       +#+ +#+            +#+     +#+        +#+        +#+        +#+    +#+
#+#    #+# #+#            #+#     #+#        #+#        #+#        #+#    #+#
 ########  ########## ########### ###        ###        ########## ###    ###
                             Roblox image slipper\n"""

def printName():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(asciiName)

def menu(a):
    printName()
    return input(f'{a}: ')
#endregion

file = menu("Image file").replace("\"", "")

img = Image.open(file)

if menu("Resize? (y/n)") == "y":
    size = menu("Size (x,y): ").split(",")
    img = img.resize((int(size[0]),int(size[1])))

def progressBar(msg,number,outOf):
    count = math.ceil(((number+1)/outOf)*30)
    present = math.ceil(((number+1)/outOf)*100)
    print(f'{msg} (O{"o"*count}f{"_"*(30-count)}) {present}% ', end='\r')

#region methods
# Make images with alphas from 150 to 255
def alphasMethod():
    printName()
    for count, a in enumerate(range(155,255), start=1):
        progressBar("Making images", count, 100)
        rgba = img.convert("RGBA")
        datas = rgba.getdata()

        newData = [(item[0], item[1], item[2], a) for item in datas]
        rgba.putdata(newData)
        rgba.save(f'{folder}/{count}.png', "PNG")
    menu(f'Images have been saved to the folder "{folder}"')

# Random color on a random pixel
def randomColorMethod(count):
    printName()
    for a in range(0,count):
        progressBar("Making images", a, count)
        rgba = img.convert("RGBA")
        datas = rgba.getdata()

        newData = []

        for item in datas:
            newData.append(item)

        # Picks random pixel to replace
        ran = random.randint(0, len(newData))
        # Sets the color
        newData[ran]=(
            random.randint(0,item[0]),
            random.randint(0,item[1]),
            random.randint(0,item[2]), item[3])
        rgba.putdata(newData)
        rgba.save(f'{folder}/{a+1}.png', "PNG")
    menu(f'Images have been saved to the folder "{folder}"')

# Add static to image
def staticMethod(count,intensity):
    printName()
    for a in range(0,count):
        progressBar("Making images", a, count)
        rgba = img.convert("RGBA")
        datas = rgba.getdata()
        newData = [
            (
                item[0] + random.randint(-intensity, intensity),
                item[1] + random.randint(-intensity, intensity),
                item[2] + random.randint(-intensity, intensity),
                item[3],
            )
            for item in datas
        ]
        rgba.putdata(newData)
        rgba.save(f'{folder}/{a+1}.png', "PNG")
    menu(f'Images have been saved to the folder "{folder}"')

# Remove black with static
def testMethod(count):
    printName()
    for a in range(0,count):
        progressBar("Making images", a, count)
        rgba = img.convert("RGBA")
        datas = rgba.getdata()
        
        
        newData = [
            (
                item[0],
                item[1],
                item[2],
                item[3] - (random.randint(200,255)-round((item[0]+item[1]+item[2])/3)),
            )
            for item in datas
        ]

        rgba.putdata(newData)
        rgba.save(f'{folder}/{a+1}.png', "PNG")
    menu(f'Images have been saved to the folder "{folder}"')
#endregion

choice = menu("""Choose method\n\n1. Alpha (change alpha from 150-255)\n2. Random color (sets a random pixel to a random color)\n3. Static (adds a static to the image)\n4. Remove "shadows" (Shitty method + static :skull:)\n\nChoice""")
match choice:
    case "1":
        alphasMethod()
    case "2":
        randomColorMethod(int(menu("How many images?")))
    case "3":
        staticMethod(int(menu("How many images?")),int(menu("How much intensity? (1-255)")))
    case "4":
        testMethod(int(menu("How many images?")))
    case _:
        print("Invalid choice")
