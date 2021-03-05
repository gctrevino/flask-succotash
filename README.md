# flask-succotash
### This is a Simple Flask app

## Requirements
1. Build a simple Flask application that accepts a JSON list of objects (developer's choice as to what the data would be), sorts it, and returns the results.

2. Put the Flask application into a Docker container and expose whatever port number to the host.

3. Provide the Dockerfile, source code, and a Makefile or other script that we could use to build the Docker container on our computers and try it out.

*Disclaimer: The following has been tested on an Ubuntu 18.04 machine*

## How to generate container
To generate the flask-app container run
```bash
docker build -t flask-app:latest .
```

## How to run the container
To start the container in foreground mode run:
```bash
docker run -it -p 5000:5000 --rm flask-app
```

To start the container in background mode run:
```bash
docker run -d -p 5000:5000 --rm flask-app
```

## How to run the tests
To run the small test set included with this project
```bash
python3 tests.py
```

## ToDo
### App
- [x] Handle error when something other than numbers are provided
- [x] Handle something other than json
- [ ] Improve sorting method
- [ ] ...
### Tests
- [x] Add NaN tests
- [x] Add garbage tests
- [ ] Add bigger datasets and see the app crumble
- [ ] ...
### Template
- [ ] Add a UI for testing
