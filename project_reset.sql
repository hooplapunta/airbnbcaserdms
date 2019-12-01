\connect postgres

drop database if exists project;
create database project;

\connect project;

\i project_create.sql

\i project_load.sql
