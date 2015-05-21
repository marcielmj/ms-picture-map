
import webapp2
import views

app = webapp2.WSGIApplication([('/', views.Index),
    ('/gallery', views.Gallery),
    ('/new', views.NewPictureForm),
    ('/upload', views.NewPictureUpload),
    ('/picture/([0-9]+)', views.PictureDetails),
    ('/photo/([^/]+)?', views.PhotoView),
    ('/upload_fail', views.UploadFail),
    ('/404', views.NotFound)
    ], debug=False)

admin = webapp2.WSGIApplication([('/admin', views.AdminPage),
    ('/admin/delete/([0-9]+)', views.DeletePicture)
    ], debug=False)