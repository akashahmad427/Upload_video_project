from videoapp import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.first,name='first'),
    path('signup/',views.home2,name='signup'),
    path('login/',views.user_login,name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.user_logout,name='logout'),
    path('delete/<int:stu>/',views.delete,name='delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)