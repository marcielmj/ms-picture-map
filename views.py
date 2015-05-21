
import pyprime
import models
import time

class Index(pyprime.RequestHandler):
    def get(self):
        self.render('index.html')

class UploadFail(pyprime.RequestHandler):
    def get(self):
        self.render('upload_fail.html')

class NotFound(pyprime.RequestHandler):
    def get(self):
        self.render('404.html');

class AdminPage(pyprime.RequestHandler):
    def get(self):
        pictures = models.Picture.query().order(-models.Picture.date).fetch()
        self.render('admin.html', pictures=pictures)

class Gallery(pyprime.RequestHandler):
    def get(self):
        pictures = models.Picture.query().order(-models.Picture.date).fetch()
        self.render('gallery.html', pictures=pictures)

class PictureDetails(pyprime.RequestHandler):
    def get(self, picture_id):
        picture = models.Picture.get_by_id(int(picture_id))
        if picture is None:
            self.redirect('/404')

        self.render('picture.html', picture=picture)

class NewPictureForm(pyprime.RequestHandler):
    def get(self):
        upload = pyprime.create_upload_url('/upload')
        self.render('newpicture.html', url=upload)

class NewPictureUpload(pyprime.UploadHandler):
    def post(self):
        try:
            photo = self.get_uploads()[0]
            title = self.request.get('title')
            date = self.request.get('date')
            description = self.request.get('description')
            lat = self.request.get('lat')
            lng = self.request.get('lng')
            
            new_picture = models.Picture(title=title, date=date, description=description, lat=lat, lng=lng, photo=photo.key())
            new_picture.put()

            self.redirect('/picture/%s' % str(new_picture.key.id()))
        except:
            self.redirect('/upload_fail')

class PhotoView(pyprime.DownloadHandler):
    def get(self, photo_key):
        if not pyprime.get(photo_key):
            self.error(404)
        else:
            self.send_blob(photo_key)

class DeletePicture(pyprime.RequestHandler):
    def get(self, picture_id):
        picture = models.Picture.get_by_id(int(picture_id))

        if picture is None:
            self.redirect('/404')

        picture.key.delete()
        time.sleep(0.1) #
        self.redirect('/admin')
