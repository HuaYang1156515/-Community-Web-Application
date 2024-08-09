Community Web Application

Overview
The project focuses on developing a web-based application designed to promote community service and engagement by organizing and managing events. The application will serve the local community and allow users to seamlessly create, view and register for local events.

Features
A web application for managing community events, with roles for admins, users, and guests, each with specific access permissions.
Applied hashing and vaildation

Structure
community_event_planner/
      common/
          hashing.py
          validation.py
      config/
          connect.py
          setting.py
      controllers/
          guest_controller.py
          user_controller.py
          admin_controller.py
      models/
          user.py
          event.py
          booking.py
      services/
          app_service.py
          user_service.py
          event_service.py
          admin_service.py
      static/
          css/
          js/
          images/
      templates/
          base.html
          home.html
          login.html
          register.html
          event_list.html
          event_detail.html
          create_event.html
          edit_event.html
          user_profile.html
          admin_dashboard.html
      tests/
          test_user.py
          test_event.py
      .gitignore
      app.py
      config.py
└     requirements.txt
