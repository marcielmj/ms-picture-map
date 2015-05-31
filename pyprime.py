
import webapp2
import jinja2
import os

from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import blobstore

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
JINJA2_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR), autoescape=True)

def jinja2_render(template, **kwargs):
    t = JINJA2_ENVIRONMENT.get_template(template)
    return t.render(kwargs)

def create_upload_url(url):
    return blobstore.create_upload_url(url)

def get(blob_key):
    return blobstore.get(blob_key)

class RequestHandler(webapp2.RequestHandler):
    def write(self, *args, **kwargs):
        self.response.write(*args, **kwargs)

    def template_render(self, template, **kwargs):
        return jinja2_render(template, **kwargs)

    def render(self, template, **kwargs):
        self.write(self.template_render(template, **kwargs))

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    pass

class DownloadHandler(blobstore_handlers.BlobstoreDownloadHandler):
    pass
