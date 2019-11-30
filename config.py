import os

from dotenv import load_dotenv

app_dir = os.path.dirname(__file__)
env_path = os.path.join(app_dir, '.env')
load_dotenv(dotenv_path=env_path)


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")


class DevelopmentConfig(Config):
    DATABASE_URI = os.environ.get("DEV_DATABASE_URI")


class ProductionConfig(Config):
    DATABASE_URI = os.environ.get("PROD_DATABASE_URI")


if os.environ.get("FLASK_ENV") == 'production':
    configObject = ProductionConfig
else:
    configObject = DevelopmentConfig
