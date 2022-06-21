# demo/urls.py

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "website"
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('track/<int:id>', views.track, name='track'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('account/', views.account, name='account'),
    path('orders/', views.orders, name='orders'),
    path('change_dest/<int:package_id>/<int:truck_id>',
         views.change_dest, name='change_dest'),
    path('resend/<int:package_id>', views.resend, name='resend'),
    # path('account/package/', views.package_detail, name='package_detail'),
]

urlpatterns += static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
