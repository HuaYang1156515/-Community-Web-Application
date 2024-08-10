-- Insert users (including admin and regular users)
INSERT INTO users (name, login, password, role, status, pic, description, created_at) VALUES
('Admin User', 'admin', 'admin', 'admin', '0', NULL, 'Administrator account', NOW()),
('John Doe', 'john_doe', '1558303a44eb61bf743bfaba62b72d555c82f2c7', 'user', '0', NULL, 'Regular user', NOW()),
('Jane Smith', 'jane_smith', '054581f81f87351dc64e15b38bffa079d263cb2a', 'user', '0', NULL, 'Regular user', NOW());

-- Insert categories
INSERT INTO categories (name, status) VALUES
('Party', '0'),
('Workshop', '0'),
('Seminar', '0');

-- Insert events
INSERT INTO events (name, description, location, date, status, created_by, category_id) VALUES
('Beach Party', 'Join us for a fun beach party!', 'Beach', '2024-08-15 18:00:00', '0', 2, 1),
('Python Workshop', 'Learn Python basics in this workshop.', 'Library', '2024-08-20 10:00:00', '0', 3, 2),
('Business Seminar', 'Networking and business development seminar.', 'Conference Hall', '2024-09-01 09:00:00', '0', 2, 3);

-- Insert event registrations
INSERT INTO event_registrations (event_id, user_id, status, created_at) VALUES
(1, 2, '0', NOW()),
(2, 3, '0', NOW()),
(3, 2, '0', NOW());

-- Insert favorites
INSERT INTO favorites (user_id, event_id, created_at) VALUES
(2, 1, NOW()),
(3, 2, NOW()),
(2, 3, NOW());
