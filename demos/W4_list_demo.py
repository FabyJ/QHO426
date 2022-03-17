
⌄
⌄
⌄
#Declare an empty list
bleh = []
meh = list()
#Declare a non-empty
yummy = ["Pizza", "Lasagne", "Fish and Chips"]
#Print an entire list
print(yummy)
#Printing a single item
print(yummy[2])
#Printing some items
print(yummy[:2])
#Add elements to our list (expand it) - adding at the end
print(bleh)
bleh.append("Sea food")
bleh.append("Soup")
bleh.append("Liver")
print(bleh)
#Adding multiple items to the list, based on user input
for i in range(5):
    yummy.append(input("Enter new yummy food: ")) #- expand list
    #yummy[i] = input() - replace items]
print(yummy)
#Adding new items, at specific positions on the list
print(bleh)
bleh.insert(1, "Mashed Potatoes")
print(bleh)
bleh.insert(3, "Cabbage")
print(bleh)
#Remove an item from list, based on name
if "Mashed Potatoes" in bleh:
    bleh.remove("Mashed Potatoes")
bleh.remove("Soup")
#Remove item by index
x = bleh.pop(1)
print(bleh)
print(x)
#Alternative way of deleting an item via index
del bleh[1]
print(bleh)
#Extending a list
bleh.extend(["Fish", "Frankfurters", "Beetroot"])
print(bleh)
bleh.extend(yummy)
print(bleh)
#Checking for particular data type
lista = ["Fred", True, 6, 8, -3.6, False, "Lala", 55]
for item in lista:
    if isinstance(item, str):
        print(item)