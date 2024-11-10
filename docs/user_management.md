# User Management API Documentation

This document covers the user-related endpoints in ResumeAI, including profile management and resume upload.

## Endpoints

### 1. Get User Profile
- **Endpoint**: `/user/profile`
- **Method**: `GET`
- **Authorization**: JWT token required
- **Description**: Retrieves the authenticated user's profile information.

#### Responses
- **200 OK**: Returns user profile details.
  ```json
  {
    "username": "exampleuser",
    "email": "user@example.com",
    "resumes": ["resume1.pdf", "resume2.pdf"]
  }
  ```
- **401 Unauthorized**: Missing or invalid token.
  ```json
  {
    "error": "Unauthorized access."
  }
  ```

### 2. Update User Profile
- **Endpoint**: `/user/profile`
- **Method**: `PUT`
- **Authorization**: JWT token required
- **Description**: Updates the user’s profile information.

#### Request Body
```json
{
  "email": "newemail@example.com"
}
```

#### Responses
- **200 OK**: Profile updated successfully.
  ```json
  {
    "message": "Profile updated."
  }
  ```
- **400 Bad Request**: Invalid fields.
  ```json
  {
    "error": "Invalid email format."
  }
  ```

### 3. Upload Resume
- **Endpoint**: `/user/upload_resume`
- **Method**: `POST`
- **Authorization**: JWT token required
- **Description**: Allows the user to upload a resume file.

#### Request
- **Form-Data**: File upload using form-data with key `resume_file`.

#### Responses
- **200 OK**: Resume uploaded successfully.
  ```json
  {
    "message": "Resume uploaded successfully.",
    "resume_url": "/path/to/resume.pdf"
  }
  ```
- **400 Bad Request**: File not provided or unsupported format.
  ```json
  {
    "error": "Resume file is required and must be in PDF format."
  }
  ```

---

## Error Codes

- **400 Bad Request**: Validation error or missing fields.
- **401 Unauthorized**: Missing or invalid token.
- **500 Internal Server Error**: Unexpected server error, check logs for details.
