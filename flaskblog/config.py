import os


class Config:
    SECRET_KEY = "xxxx"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "xxxx"
    MAIL_PASSWORD = "xxxx"
