from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.start_up,name="start_up"),
    path('register/',views.register,name="register"),
    path('registeraction/',views.registeraction,name="registeraction"),
    path('sign_in/',views.sign_in,name="sign_in"),
    path('sign_inaction/',views.sign_inaction,name="sign_inaction"),
    path('shows_guest/',views.shows_guest,name="shows_guest"),
    path('show_details_guest<int:id>/',views.show_details_guest,name="show_details_guest"),
    path('news/',views.news,name="news"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)