# System Boundaries

## What It Does

- System allows authenticated users submit computational jobs of predefined types.
- System processes jobs asynchronously, and manage them along all their lifecycle.
- The system allows users to retrieve job status, timestamps, and result data. Internal retry mechanics are not exposed.
- System stores metadata to keep track and manage the jobs processing.
- System supports to cancel a job processing, unless job is finished or dead. If a cancel it's requested this should be the behavior:
	- If job is pending, it just becomes cancelled.
	- If job is running, interrupts the processing as if would have failed and becomes cancelled.
	- If job is failed, just becomes cancelled.
	- If job is finished or dead, cancel does nothing.

## What It Does Not Do

- System does not allow users to create the execution logic of a job.
- System does not allow users to create a new job types.
- System does not wait until a job is done to do a reply.
- Client users cannot configure retry limits, timeout values, or execution strategies.
- System should not let users modify or keep track of the orchestration of the jobs, neither its own jobs nor, and even less, the general jobs.

# User Roles

- **Client**: the user that will use the system via jobs processing requests and query his jobs state and results.

# Job Types 

- **Matrix multiplication**: generate two random matrices of nxn and performs basic matrix multiplication.
- **Prime computation**: compute the prime numbers up to the n-th prime number.
- **CSV aggregation**: generate adequate data related to the given aggregation option (mean, sum, group-by-simulation). 

# API Endpoints List

- GET /job <- returns only current user job
- GET /job/{job_id}
- POST /job
  POST /job/{job_id}/cancel

# Job Lifecycle Diagram

Diagram on docs/diagrams

# Database Schema Draft

Diagram on docs/diagrams

# Folder Structure Draft

```
backend-system-v1/
│
├── app/
│   ├── main.py
│   │
│   ├── api/
│   │   ├── router.py
│   │   └── dependencies.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── logging.py
│   │
│   ├── domain/
│   │   ├── job_status.py
│   │   └── exceptions.py
│   │
│   ├── models/
│   │   └── job_model.py
│   │
│   ├── schemas/
│   │   ├── job_request.py
│   │   └── job_response.py
│   │
│   ├── repository/
│   │   └── job_repository.py
│   │
│   ├── orchestration/
│   │   ├── job_service.py
│   │   ├── lifecycle_manager.py
│   │   └── retry_policy.py
│   │
│   ├── execution/
│   │   ├── executor_registry.py
│   │   ├── cpu_tasks.py
│   │   └── process_pool.py
│   │
│   └── db/
│       ├── base.py
│       ├── session.py
│       └── migrations/
│
├── tests/
│   ├── unit/
│   └── integration/
│
├── alembic/
├── requirements.txt
└── README.md
```

# Separation of Concerns

- API: manages all HTTP related concerns.
- orchestration: coordinates async jobs processing without blocking the main program flow.
- executor: it's responsible for doing the actual process of the job.
- DB: where all persistent data and metadata is stored.