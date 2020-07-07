
## How to install  rpm (on either Centos 7 or inside container)
 
 1. Install rpm (in container)
```console
container-prompt> cd /usr/src/dist; rpm -Uvh <rpm-name>.noarch.rpm
```
## Sundries
This project contains a number of sub-directories that contain CODE-SNIPPETS rather than fully functional working code
 
 1. photo-display-over-rest
```console
This sample code calls a rest api to get a list of users and then calls
a rest api /user/{id}/photo to pass a base64 encoded image over REST.
Html file is fully functional. Python code gives snippets of how a file is read server side and returned over REST
```
 2. proxy-to-keycloak-login
```console
This sample code shows how a GUI app can proxy its login page to an openidc auth provider: keycloak
```


