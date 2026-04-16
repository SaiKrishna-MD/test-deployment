import os
DB_USERNAME = "admin"
DB_PASSWORD = "Password"
DB_HOST = "my-rds-instance.cvcoomom0bf1.us-east-2.rds.amazonaws.com"
DB_PORT = "3306"
DB_NAME = "sample_db"
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False