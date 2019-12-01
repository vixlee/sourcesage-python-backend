# Interface Specification

HTTP 1.0 or higher must be used.

## User API

| URL                       | HTTP Method     | Description                                                                 |
| ------------------------- | ----------------| ----------------------------------------------------------------------------|
| `/api/v1/sign-up`         | POST            | Register new user                                                           |
| `/api/v1/login`           | POST            | Login user-api                                                              |
| `/api/v1/me`              | GET             | Show details logged user. Authorization: Bearer <Access-Token> is required. |
| `/api/v1/reset-password`  | POST            | Change password                                                             |
| `/api/v1/forgot-password` | POST            | Forgot password, user provide `email`                                       |


## HTTP Request Methods

The following HTTP methods can be used by the client:

### GET

Fetch information about a resource or a resource list. Expected status on
success is "200 OK".

### POST

Create a new resource. Expected status on success is "201 Created".

## HTTP Request Headers

The following HTTP headers are recognized, and in certain cases required, by the
server:

### Accept

Requests may contain an optional `Accept: application/json;
indent=<indent-size>` header in order to request a pretty-printed JSON response
with the specified indentation size.

### Content-Length

All requests that contain a body must include a `Content-Length:
<length-of-body>` header.

### Content-Type

All requests that contain a body must include a `Content-Type: application/json`
header.


### Authorization

All requests must contain an `Authorization: Bearer <Access-Token>` header that
identifies 

## HTTP Response Codes

The following HTTP response codes can be returned by the server:

### 200 OK

The GET request was successfully completed.

### 201 Created

The POST request was successfully completed.

### 401 Unauthorized 

The request has not been applied because it lacks valid authentication credentials for the target resource

### 400 Bad Request

The request data is not pass with validation in server.

### 404 Not Found

The resource does not exist.

### 405 Method Not Allowed

The request method is not allowed.  The HTTP methods allowed are POST, GET,
PUT and DELETE.

### 500 Internal Server Error

The server encountered an unexpected condition that prevents it from
fulfilling the request.
