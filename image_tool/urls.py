"""
URL configuration for image_tool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from imageapp import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('Login',views.log,name="Login"),
    path('Signup',views.reg,name="Signup"),
    path('Forgotpass',views.forgot,name="for"),
    path('ContactUs',views.cont,name="contactus"),
    path('',views.indexes,name="Index"),
    path('Foot',views.foot),
    path('Sidebar',views.sidebar),
    path('Changepassword',views.chngepass,name="changepassword"),
    path('Base',views.bas),
    path('Viewfaq',views.faqs,name="faq"),
    path('DetailBlog/<int:id>',views.detblog,name="detailblog"),
    path('Article',views.arti,name="article"),
    path('main',views.img,name="main"),
    path('Aboutus',views.about,name="about"),
    path('Tools',views.too,name="tools"),
    path('Tool',views.tool,name="tool"),
    path('Editors',views.editr, name="editors"),
    path('Logout',views.logout,name="Logout"),
    path('Review',views.review,name="review"),
    path('Helpsupport',views.Helps,name="helpsupport"),
    path('EditProfile',views.Editp,name="editprofile"),
    path('UserProfile',views.Userprof,name="myprofile"),
    path('Imgtotext',views.imgtxt,name="imgtxt"),
    path('Cartoon',views.cartoon,name="cartoon"),
    path('Flip',views.flip,name="flip"),
    path('Fliph',views.Fliph,name="fliph"),
    path('Flipv',views.Flipv,name="flipv"),
    path('Face',views.facereco,name="face"),
    path('Remove',views.rem,name="rem"),
    path('Textimg',views.txt ,name="txt"),
    path('Blur',views.bluri,name="blur"),
    path('GBlur',views.gblur,name="gblur"),
    path('MBlur',views.mblur,name="mblur"),
    path('BBlur',views.bblur,name="bblur"),
    path('Contrast',views.contrast,name="contrast"),
    path('Contour',views.contour,name="contour"),
    path('Video',views.video,name="video"),
    path('Add',views.addtext,name="add"),
    path('Png',views.png,name="png"),
    path('Jpg',views.jpg,name="jpg"),
    path('Greyscale',views.greys,name="grey"),
    path('Resize',views.resi,name="resize"),
    path('Barcode',views.bar,name="barcode"),
    path('Qrcode',views.qrcode,name="qrcode"),
    path('Result',views.res,name="result"),
    path('TextResult',views.txtres,name="textresult"),
    path('Rotate',views.rotating,name="rotate"),
    path('Enhance',views.enhance,name="enhance"),
    path('GIFS',views.creategif,name="gif"),
    path('Shifting',views.shift, name="shift"),
    path('Scaling',views.scale, name="scale"),
    path('Detection',views.edge, name="edge"),
    path('News',views.latest, name="news"),
]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 