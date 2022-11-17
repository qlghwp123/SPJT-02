from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/agreement/", views.agreement, name="agreement"),
    path("signup/<int:is_seller>/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("mypage/", views.mypage, name="mypage"),
    path("cart/", views.cart, name="cart"),
    path("cart/add/<int:product_id>/", views.add_cart, name="add_cart"),
    path("cart/delete/<int:product_id>/", views.delete_cart, name="delete_cart"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("wishlist/add/<int:product_id>", views.add_wishlist, name="add_wishlist"),
    path("review/", views.review, name="review"),
    path("check/", views.check, name="check"),
    path("check_id/", views.check_id, name="check_id"),
    path("login/naver_callback/", views.naver_callback, name="naver_callback"),
    path("id_check/", views.id_check, name="id_check"),
    path("id_check_naver/", views.id_check_naver, name="id_check_naver"),
    ##
    path("product_management/", views.product_management, name="product_management"),
]
