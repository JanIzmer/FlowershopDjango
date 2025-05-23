from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include("title.urls")),
    path('admin/', admin.site.urls),
    path('customer/', include('Customer.urls')),
    path('cart/', include('Cart.urls')),
    path('order/', include('Order.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
