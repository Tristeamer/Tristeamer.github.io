//site scripting stuff

var x = 0;
var y = 0;
var sitel1 = "This site isn't really finished but lowkey I have no idea what to even put here so its empty asf <3";
var sitel2 = "test";
var sitivt = 5;

function site() {
  if (x < sitel1.length) {
    document.getElementById("site").innerHTML += sitel1.charAt(x);
    x++;
    setTimeout(site, sitivt);
  }
}
setTimeout(() => {site();}, 3300);