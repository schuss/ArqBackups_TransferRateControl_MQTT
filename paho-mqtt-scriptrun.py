import paho.mqtt.client as mqtt
import os

mybroker = "BROKER_IP_GOES_HERE"
myport = "1883"
myuser = "MQTT_USERNAME_GOES_HERE"
myupass = "MQTT_PASSWORD_GOES_HERE"
mytopic = "MQTT_TOPIC_GOES_HERE"


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(mytopic)



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    # NOTE: MQTT payloads based on example setup, you may need/wish to change these
    # payload indicates limiting arq backup speed
    if (msg.payload) == "arq-backup-speed-limited":
        print "Limited"
        os.system(" open PATH_TO_FIXED_TRANSFER_RATE_SCRIPT_GOES_HERE")

    # payload indicates no limit for arq backups
    elif (msg.payload) == "arq-backup-speed-maximum":
        print "Max"
        os.system(" open PATH_TO_MAX_TRANSFER_RATE_SCRIPT_GOES_HERE")

    else:
    # other payload - log it
        print " >>> Unknown payload received"
        print(" >>> "+msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.username_pw_set(myuser, myupass)
client.will_set(mytopic, payload="surprise-disconnect", qos=1, retain=False)
client.connect(mybroker, myport, 600)

# stay open and listen!
client.loop_forever()
