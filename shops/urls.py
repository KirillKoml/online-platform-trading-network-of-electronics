from django.urls import path

from shops.apps import ShopsConfig
from shops.views import ContactsListAPIView, ContactsCreateAPIView, ContactsUpdateAPIView, ContactsDestroyAPIView, \
    ContactsRetrieveAPIView, ProductListAPIView, ProductCreateAPIView, ProductUpdateAPIView, ProductDestroyAPIView, \
    ProductRetrieveAPIView, FactoryListAPIView, FactoryCreateAPIView, FactoryUpdateAPIView, FactoryDestroyAPIView, \
    FactoryRetrieveAPIView, RetailNetworkListAPIView, RetailNetworkCreateAPIView, RetailNetworkUpdateAPIView, \
    RetailNetworkDestroyAPIView, RetailNetworkRetrieveAPIView, IndividualEntrepreneurListAPIView, \
    IndividualEntrepreneurCreateAPIView, IndividualEntrepreneurUpdateAPIView, IndividualEntrepreneurDestroyAPIView, \
    IndividualEntrepreneurRetrieveAPIView

app_name = ShopsConfig.name

urlpatterns = [
    # Урлы для модели контактов
    path('contacts_list/', ContactsListAPIView.as_view(), name='contacts-list'),
    path('contacts_create/', ContactsCreateAPIView.as_view(), name='contacts-create'),
    path('<int:pk>/contacts_update/', ContactsUpdateAPIView.as_view(), name='contacts-update'),
    path('<int:pk>/contacts_destroy/', ContactsDestroyAPIView.as_view(), name='contacts-destroy'),
    path('<int:pk>/contacts_retrieve/', ContactsRetrieveAPIView.as_view(), name='contacts-list'),

    # Урлы для модели продуктов
    path('product_list/', ProductListAPIView.as_view(), name='product-list'),
    path('product_create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('<int:pk>/product_update/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('<int:pk>/product_destroy/', ProductDestroyAPIView.as_view(), name='product-destroy'),
    path('<int:pk>/product_retrieve/', ProductRetrieveAPIView.as_view(), name='product-list'),

    # Урлы для модели заводов
    path('factory_list/', FactoryListAPIView.as_view(), name='factory-list'),
    path('factory_create/', FactoryCreateAPIView.as_view(), name='factory-create'),
    path('<int:pk>/factory_update/', FactoryUpdateAPIView.as_view(), name='factory-update'),
    path('<int:pk>/factory_destroy/', FactoryDestroyAPIView.as_view(), name='factory-destroy'),
    path('<int:pk>/factory_retrieve/', FactoryRetrieveAPIView.as_view(), name='factory-list'),

    # Урлы для модели розничных сетей
    path('retail_network_list/', RetailNetworkListAPIView.as_view(), name='retail_network-list'),
    path('retail_network_create/', RetailNetworkCreateAPIView.as_view(), name='retail_network-create'),
    path('<int:pk>/retail_network_update/', RetailNetworkUpdateAPIView.as_view(), name='retail_network-update'),
    path('<int:pk>/retail_network_destroy/', RetailNetworkDestroyAPIView.as_view(), name='retail_network-destroy'),
    path('<int:pk>/retail_network_retrieve/', RetailNetworkRetrieveAPIView.as_view(), name='retail_network-list'),

    # Урлы для модели индивидуальных предпринимателй
    path('individual_entrepreneur_list/', IndividualEntrepreneurListAPIView.as_view(), name='individual_entrepreneur-list'),
    path('individual_entrepreneur_create/', IndividualEntrepreneurCreateAPIView.as_view(), name='individual_entrepreneur-create'),
    path('<int:pk>/individual_entrepreneur_update/', IndividualEntrepreneurUpdateAPIView.as_view(), name='individual_entrepreneur-update'),
    path('<int:pk>/individual_entrepreneur_destroy/', IndividualEntrepreneurDestroyAPIView.as_view(), name='individual_entrepreneur-destroy'),
    path('<int:pk>/individual_entrepreneur_retrieve/', IndividualEntrepreneurRetrieveAPIView.as_view(), name='individual_entrepreneur-list'),
]