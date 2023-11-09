FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /api

# Copy first api requirements to leverage cache
COPY ./api/requirements.txt /api/requirements.txt

# Install required python libraries
RUN pip install -r requirements.txt

# Install Spacy model
RUN python -m spacy download en_core_web_sm

# Copy current directory inside root directory of the container
ADD ./api /api

# Run Flask application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]