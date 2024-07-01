const sliderCam = document.getElementById('camera');
const anguloCam = document.getElementById('anguloCam');
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

let sliders = [sliderCam, sliderBas, sliderHom, sliderCod, sliderMun, sliderPin];

function update_value(slider, angulo) {
    slider.addEventListener('input', function() {
        angulo.textContent = slider.value;
    });

    angulo.textContent = slider.value;
}

update_value(sliderCam, anguloCam);
update_value(sliderBas, anguloBas);
update_value(sliderHom, anguloHom);
update_value(sliderCod, anguloCod);
update_value(sliderMun, anguloMun);
update_value(sliderPin, anguloPin);

sliders.forEach(slider => {
    slider.addEventListener('input', function() {
        let form_control = new FormData(document.getElementById('form-control'));
        let parametros = new URLSearchParams(form_control).toString();
        fetch('/control_servo?' + parametros, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
            }
        })
        console.log(slider.id + ': ' + slider.value);
    });
})

