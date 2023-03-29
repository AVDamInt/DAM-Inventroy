var deviceDetails = document.getElementById("deviceObj").value;
function myFunction() {
  console.log(JSON.parse(deviceDetails))
  var parsedData = JSON.parse(deviceDetails)
  console.log(parsedData[0].fields)
  var contratto = parsedData[0].fields.contract
  var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
         if (this.readyState == 4 && this.status == 200) {
             alert(this.responseText);
         }
    };
    xhttp.open("GET", 'http://localhost:8013/api/print/text?text=CONTRATTO+'+contratto+'&font_family=DejaVu+Sans+(Oblique)&font_size=70&label_size=39x90&align=left&orientation=standard&margin_top=24&margin_bottom=45&margin_left=35&margin_right=35', true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.setRequestHeader('Access-Control-Allow-Origin', 'localhost');
    xhttp.send();
}

