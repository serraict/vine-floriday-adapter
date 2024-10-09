# Vine-Floriday Adapter: Software Architecture

## 1. Introduction

The Vine-Floriday Adapter is a software solution designed to retrieve trade information from the Floriday platform, allowing suppliers to analyze their quotations, orders, and catalogs locally. This document outlines the high-level architecture of the system, its main components, and the technologies used.

## 2. System Overview

The system is primarily built using Python and consists of several key components that work together to fetch, process, and store data from the Floriday platform.

## 3. Main Components

### 3.1 Data Retrieval Module

- Located in: `src/floridayvine/floriday/`
- Purpose: Interfaces with the Floriday API to fetch trade information.
- Key files:
  - `misc.py`: Contains miscellaneous functions for interacting with Floriday.

### 3.2 Data Processing Module

- Located in: `src/floridayvine/`
- Purpose: Processes and transforms the data retrieved from Floriday.
- Key files:
  - `__main__.py`: Entry point for the application, orchestrates the overall process.

### 3.3 Persistence Module

- Located in: `src/floridayvine/`
- Purpose: Handles data storage and retrieval from the local database.
- Key files:
  - `persistence.py`: Manages database operations.

### 3.4 MinIO Integration

- Located in: `src/floridayvine/`
- Purpose: Potentially handles object storage, based on the presence of `minio.py`.
- Key files:
  - `minio.py`: Likely contains functions for interacting with MinIO object storage.

## 4. Data Flow

1. The Data Retrieval Module fetches trade information from the Floriday API.
2. The Data Processing Module transforms and prepares the data for storage.
3. The Persistence Module stores the processed data in the MongoDB database.
4. (Optional) The MinIO Integration may be used for storing larger objects or files.

## 5. Technologies and Frameworks

- **Programming Language**: Python
- **Database**: MongoDB
  - Chosen for its flexibility and potential integration with Dremio data lake solution.
- **API Integration**: Custom implementation for Floriday API
- **Object Storage**: Potential use of MinIO (to be confirmed)
- **Containerization**: Docker (as evidenced by Dockerfile and docker-compose.yml)
- **Version Control**: Git

## 6. Deployment and Execution

- The application is containerized using Docker, allowing for easy deployment and scaling.
- A cron job (`floridayvine-crontab` and `floridayvine-cronjob/`) is set up for scheduled execution of the data retrieval and processing tasks.

## 7. Testing

- Located in: `tests/`
- Includes unit tests for various components of the system.
- Key test files:
  - `test_can_run_script.py`
  - `test_floriday.py`
  - `test_upload_files_to_vine.py`

## 8. Configuration and Environment

- Environment variables are used for configuration (`.env.example`).
- Python version is managed using `.python-version`.

## 9. Future Considerations

- The architecture is designed to be flexible, allowing for potential integration with other data lake solutions compatible with MongoDB.
- The modular structure allows for easy expansion to include additional data sources or processing capabilities.

## 10. Conclusion

The Vine-Floriday Adapter provides a robust solution for retrieving and locally storing trade information from the Floriday platform. Its modular architecture and use of modern technologies ensure scalability and maintainability for future enhancements.
