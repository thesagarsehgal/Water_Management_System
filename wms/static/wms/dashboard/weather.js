var  icon;
// city="Sri City";
getWeather(city);
function getWeather(city) { 
  $.getJSON('https://cors-anywhere.herokuapp.com/http://api.openweathermap.org/data/2.5/weather?q='+"Suluru,IN"+'&units=metric&APPID=980c7bce6e29636a5daa7ef7711f0f7e', function(data){         
  //$("#weatherData").html(JSON.stringify(data));
  cityName = city;
  country = data.sys.country;
  temp = data.main.temp;
  // condition ="rainy";
  condition ="no rain";
  

  //icon = data.weather[0].icon;
  humidity = data.main.humidity;
  wind = data.wind.speed;
  $("#location").html(cityName+', '+country);
  $("#temp").html(temp+'\xB0'+'C');
  //var ima="<img src="+"http://openweathermap.org/img/w/"+icon+".png>";
  //document.getElementById('a').style.backgroundImage="url(http://openweathermap.org/img/w/"+data.weather[0].icon+".png)";
  document.getElementById("a").style.backgroundSize = "300px 300px"; 
  document.getElementById("a").style.opacity = "0.7"; 
  $("#icon").html("<img src="+"http://openweathermap.org/img/w/"+icon+".png>");
  // $("#condition").html(condition);
  $("#humidity").html('Humidity: '+humidity+'%');
  $("#wind").html('wind speed: '+wind+'m/s');
  // setBackground();
  });
}
