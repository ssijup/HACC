"""khcaa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from phase1 import views
from django.conf.urls.static import static
from . import settings
from phase1.views import RequestMembershipView, MembersLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('request_membership/', RequestMembershipView.as_view(), name='request_membership' ),
    path('members_login/', MembersLoginView.as_view(), name='members_login' ),
    path('', views.members, name='members' ),
    path('membership_payment/', views.membership_payment, name='membership_payment' ),
    path('advocates_dashboard/', views.advocates_dashboard, name='advocates_dashboard' ),
    path('advocates_dashboard_more/', views.advocates_dashboard_more, name='advocates_dashboard_more' ),
    path('website_payment/', views.website_payment, name='website_payment' ),
    path('website_active/', views.website_active, name='website_active' ),
    path('website/', views.website, name='website' ),
    path('error404/', views.error404, name='error404' ),
    path('pending/', views.pending, name='pending' ),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard' ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
