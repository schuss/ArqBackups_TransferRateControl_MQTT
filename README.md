# ArqBackups_TransferRateControl_MQTT


A simple Python script leveraging Paho MQTT library to trigger these applescripts based on an MQTT message:

Applescripts available here: https://github.com/schuss/ArqBackups_TransferRateControl_Applescript

Python leverages Paho MQTT and is based on templates/examples from here:
https://github.com/eclipse/paho.mqtt.python/tree/master/examples


The point of this project: to use MQTT messages (from HomeAssistant, in my case) to impose upload rate limits on Arq Backups transfers based on known/expected network conflicts.  For example: allow maximum upload rate when no one is home using the connection, unless someone connects to Plex remotely.  Impose rate limits anyone someone is home and awake, to protect upload bandwidth for gaming/streaming.
