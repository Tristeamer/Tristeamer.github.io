//site scripting stuff

var x = 0;
var sitel1 = "Welcome to my site!! :) (this page is still a work in progress but that's probably pretty evident lmao)";
var sitivt = 5;

function site() {
  if (x < sitel1.length) {
    document.getElementById("site").innerHTML += sitel1.charAt(x);
    x++;
    setTimeout(site, sitivt);
  }
}


setTimeout(() => {site();}, 3300);