from django import views
from django.urls import path

from cinimaapp import views

app_name='cinimaapp'




urlpatterns = [
    # path('',views.home,name='home'),
    path('',views.HomeView.as_view(),name='home'),

    # path('detail/<int:n>/',views.detail,name="detail"),
    path('detail/<int:pk>', views.Detail.as_view(),name='detail'),

    # path('update/<int:n>/',views.update,name='update'),
    path('update/<int:pk>',views.Update.as_view(),name='update'),

    # path('delete/<int:n>/',views.delete,name="delete"),
    path('delete/<int:pk>',views.Delete.as_view(),name='delete'),

    # path('addmovie/',views.addmovie,name='addmovie'),

    # path('add/',views.add,name='add'),
    path('add/',views.AddMovie.as_view(),name='add'),

    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),

]
