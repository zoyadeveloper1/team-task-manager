# Team Task Manager

A full-stack Team Project & Task Management web application built with **Python, Django, SQLite, HTML, CSS, and Bootstrap**.

This application allows admins to manage projects, team members, and tasks, while team members can view assigned tasks, update task status, and add progress comments.

## Features

### Admin

* Admin authentication
* Role-based access control
* Create projects
* View projects
* Edit projects
* Delete projects
* View project progress
* Add team members
* View team members
* Create tasks
* Assign tasks to team members
* Set task priority
* Set task status
* Set task deadlines
* Edit tasks
* Search and filter tasks
* View task details
* Maintain deadline change history

### Team Member

* Secure login
* Role-based dashboard
* View assigned tasks
* View project information
* View task priority
* View task deadline
* Update task status
* Add progress comments
* View progress history

## Special Feature: Deadline History

When an admin changes a task deadline, the application stores the previous deadline and the new deadline.

Example:

| Old Deadline | New Deadline | Changed By | Changed At   |
| ------------ | ------------ | ---------- | ------------ |
| Aug 31, 2026 | Sep 5, 2026  | durga      | Aug 28, 2026 |

This provides a complete history of deadline changes.

## Technology Stack

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* Django Templates

### Backend

* Python
* Django

### Database

* SQLite

### Authentication

* Django Authentication System
* Custom User Model
* Role-based access control

### Deployment

* GitHub
* Render

## Project Architecture

This project uses a **Server-Side Rendering (SSR)** architecture.

```text
Browser
   |
   v
Django
   |
   +-- Templates
   |
   +-- Views
   |
   +-- Forms
   |
   +-- Models / ORM
   |
   v
SQLite Database
```

The frontend and backend are implemented inside the same Django project and can be deployed as a single web service.

## Project Structure

```text
team-task-manager/
│
├── accounts/
│   ├── migrations/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── projects/
│   ├── migrations/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── tasks/
│   ├── migrations/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── accounts/
│   ├── projects/
│   └── tasks/
│
├── static/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

## Database Models

### User

```text
User
----------------
id
username
email
password
role
```

Roles:

```text
ADMIN
TEAM_MEMBER
```

### Project

```text
Project
----------------
id
name
description
start_date
end_date
created_at
updated_at
```

### Task

```text
Task
----------------
id
project
title
description
assigned_to
priority
status
deadline
created_at
updated_at
```

### Task Comment

```text
TaskComment
----------------
id
task
user
comment
created_at
```

### Deadline History

```text
DeadlineHistory
----------------
id
task
old_deadline
new_deadline
changed_by
changed_at
```

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/YOUR-USERNAME/team-task-manager.git
```

Go to the project:

```bash
cd team-task-manager
```

### 2. Create Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Admin User

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/accounts/login/
```

## Login Flow

### Admin

```text
Login
   ↓
Role = ADMIN
   ↓
Admin Dashboard
```

### Team Member

```text
Login
   ↓
Role = TEAM_MEMBER
   ↓
Team Member Dashboard
```

## Main URLs

| URL                           | Description           | Access                  |
| ----------------------------- | --------------------- | ----------------------- |
| `/accounts/login/`            | Login page            | Public                  |
| `/accounts/logout/`           | Logout                | Authenticated           |
| `/accounts/admin-dashboard/`  | Admin dashboard       | Admin                   |
| `/accounts/member-dashboard/` | Team member dashboard | Team Member             |
| `/accounts/team-members/`     | Team member list      | Admin                   |
| `/accounts/team-members/add/` | Add team member       | Admin                   |
| `/projects/`                  | Project list          | Admin                   |
| `/projects/create/`           | Create project        | Admin                   |
| `/projects/<id>/edit/`        | Edit project          | Admin                   |
| `/projects/<id>/delete/`      | Delete project        | Admin                   |
| `/tasks/`                     | Task list             | Admin                   |
| `/tasks/create/`              | Create task           | Admin                   |
| `/tasks/<id>/edit/`           | Edit task             | Admin                   |
| `/tasks/<id>/`                | Task details          | Admin / Assigned Member |
| `/tasks/my-tasks/`            | Assigned tasks        | Team Member             |

## API / Endpoint Reference

The application primarily uses Django server-rendered views.

### Authentication

```text
GET  /accounts/login/
POST /accounts/login/
GET  /accounts/logout/
```

### Projects

```text
GET  /projects/
GET  /projects/create/
POST /projects/create/
GET  /projects/<id>/edit/
POST /projects/<id>/edit/
GET  /projects/<id>/delete/
POST /projects/<id>/delete/
```

### Tasks

```text
GET  /tasks/
GET  /tasks/create/
POST /tasks/create/
GET  /tasks/<id>/
GET  /tasks/<id>/edit/
POST /tasks/<id>/edit/
```

### Team Member Task Actions

```text
GET  /tasks/my-tasks/
POST /tasks/<id>/status/
POST /tasks/<id>/comment/
```

## Search and Filters

Admin users can filter tasks using:

```text
Search by task title
Project
Assigned Team Member
Priority
Status
```

Example:

```text
/tasks/?search=frontend&priority=HIGH&status=TODO
```

## Validation

The application includes form validation for:

* Required fields
* Project date validation
* Task deadline
* Valid task status
* Valid task priority
* Team member assignment

## Security

The application uses:

* Django password hashing
* CSRF protection
* Authentication
* Role-based authorization
* Login-required protected views
* Restricted access to assigned tasks

## Error Handling

The application handles common cases such as:

* Invalid login credentials
* Unauthorized dashboard access
* Unauthorized task access
* Missing task records
* Missing project records
* Invalid form submissions

## Future Enhancements

Possible improvements:

* Email notifications
* File attachments
* Task activity history
* Automated tests
* Docker support
* REST API using Django REST Framework
* PostgreSQL production database
* Advanced reporting and analytics

## Deployment

The application can be deployed as a single Django web service.

Typical production flow:

```text
GitHub
   ↓
Render
   ↓
Django Web Service
   ↓
Application
```

## Author

**Team Task Manager**

Built using:

```text
Python
Django
SQLite
HTML
CSS
Bootstrap
```
