from django.contrib import admin
from django.urls import path, include
from search_indexes.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('search/', include('search_indexes.urls'))
]
