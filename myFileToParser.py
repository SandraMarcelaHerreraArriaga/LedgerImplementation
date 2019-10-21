import transaction

f = open("Expenses.ledger","r") 
myList = " "
for line in f:
    myList = myList + line.strip()
    myList.replace(' / \t','')

print(myList)

print(type(myList) is str)  # True
tree = transaction.parse(myList)




