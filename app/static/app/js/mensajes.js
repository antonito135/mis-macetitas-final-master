frameElement


function eliminar(codigo){
    Swal.fire({
        title: '¿Estas seguro?',
        text: "No podrás revertir esto.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Estoy seguro.'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire(
            'Eliminado!',
            'Tu producto a sido eliminado..',
            'success'
          ).then(function() {
              window.location.href = "/productos/eliminar/"+ codigo + "/";
          })
        }
      })

}

function eliminarUsuario(id){
    Swal.fire({
        title: '¿Estas seguro?',
        text: "No podrás revertir esto.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Estoy seguro.'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire(
            'Eliminado!',
            'Tu producto a sido eliminado..',
            'success'
          ).then(function() {
              window.location.href = "/usuario/eliminar_usuario/"+ id + "/";
          })
        }
      })

}