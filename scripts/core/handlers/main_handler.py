# library imports
from sqlalchemy.orm import aliased
from collections import OrderedDict

# custom imports
from scripts.logging.log_module import logger as log
from scripts.constants.connections import connection
from scripts.core.models.table_models import OfficesModel, EmployeesModel

class Employees:

    def __init__(self) -> None:
        pass
    
    def get_employees(self):
        final_json = {"data": []}
        try:

            log.debug("Querying employee data.")

            Emp_alias = aliased(EmployeesModel)
            employees_query = connection.fetch_all_data_with_join(
                table_list=(
                    EmployeesModel, 
                    OfficesModel, 
                    Emp_alias
                ),
                conditions_list=(
                    EmployeesModel.officeCode == OfficesModel.officeCode, 
                    EmployeesModel.reportsTo == Emp_alias.employeeNumber
                ),
                sort=EmployeesModel.employeeNumber
            )

            for each_employee in employees_query:
                temp_json = OrderedDict()
                temp_json["employeeNumber"] = each_employee[0].employeeNumber
                temp_json["lastName"] = each_employee[0].lastName
                temp_json["firstName"] = each_employee[0].firstName
                temp_json["extension"] = each_employee[0].extension
                temp_json["email"] = each_employee[0].email
                temp_json["officeCode"] = each_employee[0].officeCode
                temp_json["jobTitle"] = each_employee[0].jobTitle
                temp_json["city"] = each_employee[1].city
                temp_json["phone"] = each_employee[1].phone
                temp_json["reportsTo"] = each_employee[2].employeeNumber
                temp_json["reportToLastName"] = each_employee[2].lastName
                temp_json["reportToFirstName"] = each_employee[2].firstName

                final_json["data"].append(temp_json)
                
        except Exception as e:
            log.error("Error while fetching employees data: " + str(e))

        return final_json