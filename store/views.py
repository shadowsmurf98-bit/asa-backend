from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Character, Transaction
from .serializers import CharacterSerializer, TransactionSerializer

class CharacterListView(generics.ListAPIView):
    queryset = Character.objects.filter(is_sold=False)
    serializer_class = CharacterSerializer

class CharacterDetailView(generics.RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class WalletView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        characters = Character.objects.filter(owner=request.user)
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data)

class ClaimCharacterView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        character = get_object_or_404(Character, pk=pk)
        if character.is_sold:
            return Response({'error': 'Character already claimed'}, status=400)
        character.owner = request.user
        character.is_sold = True
        character.save()
        Transaction.objects.create(
            buyer=request.user,
            character=character,
            amount=character.price
        )
        return Response({'message': 'Character claimed successfully'})
