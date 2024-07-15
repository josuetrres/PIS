#include <WiFi.h>
#include <ESPAsyncWebServer.h>
#include <HTTPClient.h>
#include <ESP32Servo.h>
#include "articulacion.h"

//CONTRASEÑA DE LA RED
const char* ssid = "ROSA";
const char* password = "SKS.2022.1";

AsyncWebServer server(80); //Inicia un server que recibe datos de la app en el puerto 80

Servo s_camera, s_base, s_hombro, s_codo, s_muneca, s_pinza;

//Se crean los objetos de la clase Articulacion
Articulacion camera(s_camera, 2);
Articulacion base(s_base, 15);
Articulacion hombro(s_hombro, 16);
Articulacion codo(s_codo, 17);
Articulacion muneca(s_muneca, 18);
Articulacion pinza(s_pinza, 19);

void setup() {
  Serial.begin(115200);
  
  //Iniciar el WIFI
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  
  Serial.println("Connected to WiFi");
  Serial.println(WiFi.localIP());

  //Inicializar los servos de la clase Articulacion
  camera.inicializar();
  base.inicializar();
  hombro.inicializar();
  codo.inicializar();
  muneca.inicializar();
  pinza.inicializar();

  //Recibe los datos de la app por GET
  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
    String cameraVal, baseVal, hombroVal, codoVal, munecaVal, pinzaVal, forwardVal, backwardVal, leftVal, rightVal;

    //Verifica si la app envia esos datos correctamente
    if (request->hasParam("camera") 
    && request->hasParam("base") 
    && request->hasParam("hombro") 
    && request->hasParam("codo") 
    && request->hasParam("muneca") 
    && request->hasParam("pinza") 
    && request->hasParam("forward") 
    && request->hasParam("backward") 
    && request->hasParam("left") 
    && request->hasParam("right")){
      //Obtiene los valores de los parametros y se guardan en variables
      cameraVal = request->getParam("camera")->value();
      baseVal = request->getParam("base")->value();
      hombroVal = request->getParam("hombro")->value();
      codoVal = request->getParam("codo")->value();
      munecaVal = request->getParam("muneca")->value();
      pinzaVal = request->getParam("pinza")->value();

      forwardVal = request->getParam("forward")->value();
      backwardVal = request->getParam("backward")->value();
      leftVal = request->getParam("left")->value();
      rightVal = request->getParam("right")->value();

      //Mueve los servos a los angulos que se le envian desde la app
      camera.mover(cameraVal.toInt());
      base.mover(baseVal.toInt());
      hombro.mover(hombroVal.toInt());
      codo.mover(codoVal.toInt());
      muneca.mover(munecaVal.toInt());
      pinza.mover(pinzaVal.toInt());

      //Respuesta del ESP32
      request->send(200, "text/plain", "Servomotores movidos");

    } else {
      request->send(200, "text/plain", "No funca");
    }
  });

  server.begin();
}

void loop() {
  if (WiFi.status() == WL_CONNECTED){
    //Crea un http para enviar datos a la api externa
    HTTPClient http;
    //Datos que se enviaran a la api con el formato etiqueta-valor
    String data = "?dato1=" + valor1 "&dato2="+ valor2;

    //Inicia la conexion con la api
    http.begin("http://ip/estadisticas/api"); //Link de la api
    http.addHeader("Content-Type", "application/x-www-form-urlencoded"); //Tipo de contenido que se enviara

    int httpCode = http.POST(data); //Codigo de respuesta

    if (httpCode > 0) {
      Serial.println("Codigo de respuesta" + String(httpCode));
      if (httpCode == 200) { //200 es que se envio correctamente
        Serial.println("El servidor respondio correctamente");
        Serial.println(http.getString());
      } else {
        Serial.println("Error en el servidor");
      }
      http.end();
    }
    Serial.println("Error en la conexion wifi");
  }

  delay(1000);
}