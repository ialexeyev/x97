/* SKILL UP application main page scripts */

window.onload = () => {
  document.body.style.opacity = "1";
}

setInterval(() => {
    console.log('hey');
}, 6000); // Every minute

window.onbeforeunload = () => {
  console.log('bye')
}