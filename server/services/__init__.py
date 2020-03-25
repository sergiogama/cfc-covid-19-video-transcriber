# The content of this file was generated by IBM Cloud
# Do not modify it as it might get overridden

from ibmcloudenv import IBMCloudEnv
from . import service_manager
from flask_mqtt import Mqtt
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import SpeechToTextV1 
from dotenv import load_dotenv
import os

IBMCloudEnv.init()


def initServices(app):
	# Setup MQTT
	app.config['MQTT_BROKER_URL'] = 'test.mosquitto.org'
	app.config['MQTT_BROKER_PORT'] = 1883
	mqtt = Mqtt(app)
	app.config['MQTT_CLIENT'] = mqtt

	# Setup IBM Watson
	load_dotenv()
	authenticator = IAMAuthenticator(os.getenv("IAM_AUTHENTICATOR")) 
	service = SpeechToTextV1(authenticator=authenticator) 
	app.config['SPEECH_TO_TEXT'] = service

	return