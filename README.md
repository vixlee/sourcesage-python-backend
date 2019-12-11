# SourceSage Python Techincal Testing by Vix Lee (lehungvi.cntt@gmail.com)

## Overview
The application is a Rest-Ful API for
This app is served to the client by `app.py` on port 8000 default.

## Hosting for review

```URL
https://restful-user-api.herokuapp.com
```

## Installation
Under root folder, run command:
```
make install
```

## Running
Under root folder, run command:
```
make run
```
## Usage Example

### Sign-up new user

```bash
curl -i https://restful-user-api.herokuapp.com/api/auth/sign-up \
    -H "Content-Type: application/json" \
    -X POST \ 
    -d '{"email": "lehungvi.1609@gmail.com", "password": "P@ssw0rd123","age": 28,"gender": 1,"name": "Le Hung Vi"}'

HTTP/1.0 201 CREATED
Content-Type: text/html; charset=utf-8
Content-Length: 0
Server: Werkzeug/0.16.0 Python/3.6.8
Date: Tue, 03 Dec 2019 05:20:01 GMT

```

### Login

```bash
curl -i https://restful-user-api.herokuapp.com00/api/auth/login \
    -H "Content-Type: application/json" \
    -X POST \
    -d '{"email": "lehungvi.1609@gmail.com", "password": "LeHungVi"}'
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 363
Server: Werkzeug/0.16.0 Python/3.6.8
Date: Tue, 03 Dec 2019 05:22:32 GMT

{"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NzUzNTA2NTMsIm5iZiI6MTU3NTM1MDY1MywianRpIjoiYWU1YmE5YzQtNTAyYi00ZmU0LTk4NmMtMDlkOGFhYmIzMmQ1IiwiZXhwIjoxNTc1MzUwNzEzLCJpZGVudGl0eSI6eyJlbWFpbCI6ImxlaHVuZ3ZpLjE2MDlAZ21haWwuY29tIiwicGFzc3dvcmQiOiJMZUh1bmdWaSJ9LCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.u0_4u6WQYmLyd6NKGkc41EtHCElW8wO_5mrH54bD-9c"}
```
### Show logged user information

```bash
curl -i https://restful-user-api.herokuapp.com:8000/api/auth/me \
    -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NzUzNTA2NTMsIm5iZiI6MTU3NTM1MDY1MywianRpIjoiYWU1YmE5YzQtNTAyYi00ZmU0LTk4NmMtMDlkOGFhYmIzMmQ1IiwiZXhwIjoxNTc1MzUwNzEzLCJpZGVudGl0eSI6eyJlbWFpbCI6ImxlaHVuZ3ZpLjE2MDlAZ21haWwuY29tIiwicGFzc3dvcmQiOiJMZUh1bmdWaSJ9LCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.u0_4u6WQYmLyd6NKGkc41EtHCElW8wO_5mrH54bD-9c"
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 134
Server: Werkzeug/0.16.0 Python/3.6.8
Date: Tue, 03 Dec 2019 05:24:39 GMT

{"age":28,"email":"lehungvi.1609@gmail.com","gender":1,"name":"Le Hung Vi","password":"UjWLeDPmpIorqg1AUn00Oh+kGEYjLlptwcx7iHWQVxk="}
```
