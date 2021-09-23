from .base import *

# import dj_database_url

env = os.environ.copy()
# SECRET_KEY = env["SECRET_KEY"]

# DATABASES["default"] = dj_database_url.config()


DEBUG = True

try:
    from .local import *
except ImportError:
    pass
