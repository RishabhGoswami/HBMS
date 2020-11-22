from django.contrib import admin
from django.urls import path,include
from . import views
from . views import BookCreateView,UserListView,BookDeleteView,ContactCreateView,ContactListView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('categorydetail/<int:pk>',views.categorydetail,name='categorydetail'),
    path('gallery',views.gallery,name='gallery'),
    path('about',views.about,name='about'),
    path('facility',views.facility,name='facility'),
    path('book',BookCreateView.as_view(),name='book'),
    path('contactlist',ContactCreateView.as_view(),name='contactlist'),
    path('seequeries',ContactListView.as_view(),name='seequeries'),
    path('see/<str:username>',UserListView.as_view(),name='see'),
    path('delete/<int:pk>',BookDeleteView.as_view(),name='delete'),
    path('complete/<int:pk>',views.complete,name='complete'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
    path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
]
