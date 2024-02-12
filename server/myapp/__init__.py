from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_cors import CORS
import os
# app = Flask(__name__)
app = Flask(
    __name__,
    static_url_path='',
    static_folder = '../../client/dist',
    template_folder='../../client/dist'
)

# CORS(app)
# app = Flask(__name__, template_folder='templates')


# os.environ.get('DATABASE_URI')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tour.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)


