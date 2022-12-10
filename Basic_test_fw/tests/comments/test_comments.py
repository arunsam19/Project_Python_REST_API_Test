
from lib.comments import Comments
import logging

def test_get_all_comments(login_as_admin):
   response = Comments().get_all_comments(login_as_admin)
   logging.info("logthis")
   assert response.ok

