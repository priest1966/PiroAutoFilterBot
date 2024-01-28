FROM python:3.10-slim-buster

# Create a non-root user
RUN useradd -ms /bin/bash pirouser

# Update and install dependencies
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y git build-essential

WORKDIR /PiroAutoFilterBot
# Copy requirements file separately and install dependencies
COPY requirements.txt /PiroAutoFilterBot/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Set ownership of the application directory to the non-root user
RUN chown -R pirouser:pirouser /PiroAutoFilterBot

# Switch to the non-root user
USER pirouser

CMD ["python3", "bot.py"]