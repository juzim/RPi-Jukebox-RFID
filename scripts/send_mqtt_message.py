#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import os, subprocess, re, ssl, time, datetime, configparser, sys


# ----------------------------------------------------------
#  Prerequisites
# ----------------------------------------------------------
# pip3 install paho-mqtt


# ----------------------------------------------------------
#  SETTINGS
# ----------------------------------------------------------
config = configparser.ConfigParser()
config.read('../settings/mqtt.conf')
default_config = config['DEFAULT']
DEBUG = False
mqttBaseTopic = "phoniebox/tag_scanned"             # MQTT base topic
mqttClientId = "phoniebox"              # MQTT client ID
mqttHostname = default_config['host']                # MQTT server hostname
mqttPort = default_config['port']                         # MQTT server port (typically 1883 for unencrypted, 8883 for encrypted)
mqttUsername = default_config['username']                       # username for user/pass based authentication
mqttPassword = default_config['password']                       # password for user/pass based authentication
mqttCA = ""    # path to server certificate for certificate-based authentication
mqttCert = ""    # path to client certificate for certificate-based authentication
mqttKey = ""     # path to client keyfile for certificate-based authentication
mqttConnectionTimeout = 60              # in seconds; timeout for MQTT connection
refreshIntervalPlaying = 5              # in seconds; how often should the status be sent to MQTT (while playing)
refreshIntervalIdle = 30                # in seconds; how often should the status be sent to MQTT (when NOT playing)

# ----------------------------------------------------------
#  DO NOT CHANGE BELOW
# ----------------------------------------------------------

# create client instance
client = mqtt.Client(mqttClientId)

# configure authentication
if mqttUsername != "" and mqttPassword != "":
    client.username_pw_set(username=mqttUsername, password=mqttPassword)

if mqttCert != "" and mqttKey != "":
    if mqttCA != "":
        client.tls_set(ca_certs=mqttCA, certfile=mqttCert, keyfile=mqttKey)
    else:
        client.tls_set(certfile=mqttCert, keyfile=mqttKey)
elif mqttCA != "":
    client.tls_set(ca_certs=mqttCA)

# attach event handlers

# connect to MQTT server
print("Connecting to " + mqttHostname + " on port " + str(mqttPort))
client.connect(mqttHostname, mqttPort, mqttConnectionTimeout)

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

client.publish(mqttBaseTopic + "/" + mqttClientId, sys.argv[1])
