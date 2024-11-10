# Authentication API Documentation

This document describes the authentication endpoints for ResumeAI, which include signup and login functionality. Authentication uses JWT tokens for secure access control.

## Endpoints

### 1. User Signup
- **Endpoint**: `/auth/signup`
- **Method**: `POST`
- **Description**: Creates a new user account with a unique username, email, and password.
  
#### Request Body
```json
{
  "username": "exampleuser",
  "email": "user@example.com",
  "password": "examplepass"
}
```

#### Responses
- **201 Created**: User successfully created.
  ```json
  {
    "message": "User registered successfully."
  }
  ```
- **400 Bad Request**: Invalid or missing fields.
  ```json
  {
    "error": "Username or email already exists."
  }
  ```

### 2. User Login
- **Endpoint**: `/auth/login`
- **Method**: `POST`
- **Description**: Authenticates the user and returns a JWT token for authorized access.

#### Request Body
```json
{
  "username": "exampleuser",
  "password": "examplepass"
}
```

#### Responses
- **200 OK**: Login successful, returns a JWT token.
  ```json
  {
    "token": "your.jwt.token"
  }
  ```
- **401 Unauthorized**: Incorrect username or password.
  ```json
  {
    "error": "Invalid credentials."
  }
  ```

### Token Usage
- Include the JWT token in the `Authorization` header for routes that require authentication:
  ```http
  Authorization: Bearer your.jwt.token
  ```
- The token will expire after a set period, after which users need to log in again.

---

## Error Codes

- **400 Bad Request**: Validation error or missing required fields.
- **401 Unauthorized**: Invalid credentials or missing JWT token in the request header.
