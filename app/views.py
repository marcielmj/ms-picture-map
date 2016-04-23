
import handler
import models
import time

class Index(handler.Request):
    def get(self):
        self.render('index.html')


class UploadFail(handler.Request):
    def get(self):
        self.render('upload_fail.html')


class NotFound(handler.Request):
    def get(self):
        self.render('404.html');


class AdminPage(handler.Request):
    def get(self):
        pictures = models.Picture.query().order(-models.Picture.date).fetch()
        self.render('admin.html', pictures=pictures)


class Gallery(handler.Request):
    def get(self):
        pictures = models.Picture.query().order(-models.Picture.date).fetch()
        self.render('gallery.html', pictures=pictures)


class PictureDetails(handler.Request):
    def get(self, picture_id):
        picture = models.Picture.get_by_id(int(picture_id))
        if picture is None:
            self.redirect('/404')

        self.render('picture.html', picture=picture)


class NewPictureForm(handler.Request):
    def get(self):
        upload = handler.create_upload_url('/upload')
        self.render('newpicture.html', url=upload)


class NewPictureUpload(handler.Upload):
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
        except Exception:
            self.redirect('/upload_fail')


class PhotoView(handler.Download):
    def get(self, photo_key):
        if not handler.get(photo_key):
            self.error(404)
        else:
            self.send_blob(photo_key)


class DeletePicture(handler.Request):
    def get(self, picture_id):
        picture = models.Picture.get_by_id(int(picture_id))

        if picture is None:
            self.redirect('/404')

        picture.key.delete()
        time.sleep(0.1) #
        self.redirect('/admin')
