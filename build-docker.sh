#!/usr/bin/env bash

DOCKER_ID_USER="zubrik"
IMAGE_NAME="event-generator:"
EPS="1"
TAG="eps"

docker buildx build --platform=linux/arm64 --no-cache -t "${DOCKER_ID_USER}/${IMAGE_NAME}${EPS}${TAG}" .