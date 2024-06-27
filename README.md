# Fortunesoft Task

Here are the steps to run the code<br>
1. Install Python >= 3.11
2. In the Python Environment, install all the requirements with the command: `pip install -r requirements.txt`
3. In `conf/application.conf` under the section `MYSQL`, mention the credentials of your MYSQL (Host, Port, User, Password) to their respective keys.
4. Mention specific host and port for the services if you want in `conf/application.conf` under the section `SERVICE`
5. Run the `app.py` file
6. In your browser/rest-client, hit the url: `http://<host>:<port>/main/employees`
7. If everything is properly configured, it should give a list of employees information.