#!/bin/bash
#######################################
#Script gets current external ip from 'whatismyipaddress' webserver, 
#checks whether ip has changed (by comparing ip with that
#stored in local file), and if IP has changed it makes
#an http request to no-ip dn server to update dn and then
#store this new ip in a local file
#
#Kevin Goode 10/8/2014
######################################
source './config.sh'
function  getExternalIP()
{
	local ip=$(curl -s -X GET http://bot.whatismyipaddress.com)
	echo $ip
}
######################################
#Sets no-ip DNS
#Arg1 is username,
#Arg2 is password
#Arg3 is hostname
#Arg4 is external ip
#####################################
function setNoIpDNS()
{
    #See no-ip webpage for protocol:  http://www.noip.com/integrate/request
    local output=$(curl -s -X GET http://$1:$2@dynupdate.no-ip.com/nic/update?hostname=$3&myip=$4)
}
function setAllDNS()
{
   for val in ${DNSLIST[@]}; do
       $(setNoIpDNS $USERNAME $PASSWORD $val $1)
   done;
}
function main()
{
    echo "############################################"
    echo "Starting script to update no-ip domain names"
    OLDIP=""
    #Only update DNs if IP has changed
    if [ -e $EXTERNALIPFILE ] 
    then
        echo "Getting stored ip"
        OLDIP=$(cat  $EXTERNALIPFILE )
    else
        echo "File containing ip does not exist" 
    fi
    echo "Old Exernal IP is     : $OLDIP"
    echo "Getting current ip"
    IP=$(getExternalIP)
    echo "Current External IP is: $IP"
    if [ "$OLDIP" != "$IP" ]
    then
        echo "Updating ips"
        setAllDNS $IP
        echo  "Updating file"
        echo $IP > $EXTERNALIPFILE
    else
        echo "Ip has not changed. Nothing to do"
    fi
    echo "Done. Script finished"
    echo "############################################"

}
main

