import pandas as pd
import numpy as np
from .models import Transaction
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def get_user_transactions(user):
    """Retrieve all transactions for a user and return a pandas DataFrame."""
    transactions = Transaction.objects.filter(user=user).values('amount', 'date', 'category')
    df = pd.DataFrame(list(transactions))
    return df

def prepare_data(df):
    """Preprocess the data for machine learning."""
    # Convert date to datetime and extract year, month, and day
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day

    # For simplicity, we'll predict monthly spending; group by year and month
    monthly_data = df.groupby(['year', 'month']).agg({'amount': 'sum'}).reset_index()
    return monthly_data


def train_model(df):
    """Train a model to predict future expenses based on past transactions."""
    df = prepare_data(df)

    # Create features (year, month) and target (amount)
    X = df[['year', 'month']]
    y = df['amount']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a simple linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Calculate accuracy or other metrics on test data
    score = model.score(X_test, y_test)

    return model, score

def predict_future_expenses(user, months_ahead=3):
    """Predict the user's expenses for the next few months."""
    df = get_user_transactions(user)
    if df.empty:
        return None

    # Train the model
    model, score = train_model(df)

    # Predict future expenses for the next few months
    last_year = df['year'].max()
    last_month = df[df['year'] == last_year]['month'].max()

    predictions = []
    for i in range(1, months_ahead + 1):
        next_year = last_year
        next_month = last_month + i
        if next_month > 12:
            next_month -= 12
            next_year += 1

        # Predict for the next year/month
        future_expense = model.predict(np.array([[next_year, next_month]]))
        predictions.append({
            'year': next_year,
            'month': next_month,
            'predicted_amount': future_expense[0]
        })

    return predictions
