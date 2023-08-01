const loader = document.getElementById("loader");
const div1 =  document.getElementById("div1");
const contenedor = document.getElementById("contenedor");

var varGlobal;

function mostrar(){
    varGlobal = setTimeout(verPagina,3000);
    //document.body.style.backgroundImage="url(../img/imagen1.jpeg)";
    //document.body.style.backgroundColor='black';
    document.body.classList.add("imagenloader");

}

document.body.onload = mostrar();

function verPagina(){
    loader.style.display = "none";
    div1.style.display="block";
    document.body.classList.add("cambiar");

  
}
