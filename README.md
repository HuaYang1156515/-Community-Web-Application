#  Community Web Application

## Introduction
The Community Event Planner Web Application is designed to support users organize, manage, and participate in their community events. It provides an easy-to-use platform where users can register, create events, view event details, and engage with their local community. This guide will walk you through the main features of the application.

## Features
- A web application for managing community events, with roles for admins, users, and guests, each with specific access permissions.
- User Registration and Login: Create an account to access personalized features, such as event creation and management.
- Event Creation: Users can create new events, set event details (name, location, date, etc.), and share them with the community.
- Event Registration: View and register for upcoming events.
- Favorites: Mark events as favorites to easily find them later.

## Getting Start
Visit the homepage and **register** by filling in your details, then **log in** using your password. Once logged in, you can create events by clicking **Create Event**, filling in event details, and submitting. To view or register for events, go to the **Events** page, select an event, and click **Join**. You can favorite events by clicking the **Favorite** button. Manage your profile by clicking **Profile**, where you can view or edit your information. To log out, simply click **Logout** in the top-right corner. For further assistance, contact support@communityeventplanner.com.





## Project Structure

The project follows the following directory structure:

- **/static:** Contains static files such as CSS, JS, and images.
- **/templates:** Holds HTML templates for rendering views.
- **app.py:** The main entry point for the Flask application.
- **/config:** Configuration files and settings.
- **/services:** Modules for various services, including user, workshop, and payment services.
- **/controllers:** Contains controllers for different functionalities like authentication and managing different user roles.
- **/tests:** Unit tests for different components of the application.
- **/common:** Common functionalities shared across the application.
- **requirements.txt:** Lists the required Python packages.
- **README.md:** This file, providing an overview of the project.

- community_event_planner/
   
  - config/
      - _init_.py 
      - connect.py
      - setting.py
  - controllers/
      - category_controller.py
      - user_controller.py
      - admin_controller.py
      - event_controller.py
  - models/
      - user_model.py
      - event_registration_model.py
      - event_model.py
      - favorite_model.py
      - category_model.py      
  - services/
      - _init_.py
      - user_service.py
      - event_service.py
      - admin_service.py
      - app_service.py
      - category_service.py
      - DbText.py
  - static/
      - css/
      - js/
      - images/
  - templates/
      - admin
        - admin_dashboard.html
        - base.html
        - dashboard.html
        - /category
        - /event
        - users
      - front
        - base.html
        - home.html
        - profile.html
        - login.html
        - /event
        - /help
  - .gitignore
  - app.py
  - config.py
  - requirements.txt
