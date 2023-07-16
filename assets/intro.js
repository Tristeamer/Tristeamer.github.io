//intro scripting stuff

document.getElementById("name").innerHTML = "[user@tristeamer.github.io]$ ";

var i = 0;
var line = "sudo chmod +X website.sh && ./website.sh";
var intivt = 60;

function intro() {
  if (i < line.length) {
    document.getElementById("intro").innerHTML += line.charAt(i);
    i++;
    setTimeout(intro, intivt);
  }
}

setTimeout(() => {intro();}, 500);