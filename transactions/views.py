import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .forms import TransactionForm
from .ml_utils import predict_future_expenses
from django.http import JsonResponse
from .models import Expense
import json

def homepage(request):
    return render(request, 'transactions/homepage.html')

@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'transactions/dashboard.html', {'transactions': transactions})

@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
    return render(request, 'transactions/add_transaction.html', {'form': form})

@login_required
def delete_transaction(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id, user=request.user)
    transaction.delete()
    return redirect('dashboard')

@login_required
def predict_expenses(request):
    predictions = predict_future_expenses(request.user)
    return render(request, 'transactions/predict_expenses.html', {'predictions': predictions})

@login_required
def expense_data(request):
    transactions = Transaction.objects.filter(user=request.user).values('amount', 'date', 'category')
    df = pd.DataFrame(list(transactions))

    if not df.empty:
        df['date'] = pd.to_datetime(df['date'])
        df['month'] = df['date'].dt.to_period('M')

        # Aggregate monthly data
        monthly_data = df.groupby('month').agg({'amount': 'sum'}).reset_index()

        # Convert to JSON-friendly format
        labels = monthly_data['month'].astype(str).tolist()
        amounts = monthly_data['amount'].tolist()

        data = {
            'labels': labels,
            'amounts': amounts,
        }
    else:
        data = {
            'labels': [],
            'amounts': [],
        }

    return JsonResponse(data)

def visualize_expense(request):
    expenses = Expense.objects.all()
    expense_data = {}

    for expense in expenses:
        expense_data[expense.month] = float(expense.amount)

    context = {
        'expense_data': json.dumps(expense_data),  # Serialize data here
    }

    return render(request, 'transactions/visualize_expense.html', context)