
import webapp2

from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import blobstore
from webapp2_extras import jinja2

def create_upload_url(url):
    return blobstore.create_upload_url(url)

def get(blob_key):
    return blobstore.get(blob_key)


class Request(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def write(self, *args, **kwargs):
        self.response.write(*args, **kwargs)

    def render(self, template, **kwargs):
        self.write(self.jinja2.render_template(template, **kwargs))


class Upload(blobstore_handlers.BlobstoreUploadHandler):
    pass


class Download(blobstore_handlers.BlobstoreDownloadHandler):
    pass
