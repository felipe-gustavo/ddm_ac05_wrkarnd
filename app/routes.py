from flask import Flask, request

from services.get_property_by_id import getPropertyByIdService
from services.list_properties_by_user_service import listPropertiesByUserService
from services.list_properties_service import listPropertiesService
from services.create_property_service import createPropertyService
from services.sigin_service import signinService
from services.sigup_service import signupService

app = Flask(__name__)


@app.route("/users", methods=["POST"])
def createUser():
    return signupService(request.get_json()), 201


@app.route("/users/login", methods=["POST"])
def login():
    return signinService(request.get_json()), 200


@app.route("/properties/<userId>", methods=["POST"])
def createProperty(userId):
    return createPropertyService(userId, request.get_json()), 200


@app.route("/properties", methods=["GET"])
def listProperties():
    return listPropertiesService(), 200


@app.route("/properties/<propertyId>", methods=["GET"])
def getProperty(propertyId):
    return getPropertyByIdService(propertyId), 200


@app.route("/properties/users/<userId>", methods=["GET"])
def listPropertiesByUser(userId):
    return listPropertiesByUserService(userId), 200


def __main__():
    app.run(host="0.0.0.0", debug=True, port="5000")
