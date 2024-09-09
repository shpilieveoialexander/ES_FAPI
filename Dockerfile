# This is base dockerfile which helps to reduce images memory size
# Build image from python v3.11
FROM python:3.11

LABEL developer="Alexsandr Shpilevoy <shpilevoy29@gmail.com>"

# Remove apt cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Set workdir in future container
WORKDIR /backend/

# Copy file requirements.txt with Python dependencies
COPY ./requirements.txt /backend/

# Install Python dependencies
RUN pip install -r requirements.txt