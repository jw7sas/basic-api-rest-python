""" Clase de usuarios. """
class User():

    def __init__(self, user):
        if(user): 
            self.name = user["name"]
            self.lastname = user["lastName"]

