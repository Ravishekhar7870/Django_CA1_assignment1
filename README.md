# 🏫 Django CA1 Assignment – University Portal

This is a simple Django-based university portal built as part of a CA1 assignment. It allows students to:

- View their profile
- Check enrolled subjects
- Submit feedback
- View custom greetings based on year
- Experience custom 404 error pages
- Run unit tests for core features

---

## 🛠️ Tech Stack

- Python 3.x
- Django 4.x
- HTML (Django Templates)

---

## 🔧 Features

### ✅ 1. View Student Profile

- URL: `/student/<roll_number>/`
- Displays name, roll number, department, and a greeting.
- If the student is in **year 1**, shows "Welcome Freshman!" else "Welcome Back!"

### ✅ 2. List Enrolled Subjects

- URL: `/subjects/`
- Shows a list of hardcoded subjects (`['AI', 'DBMS', 'Networking']`)

### ✅ 3. Feedback Form

- URL: `/feedback/`
- Accepts name, email, and message
- On submission, redirects to a thank-you page

### ✅ 4. Custom 404 Page

- If the roll number doesn't exist, a custom 404 page is shown.

### ✅ 5. Unit Testing

- Tests for `/student/101/`:
  - Checks for HTTP 200 response
  - Checks if the student name is rendered

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Ravishekhar7870/Django_CA1_assignment1.git
cd Django_CA1_assignment1
```
### 2.Create Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
### 3. Install Django
```bash
pip install django
```
### 4. Run the Server
```bash
python manage.py runserver
```
### 5. Visit
```bash
(http://127.0.0.1:8000/student/101/

http://127.0.0.1:8000/subjects/

http://127.0.0.1:8000/feedback/)
```
### 6. Running test
```bash
python manage.py test

```



