FROM ubuntu:latest

WORKDIR /usr/app/src

ARG LANG="en_US.UTF-8"

# Download and install Dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       locales \
       python3-pip \
       python3-yaml \
       python3-venv \
       build-essential \
       libatlas-base-dev \
       libjpeg-dev \
       libpng-dev \
       rsyslog \
       systemd \
       systemd-cron \
       sudo \
    && apt-get clean \
    && locale-gen $LANG

# Set the locale
ENV LANG=${LANG}
ENV LANGUAGE=${LANG}
ENV LC_ALL=${LANG}

# Copy the requirements file from the current directory
COPY requirements.txt ./

# Create a virtual environment
RUN python3 -m venv /usr/app/venv

# Upgrade pip and setuptools in the virtual environment
RUN /usr/app/venv/bin/pip install --upgrade pip setuptools

# Install Python dependencies from requirements.txt in the virtual environment
RUN /usr/app/venv/bin/pip install -r requirements.txt

# Copy the entire contents of the current directory
COPY . .

# Set the PATH to include the virtual environment's binaries
ENV PATH="/usr/app/venv/bin:$PATH"

# Expose the port for Streamlit
EXPOSE 8501

# Tell the image what to do when it starts as a container
CMD ["streamlit", "run", "1_🏠_Home.py"]