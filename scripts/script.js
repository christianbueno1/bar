var http_request = false;

function makeRequest(url){
    http_request = false;
    if (window.XMLHttpRequest) { // Mozilla, Safari,...
        http_request = new XMLHttpRequest();
        if (http_request.overrideMimeType) {
            http_request.overrideMimeType('application/json');
            // Ver nota sobre esta linea al final
        }
    } else if (window.ActiveXObject) { // IE
        try {
            http_request = new ActiveXObject("Msxml2.XMLHTTP");
        } catch (e) {
            try {
                http_request = new ActiveXObject("Microsoft.XMLHTTP");
            } catch (e) {}
        }
    }

    if (!http_request) {
        alert('Falla :( No es posible crear una instancia XMLHTTP');
        return false;
    }
    http_request.onreadystatechange = fullContent;
    http_request.open('GET', url, true);
    http_request.send(null);
}
function fullContent(){
    if (http_request.readyState == 4) {
        if (http_request.status == 200) {
            /*Aquí deben procesar el JSON y mostrar la respuesta en el HTML
            Utilice JSON.parse() para convertir la respuesta en un objeto
            */
            var jsondata = JSON.parse(http_request.responseText);
            // console.log(jsondata);
            // console.log(jsondata[2]["calorias"]);

            // var h2platillo = document.getElementById("h2platillo0");
            var pnutricional = document.getElementById("pnutricional0");
            // var pname = document.getElementById("pname0");
            // var pfacultad = document.getElementById("pfacultad0");

            // pnutricional.innerHTML = "<span> hello</span>";
            // pnutricional.insertAdjacentHTML("afterend", "<p>hello</p>");
            // pnutricional.outerHTML = "<p> hello </p>";

            // h2platillo.innerHTML = titleCase(jsondata[0]["platillo"]);
            // pnutricional.innerHTML += "<span> calorias: "+jsondata[0]["calorias"]+", grasa: "+jsondata[0]["grasa"]+", carbohidratos: "+jsondata[0]["carbohidratos"]+", proteinas: "+jsondata[0]["proteinas"]+"</span>";
            // pname.innerText =titleCase(jsondata[0]["nombre"]);
            // pfacultad.innerHTML = jsondata[0]["facultad"].toUpperCase();

            // for (i in jsondata) {
            //     console.log(jsondata[i]);
            //     for(ii in jsondata[i]) {
            //         console.log(ii);
            //     }
            // }

            var h2platillo;
            var pnutricional;
            var pname;
            var pfacultad;
            for(i in jsondata) {
                var h2platillo = document.getElementById("h2platillo"+i);
                var pnutricional = document.getElementById("pnutricional"+i);
                var pname = document.getElementById("pname"+i);
                var pfacultad = document.getElementById("pfacultad"+i);
                h2platillo.innerHTML = titleCase(jsondata[i]["platillo"]);
                pnutricional.innerHTML += "<span> calorias: "+jsondata[i]["calorias"]+", grasa: "+jsondata[i]["grasa"]+", carbohidratos: "+jsondata[i]["carbohidratos"]+", proteinas: "+jsondata[i]["proteinas"]+"</span>";
                pname.innerText =titleCase(jsondata[i]["nombre"]);
                pfacultad.innerHTML = jsondata[i]["facultad"].toUpperCase();                             
            }
        } else {
            alert('Hubo problemas con la petición.');
        }
    }    
}

window.onload = function() {
    makeRequest("https://api.myjson.com/bins/t6ulz");
}