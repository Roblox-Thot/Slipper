from PIL import Image
import random, os, math

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

def progressBar(msg,number,outOf):
    count = math.ceil(((number+1)/outOf)*30)
    present = math.ceil(((number+1)/outOf)*100)
    print(f'{msg} (O{"o"*count}f{"_"*(30-count)}) {present}% ', end='\r')

class Methods:
    def __init__(self, image, folder) -> None:
        self.img = image
        self.folder = folder

    # Make images with alphas from 150 to 255
    def alphasMethod(self):
        printName()
        for count, a in enumerate(range(155,255), start=1):
            progressBar("Making images", count, 100)
            rgba = self.img.convert("RGBA")
            datas = rgba.getdata()

            newData = [(item[0], item[1], item[2], a) for item in datas]
            rgba.putdata(newData)
            rgba.save(f'{self.folder}/{count}.png', "PNG")

    # Random color on a random pixel
    def randomColorMethod(self,count):
        printName()
        for a in range(0,count):
            progressBar("Making images", a, count)
            rgba = self.img.convert("RGBA")
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
            rgba.save(f'{self.folder}/{a+1}.png', "PNG")

    # Add static to image
    def staticMethod(self,count,intensity):
        printName()
        for a in range(0,count):
            progressBar("Making images", a, count)
            rgba = self.img.convert("RGBA")
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
            rgba.save(f'{self.folder}/{a+1}.png', "PNG")

    # Remove black with static
    def transStaticMethod(self,count,intensity):
        printName()
        for a in range(0,count):
            progressBar("Making images", a, count)
            rgba = self.img.convert("RGBA")
            datas = rgba.getdata()
            
            
            newData = [
                (
                    item[0],
                    item[1],
                    item[2],
                    item[3] - random.randint(0, intensity),
                )
                for item in datas
            ]

            rgba.putdata(newData)
            rgba.save(f'{self.folder}/{a+1}.png', "PNG")

    # Remove black with static
    def shadowMethod(self,count):
        printName()
        for a in range(0,count):
            progressBar("Making images", a, count)
            rgba = self.img.convert("RGBA")
            datas = rgba.getdata()
            
            
            newData = [
                (
                    item[0] + random.randint(-1,1),
                    item[1] + random.randint(-1,1), # Used fo a tiny bit of static
                    item[2] + random.randint(-1,1),
                    item[3] - (random.randint(250,255)-round((item[0]+item[1]+item[2])/3)),
                )
                for item in datas
            ]

            rgba.putdata(newData)
            rgba.save(f'{self.folder}/{a+1}.png', "PNG")

if __name__ == "__main__":
    file = menu("Image file").replace("\"", "")

    img = Image.open(file)

    if menu("Resize? (y/n)") == "y":
        size = menu("Size (x,y): ").split(",")
        img = img.resize((int(size[0]),int(size[1])))

    folder = "out"

    if not os.path.exists(folder):
        os.makedirs(folder)
    else:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')

    methodFunctions = (Methods(img,folder))

    methodList = [
        "Alpha (change alpha from 150-255)",
        "Random color (sets a random pixel to a random color)",
        "Static (adds a static to the image)",
        "Remove \"shadows\" (Shitty method + static :skull:)",
        "Transparent static (Shitty method if high intensity)"
    ]

    methods = "Choose method\n\n"
    for x in range(len(methodList)):
        methods = f'{methods}{x + 1}. {methodList[x]}\n'

    choice = menu(methods+"\nChoice")
    match choice:
        case "1":
            methodFunctions.alphasMethod()
            menu(f'Images have been saved to the folder "{folder}"')
        case "2":
            methodFunctions.randomColorMethod(int(menu("How many images?")))
            menu(f'Images have been saved to the folder "{folder}"')
        case "3":
            methodFunctions.staticMethod(int(menu("How many images?")),int(menu("(DONT USE HIGH NUMBERS)\n\nHow much intensity? (1-255)")))
            menu(f'Images have been saved to the folder "{folder}"')
        case "4":
            methodFunctions.shadowMethod(int(menu("How many images?")))
            menu(f'Images have been saved to the folder "{folder}"')
        case "5":
            methodFunctions.transStaticMethod(int(menu("How many images?")),int(menu("(DONT USE HIGH NUMBERS)\n\nHow much intensity? (1-255)")))
            menu(f'Images have been saved to the folder "{folder}"')
        case _:
            print("Invalid choice")
