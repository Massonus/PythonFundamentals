import dropbox
import dropbox.files
import os

#!/usr/bin/env python3
from dropbox import DropboxOAuth2FlowNoRedirect

'''
This example walks through a basic oauth flow using the existing long-lived token type
Populate your app key and app secret in order to run this locally
'''
APP_KEY = "87b5x0oevsak3x9"
APP_SECRET = "c0j50xevkstje4f"

auth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)

authorize_url = auth_flow.start()
print("1. Go to: " + authorize_url)
print("2. Click \"Allow\" (you might have to log in first).")
print("3. Copy the authorization code.")
auth_code = input("Enter the authorization code here: ").strip()

try:
    oauth_result = auth_flow.finish(auth_code)
except Exception as e:
    print('Error: %s' % (e,))
    exit(1)

with dropbox.Dropbox(oauth2_access_token=oauth_result.access_token) as dbx:
    dbx.users_get_current_account()
    print("Successfully set up client!")


# def upload_file():
#     for file in os.listdir("local_files"):
#         with open(os.path.join("local_files", file), "rb") as f:
#             data = f.read()
#             dbx.files_upload(data, f"/{file}")


def upload_file():
    with open("local_files/test.txt", "rb") as f:
        data = f.read()
        dbx.files_upload(data, "/test.txt")


upload_file()
