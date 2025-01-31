from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FAQViewSet

router = DefaultRouter()
router.register(r'faqs', FAQViewSet, basename="faq")  # Adding basename for safety

urlpatterns = [
    path('', include(router.urls)),  # Remove 'api/' prefix here
]
