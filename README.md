# flask-succotash
Simple Flask app \
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
---
### Tests
- [x] Add NaN tests
- [x] Add garbage tests
- [ ] Add bigger datasets and see the app crumble
- [ ] ...
### App
- [x] Handle error when something other than numbers are provided
- [x] Handle something other than json
- [ ] Improve sorting method
- [ ] ...
### Template
- [ ] Add a UI for testing
