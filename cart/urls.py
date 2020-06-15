from django.conf import settings
from django.urls import reverse
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('addtocart/<int:id>/', views.addtocart, name='addtocart'),
    path('deleteitem/<int:id>/', views.delete_cart_item, name='deleteitem'),
    path('schedule/<int:id>/', views.cart_item_form, name='schedule'),
    path('checkout/', views.checkout_form, name='checkout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
