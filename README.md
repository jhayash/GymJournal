# 🏋️ GymJournal

GymJournal is a Django-based web application that allows users to log and track workouts, exercises, and progress over time. It features a flexible workout planner, detailed reports, and a clean administrative interface.

## 🚀 Features

- Create, edit, and delete workouts
- Add custom exercises with sets, reps, and weight
- Filter workouts by date or exercise type
- Generate dynamic reports (e.g., total workouts, average duration)
- Admin dashboard with summary statistics
- User authentication and personalized workout history
- Built using Django ORM and prepared statements for secure database access

## 📊 Technologies Used

- Python 3.11+
- Django 5.x
- SQLite (default) or PostgreSQL (optional)
- HTML/CSS (Django templates)
- Git/GitHub for version control

## 📦 Setup Instructions

1. Clone the repository:
   ```bash
   git clone git@github.com:jhayash/GymJournal.git
   cd GymJournal
   
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
4. Run migrations:
   ```bash
   python manage.py migrate
   
5. Create a superuser to access the admin:
   ```bash
   python manage.py createsuperuser
   
6. Start the development server
   ```bash
   python manage.py runserver
   
7. Visit this site: http://127.0.0.1:8000/admin/
