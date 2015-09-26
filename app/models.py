
from google.appengine.ext import ndb

class Picture(ndb.Model):
    title = ndb.StringProperty(required=True)
    date = ndb.StringProperty(required=True)
    description = ndb.TextProperty(required=True)
    lat = ndb.StringProperty(required=True)
    lng = ndb.StringProperty(required=True)
    photo = ndb.BlobKeyProperty(required=True)
