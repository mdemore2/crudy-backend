# crudy-backend
Simple CRUD Backend for RAP

## Getting Started

### Dependencies

This app is built in tandem with a frontend React app, it is implemented in [crudy-frontend](https://github.com/mdemore2/crudy-frontend).

It also requires Python.

### Running the app (locally)

1. Clone this repository
`git clone git@github.com:mdemore2/crudy-backend.git`

2. Install required packages
`pip install -r requirements.txt`

3. Run the server
`python wearhaus/manage.py runserver`

Note: You may need to execute `python wearhaus/manage.py migrate` to create necessary tables in the database before the first run of the app.

### Deploying the app

The deployment branch is `pyworker` which leverages Cloudflare's Python Workers as a runtime and [django-cf](https://github.com/G4brym/django-cf) to connect to Cloudflare's D1 Database.

## Built With

- Django

Deployed using Cloudflare Python Workers, leveraging Cloudflare's D1 Database.

