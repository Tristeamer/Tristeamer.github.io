# Testfile

name = input("Level Name: ")
creators = input("Level Creators: ")
verifier = input("Verifier:")
game_ver = input("Game version: ")
lvl_length = input("Level length: ")
lvl_id = input("Level ID: ")
lvl_desc = input("Level description: ")

with open("data/levels/1.lvl", "w") as lvl_dbf:
    lvl_dbf.write(name+"\n")
    lvl_dbf.write(creators+"\n")
    lvl_dbf.write(verifier+"\n")
    lvl_dbf.write(game_ver+"\n")
    lvl_dbf.write(lvl_length+"\n")
    lvl_dbf.write(lvl_id+"\n")
    lvl_dbf.write(lvl_desc+"\n")

lvl_dbf.close()