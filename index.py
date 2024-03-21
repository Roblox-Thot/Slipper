from PIL import Image
import random, os, math

class Functions:
    def __init__(self) -> None:
        self.ascii_name:str = """ ::::::::  :::        ::::::::::: :::::::::  :::::::::  :::::::::: :::::::::
:+:    :+: :+:            :+:     :+:    :+: :+:    :+: :+:        :+:    :+:
+:+        +:+            +:+     +:+    +:+ +:+    +:+ +:+        +:+    +:+
+#++:++#++ +#+            +#+     +#++:++#+  +#++:++#+  +#++:++#   +#++:++#:
    +#+ +#+            +#+     +#+        +#+        +#+        +#+    +#+
#+#    #+# #+#            #+#     #+#        #+#        #+#        #+#    #+#
########  ########## ########### ###        ###        ########## ###    ###
                            Roblox image slipper\n"""

    def printName(self) -> None:
        """Prints the ascii art name (cringe)
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.ascii_name)

    def menu(self, text:str) -> str:
        """Prints the name and gives an input with text

        Args:
            text (str): text to show after printing the title

        Returns:
            str: the return of the input
        """
        self.printName()
        return input(f'{text}: ')

    def progressBar(self, msg:str, number:int, outOf:int) -> None:
        """Display a progress bar in the console.

        Args:
            msg (str): A message to display along with the progress bar.
            number (int): The current progress number.
            outOf (int): The total number representing completion.
        """
        count:int = math.ceil(((number+1)/outOf)*30)
        present:int = math.ceil(((number+1)/outOf)*100)
        print(f'{msg} (O{"o"*count}f{"_"*(30-count)}) {present}% ', end='\r')

class Methods:
    def __init__(self, image:Image, folder:str) -> None:
        """Method class holding all the methods used

        Args:
            image (Image): image to be used by any method
            folder (str): the path to the folder to contain the images
        """
        self.img = image
        self.folder = folder
        self.func = Functions()

    def alphasMethod(self) -> None:
        """Makes images with alphas from 150 to 250
        """
        self.func.printName()
        for count, a in enumerate(range(155,255), start=1):
            self.func.progressBar("Making images", count, 100)
            rgba = self.img.convert("RGBA")
            datas = rgba.getdata()

            newData = [(item[0], item[1], item[2], a) for item in datas]
            rgba.putdata(newData)
            rgba.save(f'{self.folder}/{count}.png', "PNG")

    def randomColorMethod(self, count:int) -> None :
        """Makes images with one random pixel set to a random color

        Args:
            count (int): the amount of images to make
        """
        self.func.printName()
        for a in range(count):
            self.func.progressBar("Making images", a, count)
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
    def staticMethod(self, count:int, intensity:int) -> None :
        self.func.printName()
        for a in range(count):
            self.func.progressBar("Making images", a, count)
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

    def transStaticMethod(self, count:int, intensity:int) -> None :
        """Make static with the alpha channel

        Args:
            count (int): the amount of images to make
            intensity (int): how much alpha to apply
        """
        self.func.printName()
        for a in range(count):
            self.func.progressBar("Making images", a, count)
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

    def shadowMethod(self, count:int) -> None :
        """Removes the black parts of an image

        Args:
            count (int): the amount of images to make
        """
        self.func.printName()
        for a in range(count):
            self.func.progressBar("Making images", a, count)
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

    def lightMethod(self,count:int) -> None :
        """Remove the whites with static for diff hashes

        Args:
            count (int): the amount of images to make
        """
        self.func.printName()
        for a in range(count):
            self.func.progressBar("Making images", a, count)
            rgba = self.img.convert("RGBA")
            datas = rgba.getdata()
            
            
            newData = [
                (
                    item[0] + random.randint(-1,1),
                    item[1] + random.randint(-1,1), # Used fo a tiny bit of static
                    item[2] + random.randint(-1,1),
                    item[3] - (random.randint(250,255)-round(255-(item[0]+item[1]+item[2])/3)),
                )
                for item in datas
            ]

            rgba.putdata(newData)
            rgba.save(f'{self.folder}/{a+1}.png', "PNG")

if __name__ == "__main__":
    FUNCS:Functions = Functions()
    FILE:str = FUNCS.menu("Image file").replace("\"", "")

    img:Image = Image.open(FILE)

    if FUNCS.menu("Resize? (y/n)") == "y":
        size = FUNCS.menu("Size (x,y): ").split(",")
        img = img.resize((int(size[0]),int(size[1])))

    FOLDER:str = "out"

    if not os.path.exists(FOLDER):
        os.makedirs(FOLDER)
    else:
        for filename in os.listdir(FOLDER):
            file_path = os.path.join(FOLDER, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')

    method_functions:Methods = Methods(img,FOLDER)

    method_list:list = [
        "Alpha (change alpha from 150-255)",
        "Random color (sets a random pixel to a random color)",
        "Static (adds a static to the image)",
        "Remove \"shadows\" (Shitty method + static :skull:)",
        "Remove \"highlights\" (Shitty method + static :skull:)",
        "Transparent static (Shitty method if high intensity)"
    ]

    methods:str = "Choose method\n\n"
    for x in range(len(method_list)):
        methods = f'{methods}{x + 1}. {method_list[x]}\n'

    choice:str = FUNCS.menu(methods+"\nChoice")
    match choice:
        case "1":
            method_functions.alphasMethod()
            FUNCS.menu(f'Images have been saved to the folder "{FOLDER}"')

        case "2":
            images = FUNCS.menu("How many images?")
            method_functions.randomColorMethod(int(images))
            FUNCS.menu(f'Images have been saved to the folder "{FOLDER}"')

        case "3":
            images = FUNCS.menu("How many images?")
            intensity = FUNCS.menu("(DONT USE HIGH NUMBERS)\n\nHow much intensity? (1-255)")
            method_functions.staticMethod(int(images),int(intensity))
            FUNCS.menu(f'Images have been saved to the folder "{FOLDER}"')

        case "4":
            images = FUNCS.menu("How many images?")
            method_functions.shadowMethod(int(images))
            FUNCS.menu(f'Images have been saved to the folder "{FOLDER}"')

        case "5":
            images = FUNCS.menu("How many images?")
            method_functions.lightMethod(int(images))
            FUNCS.menu(f'Images have been saved to the folder "{FOLDER}"')

        case "6":
            images = FUNCS.menu("How many images?")
            intensity = FUNCS.menu("(DONT USE HIGH NUMBERS)\n\nHow much intensity? (1-255)")
            method_functions.transStaticMethod(int(images),int(intensity))
            FUNCS.menu(f'Images have been saved to the folder "{FOLDER}"')

        case _:
            print("Invalid choice")
            input("Press enter to exit")
