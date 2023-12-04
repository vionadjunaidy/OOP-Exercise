from classDefinition import Food

def list_of_objectsVD():
    objects = []

    while True:
        no_of_items = input(f'Input the number of items: ')
    
        if no_of_items > 0:
            break
        
    for item in range(no_of_items):
        name_of_item = input(f'Input name of item: ')

        while True:
            no_of_pounds = input(f'Input the number of pounds: ')
            if no_of_pounds > 0:
                break
        
        objects.append(Food(name_of_item, no_of_pounds))
   

list_of_objectsVD()