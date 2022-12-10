from lib.utils import build_request_headers
from config import SESSION, APP_URL

class Comments:
    
    def __init__(self):
        # Define and select resource based on the given version if needed
        self.comment_url = "/comments"

    def get_all_comments(self, access_token):
        request_headers = build_request_headers(access_token)
        response = SESSION.get(f"{APP_URL}{self.comment_url}", headers=request_headers)
        return response