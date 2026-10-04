# Patient Management API

A simple and beginner-friendly Patient Management REST API built using FastAPI and Pydantic.

This project demonstrates how to build CRUD APIs using FastAPI, perform request validation with Pydantic, handle errors using HTTPException, and work with path parameters, query parameters, and request bodies.

## Project Overview

The Patient Management API allows users to:

* Get patient details
* Add new patients
* Update existing patient information
* Delete patients
* Validate patient input
* Handle invalid patient IDs
* Use path and query parameters
* Automatically generate API documentation using Swagger UI

The project currently uses a Python dictionary as a temporary in-memory database.

## Features

### GET - Get Patient

Retrieve a patient using a patient ID.

Path parameter example:

```text
GET /patient/P101
```

Query parameter example:

```text
GET /patient?id=P101
```

If the patient does not exist, the API returns:

```text
404 Patient not found
```

### POST - Add Patient

Add a new patient to the system.

Example request:

```json
{
    "id": "P121",
    "name": "Ravi",
    "age": 30,
    "gender": "Male",
    "disease": "Fever",
    "city": "Delhi"
}
```

The API checks whether the patient ID already exists.

If the ID already exists, the API returns:

```text
400 Patient already exists
```

### PUT - Update Patient

Update information of an existing patient.

Example:

```text
PUT /patient/P101
```

Request body:

```json
{
    "age": 25,
    "city": "Delhi"
}
```

Only the provided fields are updated.

The following fields can be updated:

* Name
* Age
* Gender
* Disease
* City

### DELETE - Delete Patient

Delete a patient using the patient ID.

Example:

```text
DELETE /patient/P101
```

If the patient exists, the patient is removed from the dictionary and the deleted information is returned.

If the patient does not exist:

```text
404 Patient not found
```

## CRUD Operations

| HTTP Method | Endpoint           | Purpose                           |
| ----------- | ------------------ | --------------------------------- |
| GET         | `/patient/{id}`    | Get patient using path parameter  |
| GET         | `/patient?id=P101` | Get patient using query parameter |
| POST        | `/patient`         | Add a new patient                 |
| PUT         | `/patient/{id}`    | Update an existing patient        |
| DELETE      | `/patient/{id}`    | Delete a patient                  |

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn
* REST API
* Swagger UI

## Python Concepts Used

This project also demonstrates several important Python concepts:

* Dictionary
* Functions
* Classes
* Type annotations
* Optional values
* Conditional statements
* Dictionary methods
* `pop()` method
* Exception handling
* Data validation

## FastAPI Concepts Used

The project demonstrates:

* FastAPI application creation
* GET requests
* POST requests
* PUT requests
* DELETE requests
* Path parameters
* Query parameters
* Request body
* Pydantic `BaseModel`
* `Field`
* `Annotated`
* `Optional`
* `Literal`
* `HTTPException`
* Status codes
* Automatic API documentation

## Pydantic Validation

The project uses Pydantic to validate incoming request data.

For example, age is validated using:

```python
age: Annotated[int, Field(gt=0)]
```

This means that the age must be greater than `0`.

Gender is restricted using:

```python
gender: Literal["Male", "Female"]
```

This means only `Male` or `Female` can be provided.

## Error Handling

The API uses FastAPI's `HTTPException` for handling errors.

Example:

```python
raise HTTPException(
    status_code=404,
    detail="Patient not found"
)
```

The project handles situations such as:

* Patient not found
* Duplicate patient ID
* Invalid patient data

## Project Structure

```text
Patient-Management-FastAPI/
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the project folder

```bash
cd Patient-Management-FastAPI
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install fastapi uvicorn pydantic
```

Or install everything from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Requirements

The `requirements.txt` file can contain:

```text
fastapi
uvicorn
pydantic
```

## Running the Application

Run the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## Swagger API Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

From Swagger UI, you can test:

* GET
* POST
* PUT
* DELETE

without needing a separate API testing tool.

## Example API Flow

### Get Patient

```text
GET /patient/P101
```

Response:

```json
{
    "patient": {
        "name": "Aakansha",
        "age": 22,
        "gender": "Female",
        "disease": "Diabetes",
        "city": "Jaipur"
    }
}
```

### Add Patient

```text
POST /patient
```

Request:

```json
{
    "id": "P121",
    "name": "Ravi",
    "age": 30,
    "gender": "Male",
    "disease": "Fever",
    "city": "Delhi"
}
```

### Update Patient

```text
PUT /patient/P121
```

Request:

```json
{
    "age": 31,
    "city": "Mumbai"
}
```

### Delete Patient

```text
DELETE /patient/P121
```

The API returns the deleted patient's information.

## Current Database

This project uses a Python dictionary as an in-memory data store.

Example:

```python
patient = {
    "P101": {
        "name": "Aakansha",
        "age": 22,
        "gender": "Female",
        "disease": "Diabetes",
        "city": "Jaipur"
    }
}
```

This is useful for learning and demonstration purposes.

However, dictionary data is temporary. Any changes will be lost when the application restarts.

## Future Improvements

The project can be upgraded further by adding:

* MySQL or PostgreSQL database
* SQLAlchemy ORM
* JWT authentication
* User login and registration
* Patient search and filtering
* Pagination
* Database relationships
* Automated testing
* Docker support
* Environment variables
* Cloud deployment
* Role-based access control

## Learning Outcomes

Through this project, I learned how to:

* Create REST APIs using FastAPI
* Work with HTTP methods
* Create GET, POST, PUT and DELETE endpoints
* Use path parameters
* Use query parameters
* Accept JSON request bodies
* Validate data using Pydantic
* Use `Annotated`, `Optional`, `Literal`, and `Field`
* Handle API errors using `HTTPException`
* Build basic CRUD functionality
* Test APIs using Swagger UI

## Project Status

Current version: `1.0.0`

Status: Completed beginner/intermediate FastAPI CRUD project.

## Disclaimer

This project uses sample data for educational purposes only.

The patient information in this project is fictional and should not be considered real medical data.

Do not upload real patient or other sensitive medical information to GitHub.

## Author

Aakansha Saxena

## License

This project is created for educational and portfolio purposes.
