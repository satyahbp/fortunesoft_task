# library imports
import json
from flask import Blueprint, Response

# custom imports
from scripts.constants.app_configuration import BASE_URL
from scripts.constants.app_constants import Blueprints, Endpoints
from scripts.core.handlers.main_handler import Employees
from scripts.logging.log_module import logger as log

main_blueprint = Blueprint(Blueprints.main_blueprint, __name__)
employees_obj = Employees()

@main_blueprint.route(
    BASE_URL + Endpoints.employees_data, 
    methods = ["GET"]
)
def employees_service_func():
    resp = {
        "status": "failed",
        "message": "failed to fetch data"
    }
    try:
        resp = employees_obj.get_employees()
    except Exception as e:
        log.error("Error while fetching employee data: " + str(e))

    response = Response(
        json.dumps(resp),
        status=200,
        mimetype="application/json"
    )

    return response

