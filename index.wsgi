import os
import sys
root = os.path.dirname(__file__)
sys.path.insert(0,os.path.join(root,'site-packages'))

import sae

python .manage.py deploy

from manage import app
application = sae.create_wsgi_app(app)