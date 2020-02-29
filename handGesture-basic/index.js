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
  isActive = false
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
  var canvas = document.getElementById('canvas');
  width = window.innerWidth / 2;
  height = window.innerHeight;
  var c = canvas.getContext("2d");
  c.beginPath();
  c.rect(0,0,(0.2 * width), height)
  c.rect((0.8 * width), 0, (0.2 * width), height)
  c.stroke()
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
  var filtered_preds = []

  predictions.forEach(prediction => {
    if (prediction.score >= 0.75) {
      filtered_preds.push(prediction)
    }
  })
  //console.log(filtered_preds)
  if (filtered_preds.length > 1) {
    w = window.innerWidth / 2;
    h = window.innerHeight;
    hand1 = filtered_preds[0]
    hand2 = filtered_preds[1]

    box1 = hand1.bbox
    box2 = hand2.bbox
    x1 = box1[0]
    y1 = box1[1]
    width1 = box1[2]
    height1 = box1[3]
    x2 = box2[0]
    y2 = box2[1]
    width2 = box2[2]
    height1 = box1[3]
    cX = x + (width / 2)
    //maxx = x + width
    swipeLeft = w * 0.3
    swipeRight = 0.7 * w
    //console.log(w, cX)
    cY = y + (height / 2)
    confidence = hand["score"]
    if (loc == "center") {
      if (cX < swipeLeft) {
        console.log("You swiped left.")
        //isActive = true
        loc = "left"
        //setTimeout(disable, 5000)
      } else if (cX > swipeRight) {
        console.log("You swiped right.")
        //isActive = true
        loc = "right"
        //setTimeout(disable, 5000)
      }
      //console.log("Predictions: ", hand, cX, cY);
    } else { 
      if (cX > swipeLeft && cX < swipeRight) {
        loc = "center"
      }
    }
  } else if (filtered_preds.length > 0) {
    w = window.innerWidth / 2;
    h = window.innerHeight;
    hand = filtered_preds[0]
    // Filter out by confidence > 0.70
    box = hand.bbox
    x = box[0]
    y = box[1]
    width = box[2]
    height = box[3]
    cX = x + (width / 2)
    //maxx = x + width
    swipeLeft = w * 0.3
    swipeRight = 0.7 * w
    //console.log(w, cX)
    cY = y + (height / 2)
    confidence = hand["score"]
    if (loc == "center") {
      if (cX < swipeLeft) {
        console.log("You swiped left.")
        //isActive = true
        loc = "left"
        //setTimeout(disable, 5000)
      } else if (cX > swipeRight) {
        console.log("You swiped right.")
        //isActive = true
        loc = "right"
        //setTimeout(disable, 5000)
      }
      //console.log("Predictions: ", hand, cX, cY);
    } else { 
      if (cX > swipeLeft && cX < swipeRight) {
        loc = "center"
      }
    }
  }
};


