
# https://github.com/gctrevino/flask-succotash


# create a ubuntu base image with python 3 installed.
FROM python:3

# set the maintainer label
LABEL MAINTAINER Gilberto Treviño "trevigno@gmail.com"

# set the working directory
WORKDIR /app

# copy all the needed files to container
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt

# install libraries and dependencies
RUN apt-get -y update
RUN pip3 install -r requirements.txt

# get lean
RUN apt-get clean
RUN apt-get -y autoremove
RUN rm -rf /var/lib/apt/lists/*

# expose the required port
EXPOSE 5000

# set the entrypoint
ENTRYPOINT [ "python3" ]

# run the command
CMD [ "main.py" ]
