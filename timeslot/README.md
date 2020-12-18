To build an image:

```
$ docker build -t timeslot .
```

Running as a container

```
$ docker run -p 4000:4000 -t timeslot:latest __init__.py
```
