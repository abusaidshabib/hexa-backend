# Setting Up a Django Project

This guide walks you through the process of settings up a new Django project from scratch

## Prerequisites
- Python installed (version 3.8 or higher recommended)
- pip (Python package manager)
- Virtualenv (optional but recommended)

## Step 1: Install Django
1. Open your terminal/command prompt
2. (Optional) Create and activate a virtual environment:

## Step 2: command to create database on postgres sql

CREATE DATABASE hexadrf;
CREATE ROLE hexadrf WITH LOGIN PASSWORD 'hexadrf';
GRANT ALL PRIVILEGES ON DATABASE hexadrf TO hexadrf;
ALTER DATABASE hexadrf OWNER TO hexadrf;

## Step 3: Create env file with all important variable

```bash



# Create virtual environment
# python -m venv myenv

# Activate (Windows)
# myenv\Scripts\activate

# Activate (Mac/Linux)
# source myenv/bin/activate


# django-admin startproject hexadrf

