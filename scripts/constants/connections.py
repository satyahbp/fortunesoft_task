# library imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# custom imports
from scripts.constants.app_configuration import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
from scripts.utilities.mysql_utilities import MySQLUtility

connection = MySQLUtility(
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    db=MYSQL_DB
)