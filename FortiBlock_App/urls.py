from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
			path("Login.html", views.Login, name="Login"),
			path("LoginAction", views.LoginAction, name="LoginAction"),
			path("Signup.html", views.Signup, name="Signup"),
			path("SignupAction", views.SignupAction, name="SignupAction"),	    
			path("UploadImage.html", views.UploadImage, name="UploadImage"),
			path("UploadImageAction", views.UploadImageAction, name="UploadImageAction"),	
			path("RevokeUserAction", views.RevokeUserAction, name="RevokeUserAction"),
			path("RevokeUser.html", views.RevokeUser, name="RevokeUser"),
			path("AccessShareData", views.AccessShareData, name="AccessShareData"),
			path("Download", views.Download, name="Download"),
			path("IndirectAccess", views.IndirectAccess, name="IndirectAccess"),
			path("IndirectAccessAction", views.IndirectAccessAction, name="IndirectAccessAction"),
			path("Graph", views.Graph, name="Graph"),
]