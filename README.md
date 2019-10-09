# mqtt-auth-connection

It consists of a docker-compose file that runs an mqtt server. It has two volumes mounted, required to set the auth parameters. Only clients that manage the same credentials at the connection time are served.

## how it works
- `docker-compose up` to launch the mqtt server


## password generation
- create a text file, like the figure below

<img align="center" width="458" height="182" src="https://github.com/enbis/mqtt-auth-connection/blob/master/images/mqtt-auth1.png">

- install `mosquitto`

- now encrypt the password with the command `mosquitto_passwd -U <text_file>`. The result of the encryption is shown in the figure below 

<img align="center" width="791" height="127" src="https://github.com/enbis/mqtt-auth-connection/blob/master/images/mqtt-auth2.png">
