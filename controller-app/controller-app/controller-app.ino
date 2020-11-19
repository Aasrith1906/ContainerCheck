
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <ArduinoJson.h> 
#include <ESP8266WiFi.h>
#define LASER_PIN 1
#define SENSOR_PIN a0
#define Threshold 0

HTTPClient http;
const char *ssid = "Lol_5G"
const char *password = "Aasrith@1906";
const char *server = "cc-website.api.com"
const uint16_t port = 80;

using namespace websockets;

WebsocketsClient client;


void setup() {
  pinMode(LASER_PIN, OUTPUT);
  pinMode(SENSOR_PIN,INPUT);
  digitalWrite(LASER_PIN , HIGH);
  Serial.begin(9600);
  WiFi.begin(ssid,password);

  if(WiFi.status() != WL_CONNECTED)
  {
    Serial.println("WiFi not connected");
    return;
  }
}

void loop() {

   float sensor_read = analogRead(SENSOR_PIN);

   if(sensor_read>Threshold)
   {
    send_empty();   
   }
   else
   {
    send_full();
   }
}

int send_empty()
{
  int status_ = 0;
 
  return status_;
}

int send_full()
{
  int status_ = 0;

  return status_;
}
