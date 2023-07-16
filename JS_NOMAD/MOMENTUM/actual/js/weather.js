const API_KEY = "f192c0ae8a13333604f029d533ed2b8f"



function onGeoOk(position) {
    console.log(position)
    const lat = position.coords.latitude
    const lon = position.coords.longitude
    console.log("YOU LIVE IT", lat, lon)
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`
    // console.log(url)
    fetch(url)
      .then(response => response.json())
      .then(data=>{
        const weather = document.querySelector("#weatehr span:first-child")
        const city = document.querySelector("#weatehr span:last-child")
        city.innerText =  data.name
        weather.innerText = `${data.weather[0].main} / ${data.main.temp}`
      // console.log(data.name, data.weather[0].main)
    })
}
function onGeoError() {
  alert("위치를 찾을 수 없어서 날씨 정보를 제공할 수 없습니다.")
}


navigator.geolocation.getCurrentPosition(onGeoOk, onGeoError)


// https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API%20key}