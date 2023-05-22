# config/settings.py

from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    #Database Hostinger 
    db_user: str = os.getenv("DB_USER")
    db_password: str = os.getenv("DB_PASSWORD")
    db_host: str = os.getenv("DB_HOST")
    db_name: str = os.getenv("DB_NAME")

    #Database Local Van 
    db_user_local: str = os.getenv("DB_USER_LOCAL")
    db_password_local: str = os.getenv("DB_PASSWORD_LOCAL")
    db_host_local: str = os.getenv("DB_HOST_LOCAL")
    db_name_local: str = os.getenv("DB_NAME_LOCAL")

    #AWS Details
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION = os.getenv("AWS_REGION")
    AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
    AWS_IMAGE_PATH = os.getenv("AWS_IMAGE_PATH")
    AWS_PALLETES_PATH = os.getenv("AWS_PALLETES_PATH")
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        
    #Secret Key Details
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'

settings = Settings()