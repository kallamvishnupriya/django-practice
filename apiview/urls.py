from django.urls import path
from .views import studentlist,studentlistdetails

urlpatterns=[
    path('studentlist/',studentlist),
    path('studentdetails/',studentlistdetails),
]


# # urls.py(for viewSets)
# router.register('students', StudentViewSet)
# urlpatterns = router.urls