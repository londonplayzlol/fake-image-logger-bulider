import os
import requests
os.system(f'cls & mode 100,20 & title image logger! Version 0.1 made by london playz#0225!')
logo = """  _                              _                             
 (_)                            | |                            
  _ _ __ ___   __ _  __ _  ___  | | ___   __ _  __ _  ___ _ __ 
 | | '_ ` _ \ / _` |/ _` |/ _ \ | |/ _ \ / _` |/ _` |/ _ \ '__|
 | | | | | | | (_| | (_| |  __/ | | (_) | (_| | (_| |  __/ |   
 |_|_| |_| |_|\__,_|\__, |\___| |_|\___/ \__, |\__, |\___|_|   
                     __/ |                __/ | __/ |          
                    |___/                |___/ |___/                                  
                    made by london playz#0225
      """
print(logo)
image = '1'

gif = '2'
video = '3'
webhook = input("enter ur webhook!")
image = input("enter a image")

x= (input('select ur grabber 1. image 2. gif 3. video'))
path= 'C:\\Users\\gamin\Desktop\\image logger'
os.chdir(path)
newfolder='grabber folder'
os.makedirs(newfolder)
if x == "1":
    print("ur file is making")
path2='C:\\Users\\gamin\\Desktop\\image logger\\grabber folder'
os.chdir(path2)
newimage='image logger'
os.makedirs(newimage)
os.chdir(path2)
newimage='gif logger'
os.makedirs(newimage)
os.chdir(path2)
newimage='video logger'
os.makedirs(newimage)
path3='C:\\Users\\gamin\\Desktop\\image logger\\grabber folder\\image logger'
os.chdir(path3)
os.makedirs(image)








