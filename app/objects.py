

object_ID = 0
objects = {}

def add(object: any):
    global object_ID
    
    object_ID += 1
    objects[object_ID] = object
    return object_ID

def get(ID: int):
    return objects.get(ID, None)

def remove(ID: int):
    if objects.get(ID):
        objects[ID] = None
    else:
        print("Failed to remove object")

def getAll():
    return objects