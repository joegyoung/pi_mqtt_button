import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
from time import sleep

led=11
buttonPin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("godot/butter")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.payload == "on":
      GPIO.output(led,GPIO.HIGH)
    if msg.payload == "off":
      GPIO.output(led,GPIO.LOW)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)


client.loop_start()

while True:
  if GPIO.input(buttonPin) == GPIO.LOW:
    print("Pin 7 is LOW...")
  sleep(0.15)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
yyclient.loop_forever()
