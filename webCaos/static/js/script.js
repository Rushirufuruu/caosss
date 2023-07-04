function validar() {
    let resp;
    resp = validarPassword();
    if(resp = false){
      return false;
    }
    resp = validarNombre();
    if(resp = false){
      return false;
    }
    resp = validarApellido();
    if(resp = false){
      return false;
    }
    resp = validarEdad();
    if(resp = false){
      return false;
    }
    return true;

}

 //validar que las contraseñas sean iguales con javascript
function validarPassword() {
    let pass1 = document.getElementById('pwdPass1').value;
    let pass2 = document.getElementById('pwdPass2').value;

    if(pass1 == ''){
      alert('Debe ingresar una contraseña')
      return false;
    }else if(pass1 != pass2){
      alert('Las contraseñas deben ser iguales');
      return false;
    }else{
      return true;
   }
}
//validar el largo del nombre con javascript
function validarNombre(){
    let nom = document.getElementById('txtNombre').value;
    if(nom.length < 2){
      alert('El nombre debe tener al menos 2 caracteres')
      return false;
    }else{
      return true;
    }
}

function validarApellido(){
  let ape = document.getElementById('txtApellido').value;
  if(ape.length < 2){
    alert('El apellido debe tener al menos 2 caracteres')
    return false;
  }else{
    return true;
  }
}




function validarEdad() {
  let fecha_mia = document.getElementById("datFecha").value;
  let fecha_sistema= new Date();
  console.log('Fecha Mia:'+fecha_mia);
  console.log('Fecha Sistema:'+fecha_sistema);

  let ano= fecha_mia.slice(0,4);
  let mes= fecha_mia.slice(5,7);
  let dia= fecha_mia.slice(8,10);
  console.log('Año:'+ano);
  console.log('Mes:'+mes);
  console.log('Dia:'+dia);

  let mi_fecha_gmt= new Date(ano,(mes-1),dia);
  console.log('Mi fecha gmt:'+mi_fecha_gmt);

  if (mi_fecha_gmt>fecha_sistema) {
      alert('fecha de nacimiento mayor a fecha actual');
      return false;
  }
  let dia_mili= 1000*60*60*24;
  console.log('Milisegundos por dia:'+dia_mili);
  let dias_vividos=(fecha_sistema.getTime()-mi_fecha_gmt.getTime())/dia_mili;
  let mi_edad= Math.trunc( dias_vividos/365);
  console.log('Edad:'+mi_edad); 
  if (mi_edad<18) {
      alert('es menor de edad');
      return false;
  }
  return true;
}


  


//validar el rut con jquery
$(document).ready(function() {
    $("#Enviar").click(function() {
    var rut = $("#txtRut").val();
      
    // Eliminar puntos y guión del Rut
    rut = rut.replace(/\./g,'');
    rut = rut.replace(/\-/g,'');
      
      // Validar formato del Rut
    if (!/^[0-9]{7,8}[kK0-9]$/.test(rut)) {
        alert("El Rut no tiene el formato correcto");
        return false;
       }
      
      // Validar dígito verificador
      var dv = rut.charAt(rut.length - 1);
      var rutSinDV = rut.substring(0, rut.length - 1);
      var suma = 0;
      var factor = 2;
      for (var i = rutSinDV.length - 1; i >= 0; i--) {
        suma += factor * rutSinDV.charAt(i);
         factor = factor === 7 ? 2 : factor + 1;
      }
      var dvCalculado = 11 - (suma % 11);
      if (dvCalculado === 11) {
        dvCalculado = "0";
      } else if (dvCalculado === 10) {
        dvCalculado = "K";
      }
      if (dv.toUpperCase() !== dvCalculado.toString()) {
        alert("El Rut no es válido");
        return false;
      }
    });
});


//validar el formato del correo con jquery
$(document).ready(function() {
    $("#Enviar").click(function() {
      var correo = $("#txtEmail").val();
      var re = /^[^\s@]+@[^\s@]+\.[^\s@]{2,3}$/;
      if (!re.test(correo)) {
        alert("El correo electrónico no es válido");
        return false;
      }
      return true;
    });
});








