create table users (id uuid primary key, f_name TEXT, l_name TEXT, age int check( age between 18 and 75), gender TEXT, city TEXT, mobile varchar(10), email TEXT, password TEXT, created_at timestamp not null default now(), role TEXT not null default 'user', constraint valid_role check (role in ('manager', 'employee', 'user')));

create table attendee_profile (attendee_id uuid primary key, points int check (points between 0 and 1000) not null default 0, foreign key(attendee_id) references users(id));

create table manager_profile (manager_id uuid primary key, organization TEXT not null, Bank_details jsonb not null, registartion_no varchar(12), license jsonb, foreign key(manager_id) references users(id));

create table employee_profile (employee_id uuid primary key, experiance jsonb not null, Bank_details jsonb not null, foreign key(employee_id) references users(id));
