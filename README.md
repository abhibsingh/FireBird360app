# Appium Test Automation

This repository contains automated UI tests for the Artist360 Android application using Appium and Python.

## Prerequisites
- Docker and Docker Compose
- Android APK file locally available

## Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. Create and configure your environment file:
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env file with your local APK path
# Example for macOS:
# APK_PATH=/Users/username/Downloads/app-dev-release.apk
# Example for Windows:
# APK_PATH=C:/Users/username/Downloads/app-dev-release.apk
# Example for Linux:
# APK_PATH=/home/username/downloads/app-dev-release.apk
```

3. Build and run using Docker:
```bash
docker-compose build
docker-compose up
```

## Important Notes
- The APK_PATH must be an absolute path to your APK file
- Ensure the APK file exists at the specified path
- The path must be accessible to Docker
- For Windows users, use forward slashes (/) in the path

## Troubleshooting
If you encounter errors:
1. Verify your APK path is correct in .env file
2. Ensure Docker has permission to access the APK location
3. Check that the APK file exists and is readable 