from fastapi_mail import FastMail, ConnectionConfig
from dotenv import load_dotenv
load_dotenv('.env')
import os


conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=int(os.getenv("MAIL_PORT")),
    MAIL_SERVER=os.getenv("MAIL_SERVER"),
    MAIL_STARTTLS=os.getenv("MAIL_STARTTLS")== "True",  
    MAIL_SSL_TLS=os.getenv("MAIL_SSL_TLS")== "True", 
    USE_CREDENTIALS=os.getenv("USE_CREDENTIALS") == "True",
    VALIDATE_CERTS=os.getenv("VALIDATE_CERTS") == "True"
)

fm = FastMail(conf)
