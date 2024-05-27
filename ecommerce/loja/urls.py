from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", homepage, name="homepage"),
    path("loja/", lojas, name="lojas"),
    path("minhaconta/", minha_conta, name="minha_conta"),
    path("login/", login, name="login"),
    path("carrinho/", carrinho, name="carrinho"),
    path("checkout/", checkout, name="checkout"),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
