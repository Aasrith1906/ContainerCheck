from flask.cli import FlaskGroup
from rest_api import app 

cli = FlaskGroup(app)

if __name__ == '__main__':

    cli()