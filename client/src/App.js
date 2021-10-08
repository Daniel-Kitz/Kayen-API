import React, { useState, useEffect } from 'react';
import Chart from './components/Chart.js';
import Topbar from './components/topbar/Topbar.js';
import Button from '@mui/material/Button';
import BasicCard from './components/BasicCard.js';
import { Card, CardContent, Container, CssBaseline } from '@mui/material';
import { Box } from '@mui/system';

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
    <React.Fragment>
      <CssBaseline>
        <Container>
          <Box sx={{marginTop:'2em', marginBottom:'2em'}}>
            <Button variant="contained">Hello</Button>
          </Box>
          <Box sx={{height: '100vh'}}>
            <Box>
              <Card>
                <CardContent>
                  <Chart sensordata={soil} chartlabel={"soil"} chartbgcolor={"red"} chartbordercolor={"red"}/>
                </CardContent>
              </Card>
            </Box>
          </Box>
        </Container>
      </CssBaseline>
    </React.Fragment>
  );
}

export default App
