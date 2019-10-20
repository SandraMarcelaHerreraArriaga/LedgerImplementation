import sys

def main():
    arguments = sys.argv[2::]
    inputCommand = sys.argv[1]
    checkIfValidCommands(inputCommand,arguments)
                        
def checkIfValidCommands(command,arguments):
    validCommands = ["bal","balance","register","reg","print"]
    validArgumentCommands = ["--price-db","--file","-f","--sort","-s"]
    argumentCommand = []
    valueArgumentCommand = []

    if command not in validCommands:
         return False
    else:
        for index, argument in enumerate(arguments):
            if argument in validArgumentCommands:
                argumentCommand.append(argument)
                if index+1 < len(arguments):
                    valueArgumentCommand.append(arguments[index+1])
    print(argumentCommand)
    print(valueArgumentCommand)

    if command == "balance"  or  command == "bal" :
        print("Tarea de comando balance")
    elif command == "register" or  command == "reg"  :
        print("Tarea de comando register")
    elif command == "print": 
        print("Tarea de comando print")

if __name__ == "__main__":
    main()

 

    

