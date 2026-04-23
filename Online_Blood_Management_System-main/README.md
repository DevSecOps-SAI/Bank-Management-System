# Online_Blood_Management_System



A role-based blood bank management system built with **Django** and **MySQL**, allowing **Admins**, **Donors**, and **Patients** to manage and access blood stock, donation, and request workflows.

---

##  Live Roles Overview

###  Admin
- View dashboard with total units, requests, donations, and users
- Manage **blood stock**: update quantities for all blood groups
- Manage **donors** and **patients**: view, edit, delete profiles
- Approve or reject **donation records**
- Approve or reject **patient requests** based on stock availability
- View request history

###  Donor
- Upload donation requests
- Track donation status
- View donation history

###  Patient
- Request specific blood groups and units
- Track request status (Approved, Rejected, Pending)

---

##  Features

-  **Authentication**: Separate dashboards and login redirects for each role
-  **Inventory Management**: View and update live blood stock (Admin)
-  **Donor Management**: Add, update, and delete donor details
-  **Patient Request Handling**: Admin approval/rejection logic based on availability
-  **Donation Approval**: Accept/reject donor donations and update stock
-  **Real-Time Dashboard**: For Admin, with detailed counts and summaries

---

##  Technologies Stack

- **Backend**: Django 5.2
- **Database**: MySQL
- **Frontend**: HTML, Bootstrap, Django Templates
- **Authentication**: Django `auth` with `Group`-based role check
- **Image & File Handling**: Pillow
- **Widgets**: `django-widget-tweaks`

---

##  Setup Instructions

### 1. Clone the Repository
bash
`git clone https://github.com/your-username/blood-management-system.git` <br>
`cd blood-management-system`

### 2. Create Virtual Environment
bash
`python3 -m venv venv` <br>
`source venv/bin/activate`   # or venv\Scripts\activate on Windows

### 3. Install Dependencies
bash
`pip install -r requirements.txt`

### 4. Run Migrations
bash
`python manage.py makemigrations` <br>
`python manage.py migrate` 
### 6. Create Superuser (Admin)
bash
`python manage.py createsuperuser`

### 7. Run the Server
bash
`python manage.py runserver` <br>
Then open http://localhost:5000 in your browser.



##  Contributors

| Name | GitHub |
|------|--------|
| A Sai Vara Prasad Reddy | [@ASVPGitHub](https://github.com/ASVPREDDY) | 
| N Paul Prasanna Kumar | [@PaulGitHub](https://github.com/Paul9441) |
| G Shyam | [@ShyamGitHub](https://github.com/gangolashyam) |
|C H Rajesh |
|M D Numan |
| Puthenveettil Prasannan Ashwin | [@AshwinGitHub](https://github.com/yourusername) |


