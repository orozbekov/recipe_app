const getElement = (selector) => {
  const element = document.querySelector(selector)

  if (element) return element
  throw Error(
    `Please double check your class names, there is no ${selector} class`
  )
}

var counter = 2;
setInterval(function() {
   document.getElementById('radio' + counter).checked = true;
   counter++;
   if(counter > 5){
      counter = 1;
   }
},5000);