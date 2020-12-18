To build an image:

```
$ docker build -t dentist .
```

Running as a container

```
$ docker run -p 8000:8000 -t dentist:latest __init__.py
```
