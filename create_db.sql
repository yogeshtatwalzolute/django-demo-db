-- Run this as a PostgreSQL superuser (e.g. postgres):
--   psql -U postgres -f create_db.sql

CREATE USER django_user WITH PASSWORD 'yourpassword';
CREATE DATABASE django_demo OWNER django_user;
GRANT ALL PRIVILEGES ON DATABASE django_demo TO django_user;
