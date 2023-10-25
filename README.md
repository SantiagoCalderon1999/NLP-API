# NLP-API

## Overview

This project is a Named Entity Recognition (NER) API that utilizes spaCy for natural language processing, Flask as a web framework, and Google Cloud Build and Google Cloud Run for deployment. Named Entity Recognition is a crucial task in NLP that identifies and categorizes entities (e.g., names, dates, locations) within text.


# Dependencies:

- **spaCy:** Used for Named Entity Recognition. You'll need to train or use pre-trained models for entity recognition.

- **Flask:** A lightweight web framework for creating the API endpoints and handling HTTP requests.

- **Google Cloud Build:** CI/CD pipeline for building and packaging the API for deployment.

- **Google Cloud Run:** Serverless platform for deploying and running the API in a scalable, containerized environment.

## Setup
Before using the API, you need to set up your development environment and prepare the NER model.

### Clone the Repository:

```bash
$ pip install -r requirements.txt
```

### Install Dependencies:

```bash
$ pip install -r requirements.txt
```


## Deployment

This repo includes a CD pipeline in Cloud Build, which deploys the API to Cloud Run. The service can be consumed using the following url: https://nlp-api-h4zydlqkdq-uc.a.run.app/
