import React from 'react';
import { Line } from 'react-chartjs-2';

const Chart = ({sensordata, chartlabel, chartbgcolor, chartbordercolor}) => {

    const data = {
        labels: Object.keys(sensordata),
        datasets: [
          {
            label: chartlabel,
            data: Object.values(sensordata),
            fill: false,
            tension: 0.2,
            backgroundColor: chartbgcolor,
            borderColor: chartbordercolor,
          },
        ],
    };

    const options = {
        responsive: true,
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
              },
            },
          ],
        },
    };

    return (
    <>
        <div className='header'>
            <h1 className='title'>Test</h1>
        </div>
        <Line data={data} options={options} />
    </>);
}

export default Chart;