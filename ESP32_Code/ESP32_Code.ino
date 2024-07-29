#include <WiFi.h>
#include <ESPAsyncWebServer.h>
#include <HTTPClient.h>
#include <ESP32Servo.h>
#include "Motor.h"

//CONTRASEÑA DE LA RED
const char* ssid = "Internet_UNL";
const char* password = "UNL1859WiFi";

AsyncWebServer server(80); //Inicia un server que recibe datos de la app en el puerto 80

Servo s_camera, s_base, s_hombro, s_codo, s_muneca, s_pinza, s_radar;
int posCamera = 90, posBase = 90, posHombro = 90, posCodo = 90, posMuneca = 90, posPinza = 90, posRadar = 90;

Motor motor1(18, 5);
Motor motor2(17, 16);

void iniciarServo(Servo &servo, int pin, int pos = 90){
  servo.attach(pin);
  servo.write(pos);
}

void moverServo(Servo &servo, int &posAnt, int posNew, int velocidad = 20){
  if (posAnt > posNew) {
      for (int i = posAnt; i >= posNew; i--) {
          servo.write(i);
          delay(velocidad);
      }
  } else {
      for (int i = posAnt; i <= posNew; i++) {
          servo.write(i);
          delay(velocidad);
      }
  }
  posAnt = posNew;
}

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

  iniciarServo(s_camera, 32, posCamera);
  iniciarServo(s_base, 33, posBase);
  iniciarServo(s_hombro, 27, posHombro);
  iniciarServo(s_codo, 14, posCodo);
  iniciarServo(s_muneca, 12, posMuneca);
  iniciarServo(s_pinza, 13, posPinza);
  iniciarServo(s_radar, 2, posRadar);

  motor1.inicializar();
  motor2.inicializar();

  //Recibe los datos de la app por GET
  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
    String cameraVal, baseVal, hombroVal, codoVal, munecaVal, pinzaVal, forwardVal, backwardVal, leftVal, rightVal;

    //Verifica si la app envia esos datos correctamente
    if (request->hasParam("base") 
    && request->hasParam("hombro") 
    && request->hasParam("codo") 
    && request->hasParam("muneca") 
    && request->hasParam("pinza") 
    && request->hasParam("camera") 
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
      moverServo(s_base, posBase, baseVal.toInt());
      Serial.println(baseVal);
      moverServo(s_camera, posCamera, cameraVal.toInt());
      Serial.println(cameraVal);
      moverServo(s_hombro, posHombro, hombroVal.toInt());
      Serial.println(hombroVal);
      moverServo(s_codo, posCodo, codoVal.toInt());
      Serial.println(codoVal);
      moverServo(s_muneca, posMuneca, munecaVal.toInt());
      Serial.println(munecaVal);
      moverServo(s_pinza, posPinza, pinzaVal.toInt());
      Serial.println(pinzaVal);
      moverServo(s_radar, posRadar, 90);

      if (forwardVal.toInt() == 1){
        motor1.adelante();
        motor2.adelante();
        Serial.println("Adelante");
      } else if (backwardVal.toInt() == 1){
        motor1.atras();
        motor2.atras();
        Serial.println("Atras");
      } else if (leftVal.toInt() == 1){
        motor1.adelante();
        motor2.parar();
        Serial.println("Izquierda");
      } else if (rightVal.toInt() == 1){
        motor1.parar();
        motor2.adelante();
        Serial.println("Derecha");
      } else {
        motor1.parar();
        motor2.parar();
        Serial.println("Parar");
      }

      //Respuesta del ESP32
      request->send(200, "text/plain", "Servomotores movidos");

    } else {
      request->send(200, "text/plain", "No funca");
    }
  });

  server.begin();
}

void loop() {
  /*
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
  */
}