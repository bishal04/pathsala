
from django.urls import path

from .views import (get_all_student, get_student)

urlpatterns = [
    path("", get_all_student), 
    path("<int:webapps_std_id", get_student),

]