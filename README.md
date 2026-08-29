# Team Task Management System

A modern **Server-Side Rendered (SSR) Team Task Management System** built with **Python and Django**.

The application allows administrators to manage projects, team members, and tasks, while team members can view their assigned tasks, update task status, and add progress updates.

(image.png)

## 🚀 Project Overview

Team Task Management is an internal workspace designed to help teams organize their daily project work efficiently.

The application provides role-based access for:

* **Admin**
* **Team Member**


(image-1.png)

Admins can create projects, manage team members, assign tasks, set priorities and deadlines, and monitor overall progress.

Team members can view their assigned tasks, update task status, and add progress comments.

---

## ✨ Features

### 👨‍💼 Admin

* Secure admin login
* Admin dashboard
* Create projects
* Edit projects
* Delete projects
* View project progress
* Add team members
* Manage team members
* Create tasks
* Edit tasks
* Assign tasks to team members
* Set task priority
* Set task status
* Set task deadlines
* Search tasks
* Filter tasks by:

  * Project
  * Team member
  * Priority
  * Status
* View task details
* Track completed and pending tasks
* Track overall project progress
* Maintain deadline history

### 👨‍💻 Team Member

* Secure team member login
* Team member dashboard
* View assigned tasks
* View task details
* Update task status
* Add progress comments
* Track project and task deadlines

---

## 🎯 User Roles

| Role        | Access                                        |
| ----------- | --------------------------------------------- |
| Admin       | Full project, team member and task management |
| Team Member | View assigned tasks and update progress       |

---

## 🏗️ Technology Stack

### Backend

* Python
* Django
* Django ORM
* Django Authentication
* SQLite

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* Google Fonts

### Architecture

* Server-Side Rendering (SSR)
* Django Templates
* Role-Based Access Control
* MVC/MVT architecture

---

## 📂 Project Structure

```text
team-task-manager/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── accounts/
│   ├── migrations/
│   ├── templates/
│   │   └── accounts/
│   │       ├── login.html
│   │       ├── admin_dashboard.html
│   │       ├── member_dashboard.html
│   │       ├── add_team_member.html
│   │       └── team_members.html
│   │
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── projects/
│   ├── migrations/
│   ├── templates/
│   │   └── projects/
│   │       ├── project_list.html
│   │       ├── project_form.html
│   │       └── project_confirm_delete.html
│   │
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── tasks/
│   ├── migrations/
│   ├── templates/
│   │   └── tasks/
│   │       ├── task_list.html
│   │       ├── task_form.html
│   │       ├── my_tasks.html
│   │       └── task_detail.html
│   │
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│
├── db.sqlite3
│
├── manage.py
│
└── requirements.txt
```

---

## 🗄️ Main Data Models

### User

Stores application users and their roles.

```text
User
├── username
├── email
├── password
└── role
    ├── ADMIN
    └── TEAM_MEMBER
```

### Project

Stores project information.

```text
Project
├── name
├── description
├── start_date
└── end_date
```

### Task

Stores task information.

```text
Task
├── project
├── title
├── description
├── assigned_to
├── priority
├── status
└── deadline
```

### Deadline History

Tracks deadline changes made to existing tasks.

```text
DeadlineHistory
├── task
├── old_deadline
├── new_deadline
└── changed_by
```

### Task Comment

Stores team member progress updates.

```text
TaskComment
├── task
├── user
└── comment
```

---

## 🔐 Authentication & Authorization

The project uses Django authentication for secure login.

After successful login, users are redirected based on their role:

```text
Admin
   ↓
Admin Dashboard

Team Member
   ↓
Team Member Dashboard
```

Unauthorized users are redirected away from restricted pages.

---

## 📊 Dashboard

### Admin Dashboard

The admin dashboard provides:

* Total projects
* Total tasks
* Completed tasks
* Pending tasks
* Overall completion percentage
* Project management
* Team member management
* Task management
* Quick actions

### Team Member Dashboard

The team member dashboard provides:

* Assigned task access
* Task progress workflow
* Status updates
* Progress comments

---

## 🔄 Task Workflow

```text
Create Task
     ↓
Assign Team Member
     ↓
Set Priority
     ↓
Set Deadline
     ↓
To Do
     ↓
In Progress
     ↓
Completed
```

---

## 🔎 Task Search & Filtering

Admins can quickly find tasks using:

```text
Search
   +
Project
   +
Assigned Member
   +
Priority
   +
Status
```

This makes task management easier when the number of tasks increases.

---

## 🎨 UI / UX

The interface is designed with a modern enterprise SaaS style.

Highlights include:

* Responsive layouts
* Professional typography
* Modern dashboard cards
* Sidebar navigation
* Top navigation bar
* Animated login interface
* Progress indicators
* Status badges
* Responsive tables
* Form validation states
* Password visibility toggle
* Mobile-friendly layouts

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/team-task-manager.git
```

### 2. Open the project

```bash
cd team-task-manager
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create an admin/superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 🔑 Application Flow

```text
Login
  │
  ├── Admin
  │     └── Admin Dashboard
  │           ├── Projects
  │           ├── Team Members
  │           └── Tasks
  │
  └── Team Member
        └── Member Dashboard
              └── My Tasks
                    ├── Update Status
                    └── Add Progress
```

---

## 🧪 Testing

Run Django system checks:

```bash
python manage.py check
```

Run tests:

```bash
python manage.py test
```

---

## 🔒 Security Considerations

The project uses Django's built-in security features including:

* CSRF protection
* Password hashing
* Session authentication
* Login-required views
* Role-based authorization
* Django ORM
* Server-side form validation

---

## 🌱 Future Improvements

Potential future enhancements include:

* REST API integration
* Email notifications
* Task attachments
* Real-time notifications
* Advanced analytics
* Project activity timeline
* Pagination
* PostgreSQL support
* Cloud deployment
* Docker support
* Automated testing and CI/CD

---

## 📌 Project Type

**Full Stack Web Application**

**Architecture:** Server-Side Rendering (SSR)

**Domain:** Project & Task Management

**Authentication:** Role-Based Authentication

**Database:** SQLite

---

## 👩‍💻 Author

**R. Durga Devi**

Python Full Stack Developer

Technologies:

```text
Python
Django
HTML
CSS
JavaScript
Bootstrap
SQLite
Git
GitHub
```

---

## ⭐ Project Goal

The goal of this project is to build a practical enterprise-style team workspace where administrators can manage projects and tasks while team members can collaborate through task updates and progress tracking.

---

## 📄 License

This project is developed for educational, portfolio and demonstration purposes.

```
```
