# ERP System - Testing & Usage Guide

## 🚀 Getting Started

### Step 1: Initial Setup

```bash
# Navigate to project
cd d:\ERP\ERP

# Activate virtual environment
myenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser
# Follow prompts and enter:
# Email: admin@erp.com
# Password: admin123
# User type: ADMIN

# Start development server
python manage.py runserver
```

The application will be available at: **http://localhost:8000**

---

## 🧪 Testing Different User Types

### Test Account Creation

#### **1. Organization User**
1. Go to http://localhost:8000/auth/register/
2. Fill form with:
   - Email: org@example.com
   - First Name: ABC
   - Last Name: Organization
   - Account Type: Organization
   - Password: TestPass123
3. Click Register
4. Login and complete organization profile in admin panel

#### **2. Teacher User**
1. Go to http://localhost:8000/auth/register/
2. Fill form with:
   - Email: teacher@example.com
   - First Name: John
   - Last Name: Doe
   - Account Type: Teacher
   - Password: TestPass123
3. Click Register
4. Login and complete teacher profile

#### **3. Student User**
1. Go to http://localhost:8000/auth/register/
2. Fill form with:
   - Email: student@example.com
   - First Name: Jane
   - Last Name: Smith
   - Account Type: Student
   - Password: TestPass123
3. Click Register
4. Login to access student dashboard

#### **4. Support Team User**
1. Go to http://localhost:8000/auth/register/
2. Fill form with:
   - Email: support@example.com
   - First Name: Support
   - Last Name: Agent
   - Account Type: Support Team
   - Password: TestPass123
3. Click Register
4. Login to access support dashboard

---

## 🎯 Testing Each Feature

### **Organization Testing**

**Access**: http://localhost:8000/organizations/dashboard/

1. **Dashboard**
   - View institution statistics
   - See total students, teachers, courses count

2. **Settings**
   - Navigate to http://localhost:8000/organizations/settings/
   - Update organization name, logo, banner
   - Modify contact information
   - Change headquarters address

3. **Members**
   - Navigate to http://localhost:8000/organizations/members/
   - View all registered members
   - See member types and status

---

### **Teacher Testing**

**Access**: http://localhost:8000/teachers/dashboard/

1. **Dashboard**
   - View teaching metrics
   - See courses and student count

2. **Manage Courses**
   - Navigate to http://localhost:8000/teachers/courses/
   - View assigned courses
   - See course details and enrolled students

3. **View Course Students**
   - Click on a course from courses list
   - Navigate to http://localhost:8000/teachers/course/{id}/students/
   - See all enrolled students
   - View attendance and grades

4. **Create Assignment**
   - Navigate to http://localhost:8000/teachers/course/{id}/assignment/create/
   - Fill assignment details:
     - Title
     - Description
     - Due date
     - Total marks
   - Submit

---

### **Student Testing**

**Access**: http://localhost:8000/students/dashboard/

1. **Dashboard**
   - View enrolled courses
   - See pending assignments
   - Check current GPA

2. **Browse Courses**
   - Navigate to http://localhost:8000/courses/
   - See all available courses
   - View course details

3. **Enroll in Course**
   - Click on a course
   - Navigate to http://localhost:8000/courses/{id}/
   - Click "Enroll" button
   - Course appears in your courses list

4. **View Assignments**
   - Navigate to http://localhost:8000/students/assignments/
   - See all pending assignments
   - Click to view assignment details

---

### **Support Team Testing**

**Access**: http://localhost:8000/support/dashboard/

1. **Dashboard**
   - View ticket statistics
   - See open, in-progress, resolved counts
   - View high-priority tickets

2. **View All Tickets**
   - Navigate to http://localhost:8000/support/tickets/
   - Filter by status or priority
   - See all support tickets

3. **Manage Ticket**
   - Click on a ticket
   - Navigate to http://localhost:8000/support/ticket/{id}/
   - Update ticket status
   - Assign to team member
   - Add responses/notes

4. **Create Support Ticket** (As user)
   - Navigate to http://localhost:8000/support/create/
   - Fill ticket details:
     - Subject
     - Description
     - Category
     - Priority
   - Submit ticket

---

## 🔧 Admin Panel Testing

**Access**: http://localhost:8000/admin/

1. **Login** with superuser credentials
2. **Users Management**
   - View all users
   - Filter by user type
   - Edit user details
   - Add new users

3. **Organization Management**
   - View all organizations
   - Edit organization details
   - Approve/verify organizations

4. **Course Management**
   - Create new courses
   - Assign teachers
   - Manage enrollments
   - View assignments

5. **Support Tickets**
   - View all tickets
   - Filter and search
   - Manage ticket status

---

## 📊 Data Creation for Testing

### Create Test Data in Admin

1. **Create Organization**
   - Admin → Users → CustomUser → Add User
     - Email: org@test.com
     - User Type: ORGANIZATION
   - Admin → Organizations → Organization → Add Organization
     - Assign to created user
     - Fill details

2. **Create Teacher**
   - Admin → Users → CustomUser → Add User
     - Email: teacher@test.com
     - User Type: TEACHER
   - Admin → Teachers → Teacher → Add Teacher
     - Assign to created user
     - Fill teacher details

3. **Create Student**
   - Admin → Users → CustomUser → Add User
     - Email: student@test.com
     - User Type: STUDENT
   - Admin → Students → Student → Add Student
     - Assign to created user
     - Fill student details

4. **Create Course**
   - Admin → Courses → Course → Add Course
     - Assign organization and teacher
     - Set course code, title
     - Set start/end dates

5. **Enroll Student**
   - Admin → Courses → Enrollment → Add Enrollment
     - Select student and course
     - Set status to ACTIVE

6. **Create Assignment**
   - Admin → Courses → Assignment → Add Assignment
     - Select course
     - Fill assignment details
     - Set due date

---

## ✅ Testing Checklist

### Authentication
- [ ] Register new user
- [ ] Login with credentials
- [ ] Logout successfully
- [ ] Update profile
- [ ] Can't access other user dashboards

### Organization
- [ ] Create organization profile
- [ ] Update settings
- [ ] View member list
- [ ] See statistics

### Teacher
- [ ] Access teacher dashboard
- [ ] View courses
- [ ] View students in course
- [ ] Create assignment
- [ ] Grade submissions

### Student
- [ ] Access student dashboard
- [ ] Browse courses
- [ ] Enroll in course
- [ ] View assignments
- [ ] Submit work

### Support
- [ ] Create support ticket
- [ ] View my tickets
- [ ] Support team sees tickets
- [ ] Assign ticket
- [ ] Add response
- [ ] Resolve ticket

### Admin
- [ ] Login to admin panel
- [ ] Manage users
- [ ] Manage courses
- [ ] Manage enrollments
- [ ] Manage tickets

---

## 🐛 Troubleshooting

### Issue: "No such table" error
**Solution**: Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Issue: Cannot upload files
**Solution**: Ensure media directory exists
```bash
mkdir media
```

### Issue: Superuser login fails
**Solution**: Recreate superuser
```bash
python manage.py createsuperuser
```

### Issue: CSS not loading
**Solution**: Collect static files
```bash
python manage.py collectstatic
```

### Issue: Port 8000 already in use
**Solution**: Use different port
```bash
python manage.py runserver 8001
```

---

## 📱 Testing Different Browsers

The application should work with:
- Chrome/Chromium ✓
- Firefox ✓
- Safari ✓
- Edge ✓

---

## 🔒 Security Testing

1. **SQL Injection**
   - Test with special characters in forms
   - System should handle safely

2. **CSRF Protection**
   - All forms have CSRF tokens
   - POST requests are protected

3. **Authentication**
   - Users can only access their own data
   - Role-based access is enforced

---

## 📝 Sample Test Scenarios

### Scenario 1: Complete Course Enrollment
1. Register as student
2. Login to student dashboard
3. Browse available courses
4. Enroll in a course
5. View course in dashboard
6. View course assignments
7. Submit assignment

### Scenario 2: Teacher Course Management
1. Register as teacher
2. Admin: Create course and assign to teacher
3. Teacher views their courses
4. Teacher creates assignment
5. Admin: Enroll student in course
6. Teacher views enrolled students
7. Teacher can grade student submission

### Scenario 3: Support Ticket Resolution
1. User creates support ticket
2. Support team member views ticket
3. Support team updates ticket status
4. Support team adds response
5. User receives update
6. Ticket marked as resolved

---

## 📈 Performance Testing

To test with large amounts of data:

```bash
# Create 100 test users
python manage.py shell

from users.models import CustomUser
from django.utils import timezone

for i in range(100):
    CustomUser.objects.create_user(
        email=f'user{i}@test.com',
        password='test123',
        user_type='STUDENT',
        first_name=f'User{i}',
        last_name=f'Test'
    )
```

---

## 🎓 Learning Resources

- [Django Documentation](https://docs.djangoproject.com)
- [Django Models](https://docs.djangoproject.com/en/5.2/topics/db/models/)
- [Django Views](https://docs.djangoproject.com/en/5.2/topics/http/views/)
- [Django Admin](https://docs.djangoproject.com/en/5.2/ref/contrib/admin/)

---

## 💡 Tips & Tricks

1. **Check email in console**
   - During development, emails print to console
   - Check server terminal for email output

2. **Debug queries**
   - Use `query = User.objects.filter(...).query` to see SQL

3. **Test API responses**
   - Use Django shell to test queries:
   ```bash
   python manage.py shell
   from users.models import CustomUser
   CustomUser.objects.all().count()
   ```

4. **View database directly**
   - Install DB Browser for SQLite
   - Open `db.sqlite3` to inspect data

---

**Ready to test!** Start with Step 1 and follow the testing guide for each feature.
