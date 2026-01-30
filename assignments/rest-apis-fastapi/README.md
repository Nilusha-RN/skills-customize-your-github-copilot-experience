# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, fast, and production-ready REST APIs using the FastAPI framework in Python. You will create a complete API with CRUD operations, validation, and proper HTTP status codes.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI application with basic endpoints. Your API should serve as the foundation for managing a collection of items (e.g., books, products, or tasks).

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn web server
- Create a FastAPI application instance
- Define a root endpoint (`/`) that returns a welcome message
- Run the server on localhost with automatic reloading enabled
- Include proper docstrings for endpoints

### 🛠️ Implement CRUD Operations

#### Description
Build full Create, Read, Update, and Delete endpoints for managing items in your API. Use appropriate HTTP methods (GET, POST, PUT, DELETE) and status codes.

#### Requirements
Completed program should:

- Implement a GET endpoint to retrieve all items
- Implement a GET endpoint with path parameter to retrieve a single item by ID
- Implement a POST endpoint to create a new item with validation
- Implement a PUT endpoint to update an existing item
- Implement a DELETE endpoint to remove an item
- Return proper HTTP status codes (200, 201, 204, 404, etc.)

### 🛠️ Add Data Validation and Error Handling

#### Description
Enhance your API with Pydantic models for data validation and comprehensive error handling to ensure data integrity and clear error messages.

#### Requirements
Completed program should:

- Define Pydantic models for your data structure
- Validate request body data using the Pydantic models
- Return 422 status code for validation errors with descriptive messages
- Handle 404 errors when an item is not found
- Include try-except blocks for robust error handling
- Provide informative error responses to clients

