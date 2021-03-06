from flask import Blueprint
from flask import Response
from flask import json


# create controller
controller = Blueprint("main", __name__)

@controller.route("/")
def loadBalancer():
    return Response(response=json.dumps({"response": "Hello!"}),
                 status=200,
                 mimetype="application/json")
