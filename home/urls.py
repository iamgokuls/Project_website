from django.urls import path
from home import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url,handler404

 


urlpatterns = [
    path('', views.homeview, name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.LoginPage.as_view(),name='login'),
    path('logout/',views.logoutuser,name='logoutuser'),
    path('profile/changeinfo/',views.changeinfo,name='changeinfo'),
    path('profile/changepass/',views.changepass,name='changepass'),
    path('profile/',views.profilepage,name='profile'),
    #path('error/',views.error,name='error'),
    path('history/',views.gethistory,name='history'),
    path('sethistory',views.sethistory,name='sethistory'),
    path('getmail',views.getmail,name='getmail'),
    path('feedback/',views.feedback,name='feedback'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="passwordreset.html"),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name='password_reset_complete')
]

