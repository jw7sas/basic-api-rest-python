# imports
import os
import json
from flask import Flask, jsonify, request

# imports models
from users.models import User
from users.models import Error

# imports controllers
from users.controllers import UserController

# imports Database
from app import Database

app = Flask(__name__)

""" Definición de rutas de la aplicación. """

@app.route("/")
def index():
    return "Bienvenidos Ásperos GEEK!!"

@app.errorhandler(405)
def method_not_allowed(error):
    """ Método de error 405. """
    ex = Error(error)
    return jsonify(ex.getError())

@app.errorhandler(404)
def error404(error):
    """ Método de error 400. """
    ex = Error(error)
    return jsonify(ex.getError())

@app.errorhandler(500)
def error500(error):
    """ Método de error 500. """
    ex = Error(error)
    return jsonify(ex.getError())

@app.route("/users/create", methods=["POST"])
def createUsers():
    """ Método de creación de usuarios. """
    usersJson = json.loads(request.data)
    response = []
    if usersJson:
        for userJson in usersJson:
            user = User(userJson)
            user_c = UserController()
            response.append(user_c.createUser(user))
    else:
        ex = Error("No hay usuarios para registrar")
        response = ex.getError()

    return after_request(jsonify(response))


"""
Enable CORS. Disable it if you don't need CORS
"""
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response


if __name__ == "__main__":
    Database().createTables()
    app.run("0.0.0.0", debug=True)