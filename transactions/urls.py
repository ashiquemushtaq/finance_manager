from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('delete/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
    path('predict/', views.predict_expenses, name='predict_expenses'),
    path('expense-data/', views.expense_data, name='expense_data'),
     path('visualize/', views.visualize_expense, name='visualize_expense'),  # Visualization
    
]
