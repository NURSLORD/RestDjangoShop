from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import Category, Product, SubCategory, Comment, Order
from .permissions import AdminPermission, ManagerPermission, SellerPermission, IsSixteen, CustomerPermission
from .serializer import CategorySerializer, ProductSerializer, SubCategorySerializer, \
    CommentSerializer, OrderSerializer
from rest_framework import filters


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['is_active']

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'update']:
            self.permission_classes = [AdminPermission | ManagerPermission | SellerPermission]
        else:
            self.permission_classes = [IsAuthenticated]
        return super(CategoryModelViewSet, self).get_permissions()

    # def list(self, request, *args, **kwargs):
    #     queryset = Category.objects.all()
    #     serializer = CategorySerializer(queryset, many=True)
    #     return Response(serializer.data, status=200)

    # @action(detail=False, methods=['get'])
    # def category_all(self, request, *args, **kwargs):
    #     queryset = Category.objects.all().filter(id__gt=1)
    #     return Response(CatSerializer(queryset, many=True).data)


class SubCategoryModelViewSet(ModelViewSet):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'category']
    ordering_fields = ['is_active', 'category']

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'update']:
            self.permission_classes = [AdminPermission | ManagerPermission | SellerPermission]
        else:
            self.permission_classes = [IsAuthenticated]
        return super(SubCategoryModelViewSet, self).get_permissions()


# product
class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'category', 'article', 'description']
    ordering_fields = ['is_popular', 'category', 'gender', 'brand']

    def get_permissions(self):
        if self.action in ['create', 'update']:
            self.permission_classes = [AdminPermission | ManagerPermission]
        elif self.action == 'destroy':
            self.permission_classes = [SellerPermission | AdminPermission | ManagerPermission]
        else:
            self.permission_classes = [IsAuthenticated]
        return super(ProductModelViewSet, self).get_permissions()


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'update']:
            self.permission_classes = [AdminPermission | ManagerPermission | SellerPermission | CustomerPermission
                                       & IsSixteen]
        else:
            self.permission_classes = [IsAuthenticated]
        return super(CommentModelViewSet, self).get_permissions()


# class LoginWithToken(generics.CreateAPIView):
#     queryset = User.objects.all()
#     permission_classes = [AllowAny]
#
#     def create(self, request, *args, **kwargs):
#         email = request.data['email']
#         password = request.data['password']
#         user = User.objects.filter(email=email)
#         if len(user) > 0:
#             if check_password(password, user[0].password):
#                 token = Token.objects.filter(user=user[0])
#                 if token:
#                     token.delete()
#                 token = Token(user=user[0])
#                 token.save()
#                 return Response({
#                     'token': token.key,
#                     'user_pk': user[0].pk
#                 })
#             else:
#                 return Response({
#                     'error': "password is incorrect"
#                 })
#
#         return Response({
#             'error': "login is incorrect"
#         })
class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'update']:
            self.permission_classes = [AdminPermission | ManagerPermission | SellerPermission]
        else:
            self.permission_classes = [IsAuthenticated | IsSixteen]
        return super(OrderModelViewSet, self).get_permissions()
