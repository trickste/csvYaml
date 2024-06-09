# Set working directory
FROM python:3.10-slim as builder

# Set working directory
WORKDIR /app/

# Copy requirements file
COPY ./requirements.txt .

# Install build dependencies
RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy setup script
COPY ./csvYaml .

RUN python3 setup.py bdist_wheel


# Second stage: Runtime environment
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy wheel file and req

COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /app/dist ./dist/


# Activate the virtual environment
ENV VIRTUAL_ENV /opt/venv
ENV PATH /opt/venv/bin:$PATH

# Install the wheel file
RUN pip install ./dist/*.whl

# Copy application code
COPY ./csvYaml/main.py ./templates/ ./

# Command to run the application
ENTRYPOINT ["python3", "main.py"]