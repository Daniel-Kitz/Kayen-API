import React, { useState, useEffect } from 'react';
import Chart from './components/Chart.js';
import Topbar from './components/topbar/Topbar.js';

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
          setSoil(data)
        }
      )
      fetch("/api/temp").then(
        res => res.json()
      ).then(
        data => {
          setTemp(data)
        }
      )
      fetch("/api/humid").then(
        res => res.json()
      ).then(
        data => {
          setHumid(data)
        }
      )
    }, 20000);
  }, []);

  return (
    <>
      <Topbar />
    </>
  );
}

export default App
