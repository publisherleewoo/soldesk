import axios from "axios";
import { useState } from "react";

const LeeAJAXFirst = () => {
   const [weather, setWeather] = useState(null);
   const getWeather = () => {
      axios
         .get(
            "https://api.openweathermap.org/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr"
         )
         .then((res) => {
            const description = res.data.weather[0].description;
            const temp = res.data.main.temp;
            const humidity = res.data.main.humidity;
            setWeather({ description, temp, humidity });
         });
   };
   
   return (
      <div>
         <h1>날씨 : {weather && weather.description}</h1>
         <h1>기온 : {weather && weather.temp}</h1>
         <h1>습도 : {weather && weather.humidity}</h1>
         <button onClick={getWeather}>날씨 업데이트</button>
      </div>
   );
};

export default LeeAJAXFirst;
