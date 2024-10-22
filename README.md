
# Personal Finance Manager

Django-based web application designed to help users track and manage their personal expenses. The application allows users to input their expenses, categorize them, and visualize spending trends over time with interactive charts.


## Features

- Expense Tracking: Add, edit, and delete expenses with a simple interface.
- Expense Categories: Assign expenses to different categories for better organization.
- Interactive Visualizations: Visualize monthly expenses using dynamic charts powered by Chart.js.
- Authentication: (Upcoming) Secure user authentication to ensure privacy and data security.
- Expense Reports: (Upcoming) Generate reports of your spending habits, filtered by month or category.
- Budget Alerts: (Upcoming) Set monthly budgets and receive alerts when you're close to overspending.


## Technologies Used

**Backend:** Django (Python) for handling data and business logic.

**Frontend:** HTML, CSS, and JavaScript (Chart.js for data visualization).

**Database:** SQLite (for development), with plans to integrate PostgreSQL for production.

**APIs:** Django Rest Framework (future enhancement to expose data as an API).


## How to Run

1. Clone the project

```bash
  git clone https://github.com/ashiquemushtaq/finance_manager.git
```

2. Go to the project directory

```bash
  cd finance_manager
```

3. Install dependencies

```bash
  pip install -r requirements.txt
```

4. Apply migrations

```bash
  python manage.py migrate
```
5. python manage.py createsuperuser

```bash
  python manage.py createsuperuser
```
6. Start the Django development server

```bash
  python manage.py runserver
```
7. Open your browser and visit http://127.0.0.1:8000/transactions/visualize/ to view the expense visualization.

## Work in Progress
This project is still under active development, with additional features planned, including:
- User authentication and authorization for private expense tracking.
- Advanced filtering options for better insights into spending patterns.
- Budgeting and savings goals.
- More detailed reports and customizable visualizations.
## Contribution Guidelines

Contributions are always welcome!

- Fork the repository and create a feature branch.
- Submit pull requests for review.
- Ensure that any code changes are properly documented.

