from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:52819' % ('aacuser', 'abc123'))
        self.database = self.client['AAC']
        

    
# Complete this create method to implement the C in CRUD.

    def create(self, data):
        if data is not None:
            #Insert the data, and return true if successful.
            self.database.animals.insert(data)  # data should be dictionary   
            return True
        else:
            #data was invalid.
            raise Exception("Nothing to create, because data parameter is empty")
            return False

# Create method to implement the R in CRUD. 
    def read(self, data):
        if data is not None:
            #return all records that match.
            return self.database.animals.find(data,{"_id":False})
            for item in read:
                print(item)
            #return self.database.animals.find(data,{"_id":False})
        else:
            #Data was invalid.
            raise Exception("Nothing to read, because data parameter is empty")
            return False
        
# Create method to implement the U in CRUD. 
    def update(self, searchinfo, updatedinfo):
        if searchinfo is not None:
            #return all records that match.
             return self.database.animals.update(searchinfo,updatedinfo)
             
        else:
            #Data was invalid.
            raise Exception("Nothing to update, because data parameter is empty")
            return False
        
# Create method to implement the D in CRUD. 
    def delete(self, deletedinfo):
        if deletedinfo is not None:
        #    #return all records that match.
             return self.database.animals.remove(deletedinfo)
        else:
            raise Exception("Nothing to delete, because data parameter is empty")
            return False

