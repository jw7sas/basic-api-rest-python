# imports
from users.models import User
from app import Database

""" Clase de control de usuarios. """
class UserController():

    def __init__(self):
        pass

    def createUser(self, user):
        """ Método de creación de usuarios. """
        error = False
        response = None

        try:
            db = Database().getConn()
            cursor = db.cursor()
            query = "INSERT INTO users (name, lastname) values (?,?)"
            response = cursor.execute(query, [user.name, user.lastname])
            db.commit()

            response = "Usuario: " + user.name + " " + user.lastname + ": registrado correctamente!"
        except ValueError:
            error = str(ValueError)
        finally:
            return {
                'response': response,
                'error': error
            }
            
        
