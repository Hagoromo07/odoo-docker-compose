# Odoo 14 with Docker Compose

This project provides a Docker Compose setup to run Odoo 14 with a PostgreSQL database.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

Follow these steps to set up and run Odoo 14 with Docker Compose.

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/odoo14-docker-compose.git
cd odoo14-docker-compose


2. Directory Structure
    Make sure your project directory contains the following structure:

    odoo14-docker-compose/
    ├── docker-compose.yml
    ├── config/
    │   └── (optional Odoo configuration files)
    └── addons/
        └── (optional custom addons)


3. Configuration

    The docker-compose.yml file is already set up to use the official Odoo 14 and PostgreSQL 13 images.
        web service runs the Odoo application.
        db service runs the PostgreSQL database.

4. Run the Services
    To start the services, run:

    sh: docker-compose up -d
    This command will:
        Download the required Docker images.
        Create and start the Odoo and PostgreSQL containers.

5. Access Odoo
    Once the services are up and running, you can access the Odoo web interface at:
    http://localhost:8014

6. Persistent Data
    The docker-compose.yml file includes volume definitions to persist Odoo and PostgreSQL data:
        Odoo data: odoo-web-data
        PostgreSQL data: odoo-db-data

7. Stopping the Services
    To stop the services, run:
    docker-compose down