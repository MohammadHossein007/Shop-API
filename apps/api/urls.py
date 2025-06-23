from django.urls import path, include

urlpatterns = [
    path('store/', include('apps.store.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]