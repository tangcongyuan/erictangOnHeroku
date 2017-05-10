from authentication.models import Account
from authentication.permissions import IsOwnerOrReadOnly
from authentication.serializers import AccountSerializer

from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
    'accounts': reverse('account-list', request=request, format=format),
})

class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        # if serializer.is_valid():
        try:
            # Account.objects.create_user(**serializer.validated_data)
            # return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
            Account.objects.create_user(**serializer.initial_data) # Use initial_data to let the database to catch the exception and return corresponding error msg.
            return Response(serializer.initial_data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({
                'status': 'Bad request',
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({
                'status': 'Bad request',
                'message': 'Account could not be created with received data.'
            }, status=status.HTTP_400_BAD_REQUEST)

class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
