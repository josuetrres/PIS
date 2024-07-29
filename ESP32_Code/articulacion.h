#ifndef _ARTICULACION_H
#define _ARTICULACION_H

//Autores: Alexis Roman, Daniel Sanchez, Josue Torres, Emilio Jaramillo, Benito Minga

#include <ESP32Servo.h>

class Articulacion {
private:
    Servo motor;
    int pin;
    int posInicial;
    int posNueva;
    int velocidad;
public:
    Articulacion(Servo _motor, int _pin, int _posInicial = 0, int _velocidad = 20) {
        motor = _motor;
        pin = _pin;
        posInicial = _posInicial;
        posNueva = _posInicial;
        velocidad = _velocidad;
    }

    void inicializar() {
        motor.attach(pin);
        motor.write(posInicial);
    }

    void mover(int angulo) {
        posNueva = angulo;

        if (posInicial > posNueva) {
            for (int i = posInicial; i >= posNueva; i--) {
                motor.write(i);
                delay(velocidad);
            }
        } else {
            for (int i = posInicial; i <= posNueva; i++) {
                motor.write(i);
                delay(velocidad);
            }
        }

        posInicial = posNueva;
        Serial.println("Servo movido");
    }
};

#endif