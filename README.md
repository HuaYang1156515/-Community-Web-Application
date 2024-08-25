#  Community Web Application

## Overview
The project focuses on developing a web-based application designed to promote community service and engagement by organizing and managing events. The application will serve the local community and allow users to seamlessly create, view and register for local events.

## Features
- A web application for managing community events, with roles for admins, users, and guests, each with specific access permissions.
- Applied hashing and vaildation.
- Event management with dynamic templates.

## Project Structure

The project follows the following directory structure:

- **/static:** Contains static files such as CSS, JS, and images.
- **/templates:** Holds HTML templates for rendering views.
- **app.py:** The main entry point for the Flask application.
- **/config:** Configuration files and settings.
- **/services:** Modules for various services, including user, workshop, and payment services.
- **/controllers:** Contains controllers for different functionalities like authentication and managing different user roles.
- **/tests:** Unit tests for different components of the application.
- **/common:** Common functionalities shared across the application, such as hashing functions.
- **requirements.txt:** Lists the required Python packages.
- **README.md:** This file, providing an overview of the project.

- community_event_planner/
  - common/
      - hashing.py
      - validation.py
  - config/
      - _init_.py
      - connect.py
      - setting.py
  - controllers/
      - guest_controller.py
      - user_controller.py
      - admin_controller.py
  - models/
      - category_model.py
      - event_model.py
      - event_registration_model.py
      - favorite_model.py
      - user_model.py
  - services/
      - _init_.py
      - user_service.py
      - app_service.py
      - admin_service.py
      - category_servise.py
      - DbText.py
      - event_service.py
  - static/
      - css/
      - icomoon
      - tmpls
      - js/
      - images/
  - templates/
      - admin/
      - front/
      - base.html
      - home.html
      - login.html
      - register.html
      - event_list.html
      - event_detail.html
      - event_dashboard.html
      - create_event.html
      - edit_event.html
      - profile.html
      - admin_dashboard.html
  - tests/
      - test_user.py
      - test_event.py
  - .gitignore
  - app.py
  - community_planner_schema.sql
  - insertdb.sql
  - config.py
  - readme.md
  - requirements.txt
