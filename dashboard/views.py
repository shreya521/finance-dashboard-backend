from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from records.models import FinancialRecord
from records.permissions import CanViewDashboard

class DashboardSummaryView(APIView):
    permission_classes = [IsAuthenticated, CanViewDashboard]

    def get(self, request):
        income = FinancialRecord.objects.filter(type='income').aggregate(total=Sum('amount'))['total'] or 0
        expenses = FinancialRecord.objects.filter(type='expense').aggregate(total=Sum('amount'))['total'] or 0
        net_balance = income - expenses

        category_totals = (
            FinancialRecord.objects.values('category')
            .annotate(total=Sum('amount'))
            .order_by('-total')
        )

        recent_activity = FinancialRecord.objects.order_by('-created_at')[:5].values(
            'id', 'amount', 'type', 'category', 'date', 'notes'
        )

        monthly_trends = (
            FinancialRecord.objects.annotate(month=TruncMonth('date'))
            .values('month', 'type')
            .annotate(total=Sum('amount'))
            .order_by('month')
        )

        return Response({
            "total_income": income,
            "total_expenses": expenses,
            "net_balance": net_balance,
            "category_totals": list(category_totals),
            "recent_activity": list(recent_activity),
            "monthly_trends": list(monthly_trends),
        })
