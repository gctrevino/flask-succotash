# flask-succotash
Simple Flask app

## How to generate container
To generate the flask-app container run
```
docker build -t flask-app:latest .
```

## How to run the container
To start the container in foreground mode run:
```
docker run -it -p 5000:5000 --rm flask-app
```

To start the container in background mode run:
```
docker run -d -p 5000:5000 --rm flask-app
```

## How to run the tests
To run the small test set included with this project
```
python3 tests.py
```

## ToDo
---
### Tests
* ~~Add NaN tests~~
* ~~Add garbage tests~~
* Add bigger datasets and see the app crumble
* ...
### App
* ~~Handle error when something other than numbers are provided~~
* ~~Handle something other than json~~
* Improve sorting method
* ...
