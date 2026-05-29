# ERP System Architecture

## User Type & Dashboard Routing

```
┌─────────────────────────────────────────────────────────────────┐
│                    ERP Management System                         │
│                      Landing Page (/)                            │
└─────────────────────────────────────────────────────────────────┘
                              │
                ┌─────────────┼─────────────┐
                │                           │
         ┌──────────────┐         ┌──────────────────┐
         │ Authenticated         │ Not Authenticated │
         └──────────────┘         └──────────────────┘
                │                           │
    ┌───────────┼───────────┐          Register/Login
    │           │           │               │
    ▼           ▼           ▼               ▼
┌────────┐ ┌────────┐ ┌────────┐ ┌─────────────────┐
│ Admin  │ │Support │ │Teacher │ │  Student/Org    │
└────────┘ └────────┘ └────────┘ └─────────────────┘
```

## System Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                         Django Framework                          │
├──────────────────────────────────────────────────────────────────┤
│                      URL Routing Layer                            │
│  ┌─────────────┬────────────┬──────────┬────────────┬─────────┐ │
│  │ Dashboard   │ Users Auth │ Orgs     │ Courses    │ Support │ │
│  │ Routes      │ Routes     │ Routes   │ Routes     │ Routes  │ │
│  └─────────────┴────────────┴──────────┴────────────┴─────────┘ │
├──────────────────────────────────────────────────────────────────┤
│                      Views Layer                                  │
│ ┌─────────────┬────────────┬──────────┬────────────┬─────────┐  │
│ │ Dashboard   │ User Views │ Org      │ Course     │ Support │  │
│ │ Views       │ (login,    │ Views    │ Views      │ Views   │  │
│ │             │ register)  │          │            │         │  │
│ └─────────────┴────────────┴──────────┴────────────┴─────────┘  │
├──────────────────────────────────────────────────────────────────┤
│                      Models Layer                                 │
│                    (ORM - Database)                               │
│ ┌─────────────┬────────────┬──────────┬────────────┬─────────┐  │
│ │ CustomUser  │ Organization
│ │ Teacher     │ Student      │ Course │ Enrollment │ Ticket  │  │
│ │ TeacherQual │ Assignment   │ Submit │ TktResponse│ Members │  │
│ └─────────────┴────────────┴──────────┴────────────┴─────────┘  │
├──────────────────────────────────────────────────────────────────┤
│                  SQLite Database                                  │
│                  (Development)                                    │
└──────────────────────────────────────────────────────────────────┘
        ↓
┌──────────────────────────────────────────────────────────────────┐
│           PostgreSQL Database (Production)                        │
└──────────────────────────────────────────────────────────────────┘
```

## User Role Access Control

```
                    CustomUser (Auth System)
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
   user_type              is_staff          is_superuser
        │                   │                   │
        ├─ORGANIZATION ─────┼─────────────┬────┤
        │                   │             │    │
        ├─TEACHER ──────────┼─────────────┼────┤
        │                   │             │    │
        ├─STUDENT ──────────┼─────────────┼────┤
        │                   │             │    │
        ├─SUPPORT ──────────┼─────────────┼────┤
        │                   │             │    │
        └─ADMIN ────────────┴─────────────┘────┘
             │                                  │
             └──────────────┬───────────────────┘
                            ▼
                    Dashboard Redirect
                    (Role-based routing)
```

## Data Relationships

```
┌──────────────────┐
│   CustomUser     │
│ (Base for all)   │
└────────┬─────────┘
         │
    ┌────┴────────────────┬──────────────────┬──────────────────┐
    │                     │                  │                  │
    ▼                     ▼                  ▼                  ▼
┌──────────────┐ ┌─────────────────┐ ┌──────────┐ ┌────────────────┐
│  Teacher  ◄──┼─ instructor ─────┼─ Course   │ │  Organization  │
│   1:1        │ (many-to-one)     │   1:many  │ │      1:many     │
└──────────────┘ └─────────────────┘ └────┬─────┘ └────────────────┘
    │                 │                    │
    │            ┌────┴────┐          ┌────┴────┐
    │            ▼         ▼          ▼         ▼
    │       Submission  Assignment  Student  Enrollment
    │
    ▼
┌──────────────┐
│  Student     │
│    1:1       │
└──────────────┘
    │
    └──────────────┬─────────────────┐
                   │                 │
                   ▼                 ▼
              Enrollment        Submission
              (many-to-many)    (Course Work)

┌─────────────┐
│ SupportTeam │
│    1:1      │
└──────┬──────┘
       │
       └─────────────┬──────────────┬─────────────┐
                     │              │             │
                     ▼              ▼             ▼
                  Ticket      TicketResponse  TicketRating
```

## Request-Response Flow

```
User Request
    │
    ▼
┌─────────────────────────────┐
│  URL Router (urls.py)       │
│  Matches path pattern       │
└──────────────┬──────────────┘
               │
    ┌──────────▼──────────┐
    │ Middleware Stack    │
    │ - Auth Check       │
    │ - Session          │
    │ - CSRF             │
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │ View Function       │
    │ - Process Request   │
    │ - Query Models      │
    │ - Business Logic    │
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │ Database Query      │
    │ (ORM/Models)        │
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │ Context Prepared    │
    │ (Data collected)    │
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │ Template Rendering  │
    │ (HTML generation)   │
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │ HTTP Response       │
    │ (HTML to browser)   │
    └──────────┬──────────┘
               │
               ▼
        Browser Display
```

## App Dependencies

```
                    ┌─────────────┐
                    │   Django    │
                    │  Framework  │
                    └──────┬──────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
    ┌────────┐        ┌────────┐       ┌──────────┐
    │ USERS  │        │ COURSES│       │ SUPPORT  │
    │ (Base) │        │        │       │  SYSTEM  │
    └───┬────┘        └────┬───┘       └──────────┘
        │                  │
        ├─────────┬────────┤
        │         │        │
        ▼         ▼        ▼
    ┌─────┐  ┌──────┐  ┌────────┐
    │ ORG │  │TEACH │  │STUDENT │
    └─────┘  └──────┘  └────────┘
```

## Feature Distribution

```
┌────────────────────────────────────────────────────────────┐
│              FEATURE AVAILABILITY BY ROLE                  │
├────────────────────────────────────────────────────────────┤
│                                                             │
│ Dashboard Management:                                      │
│   • Organization   ✓ (Institution stats)                 │
│   • Teacher        ✓ (Teaching metrics)                  │
│   • Student        ✓ (Learning progress)                 │
│   • Support        ✓ (Ticket metrics)                    │
│   • Admin          ✓ (System overview)                   │
│                                                             │
│ Course Management:                                         │
│   • Organization   ✓ (Approve/Monitor)                   │
│   • Teacher        ✓ (Create/Edit)                       │
│   • Student        ✓ (Enroll/View)                       │
│   • Support        ✗                                      │
│   • Admin          ✓ (Full Control)                       │
│                                                             │
│ Support Tickets:                                           │
│   • Organization   ✓ (Create/View)                        │
│   • Teacher        ✓ (Create/View)                        │
│   • Student        ✓ (Create/View)                        │
│   • Support        ✓ (Manage/Resolve)                     │
│   • Admin          ✓ (Full Control)                       │
│                                                             │
│ User Management:                                           │
│   • Organization   ✓ (View Members)                       │
│   • Teacher        ✗                                      │
│   • Student        ✗                                      │
│   • Support        ✓ (Limited)                            │
│   • Admin          ✓ (Full Control)                       │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

---

This architecture ensures:
- Clear separation of concerns
- Scalable app structure
- Role-based access control
- Easy to extend with new features
- Follows Django best practices
