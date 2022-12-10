
from lib.comments import Comments
import logging
from config import LOG

def test_get_all_comments(login_as_admin):
   LOG.info("test_get_all_comments")
   response = Comments().get_all_comments(login_as_admin)
   LOG.debug(response.json())
   assert response.ok

