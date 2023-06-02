# API Testing Project

This project contains a series of tests for a FastAPI application. The application has endpoints for user authentication, authorization, and sentiment analysis.

## Getting Started

You need Docker and Docker Compose to run the tests. To get started, build the images with the `setup.sh` script:

```bash
bash setup.sh
```

This script builds the Docker images for the tests and then starts the containers with Docker Compose.

## Tests

There are three tests:

    1. Authentication test (authentificaton.py): This test checks the /permissions endpoint with valid and invalid user credentials.

    2. Authorization test (authorize.py): This test checks the /v1/sentiment and /v2/sentiment endpoints to ensure users have the correct permissions.

    3. Content test (content.py): This test checks the sentiment analysis model's responses.

Each test runs in its own Docker container, as defined in the docker-compose.yml file.

## Design Choices

This project uses Docker to ensure that tests run in a consistent environment. Each test runs in its own container to isolate the test environments and improve the reproducibility of the tests.

The tests are written in Python, using the requests library to send HTTP requests to the API.

The logs from the tests are written to a api_test.log file. This is done by setting the LOG environment variable to 1 in the docker-compose.yml file.

