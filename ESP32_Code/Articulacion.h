#ifndef _ARTICULACION_H
#define _ARTICULACION_H

class Articulacion {
private:
    Servo servo;
    int posAnt;
    int posNew;
    int pin;
    int velocidad;
public:
    Articulacion(Servo _servo, int _posAnt, int _pin, int _velocidad){
        this->servo = _servo;
        this->posAnt = _posAnt;
        this->posNew = _posAnt;
        this->pin = _pin;
        this->velocidad = _velocidad;
    }

    void inicializar(){
        servo.attach(pin);
        servo.write(posAnt);
    }

    void mover(int _posNew, int _velocidad = 20){
        posNew = _posNew;
        velocidad = _velocidad;

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
};

#endif