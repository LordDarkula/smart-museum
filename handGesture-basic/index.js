const video = document.getElementById("myvideo");
const canvas = document.getElementById("canvas");
const context = canvas.getContext("2d");

let isVideo = false;
let model = null;
let loc = "center";

const modelParams = {
  flipHorizontal: true, // flip e.g for video
  maxNumBoxes: 20, // maximum number of boxes to detect
  iouThreshold: 0.5, // ioU threshold for non-max suppression
  scoreThreshold: 0.6 // confidence threshold for predictions.
};

function startVideo() {
  handTrack.startVideo(video).then(function(status) {
    console.log("video started", status);
    if (status) {
      isVideo = true;
      runDetection();
      //drawBounds();
    } else {
      updateNote.innerText = "Please enable video";
    }
  });
}

function disable() {
  isActive = false;
}

function runDetection() {
  model.detect(video).then(predictions => {
    processPredictions(predictions);
    model.renderPredictions(predictions, canvas, context, video);
    if (isVideo) {
      requestAnimationFrame(runDetection);
    }
  });
}

function drawBounds() {
  var canvas = document.getElementById("canvas");
  width = window.innerWidth / 2;
  height = window.innerHeight;
  var c = canvas.getContext("2d");
  c.beginPath();
  c.rect(0, 0, 0.25 * width, height);
  c.rect(0.75 * width, 0, 0.25 * width, height);
  c.stroke();
}

// Load the model.
handTrack.load(modelParams).then(lmodel => {
  // detect objects in the image.
  model = lmodel;
  updateNote.innerText = "Loaded Model!";
  trackButton.disabled = false;
});
startVideo();

let isActive = false;

let processPredictions = predictions => {
  drawBounds();
  var filtered_preds = [];

  predictions.forEach(prediction => {
    if (prediction.score >= 0.75) {
      filtered_preds.push(prediction);
    }
  });
  //console.log(filtered_preds)

  if (filtered_preds.length > 0) {
    w = window.innerWidth / 2;
    h = window.innerHeight;
    hand = filtered_preds[0];
    // Filter out by confidence > 0.70
    box = hand.bbox;
    x = box[0];
    y = box[1];
    width = box[2];
    height = box[3];
    cX = x + width / 2;
    //maxx = x + width
    swipeLeft = w * 0.3;
    swipeRight = 0.8 * w;
    //console.log(w, cX)
    cY = y + height / 2;
    confidence = hand["score"];
    if (loc == "center") {
      if (cX < swipeLeft) {
        console.log("You swiped left.");
        fetch("http://127.0.0.1:5000/update/left", {
          method: "GET",
          headers: {
            "Content-Type": "application/json"
          }
        })
          .then(res => {
            return res.json();
          })
          .then(res => {
            console.log(res);
          })
          .catch(e => {
            console.log(e);
          });
        //isActive = true
        loc = "left";
        //setTimeout(disable, 5000)
      } else if (cX > swipeRight) {
        console.log("You swiped right.");
        fetch("http://127.0.0.1:5000/update/right", {
          method: "GET",
          headers: {
            "Content-Type": "application/json"
          }
        })
          .then(res => {
            return res.json();
          })
          .then(res => {
            console.log(res);
          })
          .catch(e => {
            console.log(e);
          });
        //isActive = true
        loc = "right";
        //setTimeout(disable, 5000)
      }
      //console.log("Predictions: ", hand, cX, cY);
    } else {
      if (cX > swipeLeft && cX < swipeRight) {
        loc = "center";
      }
    }
  }
};

// test
