# Url Shortner REST API

## Question:
Write an API for a URL shortener service with three components.
- Create an API that should accept a long URL and return a short URL. API doesn’t require authentication.
- Url shortener service should store metadata about short URLs like the total number of hits, hourly hits. - An API with a shortened URL should return the data.
- API should have an endpoint for search. Search will return results matching the title of the URL.
Say the term “Python”, API should return all pages which have a partial or full match for the term.

## Documentation

| Endpoint        | Method           | Input  |Input Example|Output  |Output Example|
| ------------- |:-------------:| -----:|-----:|-----:|-----:|
| `/url`    | `POST` | `{ "url":<any_url: String> }` |`{"url":"https://www.google.com/"}`|`{"id": 2,"main_url": <any_url: String>,"short_url": <short_url>,"hits": <total_hits>,"hourly_hits": <hits_per_hour>,"title": <page_title>}`|`{"id": 2, "main_url": "https://www.google.com/", "short_url": "http://localhost:5000/CPcljp", "hits": 16, "hourly_hits": 2, "title": "Google"}`|
| `/search/<keyword>`      | `GET`      |   None |None|`"{urls":[array of url details similar to output of '/url']}`|`{"urls": [{"id": 1,"main_url": "https://www.google.com/","short_url": "http://localhost:5000/liUbsv","hits": 4,"hourly_hits": 4,"title": "Google"},{"id": 2,"main_url": "https://www.google.com/","short_url": "http://localhost:5000/CPcljp","hits": 16,"hourly_hits": 2,"title": "Google"}]}`|
| `/<short_url>` | `GET`      |    None | None| Redirect to their respective main url| None|

for example API endpoints postman collection is also added to the repository. Can be seen [here](https://github.com/sumityadavs7y/url-shortner/blob/a742abe01f092422d6199d49049165ba99662d46/Url Shortner.postman_collection.json).

## Dependencies

##### Following are the external libraries used:
- flask
- flask-restful
- sqlalchemy
- flask-sqlalchemy
- validators
- beautifulsoup4
- urllib3
- python-dotenv
- flask-cors
- gunicorn
- psycopg2

##### Following are the libraries used for dev environment:

- autopep8

for more details of the libraries Pipfile can be seen.

## Installation

URL-Shortner requires [python](https://www.python.org/) v3.8+ to run.

Install the dependencies and devDependencies and start the server.

```sh
pip install pipenv
pipenv install
pipenv run python app.py
```

## Deployment

Currently deployed at heroku. Can visit [here](https://url-shortner-sumit.herokuapp.com/).

for the current deployment Flask and PostgreSQL is used
