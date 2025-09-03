/* SKILL UP application main page scripts */

window.onload = () => {
  document.body.style.opacity = "1";
}

setInterval(() => {
    //console.log('hey');
}, 1000); // Every second

window.onbeforeunload = () => {
  console.log('bye')
}