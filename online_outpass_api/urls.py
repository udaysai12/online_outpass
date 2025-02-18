from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('outpassform', views.outpass_form, name="outpassform"),
    path('adminlogin', views.admin_login_page, name="adminlogin"),
    path('adminpage', views.admin_page, name="adminpage"),
    path('detailspage/<int:applicant_id>', views.details_page, name="detailspage")
]