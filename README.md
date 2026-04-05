# Finance Dashboard Backend

A backend system built for managing finance records, role-based access control, and dashboard analytics.

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite
- JWT Authentication
- Swagger API Docs

## Features
- User and Role Management
- JWT Authentication
- Financial Records CRUD
- Filtering, Search, Ordering
- Dashboard Summary APIs
- Role-Based Access Control
- Input Validation and Error Handling
- Data Persistence with SQLite

## Roles

### Admin
- Manage users
- Create, update, delete records
- View dashboard summary

### Analyst
- View financial records
- View dashboard summary

### Viewer
- View financial records
- View dashboard summary

## API Endpoints

### Authentication
- `POST /api/token/`
- `POST /api/token/refresh/`

### Users
- `GET /api/users/`
- `POST /api/users/`
- `GET /api/users/<id>/`
- `PUT /api/users/<id>/`
- `DELETE /api/users/<id>/`

### Financial Records
- `GET /api/records/`
- `POST /api/records/`
- `GET /api/records/<id>/`
- `PUT /api/records/<id>/`
- `DELETE /api/records/<id>/`

### Filtering Examples
- `/api/records/?type=expense`
- `/api/records/?category=Food`
- `/api/records/?search=salary`
- `/api/records/?ordering=amount`

### Dashboard
- `GET /api/dashboard/summary/`

## Setup Instructions

```bash
git clone <your-repo-url>
cd finance-dashboard-backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
