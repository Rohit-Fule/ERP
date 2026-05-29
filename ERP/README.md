# ERP Management System - Comprehensive Guide

## 📋 Project Overview

This is a Django-based **Educational Resource Planning (ERP) System** designed to manage educational institutions with support for multiple user types:

- **Organization**: Institution/School administrators
- **Teachers**: Teaching staff managing courses and students
- **Students**: Learners enrolling in courses
- **Support Team**: Customer support and issue management

---

## 📁 Project Structure

```
ERP/
├── ERP/                          # Main project configuration
│   ├── settings.py              # Django settings (apps, db, middleware)
│   ├── urls.py                  # Main URL routing
│   ├── wsgi.py                  # WSGI configuration
│   └── asgi.py                  # ASGI configuration
│
├── users/                        # User authentication & profiles
│   ├── models.py                # CustomUser model with user types
│   ├── views.py                 # Login, Register, Profile views
│   ├── admin.py                 # Admin interface
│   └── urls.py                  # User URLs
│
├── organizations/               # Organization/Institution management
│   ├── models.py                # Organization model
│   ├── views.py                 # Organization dashboard & settings
│   ├── admin.py                 # Admin interface
│   └── urls.py                  # Organization URLs
│
├── teachers/                    # Teacher management
│   ├── models.py                # Teacher & TeacherQualification models
│   ├── views.py                 # Teacher dashboard & course management
│   ├── admin.py                 # Admin interface
│   └── urls.py                  # Teacher URLs
│
├── students/                    # Student management
│   ├── models.py                # Student model
│   ├── views.py                 # Student dashboard & enrollment
│   ├── admin.py                 # Admin interface
│   └── urls.py                  # Student URLs
│
├── courses/                     # Course & enrollment management
│   ├── models.py                # Course, Enrollment, Assignment, Submission models
│   ├── views.py                 # Course listings & enrollment views
│   ├── admin.py                 # Admin interface
│   └── urls.py                  # Course URLs
│
├── support/                     # Support ticket system
│   ├── models.py                # Ticket, TicketResponse, SupportTeamMember, TicketRating
│   ├── views.py                 # Support dashboard & ticket management
│   ├── admin.py                 # Admin interface
│   └── urls.py                  # Support URLs
│
├── dashboard/                   # Main dashboard & landing page
│   ├── views.py                 # Home & dashboard views
│   └── urls.py                  # Dashboard URLs
│
├── templates/                   # HTML templates
│   ├── base.html               # Base template with styling
│   ├── users/                   # User templates
│   ├── students/                # Student templates
│   ├── teachers/                # Teacher templates
│   ├── organizations/           # Organization templates
│   ├── support/                 # Support templates
│   └── dashboard/               # Dashboard templates
│
├── static/                      # Static files (CSS, JS, Images)
├── media/                       # User-uploaded files
├── manage.py                    # Django management commands
├── db.sqlite3                   # SQLite database
└── requirements.txt             # Python dependencies
```

---

## 🔧 Setup Instructions

### 1. **Clone and Setup Environment**

```bash
# Navigate to project directory
cd d:\ERP\ERP

# Create virtual environment
python -m venv myenv

# Activate virtual environment
# On Windows:
myenv\Scripts\activate

# On Mac/Linux:
source myenv/bin/activate
```

### 2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 3. **Configure Database**

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### 4. **Create Superuser**

```bash
python manage.py createsuperuser
# Follow prompts to create admin account
```

### 5. **Run Development Server**

```bash
python manage.py runserver
```

Visit: `http://localhost:8000`

---

## 👥 User Types & Features

### **1. Organization**
- **Dashboard**: View institution statistics (students, teachers, courses)
- **Settings**: Update organization profile, logo, and contact information
- **Members**: Manage all organization members
- **Features**: 
  - Verify member accounts
  - Monitor institutional metrics
  - Approve courses and assignments

### **2. Teacher**
- **Dashboard**: View teaching metrics
- **Courses**: Manage assigned courses
- **Students**: View enrolled students per course
- **Assignments**: Create and grade assignments
- **Grading**: Manage student submissions and grades
- **Features**:
  - Track attendance
  - Manage course materials
  - Create assignments and quizzes

### **3. Student**
- **Dashboard**: View enrolled courses and pending assignments
- **Courses**: Browse and enroll in available courses
- **Assignments**: View and submit assignments
- **Grades**: Track academic performance and GPA
- **Features**:
  - Track assignment deadlines
  - View grades and feedback
  - Manage course schedule

### **4. Support Team**
- **Dashboard**: Support metrics and ticket overview
- **Tickets**: View and manage support tickets
- **Categories**: Technical, Account, Course, Enrollment, Payment, Other
- **Priorities**: Low, Medium, High, Critical
- **Features**:
  - Assign tickets to team members
  - Track resolution time
  - Rate ticket resolutions
  - Internal notes for team communication

---

## 🗄️ Database Models

### **Users App**
- **CustomUser**: Base user model with email authentication

### **Organizations App**
- **Organization**: Institution profile with stats

### **Teachers App**
- **Teacher**: Teacher profile with qualifications
- **TeacherQualification**: Teacher certifications

### **Students App**
- **Student**: Student profile with academic info

### **Courses App**
- **Course**: Course information and metadata
- **Enrollment**: Student course enrollment
- **Assignment**: Course assignments
- **Submission**: Student assignment submissions

### **Support App**
- **Ticket**: Support tickets
- **TicketResponse**: Ticket communications
- **SupportTeamMember**: Support staff profiles
- **TicketRating**: Ticket satisfaction ratings

---

## 🔐 User Authentication

- Email-based login (not username)
- Custom user model with role-based access
- Password hashing with Django's built-in system
- User type validation for dashboard access

---

## 🔗 URL Structure

```
/                               # Home/Landing page
/auth/login/                   # User login
/auth/register/                # User registration
/auth/logout/                  # User logout
/auth/profile/                 # User profile

/organizations/dashboard/      # Organization dashboard
/organizations/settings/       # Organization settings
/organizations/members/        # View members

/teachers/dashboard/           # Teacher dashboard
/teachers/courses/             # Manage courses
/teachers/course/<id>/students/  # View course students
/teachers/profile/             # Teacher profile

/students/dashboard/           # Student dashboard
/students/courses/             # Enrolled courses
/students/assignments/         # View assignments
/students/profile/             # Student profile

/courses/                      # Browse all courses
/courses/<id>/                 # Course details
/courses/<id>/enroll/          # Enroll in course

/support/dashboard/            # Support dashboard (staff only)
/support/tickets/              # All tickets (staff)
/support/ticket/<id>/          # Ticket details (staff)
/support/create/               # Create support ticket (user)
/support/my-tickets/           # My tickets (user)

/admin/                        # Django admin panel
```

---

## 🎯 Key Features

### ✅ **Multi-Role Authentication**
- Separate login/dashboard for each user type
- Role-based access control

### ✅ **Course Management**
- Create and manage courses
- Student enrollment with capacity limits
- Assignment creation and grading

### ✅ **Support System**
- Ticket creation and tracking
- Priority and category management
- Team member assignment
- Resolution ratings

### ✅ **File Management**
- Profile image uploads
- Assignment file submissions
- Support ticket attachments
- Media file serving

### ✅ **Admin Interface**
- Comprehensive Django admin panel
- User management
- Course and enrollment management
- Support ticket overview

---

## 🚀 Next Steps / Advanced Features

### To Implement:
1. **API Development**: REST API using Django REST Framework
2. **Notifications**: Email notifications for assignments/grades
3. **Analytics**: Advanced reporting dashboards
4. **Payment Integration**: Fee collection and payment tracking
5. **Calendar Integration**: Course schedule and assignment calendars
6. **Chat System**: Real-time messaging between users
7. **Mobile App**: React Native or Flutter mobile client
8. **Advanced Grading**: Rubrics, weighted scoring
9. **Certificates**: Course completion certificates
10. **Attendance Tracking**: QR code or biometric attendance

---

## 📝 Management Commands

```bash
# Create migrations for all apps
python manage.py makemigrations

# Apply all pending migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files (production)
python manage.py collectstatic

# Run development server
python manage.py runserver

# Run tests
python manage.py test

# Create app
python manage.py startapp app_name

# Shell (interactive Python)
python manage.py shell
```

---

## 🔒 Security Considerations

1. Change `SECRET_KEY` in settings.py for production
2. Set `DEBUG = False` in production
3. Configure `ALLOWED_HOSTS` for your domain
4. Use HTTPS in production
5. Enable CSRF and XSS protection
6. Set strong password requirements

---

## 📚 Technology Stack

- **Backend**: Django 5.2.14
- **Database**: SQLite (Development), PostgreSQL (Production)
- **Frontend**: HTML5, CSS3, Bootstrap (optional)
- **Image Processing**: Pillow
- **Database Adapter**: psycopg2

---

## 🤝 Contributing

To extend the system:

1. Create new app: `python manage.py startapp app_name`
2. Define models in `models.py`
3. Create views and URLs
4. Register in admin panel
5. Create templates

---

## 📞 Support & Contact

For issues or feature requests, please use the built-in support ticket system.

---

## 📄 License

This project is open source and available under MIT License.

---

**Last Updated**: 2024
**Version**: 1.0.0
