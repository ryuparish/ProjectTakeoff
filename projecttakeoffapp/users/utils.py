import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from projecttakeoffapp import mail
from projecttakeoffapp.helpers import *


def save_picture(form_picture, bucket_name, acl="public-read"):
    try:
        s3.upload_fileobj(form_picture.data, bucket_name, form_picture.data.filename, ExtraArgs={"ACL": acl, "ContentType": form_picture.data.content_type})
    except Exception as e:
        print("Something Happened: ", e)
        print(S3_KEY)
        return e
    return "{}{}".format(S3_LOCATION, form_picture.data.filename)

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='TCC_NE_CS',
                  recipients=[user.email])
    msg.body = f'''Hello CS Club Member,
    
To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)