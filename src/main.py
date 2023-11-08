from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.log import LogFormatter
from config import FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, FTP_PORT, FTP_PERM
import logging

def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm=FTP_PERM)

    handler = FTPHandler
    handler.authorizer = authorizer

    # Set up logging
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setFormatter(LogFormatter())
    logger.addHandler(ch)

    try:
        server = FTPServer(("0.0.0.0", FTP_PORT), handler)
        server.serve_forever()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()