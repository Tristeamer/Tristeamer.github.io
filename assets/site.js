//site scripting stuff

var x = 0;
var sitetext = "site text <br>";
var sitivt = 5;

function site() {
  if (x < sitetext.length) {
    document.getElementById("site").innerHTML += sitetext.charAt(x);
    x++;
    setTimeout(site, sitivt);
  }
}

setTimeout(() => {site();}, 3300);