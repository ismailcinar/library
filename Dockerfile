
# Pull base image
FROM python:3.10.2

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .




# FROM python:3.10.2
# ENV PYTHONUNBUFFERED 1
# RUN mkdir /code
# WORKDIR /code
# COPY ./requirements.txt ./requirements.txt

# RUN pip3 install --upgrade pip
# RUN pip3 install -r requirements.txt


# EXPOSE 8000
# ADD . /code
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]