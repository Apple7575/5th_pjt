

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')), # accounts 앱 연결
    path('books/', include('books.urls')),
]

