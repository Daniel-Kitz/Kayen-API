let model;
let class_indices;
let fileUpload = document.getElementById('uploadImage')
let img = document.getElementById('image')
let progressbar = document.getElementsByClassName('.progress')

async function fetchData() {
    let response = await fetch('./class_indices.json');
    let data = await response.json();
    data = JSON.stringify(data);
    data = JSON.parse(data);
    return data;
}

// Initialize/Load model
async function initialize() {
    let status = document.getElementById('currentprogressstatus')
    status.innerHTML = 'Recognizing Image... <span class="fa fa-spinner fa-spin"></span>'
    model = await tf.loadLayersModel('./tensorflowjs-model/model.json');
    status.innerHTML = 'Image Recognized!  <span class="fa fa-check"></span>'
}

async function predict() {
    // Function for invoking prediction
    let img = document.getElementById('image')
    let offset = tf.scalar(255)
    let tensorImg = tf.browser.fromPixels(img).resizeNearestNeighbor([224, 224]).toFloat().expandDims();
    let tensorImg_scaled = tensorImg.div(offset)
    prediction = await model.predict(tensorImg_scaled).data();

    fetchData().then((data) => {
        predicted_class = tf.argMax(prediction)
        class_idx = Array.from(predicted_class.dataSync())[0]
        document.querySelector('.pred_class').innerHTML = data[class_idx]
        document.querySelector('.accuracy').innerHTML = `With an accuracy of ${parseFloat(prediction[class_idx] * 100).toFixed(2)}%`
        progressbar.value = `${parseFloat(prediction[class_idx] * 100).toFixed(2)}`;
        console.log(data)
        console.log(data[class_idx])
        console.log(prediction)

    }
    );

}


fileUpload.addEventListener('change', function (e) {
    let file = this.files[0]
    if (file) {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.addEventListener("load", function () {
            img.style.display = "block"
            img.setAttribute('src', this.result);
        });
    }

    else {
        img.setAttribute("src", "");
    }

    initialize().then(() => {
        predict()
    })
})