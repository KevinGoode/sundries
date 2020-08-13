# no-ip-dnsclient
Because your local external ip provided by your internet service provider can change at any time  
this script dynamically works out what your public ip is and configures any (no-ip) free domain names you   
might have to point to this ip address. The script should be run periodically (eg every few mins)  
so that any service you export to the WWW has minimal downtime. The last public ip is cached in a file so the  
dns ips are only configured if this ip changes.    

## Background
The script works out what your public ip is and sets no-ip free DNS names with this public ip.    
The script must be run on you local network on which you which to deploy your dns services.  
You need to configure port forwarding on you service provider router to forward ports to ips within local network  
that expose services to the WWW.  
## Running  code
1. Set params in config.sh
2. Execute: 
```console
./no-ip-dns-client

```


NOTE: An encrypted file example-config.sh.gpg contains a real world example configuration. To unencrypt and use these variables
```console
gpg -d example-config.sh.gpg > config.sh
./no-ip-dns-client
```

