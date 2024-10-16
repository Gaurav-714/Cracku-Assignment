from django.urls import path
from  .views import homeView, adminLoginView, addItemVIew, logoutView

urlpatterns = [
    path('', homeView, name='home'),
    path('add-item', addItemVIew, name='add_item'),
    path('admin-login', adminLoginView, name='admin_login'),
    path('admin-logout', logoutView, name='admin_logout'),
]
