stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory (inventory):
    print ('Inventory: ')
    for i, j in inventory.items():
        print (i + " " + str(j))


displayInventory(stuff)

for i in stuff.values():
    print(i)

