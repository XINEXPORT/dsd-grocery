from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission

from .models import ShoppingList
from .serializers import ShoppingListSerializer


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class ShoppingListViewSet(viewsets.ModelViewSet):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user_id = self.kwargs["user_pk"]
        return ShoppingList.objects.filter(user_id=user_id)
