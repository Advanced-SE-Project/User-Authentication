from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


from auth import auth_routes  

app.register_blueprint(auth_routes)

if __name__ == '__main__':
    app.run(debug=True)
