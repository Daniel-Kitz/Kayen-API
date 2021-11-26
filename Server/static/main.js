var soildData = {}

fetch('/api/soil').then(function (response) {
    return response.json();
}).then(function (data) {
    drawChart(data, 'Soil', 'soilChart');
});

fetch('/api/temp').then(function (response) {
    return response.json();
}).then(function (data) {
    drawChart(data, 'Temp', 'tempChart');
});

fetch('/api/humid').then(function (response) {
    return response.json();
}).then(function (data) {
    drawChart(data, 'Humidity', 'humidChart');
});

function isMobileDevice() {
    //return (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent));
    if (window.innerWidth <= "1120") {
        return true
    }
}

function drawChart(information, label, element) {
    const data = {
        labels: Object.keys(information),
        datasets: [{
            label: label,
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: Object.values(information),
            pointStyle: 'line',
            tension: 0.1
        }]
    };

    const config = {
        type: 'line',
        data: data,
        options: {
            scales: {
                x: {
                    display: !isMobileDevice()
                }
            }
        }
    };

    const drawnChart = new Chart(
        document.getElementById(element),
        config
    );
}


document.getElementById('burger').onclick = function () {
    document.getElementById('burger').classList.toggle('is-active');
    document.getElementById('navbarBasicExample').classList.toggle('is-active');
};