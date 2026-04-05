from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import FinancialRecord
from .serializers import FinancialRecordSerializer
from .permissions import IsAdminOrReadOnly

class FinancialRecordListCreateView(generics.ListCreateAPIView):
    queryset = FinancialRecord.objects.all().order_by('-date')
    serializer_class = FinancialRecordSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    filterset_fields = ['type', 'category', 'date']
    search_fields = ['category', 'notes']
    ordering_fields = ['date', 'amount']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class FinancialRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FinancialRecord.objects.all()
    serializer_class = FinancialRecordSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
