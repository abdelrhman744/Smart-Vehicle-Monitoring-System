# Smart Vehicle Monitoring System

An AI-powered vehicle monitoring and analytics platform built with Computer Vision, FastAPI, Next.js, and PostgreSQL.

The Smart Vehicle Monitoring System aims to automatically detect vehicles in video footage, recognize license plates, classify vehicle types, identify vehicle colors, track vehicle movement, and estimate vehicle speed.

The platform combines a Python-based Computer Vision pipeline with a modern web application to provide a centralized dashboard for reviewing vehicle records and analyzing traffic data.

**Project Status:** Under Development

---

## Overview

The system is designed to process video footage from surveillance cameras and extract useful information about passing vehicles.

For each detected vehicle, the system aims to collect:

- Vehicle detection and classification.
- License plate detection and recognition.
- Vehicle color identification.
- Vehicle tracking across video frames.
- Vehicle speed estimation.
- Entry time recording.
- Persistent storage of vehicle records.
- A web dashboard for reviewing and searching records.

The project is being developed with local deployment in mind, allowing video processing and data storage to run on an organization's own infrastructure without relying on external AI APIs.

## Features

### Vehicle Detection and Classification

- Detect vehicles in video frames using YOLO-based object detection.
- Extract vehicle regions for further analysis.
- Classify detected vehicles into supported categories.
- Return detection results with bounding boxes and confidence scores.

### License Plate Recognition

- Detect license plate regions.
- Apply image preprocessing when necessary.
- Extract plate text using an Optical Character Recognition (OCR) engine.
- Associate recognized plate text with the corresponding vehicle.

### Vehicle Color Detection

- Analyze vehicle image regions using OpenCV.
- Use HSV color analysis and color clustering to estimate dominant colors.
- Map the results to supported color categories.

### Vehicle Tracking

- Track detected vehicles across consecutive video frames.
- Assign tracking IDs to distinguish vehicles during processing.
- Associate detection and recognition results with tracked vehicles.

### Speed Estimation

- Analyze vehicle movement across video frames.
- Estimate vehicle speed when suitable camera calibration and scene measurements are available.

Accurate real-world speed estimation requires appropriate camera calibration. Optical flow or pixel displacement alone does not directly provide speed in km/h.

### Web Dashboard

The web interface is planned to provide:

- Vehicle statistics and summary cards.
- Video upload and processing status.
- A searchable table of detected vehicles.
- Vehicle details, including plate number, type, color, and estimated speed.
- Entry timestamps and associated vehicle images.

### Local Deployment

The system is designed to support on-premises deployment, with local model inference and database storage, avoiding dependencies on external AI APIs.

## System Architecture

The project is organized into three main application layers.

```text
                 Next.js Frontend
                        |
                     REST API
                        |
                  FastAPI Backend
                        |
              Video Processing Layer
                        |
          +-------------+-------------+
          |             |             |
     Plate OCR    Vehicle Models    Tracking
          |             |             |
          +-------------+-------------+
                        |
                    PostgreSQL
```

### Processing Workflow

1. A user uploads a video through the web dashboard.
2. The backend creates a processing job.
3. The Computer Vision pipeline analyzes the video frames.
4. Detected vehicles are tracked and analyzed.
5. Extracted information is associated with each vehicle.
6. Results are stored in PostgreSQL.
7. The frontend retrieves and displays the results.

The processing layer may execute independent analysis tasks concurrently where appropriate.

## Tech Stack

| Component | Technologies |
|---|---|
| Frontend | Next.js, React, TypeScript |
| UI Styling | Tailwind CSS |
| Backend | Python, FastAPI |
| Computer Vision | OpenCV |
| Object Detection | YOLO |
| OCR | Local OCR engine |
| Classification | PyTorch or a compatible inference framework |
| Tracking | ByteTrack or another suitable tracking algorithm |
| Database | PostgreSQL |
| API Communication | REST API |
| Version Control | Git and GitHub |
| Deployment Target | On-Premises / Local Environment |

The final selection of models and libraries may evolve during development.

## Project Structure

The repository is expected to follow a modular structure similar to the following:

```text
Smart-Vehicle-Monitoring-System/
|
|-- backend/
|   |-- app/
|   |   |-- api/
|   |   |   |-- routes/
|   |   |-- core/
|   |   |-- models/
|   |   |-- schemas/
|   |   |-- services/
|   |   |-- database/
|   |   |-- main.py
|   |-- tests/
|   |-- requirements.txt
|   |-- .env.example
|
|-- frontend/
|   |-- app/
|   |-- components/
|   |-- lib/
|   |-- public/
|   |-- package.json
|
|-- computer_vision/
|   |-- vehicle_detection/
|   |-- vehicle_classification/
|   |-- license_plate_recognition/
|   |-- color_detection/
|   |-- tracking/
|   |-- speed_estimation/
|
|-- data/
|   |-- .gitkeep
|
|-- docs/
|
|-- .gitignore
|-- README.md
```

This is a proposed structure. Directories and files will be added as the corresponding components are implemented.

## Getting Started

### Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.11 or another version supported by the selected dependencies.
- Node.js LTS.
- npm.
- PostgreSQL.
- Git.

The exact requirements will be documented as development progresses.

### Clone the Repository

```bash
git clone https://github.com/abdelrhman744/Smart-Vehicle-Monitoring-System.git

cd Smart-Vehicle-Monitoring-System
```

### Backend Setup

Create and activate a Python virtual environment.

```bash
cd backend

python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\activate
```

On Linux or macOS:

```bash
source .venv/bin/activate
```

Install the dependencies once `requirements.txt` is available.

```bash
pip install -r requirements.txt
```

Configure the required environment variables using the project's `.env.example` file.

Start the development server once the FastAPI application is implemented.

```bash
uvicorn app.main:app --reload
```

The API documentation will be available at:

```text
http://127.0.0.1:8000/docs
```

### Frontend Setup

Open another terminal and run:

```bash
cd frontend

npm install

npm run dev
```

Open the local development address displayed by Next.js, typically:

```text
http://localhost:3000
```

### Database Setup

Create a PostgreSQL database and configure the connection string in the backend environment variables.

Database migrations and initialization instructions will be added when the database schema is finalized.

These instructions describe the intended development workflow and may require adjustments until the initial application structure and dependencies are committed.

## Planned API Endpoints

The following endpoints describe the intended API design.

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/videos` | Upload a video and initiate processing |
| GET | `/api/jobs/{job_id}` | Retrieve processing job status |
| GET | `/api/vehicles` | Retrieve vehicle records |
| GET | `/api/vehicles/{vehicle_id}` | Retrieve a vehicle record |
| GET | `/api/stats` | Retrieve dashboard statistics |

Additional endpoints may be introduced for filtering, pagination, and accessing stored vehicle images.

## Team and Responsibilities

The project is being developed collaboratively by a four-person team.

| Team Member | Responsibility |
|---|---|
| Ahmed | Vehicle Detection and Classification |
| Abd El-Shafy | License Plate Recognition and Color Detection |
| Abdo | Vehicle Tracking and Speed Estimation |
| Project Maintainer | FastAPI Backend, Next.js Frontend, and Integration |

Each team member is responsible for implementing and testing their assigned components and integrating changes through GitHub Pull Requests.

## Development Workflow

We use Git and GitHub to collaborate and manage changes.

### Branching Strategy

Each contributor should work on a dedicated branch rather than committing directly to `main`.

Suggested branch names:

```text
main
ahmed/vehicle-classification
abdelsafy/license-plate
abdo/tracking
backend-frontend
```

### Contribution Steps

1. Pull the latest changes from `main`.
2. Create or update your assigned branch.
3. Implement your task.
4. Test your changes locally.
5. Commit your changes with a descriptive message.
6. Push your branch to GitHub.
7. Open a Pull Request targeting `main`.
8. Review and merge the changes after approval.

Contributors should not commit directly to `main`.

## Privacy and Security

The project is designed for local processing and on-premises deployment.

Our intended approach includes:

- Running Computer Vision models locally.
- Storing application data in a locally hosted PostgreSQL database.
- Avoiding external AI APIs for image and video analysis.
- Keeping credentials and environment-specific configuration out of source control.
- Restricting access to vehicle records and uploaded media.

A fully offline deployment will also require installing dependencies and obtaining model weights in advance, then verifying that runtime components do not require external network access.

## Roadmap

- [ ] Set up the project structure and development environment.
- [ ] Implement vehicle detection.
- [ ] Implement vehicle classification.
- [ ] Implement license plate recognition.
- [ ] Implement vehicle color detection.
- [ ] Implement vehicle tracking.
- [ ] Implement calibrated speed estimation.
- [ ] Build the FastAPI backend.
- [ ] Design the PostgreSQL database schema.
- [ ] Build the Next.js dashboard.
- [ ] Integrate the Computer Vision pipeline with the backend.
- [ ] Add vehicle search and historical records.
- [ ] Test the system using recorded video footage.
- [ ] Optimize processing performance.
- [ ] Validate fully offline deployment.

## Project Goals

The main goals of this project are to:

- Build an end-to-end Computer Vision application.
- Explore vehicle detection, recognition, and tracking.
- Develop a modular Python processing pipeline.
- Integrate AI capabilities into a web application.
- Practice collaborative development using Git and GitHub.
- Explore local deployment without external AI APIs.

## License

A license has not yet been selected. Until one is added to the repository, all rights remain with the respective copyright holders.

---

Built with Python, Computer Vision, FastAPI, Next.js, and PostgreSQL.
