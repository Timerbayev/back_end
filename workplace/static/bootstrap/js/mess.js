const form = document.forms[0]
const butt = document.querySelector('button')
console.log(butt)

//let f  = new FormData()

butt.onclick= function (e) {e.preventDefault(), console.log(form[0].value)};

/*url = '/js/mess.js'
let xhr = new XMLHttpRequest()
xhr.open('POST','../../../templates/block.html',true)
xhr.send()*/