
# https://github.com/gctrevino/flask-succotash


# create a ubuntu base image with python 3 installed.
FROM python:3

# set the maintaner label
LABEL MAINTANER Gilberto Treviño "trevigno@gmail.com"

# set the working directory
WORKDIR /app

# copy all the needed files
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt

# install the dependencies
RUN apt-get -y update
RUN pip3 install -r requirements.txt

#Expose the required port
EXPOSE 5000

# set the entrypoint
ENTRYPOINT [ "python3" ]

# run the command
CMD [ "main.py" ]
