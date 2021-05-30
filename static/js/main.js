const socket = io();

document.querySelector("textarea").addEventListener('keyup', function (e) {
  if (e.keyCode === 13) {
    if (this.value.trim() === "") {
      return false;
    }
    socket.emit('send_message', {'msg': this.value.trim()});
    this.value = "";
  }
});

socket.on('connect', function() {
  socket.emit('connect_user', {'data': `user connected!`});
});

const maxMsgOnPage = 10;
let p = "";
let nav = '';
let br = ''
let idForElement = 1;
let countCircleMsg = 0;

socket.on('take_msg', function(msg, online) {
  console.log(msg, online);
  let online_block = document.getElementsByClassName('online');
  online_block.innerHTML = `Онлайн на сайте: ${online}`
  nav = document.createElement('nav')
  nav.innerHTML = 'test';
  nav.id = idForElement;
  p = document.createElement("p");
  p.innerHTML = msg;
  p.id = idForElement;
  br = document.createElement("br");
  br.id = idForElement++
  if (idForElement > maxMsgOnPage + 1 || countCircleMsg === 1) {
    if ((countCircleMsg === 1 || countCircleMsg === 0) && idForElement > maxMsgOnPage + 1) {
      idForElement = 1;
      countCircleMsg = 1;
    }
    let name = document.getElementById(`${idForElement}`);
    name.remove();
    let user_msg = document.getElementById(`${idForElement}`);
    user_msg.remove();
    let el_br = document.getElementById(`${idForElement}`);
    el_br.remove();
  }
  document.querySelector(".message").appendChild(nav);
  document.querySelector(".message").appendChild(p);
  document.querySelector(".message").appendChild(br);
})