var soildData = {}

fetch('/api/soil').then(function (response) {
    return response.json();
}).then(function (data) {
    drawSoilChart(data);
});

fetch('/api/temp').then(function (response) {
    return response.json();
}).then(function (data) {
    drawTempChart(data);
});

function drawSoilChart(information) {
    const data = {
        labels: Object.keys(information),
        datasets: [{
            label: 'My First dataset',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: Object.values(information),
            pointStyle: 'line',
        }]
    };

    const config = {
        type: 'line',
        data: data,
        options: {}
    };

    const myChart = new Chart(
        document.getElementById('myChart'),
        config
    );
}

function drawTempChart(information) {
    const data = {
        labels: Object.keys(information),
        datasets: [{
            label: 'My First dataset',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: Object.values(information),
            pointStyle: 'line',
        }]
    };

    const config = {
        type: 'line',
        data: data,
        options: {}
    };

    const tempChart = new Chart(
        document.getElementById('tempChart'),
        config
    );
}

document.getElementById('burger').onclick = function () {
    document.getElementById('burger').classList.toggle('is-active');
    document.getElementById('navbarBasicExample').classList.toggle('is-active');
};