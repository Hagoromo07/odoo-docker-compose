# Use Odoo 14.0 official image as the base
FROM odoo:14.0

# Switch to root to perform administrative tasks
USER root

RUN apt-get update

# Update pip and install required Python packages
RUN python3 -m pip install --upgrade pip

COPY ./etc /etc/odoo
COPY ./enterprise-addons /mnt/enterprise-addons

# Switch back to the default odoo user
USER odoo

# Install required Python dependencies
RUN pip3 install -r /etc/odoo/requirements.txt