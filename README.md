# YouTube Comment Sentiment Analyzer

## Table of Contents

- [Introduction](#introduction)  
- [Enabling APIs](#enabling-apis)  
- [Git Clone](#git-clone)  
- [Service Account Creation](#service-account-creation)  
- [Code Overview](#code-overview)  
- [Build and Deployment](#build-and-deployment)  
- [Git History](#git-history)  
- [Clean Up](#clean-up)  

---

## Introduction

This project analyzes YouTube comments for sentiment.  
By entering a YouTube video ID, it fetches comments using the YouTube Data API and evaluates their sentiment (positive, negative, or neutral) using Google Cloud's Natural Language API.  
This provides insights into how viewers are reacting to the content.

---

## Enabling APIs

Enable the required Google Cloud APIs:

gcloud services enable \
    youtube.googleapis.com \
    language.googleapis.com

## Git Clone

Clone this repository and enter the project directory:

git clone https://github.com/siddhanth2/cloud-goudernagpal-siddhan.git
cd cloud-goudernagpal-siddhan

---

## Service Account Creation

### Step 1: Create a service account

gcloud iam service-accounts create finalproject

### Step 2: Bind roles to the service account

gcloud projects add-iam-policy-binding ${GOOGLE_CLOUD_PROJECT} \
  --member="serviceAccount:finalproject@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com" \
  --role="roles/serviceusage.serviceUsageConsumer"

---

## Code Overview

- Accepts a YouTube video ID as input.
- Fetches comments using the **YouTube Data API**.
- Analyzes comment sentiment using **Google Cloud Natural Language API**.
- Outputs sentiment analysis: positive, negative, or neutral.


## Build and Deployment

### Step 1: Build Docker image using Google Cloud Build

gcloud builds submit --timeout=900 --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/final

### Step 2: Deploy to Cloud Run

gcloud run deploy final \
  --image gcr.io/${GOOGLE_CLOUD_PROJECT}/final \
  --service-account finalproject@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com \
  --set-env-vars API_KEY=<your_api_key>

> Replace `<your_api_key>` with your actual Google Cloud API key.

## Clean Up

To delete all Google Cloud resources used:

### Step 1: Delete the Cloud Run service

gcloud run services delete final

### Step 2: Delete the container image from Google Container Registry

gcloud container images delete gcr.io/${GOOGLE_CLOUD_PROJECT}/final

### Step 3: Remove IAM role from service account

gcloud projects remove-iam-policy-binding ${GOOGLE_CLOUD_PROJECT} \
  --member="serviceAccount:finalproject@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com" \
  --role="roles/serviceusage.serviceUsageConsumer"

### Step 4: Delete the service account

gcloud iam service-accounts delete finalproject@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com
