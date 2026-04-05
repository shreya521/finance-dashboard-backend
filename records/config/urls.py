from django.contrib import admin
from django.urls import path
from users.views import UserListCreateView, UserDetailView
from records.views import FinancialRecordListCreateView, FinancialRecordDetailView
from dashboard.views import DashboardSummaryView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Finance Dashboard API",
        default_version='v1',
        description="Backend API for Finance Data Processing and Access Control",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Users
    path('api/users/', UserListCreateView.as_view(), name='user-list-create'),
    path('api/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # Records
    path('api/records/', FinancialRecordListCreateView.as_view(), name='record-list-create'),
    path('api/records/<int:pk>/', FinancialRecordDetailView.as_view(), name='record-detail'),

    # Dashboard
    path('api/dashboard/summary/', DashboardSummaryView.as_view(), name='dashboard-summary'),

    # Swagger Docs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]