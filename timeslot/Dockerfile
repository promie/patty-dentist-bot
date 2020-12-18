# We are using alpine (a simple Linux Kernal) as our bas container
FROM alpine:latest

# Install python and pip
RUN apk add --no-cache py-pip
RUN pip3 install --upgrade pip

# Copy the package files to the container and then move into the directory
COPY ./app /timeslot
WORKDIR /timeslot

# Install requirements
RUN pip3 install -r requirements.txt

# Open port 4000 for external communication
EXPOSE 4000

# Run our timeslot
WORKDIR /timeslot/demo
ENTRYPOINT ["python3"]
CMD ["__init__.py"]

