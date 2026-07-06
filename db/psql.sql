create table users (id uuid primary key, f_name TEXT, l_name TEXT, age int check( age between 18 and 75), gender TEXT, city TEXT, mobile varchar(10), email TEXT, password TEXT, created_at timestamp not null default now(), role TEXT not null default 'user', constraint valid_role check (role in ('manager', 'employee', 'user')));

create table attendee_profile (attendee_id uuid primary key, points int check (points between 0 and 1000) not null default 0, foreign key(attendee_id) references users(id));

create table manager_profile (manager_id uuid primary key, organization TEXT not null, Bank_details jsonb not null, registartion_no varchar(12), license jsonb, foreign key(manager_id) references users(id));

create table employee_profile (employee_id uuid primary key, experiance jsonb not null, Bank_details jsonb not null, foreign key(employee_id) references users(id));

create table concerts (concert_id uuid primary key, manager_id uuid not null, artists jsonb not null, dt_concert timestamp not null, duration int check (duration between 1 and 8) default 1, description TEXT not null, contact TEXT, status TEXT check(status in ('live', 'ended', 'upcoming')), created_at timestamp default now(), foreign key(manager_id) references manager_profile(manager_id));

create table concert_tickets (tier_id uuid primary key, concert_id uuid, type TEXT default 'normal', cost int check (cost between 50 and 10000) default 50, description TEXT, points int check (points between 0 and 1000), foreign key(concert_id) references concerts(concert_id));

create table attendee_tickets (booking_id uuid primary key, user_id uuid, ticket jsonb not null, cost int check (cost >= 50) not null, qrcode bytea not null, foreign key(user_id) references users(id));
