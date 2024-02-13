function getStudentGrade() {
    var xhttp = new XMLHttpRequest();
    var submitName = document.getElementById("submitName").value;
    xhttp.open("GET", "http://127.0.0.1:5000/grades/" + submitName);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onload = function() {
    document.getElementById("demo").innerHTML = this.responseText;
    };
    xhttp.send();

    
}
function getGrades() {
  var xhttp = new XMLHttpRequest();
  //ask server for grades, server knows what to do based on the method (ex: "get")
  xhttp.open("GET", "http://127.0.0.1:5000/grades");
  xhttp.setRequestHeader("Content-Type", "application/json");
  xhttp.onload = function() {
    //when we get the grades from the server, display on screen
    document.getElementById("demo").innerHTML = this.responseText;
  };
  xhttp.send();
}
function createNew(){
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "http://127.0.0.1:5000/grades");
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onload = function() {
    document.getElementById("demo").innerHTML = this.responseText;
    };
    const body = {"name": document.getElementById("newName").value, "grade": document.getElementById("newGrade").value}
    xhttp.send(JSON.stringify(body));
}

function editGrades() {
  var xhttp = new XMLHttpRequest();
  var nameOfEdit = document.getElementById("editName").value;
  nameOfEdit = nameOfEdit.replace(/\s/g,"%20");
  xhttp.open("PUT", "http://127.0.0.1:5000/grades/" + nameOfEdit);
  xhttp.setRequestHeader("Content-Type", "application/json");
  xhttp.onload = function() {
    document.getElementById("demo").innerHTML = this.responseText;
  };
  const body = {"grade": document.getElementById("editGrade").value};
  xhttp.send(JSON.stringify(body));
}


function deleteGrade(){
    var xhttp = new XMLHttpRequest();
    var nameToDelete = document.getElementById("deleteStudent").value;
    nameToDelete = nameToDelete.replace(/\s/g,"%20");
    xhttp.open("DELETE", "http://127.0.0.1:5000/grades/" + nameToDelete);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onload = function() {
      document.getElementById("demo").innerHTML = this.responseText;
    };
    xhttp.send();
}
