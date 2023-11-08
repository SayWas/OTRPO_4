import os

from dotenv import load_dotenv

load_dotenv()

FTP_USER=os.getenv("FTP_USER")
FTP_PASSWORD=os.getenv("FTP_PASSWORD")
FTP_DIRECTORY=os.getenv("FTP_DIRECTORY")
FTP_PORT=int(os.getenv("FTP_PORT"))
FTP_PERM=os.getenv("FTP_PERM")
