var soildData = {}

fetch('/api/soil').then(function (response) {
    return response.json();
}).then(function (data) {
    drawChart(data, 'Soil', 'soilChart', 'rgb(0, 209, 178)');
});

fetch('/api/temp').then(function (response) {
    return response.json();
}).then(function (data) {
    drawChart(data, 'Temp', 'tempChart', 'rgb(0, 209, 178)');
});

fetch('/api/humid').then(function (response) {
    return response.json();
}).then(function (data) {
    drawChart(data, 'Humidity', 'humidChart', 'rgb(0, 209, 178)');
});

function isMobileDevice() {
    if (window.innerWidth <= "1120") {
        return true
    }
}

function drawChart(information, label, element, chartColor) {
    const data = {
        labels: Object.keys(information),
        datasets: [{
            label: label,
            backgroundColor: chartColor,
            borderColor: chartColor,
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


function toggleModal() {
    document.getElementById('modal').classList.toggle('is-active')
}

function toggleAlert(el) {
    el.parentNode.classList.toggle('is-hidden')
}

function backupChartdata() {
    fetch('/api/backupData').then(function (response) {
        return response.json();
    }).then((data) => {
        if (data == 200) {
            document.getElementById('chartAlertSuccess').classList.toggle('is-hidden')
        }
    });
}

function resetChartdata() {
    fetch('/api/resetData').then(function (response) {
        return response.json();
    }).then((data) => {
        if (data == 200) {
            document.getElementById('chartAlertSuccess').classList.toggle('is-hidden')
        }
    });
}

function importChartdata() {
    fetch('/api/importData').then(function (response) {
        return response.json();
    }).then((data) => {
        if (data == 200) {
            document.getElementById('chartAlertSuccess').classList.toggle('is-hidden')
        }
    });
}