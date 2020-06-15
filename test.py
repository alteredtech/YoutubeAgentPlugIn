from pathlib import Path
import os

playlistName = "Project Ozone 2"
text = "Minecraft - Project Ozone 2 #1: Skyblock Reloaded (Kappa)"



def parser(text, symbol):
    intro_list = []
    symFound = False
    Title = ""
    for i in range(len(text)):
        if text[i] != symbol and symFound == False:
            pass
        elif text[i] == symbol:
            symFound = True
        elif symFound:
            intro_list.append(text[i])
    Title = ''.join(intro_list)
    print(Title)

if __name__ == "__main__":
    
    parser(text,":")
    cwd = os.path.dirname(os.path.realpath(__file__))
    print(cwd+playlistName)
    Path(cwd+"/"+playlistName).mkdir(parents=True,exist_ok=True)