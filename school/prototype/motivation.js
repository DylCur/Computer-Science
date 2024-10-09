let messages = [
  "You have had {} more showers this week",
  "You have had {} less calories this week",
  "Good Morning"
];

let number = [
  12,
  31,
  15
]

var rand = Math.floor(Math.random()*messages.length);
var randNum = Math.floor(Math.random()*messages.length);

console.log(document);

if(messages[rand].indexOf("{}" > -1)){
  let temp = messages[rand].replace("{}", number[randNum])
  document.getElementById('motiv').textContent = temp;
}

else{
  document.getElementById('motiv').textContent = messages[rand];
}

// motiv.textContent = messages[rand];