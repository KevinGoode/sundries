## customise-keycloak
This article explains how to customise keycloak by creating a new theme.

How to run code on raspberry pi
 1. Install docker on raspberry pi (https://dev.to/rohansawant/installing-docker-and-docker-compose-on-the-raspberry-pi-in-5-simple-steps-3mgl)
 2. Run keycloak on raspberry pi (https://github.com/ruifigueiredo/docker-rpi-keycloak)
 ```console
 docker run --name keycloak --privileged -d -p 8180:8080 -p 9990:9990 ruifigueiredo/rpi-keycloak
 ```
 4. Configure keycloak. Login to keystone (admin/admin). Create new realm 'demo' and create a client 'example-app'.  Create 2 news users in Demo Realm: one with no roles (demo-user), one with all REALM roles (demo-admin).

To login as demo-admin:
```console
http://192.168.1.9:8180/auth/admin/demo/console 
```

 To login as demo-user IE very basic config of user password etc:
```console
http://192.168.1.9:8180/auth/realms/demo/account 
```

 5. Copy an existing theme eg: 
 ```console
  docker cp keycloak:/data/keycloak-4.8.1.Final/themes/keycloak ./theme
 ```
 6. Create favicon.ico, background.png and logo.png (123x25px) and replace files: /keycloak/login/resources/img/keycloak-bg.png with contents from background.png, all favicon.ico and logo.png in keycloak/account/resources/img and keyclok-logo.png in keycloak/admin/resources/img . Examples are in images directory
 
 7. Rename directory theme/keystone to theme/kev and copy kev back into keycloak theme directory.
 
 8. Login to keycloak and set theme of realm to 'kev'
 
  
 ![screen1](https://github.com/KevinGoode/sundries/blob/master/customise-keycloak/images/screenshot1.jpg)
 
 
 ![screen2](https://github.com/KevinGoode/sundries/blob/master/customise-keycloak/images/screenshot2.jpg)
  
### References
See [https://robferguson.org/blog/2020/04/12/keycloak-themes-part-1/](https://robferguson.org/blog/2020/04/12/keycloak-themes-part-1/)
Also see 
[https://www.keycloak.org/docs/latest/server_development/#creating-a-theme](https://www.keycloak.org/docs/latest/server_development/#creating-a-theme)

