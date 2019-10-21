import sys 
import re 
from Commands import register

def main():
    arguments = sys.argv[1::]
    inputCommand = sys.argv[1]
    checkIfValidCommands(inputCommand,arguments)
            
def checkIfValidCommands(command,arguments):
    validCommands = ["bal","balance","register","reg","print","--price-db","--file","-f","--sort","-s"]
    argumentCommand = []
    valueArgumentCommand = []

    if command not in validCommands:
         print("Comando invalido")
         return False
    else:
        for index, argument in enumerate(arguments):
            if argument in validCommands:
                argumentCommand.append(argument)
            else:
                valueArgumentCommand.append(argument)

    if command == "balance"  or  command == "bal" :
        print("Tarea de comando balance")
    elif command == "register" or  command == "reg"  :
        print("Tarea de comando register")
    elif command == "print": 
        print("Tarea de comando print")

if __name__ == "__main__":
   main()

 

    

