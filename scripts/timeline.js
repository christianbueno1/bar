var http_request = false;
var nIntervId;
var count = 0;

function makeRequest(url) {
    http_request = false;
    if (window.XMLHttpRequest) {
        http_request = new XMLHttpRequest();
        if (http_request.overrideMimeType) {
            http_request.overrideMimeType('application/json');
        }
    }else if (window.ActiveXObject) {
        try {
            http_request = new ActiveXObject("Msxml2.XMLHTTP");
        } catch (e) {
            try {
                http_request = new ActiveXObject("Microsoft.XMLHTTP");
            } catch (e) {
                
            }
        }
    }
    if (!http_request) {
        alert('Falla no es posible crear una instancia XMLHTTP');
        return false;
    }
    http_request.onreadystatechange = timeLine;
    http_request.open('GET',url, true);
    http_request.send(null);
}
function timeLine(){
    if (http_request.readyState == 4) {
        if (http_request.status == 200) {

            function myTop2() {
                // esto es solo para procar el timeline con diferentes datos
                if (count == 6) {
                    count = 0;
                }
                // here
                var jsondata = JSON.parse(http_request.responseText);
                var myfdiv = document.querySelector('section> div');
                var mdiv = document.createElement('div');
                var myh2date = document.createElement('h2');
                myh2date.classList.add("text-center","mydate","pt-3");          
                var today = new Date();
                var dd = today.getDate();
                // var mm = today.getMonth()+1; //January is 0!
                var yyyy = today.getFullYear();
                myh2date.textContent = today.getDayName()+" "+dd+" de "+today.getMonthName()+" del "+yyyy+" time: "+ today.getHours()+":"+today.getMinutes()+":"+today.getSeconds();
                var left_or_right = "left";
                mdiv.appendChild(myh2date);
                
                for (var i=0; i<2; i++){
                    var mycontainer = document.createElement('div');
                    var content = document.createElement('div');
                    var myh2dish = document.createElement('h2');
                    var myimgdish = document.createElement('img');
                    var mystrong_rest = document.createElement('strong');
                    var myprest = document.createElement('p');
                    var mystrong_facu = document.createElement('strong');
                    var mypfacu = document.createElement('p');
                    var mystrong_punt = document.createElement('strong');
                    var myppunt = document.createElement('p');
    
                    mdiv.classList.add("timeline");
    
                    if(i==1){
                        left_or_right = "right";
                    }
                    mycontainer.classList.add("mycontainer",left_or_right);
                    content.classList.add("content");
                    myh2dish.classList.add("text-center");
                    myimgdish.setAttribute('src','img/servilleta/'+jsondata[i+count].image);
                    myimgdish.setAttribute('alt','pollo al vino');
                    myimgdish.classList.add("imgsize","rounded");
                    myprest.classList.add("d-inline-block");
                    mypfacu.classList.add("d-inline-block");
                    myppunt.classList.add("d-inline-block");                var today = new Date();
                    var dd = today.getDate();
                    // var mm = today.getMonth()+1; //January is 0!
                    var yyyy = today.getFullYear();
                    myh2date.textContent = today.getDayName()+" "+dd+" de "+today.getMonthName()+" del "+yyyy+" time: "+ today.getHours()+":"+today.getMinutes()+":"+today.getSeconds();
    
                    // console.log(jsondata[i].platillo);
                    myh2dish.textContent = titleCase(jsondata[i+count].platillo);
                    mystrong_rest.textContent = "Restaurante: ";
                    myprest.textContent = titleCase(jsondata[i+count].nombre);
                    mystrong_facu.textContent = "Facultad: ";
                    mypfacu.textContent = jsondata[i+count].facultad.toUpperCase();
                    mystrong_punt.textContent = "Puntaje: ";
                    myppunt.textContent = jsondata[i+count].puntaje;
                    content.appendChild(myh2dish);
                    content.appendChild(myimgdish);
                    content.appendChild(mystrong_rest);
                    content.appendChild(myprest);
                    content.appendChild(document.createElement('br'));
                    content.appendChild(mystrong_facu);
                    content.appendChild(mypfacu);
                    content.appendChild(document.createElement('br'));
                    content.appendChild(mystrong_punt);
                    content.appendChild(myppunt);
                    mycontainer.appendChild(content);                
                    mdiv.appendChild(mycontainer);
                }            
                // console.log(myh2date);
                // console.log(today.getMonthName);
                myfdiv.insertAdjacentElement('beforebegin',mdiv);
                count+=2;
            }


            // nIntervId = setInterval(()=>{
            //     console.log("hello rr");
            // },2000);
            nIntervId = setInterval(myTop2,2000);
          
        }else {
            alert('Hubo problemas con la peticion');
        }
    }
}

window.onload = function() {
    makeRequest('data/timeline-data.json');
}

function stop() {
    clearInterval(nIntervId);
}  
