# School Management System

A custom Odoo 18 module for managing school operations, including students, staff, departments, academic years, subjects, and job positions.

## Overview

The School Management System is a custom Odoo module designed to organize and manage core school data through an integrated ERP workflow.

The project demonstrates the development of custom Odoo models, relational fields, views, sequences, security access, actions, menus, and business logic.

## Features

- Student Management
- Staff Management
- School Department Management
- Academic Year Management
- Subject Management
- Job Position Management
- Staff Number Generation
- Student Information Management
- Department Manager Assignment
- Relational Models using Many2one and One2many fields
- Custom Form and List Views
- Search Views
- Menu and Window Actions
- Access Rights and Security
- Computed Fields
- Data Validation and Business Logic

## Main Modules

### Students

Manage student information and related academic data.

### Staff

Manage school staff information, including:

- Full Name
- First Name
- Last Name
- Gender
- Date of Birth
- Age
- National ID
- Phone
- Email
- Staff Number

### Departments

Manage school departments and assign staff members as department managers.

### Academic Years

Create and manage academic years with automatically generated names.

### Subjects

Manage subjects used within the school system.

### Job Positions

Manage staff job positions and related information.

## Technical Stack

- Odoo 18
- Python
- XML
- PostgreSQL
- Odoo ORM
- QWeb
- Odoo Security & Access Rights

## Module Structure

```text
school_addons/
└── school_management/
    ├── models/
    ├── views/
    ├── security/
    ├── data/
    ├── __init__.py
    └── __manifest__.py
