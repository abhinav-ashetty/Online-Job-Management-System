# 🚀 Online Job Management System

A full-stack **Online Job Management System** developed using **Django** that connects **Recruiters** and **Job Seekers** through a modern recruitment platform. The application streamlines the hiring process by enabling recruiters to post job opportunities, automatically notify registered job seekers via email in real time, and intelligently shortlist candidates based on required skills. Job seekers can create professional profiles, upload resumes, search for jobs, apply online, and track their applications from a centralized dashboard.

# 📌 Features

## 👨‍💼 Recruiter Module

* Recruiter Registration & Secure Login
* Create, Update, and Delete Job Listings
* Manage Recruiter Profile
* View and Manage Posted Jobs
* Review Applications for Each Job
* **Automatic Candidate Shortlisting** based on required skills specified in the job posting
* View ranked candidates matching job requirements

## 👨‍💻 Job Seeker Module

* Job Seeker Registration & Secure Login
* Create and Update Professional Profile
* Upload Resume/CV
* Browse and Search Available Jobs
* Apply for Jobs Online
* Track Application Status
* Manage Personal Information

## 📧 Real-Time Email Notification System

* Automatic email notifications sent to registered job seekers whenever a recruiter posts a new job.
* Notifications help job seekers stay updated with newly available opportunities.
* Reduces the need for users to frequently check the platform for new openings.

## 🤖 Intelligent Candidate Selection Automation

* Recruiters specify the required skills while creating a job posting.
* The system compares applicants' skills with the job requirements.
* Candidates who satisfy the required skill set are automatically shortlisted.
* Simplifies the recruitment process by reducing manual screening.
* Helps recruiters quickly identify the most relevant applicants.

## 🔐 Authentication & Security

* Secure Login and Registration
* Role-Based Access Control (Recruiter & Job Seeker)
* Session Management
* Password Protection

## 🎨 User Interface

* Responsive Design
* User-Friendly Navigation
* Bootstrap-Based Interface
* Mobile-Friendly Layout

---

# 🛠 Tech Stack

### Backend

* Python
* Django 2.1.7

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap
* jQuery

### Database

* SQLite

### Deployment

* Gunicorn
* WhiteNoise
* Procfile Support

---

# 📂 Project Structure

```
Online-Job-Management-System/

├── accounts/
├── jobs/
├── jobsapp/
├── static/
├── templates/
├── screenshots/
├── requirements.txt
├── manage.py
├── Procfile
└── README.md
```

---

# 📸 Screenshots

The repository includes screenshots demonstrating the application's interface.

```
screenshots/
├── one.png
├── two.png
└── three.png
```

You can showcase these images directly in GitHub after uploading the repository.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/abhinav-ashetty/Online-Job-Management-System.git
```

## 2. Navigate into the Project

```bash
cd Online-Job-Management-System
```

## 3. Create a Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Apply Migrations

```bash
python manage.py migrate
```

---

## 6. Create a Superuser

```bash
python manage.py createsuperuser
```

---

## 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit

```
http://127.0.0.1:8000/
```

---

# 📁 Main Modules

* User Authentication
* Employer Dashboard
* Employee Dashboard
* Job Management
* Job Search
* Resume Upload
* Application Management

---

# 📦 Requirements

* Python 3.x
* Django 2.1.7
* Gunicorn
* WhiteNoise

Install using:

```bash
pip install -r requirements.txt
```

---

# 🔒 Security Notice

Before making this repository public:

* Remove `db.sqlite3` if it contains real data.
* Never commit passwords or API keys.
* Add `.env` to `.gitignore` if environment variables are used.
* Create a fresh superuser after cloning instead of sharing existing credentials.

---

# 🚀 Future Improvements

* Email Notifications
* Resume Matching
* Company Verification
* Interview Scheduling
* Job Recommendations
* Admin Analytics Dashboard
* REST API Integration
* JWT Authentication
* Docker Support
* PostgreSQL Integration
* AI-Based Resume Screening

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is intended for educational and learning purposes. You may modify and extend it according to your requirements.

---

# 👨‍💻 Author

**Abhinav Shetty**

* Information Science & Engineering Student
* Full Stack Developer
* Django Developer
* Java Programmer

If you found this project useful, consider giving it a ⭐ on GitHub.
