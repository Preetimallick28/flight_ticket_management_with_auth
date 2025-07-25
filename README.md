# flight_ticket_management_with_auth
✈️ Flight Ticket Management System
A Django-based web application for managing flight ticket bookings with full authentication, admin control, and user-friendly interfaces.

🌟 Features
🔐 Authentication System

User registration, login, logout

Secure password hashing and session handling

🎟️ Ticket Booking

Search for flights by source, destination, and date

Book, view, and cancel tickets

📋 User Dashboard

View booking history

Download/print tickets

🛠️ Admin Features

Add/Edit/Delete flights

View all user bookings

📱 Responsive Design

Clean, mobile-friendly UI with HTML/CSS/Bootstrap

🛠 Tech Stack
Frontend: HTML, CSS, Bootstrap

Backend: Python, Django

Database: SQLite (can be configured for PostgreSQL/MySQL)

Authentication: Django built-in auth system

🖼️ Screenshots
You can upload these images to your GitHub repo or hosting and replace URL_TO_IMAGE with their direct URLs.

Page	Screenshot
🔐login form- <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/50ab6482-2a38-4a8f-bb8e-a9eae6579831" />

🧾 booking form - <img width="1913" height="846" alt="image" src="https://github.com/user-attachments/assets/0c1ffa61-ccc9-452c-b8d2-438350f56e72" />

🎟️ Ticket View	 - <img width="1915" height="857" alt="image" src="https://github.com/user-attachments/assets/f66b989b-e2cd-49af-aeea-68801e8cd360" />

📋 User Dashboard	 - <img width="1914" height="748" alt="image" src="https://github.com/user-attachments/assets/146a8362-f131-4f79-899b-cd289af65a57" />

🛫 Flight List	- <img width="1915" height="870" alt="image" src="https://github.com/user-attachments/assets/758ca4cd-ea9b-4ede-8c73-52e443575bd0" />

	

🚀 Getting Started
🔧 Installation Steps
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/flight-ticket-management.git
cd flight-ticket-management
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run database migrations:

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Create superuser:

bash
Copy
Edit
python manage.py createsuperuser
Run the development server:

bash
Copy
Edit
python manage.py runserver
Open your browser and visit:

cpp
Copy
Edit
http://127.0.0.1:8000
📁 Project Structure
cpp
Copy
Edit
flight_ticket/
├── flight_app/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
🚧 Future Scope
✅ Email confirmation for bookings

✅ PDF generation for tickets

✅ Payment gateway integration

✅ REST API support
