import os

def main(path,units):

    blockNames = ["Definitions","Propositions","Examples","Exercises","Main"]

    for blockName in blockNames:

        if not os.path.exists(path+"\\"+blockName):
            os.makedirs( path+"\\"+blockName )
        f = open( path+"\\"+blockName + "\\" + blockName + ".tex" ,"w" )
        f.close()
        
        for unit in range(units):

            f = open( path+"\\"+blockName + "\\" + "unit " + str(unit+1) + ".tex" ,"w" )
            f.close()
        
    if not os.path.exists(path+"\\Main"): os.makedirs( path+"\\Main" )
    f = open(path+"\\Main\\main.tex","w")
    f.close()

p= input("Path: ")
n = input("Number of units: ")
main(p,n)
