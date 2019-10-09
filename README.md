# mqtt-auth-connection

It consists of a docker-compose file that launches an mqtt broker with restricting access: only clients that manage the same access credentials ( username and password ) at the connection time are served.

## how it works
- `docker-compose` launches the broker mqtt. It listens on `localhost:1883`. The `mainloop.py` is used to interact with the broker, passing the authentication parameters. There is a `config.json` file to set endpoint and credentials in order to interact with the broker. Changing username or password, the communication fails.

### docker-compose
- It uses the `eclipse-mosquitto` image. There are two volumes to mount, `mosquitto.conf` and `dat.txt`. The first is a configuration file, the second contains username and encrypted password.  

### mosquitto.conf
```
allow_anonymous false
password_file /mosquitto/data/dat.txt
```

### password generation
- create a text file, like the figure below

<img align="center" width="458" height="182" src="https://github.com/enbis/mqtt-auth-connection/blob/master/images/mqtt-auth1.png">

- install `mosquitto`

- now encrypt the password with the command `mosquitto_passwd -U <text_file>`. The result of the encryption is shown in the figure below 

<img align="center" width="791" height="127" src="https://github.com/enbis/mqtt-auth-connection/blob/master/images/mqtt-auth2.png">

### test
- `docker-compose up`
- `python3 mainloop.py`
If username and password used by the client are the same as those mounted on the broker, everything works. Vice versa the communication fails.
