import configparser
from os import environ

config = configparser.ConfigParser()
config.read("conf/application.conf")

SERVICE_SECTION = "SERVICE"
LOG_SECTION = "LOG"
MYSQL_SECTION = "MYSQL"

# service
HOST = config.get(SERVICE_SECTION, "host")
PORT = int(config.get(SERVICE_SECTION, "port"))
BASE_URL = config.get(SERVICE_SECTION, "base_url")

# logging
LOG_NAME = config.get(LOG_SECTION, "log_name")
LOG_BASE_PATH = config.get(LOG_SECTION, "log_path")
LOG_FILE_NAME = config.get(LOG_SECTION, "file_name")
LOG_LEVEL = config.get(LOG_SECTION, "level")
LOG_MAX_FILE_SIZE = config.get(LOG_SECTION, "max_file_size")
LOG_MAX_FILE_BACKUPS = config.get(LOG_SECTION, "max_backup")
LOG_HANDLERS = config.get(LOG_SECTION, "handlers")

# mysql
MYSQL_HOST = environ.get("MYSQL_HOST", config.get(MYSQL_SECTION, "mysql_host"))
MYSQL_PORT = environ.get("MYSQL_PORT", config.get(MYSQL_SECTION, "mysql_port"))
MYSQL_USER = environ.get("MYSQL_USER", config.get(MYSQL_SECTION, "mysql_user"))
MYSQL_PASSWORD = environ.get("MYSQL_PASSWORD", config.get(MYSQL_SECTION, "mysql_password"))
MYSQL_DB = config.get(MYSQL_SECTION, "mysql_db")
OFFICES_TABLE = config.get(MYSQL_SECTION, "offices_table")
EMPLOYEES_TABLE = config.get(MYSQL_SECTION, "employees_table")