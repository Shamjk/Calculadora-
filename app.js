function enviar() {
    var contenido = document.querySelector('#contenido');
    var v1 = document.querySelector('#t1').value.trim();
    var v2 = document.querySelector('#t2').value.trim();
    var url = "";

    if (!v1 || (!v2 && document.querySelector('#opcion1').checked)) {
        swal("Mensaje", "Ingrese valores válidos", "warning");
        return;
    }

    if (document.querySelector('#opcion1').checked)
        url = 'http://127.0.0.1:5000/suma/' + v1 + '/' + v2;
    else if (document.querySelector('#opcion2').checked)
        url = 'http://127.0.0.1:5000/resta/' + v1 + '/' + v2;
    else if (document.querySelector('#opcion3').checked)
        url = 'http://127.0.0.1:5000/multiplicacion/' + v1 + '/' + v2;
    else if (document.querySelector('#opcion4').checked)
        url = 'http://127.0.0.1:5000/division/' + v1 + '/' + v2;
    else if (document.querySelector('#opcion5').checked)
        url = 'http://127.0.0.1:5000/potenciacion/' + v1 + '/' + v2;
    else if (document.querySelector('#opcion6').checked) {
        if (!v1) {
            swal("Mensaje", "Ingrese un valor válido para seno", "warning");
            return;
        }
        url = 'http://127.0.0.1:5000/seno/' + v1;
    } else if (document.querySelector('#opcion7').checked) {
        if (!v1) {
            swal("Mensaje", "Ingrese un valor válido para coseno", "warning");
            return;
        }
        url = 'http://127.0.0.1:5000/coseno/' + v1;
    } else {
        swal("Mensaje", "Seleccione una opción", "warning");
        return;
    }

    fetch(url)
        .then(function (response) {
            if (response.ok) {
                return response.json();
            } else {
                throw "Error en la llamada";
            }
        })
        .then(function (texto) {
            console.log(texto);
            let cadena = `<h3>Resultado: ${texto.Resultado} Operación: ${texto.Operacion}</h3>`;
            contenido.innerHTML = `${cadena}`;
        })
        .catch(function (error) {
            console.error("Error en la solicitud:", error);
            swal({
                title: "Advertencia",
                text: "Ocurrió un error en la solicitud",
                icon: "warning",
                buttons: true,
                dangerMode: true,
            });
        });
}
