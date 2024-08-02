//CAMARA
const sliderCam = document.getElementById('camera');
const anguloCam = document.getElementById('anguloCam');
const incrementCam = document.getElementById('increment_camera');
const decrementCam = document.getElementById('decrement_camera');

//BRAZO
const sliderBas = document.getElementById('base');
const anguloBas = document.getElementById('anguloBas');

const sliderHom = document.getElementById('hombro');
const anguloHom = document.getElementById('anguloHom');

const sliderCod = document.getElementById('codo');
const anguloCod = document.getElementById('anguloCod');

const sliderMun = document.getElementById('muneca');
const anguloMun = document.getElementById('anguloMun');

const sliderPin = document.getElementById('pinza');
const anguloPin = document.getElementById('anguloPin');

//CARRO
const buttonForward = document.getElementById('forward');
const buttonBackward = document.getElementById('backward');
const buttonLeft = document.getElementById('left');
const buttonRight = document.getElementById('right');

//VALORES PARA LOS BOTONES
let directionValue = {
    forward: 0,
    backward: 0,
    left: 0,
    right: 0
};

//RESET
const reset = document.getElementById('reset');

//FUNCION FETCH
function fetchGet() {
    let formControl = new FormData(document.getElementById('form-control'));
    formControl.append('camera', sliderCam.value); //Agregar el valor de la camara al FormData
    formControl.append('forward', directionValue.forward);
    formControl.append('backward', directionValue.backward);
    formControl.append('left', directionValue.left);
    formControl.append('right', directionValue.right);

    let parametros = new URLSearchParams(formControl).toString();
    let url = '/control?' + parametros;
    
    fetch(url, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
        }
     });

     console.log(url);
}

//BOTONES PARA MOVER ANGULO DE LA CAMARA
incrementCam.addEventListener('click', function() {
    sliderCam.value = parseInt(sliderCam.value) + 5;
    anguloCam.textContent = sliderCam.value;

    fetchGet();
    console.log('camera: ' + sliderCam.value);
});

decrementCam.addEventListener('click', function() {
    sliderCam.value = parseInt(sliderCam.value) - 5;
    anguloCam.textContent = sliderCam.value;

    fetchGet();
    console.log('camera: ' + sliderCam.value);
});

//SLIDERS PARA CONTROL DE SERVOS
let sliders = [sliderCam, sliderBas, sliderHom, sliderCod, sliderMun, sliderPin];

function updateSliderValue(slider, angulo) {
    slider.addEventListener('input', function() {
        angulo.textContent = slider.value;
    });

    angulo.textContent = slider.value;
}

updateSliderValue(sliderCam, anguloCam);
updateSliderValue(sliderBas, anguloBas);
updateSliderValue(sliderHom, anguloHom);
updateSliderValue(sliderCod, anguloCod);
updateSliderValue(sliderMun, anguloMun);
updateSliderValue(sliderPin, anguloPin);

sliders.forEach(slider => {
    slider.addEventListener('input', function() {
        fetchGet();
        console.log(slider.id + ': ' + slider.value);
    });
})

//BOTON DE RESET
reset.addEventListener('click', function() {
    sliders.forEach(slider => {
        slider.value = 90;
        anguloCam.textContent = 90;
        anguloBas.textContent = 90;
        anguloHom.textContent = 90;
        anguloCod.textContent = 90;
        anguloMun.textContent = 90;
        anguloPin.textContent = 90;
    });

    fetchGet();
    console.log('Reset');
});

//BOTON ADELANTE
buttonForward.addEventListener('mousedown', function() {
    directionValue.forward = 1;
    fetchGet();
    console.log('forward: ' + directionValue.forward);
});

buttonForward.addEventListener('mouseup', function() {
    directionValue.forward = 0;
    fetchGet();
    console.log('forward: ' + directionValue.forward);
});


//BOTON ATRAS
buttonBackward.addEventListener('mousedown', function() {
    directionValue.backward = 1;
    fetchGet();
    console.log('backward: ' + directionValue.backward);
});

buttonBackward.addEventListener('mouseup', function() {
    directionValue.backward = 0;
    fetchGet();
    console.log('backward: ' + directionValue.backward);
});

//BOTON IZQUIERDA
buttonLeft.addEventListener('mousedown', function() {
    directionValue.left = 1;
    fetchGet();
    console.log('left: ' + directionValue.left);
});

buttonLeft.addEventListener('mouseup', function() {
    directionValue.left = 0;
    fetchGet();
    console.log('left: ' + directionValue.left);
});

//BOTON DERECHA
buttonRight.addEventListener('mousedown', function() {
    directionValue.right = 1;
    fetchGet();
    console.log('right: ' + directionValue.right);
});

buttonRight.addEventListener('mouseup', function()   {
    directionValue.right = 0;
    fetchGet();
    console.log('right: ' + directionValue.right);
});

// CONTROL POR TECLADO
document.addEventListener('keydown', function(event) {
    switch(event.key) {
        case 'w':
        case 'W':
            directionValue.forward = 1;
            fetchGet();
            console.log('forward: start');
            break;
        case 's':
        case 'S':
            directionValue.backward = 1;
            fetchGet();
            console.log('backward: start');
            break;
        case 'a':
        case 'A':
            directionValue.left = 1;
            fetchGet();
            console.log('left: start');
            break;
        case 'd':
        case 'D':
            directionValue.right = 1;
            fetchGet();
            console.log('right: start');
            break;
    }
});

document.addEventListener('keyup', function(event) {
    switch(event.key) {
        case 'w':
        case 'W':
            directionValue.forward = 0;
            fetchGet();
            console.log('forward: stop');
            break;
        case 's':
        case 'S':
            directionValue.backward = 0;
            fetchGet();
            console.log('backward: stop');
            break;
        case 'a':
        case 'A':
            directionValue.left = 0;
            fetchGet();
            console.log('left: stop');
            break;
        case 'd':
        case 'D':
            directionValue.right = 0;
            fetchGet();
            console.log('right: stop');
            break;
    }
});