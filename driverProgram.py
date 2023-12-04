from classDefinition import Food

def list_of_objectsVD():
    objects = []

    while True:
        no_of_items = int(input(f'How many items will your order today? '))
    
        if no_of_items > 0:
            break
        else:
            print(f'Number of items must be at least 1.')
        
    for item in range(no_of_items):
        print(f'Item #{item+1}')
        name_of_item = input(f'Enter food: ')

        while True:
            no_of_pounds = float(input(f'Enter amount of pounds: '))
            if no_of_pounds > 0:
                break
        
        patungVio = Food(name_of_item, no_of_pounds)
        objects.append(patungVio)

    return objects

def contents_of_listVD(objects):
    for item in objects:
        print(f'Name: {item.getName()}')
        print(f'Amount: {item.getAmount()}')
        print(f'Price: {item.getPrice()}')
        print(f'Total Cost: {item.calculateCostVD()}')

def main():
    vio = list_of_objectsVD()
    contents_of_listVD(vio)

main()
