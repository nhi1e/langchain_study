-- Drop existing tables if they exist
DROP TABLE IF EXISTS support_tickets;
DROP TABLE IF EXISTS users;

-- Create users table
CREATE TABLE users (
    user_id TEXT PRIMARY KEY,
    name TEXT,
    email TEXT
);

-- Create support_tickets table
CREATE TABLE support_tickets (
    ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    issue TEXT,
    category TEXT,
    status TEXT,
    priority TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Insert mock users
INSERT INTO users (user_id, name, email) VALUES
    ('u001', 'Alice Smith', 'alice@example.com'),
    ('u002', 'Bob Johnson', 'bob@example.com'),
    ('u003', 'Carlos Nguyen', 'carlos@example.com'),
    ('u004', 'Diana Patel', 'diana@mail.com'),
    ('u005', 'Ethan Brown', 'ethan@mail.com');

-- Insert mock support tickets
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u005', 'Cannot print', 'Software', 'Resolved', 'High', '2025-05-04 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u002', 'App crashes on launch', 'Security', 'Resolved', 'Medium', '2025-05-17 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u003', 'Keyboard not working', 'Network', 'Escalated', 'High', '2025-05-14 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u002', 'Cannot print', 'Email', 'Escalated', 'Low', '2025-06-04 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u003', 'Microphone not detected', 'Account Access', 'Escalated', 'Low', '2025-04-03 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u005', 'Can't access shared drive', 'Security', 'Escalated', 'Low', '2025-04-01 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u003', 'VPN not working', 'Security', 'In Progress', 'Low', '2025-04-22 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u005', 'Zoom not connecting', 'Software', 'In Progress', 'High', '2025-05-22 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u004', 'App crashes on launch', 'Network', 'Escalated', 'High', '2025-05-17 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u004', 'Zoom not connecting', 'Security', 'In Progress', 'Medium', '2025-05-18 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u003', 'Microphone not detected', 'Email', 'Escalated', 'High', '2025-04-19 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u004', 'Account locked', 'Network', 'In Progress', 'High', '2025-05-13 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u005', 'Two-factor auth failed', 'Security', 'Escalated', 'Low', '2025-05-18 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u005', 'Screen flickering', 'Security', 'In Progress', 'Low', '2025-04-27 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u001', 'Mouse freezing', 'VPN', 'Escalated', 'High', '2025-05-10 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u002', 'Keyboard not working', 'Hardware', 'Open', 'Low', '2025-05-06 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u001', 'Laptop overheating', 'Software', 'Open', 'Low', '2025-04-26 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u003', 'Can't access shared drive', 'Network', 'Escalated', 'Low', '2025-04-27 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u001', 'Laptop overheating', 'Software', 'Open', 'High', '2025-06-08 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u001', 'Cannot print', 'Security', 'In Progress', 'Medium', '2025-05-24 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u002', 'VPN not working', 'VPN', 'In Progress', 'Low', '2025-06-23 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u003', 'Zoom not connecting', 'Security', 'Escalated', 'Low', '2025-05-16 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u005', 'Screen flickering', 'Account Access', 'Open', 'Medium', '2025-05-01 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u003', 'Email not syncing', 'Hardware', 'In Progress', 'Medium', '2025-05-17 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u001', 'Mouse freezing', 'Account Access', 'In Progress', 'High', '2025-06-20 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u005', 'Screen flickering', 'Email', 'Escalated', 'High', '2025-06-21 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u001', 'Account locked', 'Network', 'In Progress', 'High', '2025-05-16 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u005', 'Software update stuck', 'Account Access', 'Resolved', 'Medium', '2025-04-29 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u002', 'Laptop overheating', 'Hardware', 'Escalated', 'Medium', '2025-04-26 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u005', 'VPN not working', 'Network', 'Open', 'Low', '2025-06-25 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u005', 'Cannot print', 'Security', 'Escalated', 'Medium', '2025-06-22 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u003', 'Slow internet', 'Email', 'Escalated', 'Low', '2025-05-17 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u004', 'Microphone not detected', 'VPN', 'Escalated', 'High', '2025-05-17 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u005', 'Can't access shared drive', 'Account Access', 'In Progress', 'Medium', '2025-04-06 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u005', 'Can't access shared drive', 'Security', 'Escalated', 'Medium', '2025-05-23 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u002', 'Can't access shared drive', 'Software', 'In Progress', 'Low', '2025-04-20 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u002', 'App crashes on launch', 'Hardware', 'In Progress', 'High', '2025-06-19 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u003', 'Cannot print', 'Account Access', 'Escalated', 'Medium', '2025-06-14 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u003', 'Software update stuck', 'VPN', 'In Progress', 'High', '2025-04-07 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u001', 'Forgot password', 'Email', 'Open', 'Medium', '2025-04-20 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u004', 'Zoom not connecting', 'Account Access', 'Open', 'Low', '2025-06-17 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u001', 'Two-factor auth failed', 'Network', 'In Progress', 'Medium', '2025-04-09 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u005', 'Laptop overheating', 'Network', 'Resolved', 'High', '2025-04-15 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u001', 'Keyboard not working', 'Hardware', 'Resolved', 'High', '2025-05-31 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u003', 'Mouse freezing', 'Email', 'Open', 'High', '2025-04-06 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u005', 'Laptop overheating', 'Hardware', 'Resolved', 'Medium', '2025-04-23 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u002', 'Screen flickering', 'Security', 'In Progress', 'Medium', '2025-04-27 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u005', 'Can't access shared drive', 'Hardware', 'Resolved', 'High', '2025-05-08 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u003', 'Zoom not connecting', 'Network', 'In Progress', 'High', '2025-04-07 06:40:08');
INSERT INTO support_tickets (user_id, issue, category, status, priority, updated_at) VALUES ('u003', 'Laptop overheating', 'Network', 'In Progress', 'Medium', '2025-04-01 06:40:08');