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
            backgroundColor: chartbgcolor,
            borderColor: chartbordercolor,
          },
        ],
    };

    const options = {
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
            <h1 className='title'>Line Chart</h1>
        </div>
        <Line data={data} options={options} />
    </>);
}

export default Chart;