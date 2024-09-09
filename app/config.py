import os

class Config:
    DB_SERVER = os.getenv('DB_SERVER', 'TOBI-PC\\SQLEXPRESS')
    DB_NAME = os.getenv('DB_NAME', 'CRIARPG')
    DEBUG = os.getenv('DEBUG', True)