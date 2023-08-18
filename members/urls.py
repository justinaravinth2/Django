from django.urls import path
from . import views

urlpatterns = [
   path('home/',views.mem,name="home"),
   path('addmem/',views.add,name="add"),
   path('addrec/',views.addrec,name="addrec"),
   path('home/update/<int:id>/',views.update,name="update"),
   path('home/delete/<int:id>/',views.delete,name="delete"),
   path('home/updates/<int:id>/',views.up,name="updates"),
   path('logout/',views.logout,name="logout"),
   path('',views.login_user,name="login"),
   path('register/',views.register,name="register"),
   path('register_user/',views.register_user,name="register_user")
   
]
