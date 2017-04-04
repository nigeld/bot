import os
class Config(objec):
    SECRET_KEY = 'my_secret_token'
    PAGE_ACCESS_TOKEN = 'token_facebook'

class DevelopmentConfig(Config):
    DEBUG = True
