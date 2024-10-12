# Page generator for the SGDL 
# Created by Tris 

import libs.functions

def main():
    path = input("drop .csv file here: ").replace('"',"")
    libs.functions.parse_csv(path)
main()