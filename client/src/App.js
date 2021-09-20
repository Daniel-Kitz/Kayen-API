import React, { useState, useEffect } from 'react';
import Header from './components/Header.js';
import Chart from './components/Chart.js';

function App() {

  const [soil, setSoil] = useState([{}]);
  const [humid, setHumid] = useState([{}]);
  const [temp, setTemp] = useState([{}]);
  useEffect(() => {
    setInterval(() => {
      fetch("/api/soil").then(
        res => res.json()
      ).then(
        data => {
          setHumid(data)
          console.log(data)
        }
      )
      fetch("/api/temp").then(
        res => res.json()
      ).then(
        data => {
          setTemp(data)
          console.log(data)
        }
      )
      fetch("/api/humid").then(
        res => res.json()
      ).then(
        data => {
          setSoil(data)
          console.log(data)
        }
      )
    }, 2000);
  }, []);

  return (
    <>
    <Header />
    <Chart sensordata={soil} chartlabel={'Soild Humidity in %'} chartbordercolor={'rgba(255, 99, 132, 0.2)'} chartbgcolor={'rgb(255, 99, 132)'}/>
    <Chart sensordata={temp} chartlabel={'Temperature in °C'} chartbordercolor={'rgba(132, 99, 255, 0.2)'} chartbgcolor={'rgb(32, 99, 120)'}/>
    <Chart sensordata={humid} chartlabel={'Humidity in %'} chartbordercolor={'rgba(0, 99, 132, 0.2)'} chartbgcolor={'rgb(255, 255, 255)'}/>
    </>
  );
}

export default App
