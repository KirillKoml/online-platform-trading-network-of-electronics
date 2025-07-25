from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView

from shops.models import Contacts, Product, Factory, RetailNetwork, IndividualEntrepreneur
from shops.serializers import ContactsSerializer, ProductSerializer, FactorySerializer, RetailNetworkSerializer, \
    IndividualEntrepreneurSerializer, RetailNetworkUpdateSerializer, IndividualEntrepreneurUpdateSerializer


from shops.services import FactoryFilter, RetailNetworkFilter, IndividualEntrepreneurFilter


class ContactsListAPIView(ListAPIView):
    """Класс для вывода всех моделей контактов."""
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ContactsCreateAPIView(CreateAPIView):
    """Класс для создания моделей контактов."""
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ContactsUpdateAPIView(UpdateAPIView):
    """Класс для редактирования моделей контактов."""
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ContactsDestroyAPIView(DestroyAPIView):
    """Класс для удаления моделей контактов."""
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ContactsRetrieveAPIView(RetrieveAPIView):
    """Класс для детального просмотра модели контактов."""
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class ProductListAPIView(ListAPIView):
    """Класс для вывода всех моделей продуктов."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateAPIView(CreateAPIView):
    """Класс для создания моделей продуктов."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(UpdateAPIView):
    """Класс для редактирования моделей продуктов."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDestroyAPIView(DestroyAPIView):
    """Класс для удаления моделей продуктов."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveAPIView(RetrieveAPIView):
    """Класс для детального просмотра модели продуктов."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class FactoryListAPIView(ListAPIView):
    """Класс для вывода всех моделей заводов с возможностью фильтрации по стране."""
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    filterset_class = FactoryFilter


class FactoryCreateAPIView(CreateAPIView):
    """Класс для создания моделей заводов."""
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryUpdateAPIView(UpdateAPIView):
    """Класс для редактирования моделей заводов."""
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryDestroyAPIView(DestroyAPIView):
    """Класс для удаления моделей заводов."""
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryRetrieveAPIView(RetrieveAPIView):
    """Класс для детального просмотра модели заводов."""
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class RetailNetworkListAPIView(ListAPIView):
    """Класс для вывода всех моделей розничных сетей с возможностью фильтрации по стране."""
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    filterset_class = RetailNetworkFilter


class RetailNetworkCreateAPIView(CreateAPIView):
    """Класс для создания моделей розничных сетей."""
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer


class RetailNetworkUpdateAPIView(UpdateAPIView):
    """Класс для редактирования моделей розничных сетей(поле задолженность перед поставщиком недоступно для
    изменения)."""
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkUpdateSerializer


class RetailNetworkDestroyAPIView(DestroyAPIView):
    """Класс для удаления моделей розничных сетей."""
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer


class RetailNetworkRetrieveAPIView(RetrieveAPIView):
    """Класс для детального просмотра модели розничных сетей."""
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer


class IndividualEntrepreneurListAPIView(ListAPIView):
    """Класс для вывода всех моделей индивидуальных предпринимателей с возможностью фильтрации по стране."""
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer
    filterset_class = IndividualEntrepreneurFilter


class IndividualEntrepreneurCreateAPIView(CreateAPIView):
    """Класс для создания моделей индивидуальных предпринимателей."""
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer


class IndividualEntrepreneurUpdateAPIView(UpdateAPIView):
    """Класс для редактирования моделей индивидуальных предпринимателей."""
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurUpdateSerializer


class IndividualEntrepreneurDestroyAPIView(DestroyAPIView):
    """Класс для удаления моделей индивидуальных предпринимателей."""
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer


class IndividualEntrepreneurRetrieveAPIView(RetrieveAPIView):
    """Класс для детального просмотра модели индивидуальных предпринимателей."""
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer
