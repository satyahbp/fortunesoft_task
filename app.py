# library imports
from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_cors import CORS

# custom imports
from scripts.constants.app_configuration import HOST, PORT
from scripts.core.services.main_service import main_blueprint


app = Flask(__name__)
CORS(app)

app.register_blueprint(main_blueprint)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)