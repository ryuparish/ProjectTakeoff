import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_USERNAME")
    print(os.environ.get("EMAIL_USERNAME"))
    print(os.environ.get("EMAIL_APP_PASS"))
    MAIL_PASSWORD = os.environ.get("EMAIL_APP_PASS")


S3_BUCKET                 = os.environ.get("S3_BUCKET")
S3_KEY                    = os.environ.get("S3_KEY")
S3_SECRET                 = os.environ.get("S3_SECRET")
S3_LOCATION               = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)
DEBUG                     = True
PORT                      = 5000