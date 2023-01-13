import os

SECRET_KEY = "aisjdiasjxiasj2"

SQLALCHEMY_DATABASE_URI = "{SGBD}://{usuario}:{senha}@{servidor}/{database}".format(
    SGBD="postgresql",
    usuario="postgres",
    senha="JoseGabr1elLambda",
    servidor="localhost",
    database="galery",
)

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
