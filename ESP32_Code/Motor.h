#ifndef _MOTOR_H
#define _MOTOR_H

//Autores: Alexis Roman, Daniel Sanchez, Josue Torres, Emilio Jaramillo, Benito Minga

class Motor {
private:
    int in1;
    int in2;
public:
    Motor(int _in1, int _in2){
        in1 = _in1;
        in2 = _in2;
    }

    void inicializar(){
        pinMode(in1, OUTPUT);
        pinMode(in2, OUTPUT);
    }

    void adelante(){
        digitalWrite(in1, HIGH);
        digitalWrite(in2, LOW);
    }

    void atras(){
        digitalWrite(in1, LOW);
        digitalWrite(in2, HIGH);
    }

    void parar(){
        digitalWrite(in1, LOW);
        digitalWrite(in2, LOW);
    }
};
#endif