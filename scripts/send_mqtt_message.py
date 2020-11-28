#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import os, subprocess, re, ssl, time, datetime
import sys


# ----------------------------------------------------------
#  Prerequisites
# ----------------------------------------------------------
# pip3 install paho-mqtt


# ----------------------------------------------------------
#  SETTINGS
# ----------------------------------------------------------
DEBUG = False
mqttBaseTopic = "phoniebox"             # MQTT base topic
mqttClientId = "phoniebox-tobezimmer"              # MQTT client ID
mqttHostname = "192.168.178.3"                # MQTT server hostname
mqttPort = 1883                         # MQTT server port (typically 1883 for unencrypted, 8883 for encrypted)
mqttUsername = "mqtt"                       # username for user/pass based authentication
mqttPassword = "mqtt"                       # password for user/pass based authentication
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

