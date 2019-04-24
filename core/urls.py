from django.urls import path, include
from django.contrib import admin
import core.views
from .classviews import BidderListView, ProductDelete, UserCreateView, Disc
from .classviews import ProductDetailView, AddProductView, ProductView
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    
    path('', core.views.index, name="index"),

    path('/nitin/',Disc.as_view(), name='bidding'),
    
    path('viewproduct/', login_required(ProductView.as_view()), name="view_product"),
    path('addproduct/', login_required(AddProductView.as_view()), name="add_product"),
    path('productdetails/<int:pk>', login_required(ProductDetailView.as_view()), name="product_detail"),
    path('save_bid/', login_required(core.views.save_bid), name="save_bid"),
    path('register_user/', UserCreateView.as_view(), name="register"),
    path('deleteproduct/<int:pk>', login_required(ProductDelete.as_view()), name="delete_product"),
    path('bidderlist/<int:pk>', login_required(BidderListView.as_view()), name="bidder_list"),
    path('logout/', logout_then_login, name='logout'),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.urls import path, include
from django.contrib import admin
import core.views
from .classviews import BidderListView, ProductDelete, UserCreateView
from .classviews import ProductDetailView, AddProductView, ProductView
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    path('', core.views.index, name="index"),
    path('viewproduct/', login_required(ProductView.as_view()), name="view_product"),
    path('addproduct/', login_required(AddProductView.as_view()), name="add_product"),
    path('productdetails/<int:pk>', login_required(ProductDetailView.as_view()), name="product_detail"),
    path('save_bid/', login_required(core.views.save_bid), name="save_bid"),
    path('register_user/', UserCreateView.as_view(), name="register"),
    path('deleteproduct/<int:pk>', login_required(ProductDelete.as_view()), name="delete_product"),
    path('bidderlist/<int:pk>', login_required(BidderListView.as_view()), name="bidder_list"),
    path('logout/', logout_then_login, name='logout'),
    path('page/', login_required(core.views.save_bid),name='page')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
