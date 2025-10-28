# Ticket-booking-system
TicketBoss – Real Time Event Ticket Management System

TicketBoss is a full web application that assists in managing event ticket reservations in real time. It looks and feels like an authentic professional ticket booking website but has simple to understand backend and frontend.

The primary intention of this project is to demonstrate how a Flask backend can be integrated with a good frontend designed using HTML, CSS, and JavaScript. Users are able to easily book seats for an event, cancel the booking based on the reservation ID, and can view updated summary of available and total seats.

Each operation in the project provides real time feedback to the user in the form of on screen hints and toast messages. The summary area is  updated dynamically, displaying the real time status of reservations without page reloading for every 10 seconds. This turns the application into a more interactive and real world system like application.

The project is built on a REST API structure, where everything is inJSON format. Without using complex databases, the system stores the reservation information in a plain local file, which makes it easy and simple to execute on any computer.

Visually, the dashboard has a clear and modern design. It features glass style cards, soft shadows, and responsive elements that looks good on both desktop and mobile devices. The interface shows all primary operations reserve, cancel, and summary in a single view, providing users with a good experience.

TicketBoss is perfect for starters who need to learn how APIs relate to frontend web pages, as well as for those learning to create real-time apps. It's also a brilliant example of how simplicity and good design can come together to produce a professional and useful project.

Install dependencies:

pip install flask flask-cors

Run the server:

python app.py

Open index.html in your browser to use the web page.

Api end points: Reserve seats,cancle reservaration,get summary.

Technical Details

Backend: Flask (Python)

Frontend: HTML, CSS, JavaScript

Storage: Local data.json file
