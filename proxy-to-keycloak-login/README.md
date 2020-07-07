

## proxy-to-keycloak-login
This sample code shows how a GUI app can proxy its login page to an openidc auth provider: keycloak
How to run code on raspberry pi
 1. Install docker on raspberry pi (https://dev.to/rohansawant/installing-docker-and-docker-compose-on-the-raspberry-pi-in-5-simple-steps-3mgl)
 2. Run keycloak on raspberry pi (https://github.com/ruifigueiredo/docker-rpi-keycloak)
 3. Configure keycloak. Login to keystone (admin/admin). Create new realm 'demo' and create a client 'example-app'. Edit 'example-app' client with following settings:
'Valid Redirects URL': http://192.168.1.9:3000/*
'Implicit Flow Enabled': On
4. Install webserver (eg sudo apt-get install php)
5. Run webserver (eg php -S 192.168.1.9:3000)
6. Open GUI app in browser: http://192.168.1.9:3000
Should be forwarded to keycloak login page as shown:
![Image of login](https://github.com/KevinGoode/sundries/blob/master/proxy-to-keycloak-login/images/keycloak.jpg)


Where to next? We have learnt here that Keycloak GUI can be used to configure users for a particular project and even to display login page (DETAILS TODO). However, to authenticate (and thereafter authorize) a GUI app's REST API we need to do some more work. It is common parctice to implement authn and authz middleware server side that intercepts requests and performs authn and authz before calling REST handlers. There are 2 options for token validation: online validation and offline validation

1. **Online.** Implement a function to inspect each request for a bearer token and send that token off for validation by your keycloak server at the userinfo endpoint before it is passed to your api's route handlers. - **Unfortunately this means for every REST CALL there is a authn call to keycloak**
2. **Offline.** Much **more efficient is offline** validation: A JWT Token is a base64 encoded JSON object, that **already contains** all information (claims) to do the validation offline. You only need the public key and validate the signature (to make sure that the contents is "valid").

