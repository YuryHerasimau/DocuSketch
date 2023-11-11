# DOCUSKETCH Interview Task
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Test task for the position of Python developer (DevOps trainee) at [DocuSketch](https://hh.ru/employer/5714322)


## Description
This project consists of:
- script for monitoring memory usage and generating alerts via HTTP requests to the API
- REST API service, which includes setting up Docker Compose with 2 containers: a NoSQL database and a Python application using Flask on port 8080 to process GET, POST, PUT requests (i.e. Create a key=value, change the key=new_value, read the key value).

## Getting Started

### Dependencies
Make sure you have Docker and docker-compose installed.

### Installing
1. Clone the repository:
```
git clone <repo>
python -m pip install -r ./requirements.txt
```
2. Run the script to monitor memory usage:
```
python check_memory_usage.py
```
3. Build and run docker containers with the application and database:
```
docker-compose build
docker-compose up
```

### Executing program
**Creating a key=value**
Request:
```
curl --location 'http://127.0.0.1:8080/api/key' \
--header 'Content-Type: application/json' \
--data '{
     "key": "languages",
     "value": [
         "English"
         "French"
         "German"
     ]
}'
```
Response:
```
{
     "message": "Ключ=значение успешно создано. ObjectID=654f4f90dec655a4b9e412d9"
}
```
Status code: `201 CREATED`


**Getting the key value**
Request:
```
curl --location 'http://127.0.0.1:8080/api/key/languages' \
--data ''
```
Response:
```
{
     "key": "languages",
     "value": [
         "English"
         "French"
         "German"
     ]
}
```
Status code: `200 OK`

**Updating the key=new_value**
Request:
```
curl --location --request PUT 'http://127.0.0.1:8080/api/key/languages' \
--header 'Content-Type: application/json' \
--data '{
     "value": [
         "English"
         "French"
         "German"
         "Italian"
     ]
}'
```
Response:
```
{
    "message": "Значение ключа успешно изменено"
}
```
Status code: `200 OK`

## What can be improved
- [ ] Cover the code with tests
- [ ] Add logging