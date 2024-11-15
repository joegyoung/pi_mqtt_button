import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

led=11
button = 35
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

led_on =0

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    global led_on
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("godot/butter")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global led_on
    print(msg.topic+" "+str(msg.payload.decode("utf-8")))
    if msg.payload.decode("utf-8") == "on":
      led_on = 1
      GPIO.output(led,GPIO.HIGH)
    if msg.payload.decode("utf-8") == "off":
      led_on = 0
      GPIO.output(led,GPIO.LOW)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_start()

while True:
    input_state = GPIO.input(button) # Sense the button
    if input_state == False:
        print('Button Pressed')
        print(led_on)
        time.sleep(0.2)
        # Switch on LED
        #GPIO.output(led, 1)
        if bool(led_on):
          ret= client.publish("godot/butter","off",2,True)
          led_on = 0
        else:
          ret= client.publish("godot/butter","on",2,True)
          led_on = 1
#    else :
        # Switch off LED
        #GPIO.output(led, 0)
#        ret= client.publish("godot/butter","off")
