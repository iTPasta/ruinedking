from os import path as ospath
from game_data import *
from pathing import path

#activation du système de progression
progress_ON = True
#chemin du fichier de sauvegarde de la progression
progress_file = path + "/progress.txt"

#sauvegarde la progression dans un fichier
def save_progress(lvl):
    if lvl["next_level"] in progress_codes:
        with open(progress_file,'w') as f:
            f.write(progress_codes[lvl["next_level"]])
    else:
        reset_progress()

#retourne le niveau de progression actuel
def get_progress():
    if ospath.exists(progress_file):
        code = ""
        with open(progress_file,'r') as f:
            code = f.readline()
            f.close()
        if code == "RESET":
            return "RESET"
        for lvls in progress_codes.keys():
            lvls_codes = progress_codes[lvls]
            if lvls_codes == code:
                return lvls
    return "level_0"

#ordonne de réinitialiser la progression
def reset_progress():
    with open(progress_file,'w') as f:
        f.write("RESET")

#efface la progression
def clear_progress():
    with open(progress_file,'w') as f:
        f.write("")