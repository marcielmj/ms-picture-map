
import webapp2
import views

config = {'webapp2_extras.jinja2': {'template_path': 'app/templates'}}

app = webapp2.WSGIApplication(
    routes=[
        ('/', views.Index),
        ('/gallery', views.Gallery),
        ('/new', views.NewPictureForm),
        ('/upload', views.NewPictureUpload),
        ('/picture/([0-9]+)', views.PictureDetails),
        ('/photo/([^/]+)?', views.PhotoView),
        ('/upload_fail', views.UploadFail),
        ('/404', views.NotFound)], 
    config=config,
    debug=True)

admin = webapp2.WSGIApplication(
    routes=[
        ('/admin', views.AdminPage),
        ('/admin/delete/([0-9]+)', views.DeletePicture)],
    config=config,
    debug=False)
