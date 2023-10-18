from django.urls import path
from magazine import views
from magazine import templatetags
from magazine.apps import MagazineConfig

# app_name = MagazineConfig.name

urlpatterns = [
    path('', views.AutocarListView.as_view(), name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('product/<int:pk>', views.AutocarDetailView.as_view(), name='product'),
    path('autocar_create/', views.AutocarCreateView.as_view(), name='autocar_create'),
    path('marka_create/', views.MarkaCreateView.as_view(), name='marka_create'),
    path('autocar_update/', views.AutocarUpdateView.as_view(), name='marka_create'),
]

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('contacts/', views.contacts, name='contacts'),
#     path('product/<int:pk>', views.view_product, name='product'),
#     path('autocar_create/', views.autocar_create, name='autocar_create'),
#     path('marka_create/', views.marka_create, name='marka_create'),
# ]
