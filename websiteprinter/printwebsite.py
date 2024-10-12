# Page generator for the SGDL 
# Created by Tris 

import libs.functions

def main():
    lvlpath = input("drop [LEVEL!!!!!].csv file here: ").replace('"',"")
    recpath = input("drop [RECORDS!!!].csv file here: ").replace('"',"")
    libs.functions.parse_csv(lvlpath, recpath)
main()