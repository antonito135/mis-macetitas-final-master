function cerrarsesion(){
    Swal.fire({
        title: '¿Estas seguro de cerrar sesión?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí!',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
        if (result.isConfirmed) {
            setTimeout(myURL,250);
            function myURL(){
                location.href ="index.html"
            }
        }
      })
  }

    function alerta(){

        Swal.fire({
            title: '¿Esta seguro de continuar con la compra?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#42E51A',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, confirmo!',
            cancelButtonText: 'Cancelar',
            }).then((result) => {
            if (result.isConfirmed) {
                Swal.fire({
                    icon: 'success',
                    title: 'Gracias! Tu pedido se ha confirmado',
                    showConfirmButton: false
                })
                setTimeout(myURL,1500);
                function myURL(){
                    location.href ="indexRegistrado.html"
                }
            }
            })
        }
        function alertaNR(){

            Swal.fire({
                title: '¿Esta seguro de continuar con la compra?',
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#42E51A',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Sí, confirmo!',
                cancelButtonText: 'Cancelar',
                }).then((result) => {
                if (result.isConfirmed) {
                    Swal.fire({
                        icon: 'success',
                        title: 'Gracias! Tu pedido se ha confirmado',
                        showConfirmButton: false
                    })
                    setTimeout(myURL,1500);
                    function myURL(){
                        location.href ="index.html"
                    }
                }
                })
            }
    function alertaSuscrito(){

        Swal.fire({
            title: '¿Esta seguro de continuar con la compra?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#42E51A',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, confirmo!',
            cancelButtonText: 'Cancelar',
            }).then((result) => {
            if (result.isConfirmed) {
                Swal.fire({
                    icon: 'success',
                    title: 'Gracias! Tu pedido se ha confirmado',
                    showConfirmButton: false
                  })
                setTimeout(myURL,1500);
                function myURL(){
                    location.href ="indexSuscrito.html"
                }
            }
            })
        }
function registrado(){
    Swal.fire({
        icon: 'success',
        title: 'Cuenta registrada',
        showConfirmButton: false,
        timer: 1500
      })

    setTimeout(myURL,1500);
    function myURL(){
        location.href ="indexRegistrado.html"
    }

}

    function suscripcion(){

    Swal.fire({
        title: '¿Esta seguro de suscribirse?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#42E51A',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, confirmo!',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                icon: 'success',
                title: 'Te has suscrito con exito',
                showConfirmButton: false
              })

            setTimeout(myURL,1500);
            function myURL(){
              location.href ="indexSuscrito.html"
            }
        }
        })
    }


function carrito(){
    Swal.fire({
        icon: 'success',
        title: 'Producto añadido al carrito',
        showConfirmButton: false,
        timer: 1500
      })
}