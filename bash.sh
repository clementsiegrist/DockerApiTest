#!/bin/bash

# Build the images for the tests
docker build -t authentication_test ./auth
docker build -t authorization_test ./autho
docker build -t content_test ./content

# Start Docker Compose
docker-compose up
