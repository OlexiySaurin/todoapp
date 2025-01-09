from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path("tasks/", views.TaskListCreateAPIView.as_view(), name="task-list-api"),
    path("task/<int:pk>/", views.TaskRetrieveUpdateDestroyAPIView.as_view(), name="task-detail-api"),
    # JWT token urls
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]