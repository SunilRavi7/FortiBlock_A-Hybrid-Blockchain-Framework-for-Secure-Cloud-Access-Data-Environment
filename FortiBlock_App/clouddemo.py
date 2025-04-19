# Import Module
import ftplib

# Fill Required Information
HOSTNAME = "ftp.drivehq.com"
USERNAME = "AuthPrivacyChain"
PASSWORD = "finalyearproject2023"
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
def process(filename):
    # force UTF-8 encoding
    ftp_server.encoding = "utf-8"
    #filename = "admin.py"
    # Read file in binary mode
    with open(filename, "rb") as file:
        # Command for Uploading the file "STOR filename"
        ftp_server.storbinary(f"STOR {filename}", file)
    ftp_server.quit()
