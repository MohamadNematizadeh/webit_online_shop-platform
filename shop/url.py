from django.urls import path
from .views import index, signup_view, signin_view, signout_view, profile_view ,products,product,add_to_card ,card # اصلاح ایمپورت‌ها

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # سایر مسیرها
    path('', index, name="index"),
    path('products/', products, name="products"),
    path('product/<int:product_id>/', product, name="product"),
    path('card/', card, name="card"),
    path('card/add/<int:product_id>/', add_to_card, name="add_to_card"),
    path('signup/', signup_view, name='signup'),
    path('signin/', signin_view, name='signin'),
    path('signout/', signout_view, name='signout'),
    path('profile/', profile_view, name='profile'),
]
if settings.DEBUG:
   urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)