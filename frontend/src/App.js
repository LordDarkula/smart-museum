import React, { useState, useEffect } from "react";
// import logo from "./logo.svg";
import "./style/App.css";

import Map from "./components/Map";

function App() {
  const [data, setData] = useState([]);

  //TODO: Change this to an API call
  useEffect(_ => {
    fetch("http://127.0.0.1:5000/all", {
      method: "GET", // *GET, POST, PUT, DELETE, etc.
      mode: "cors", // no-cors, *cors, same-origin
      cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
      credentials: "same-origin", // include, *same-origin, omit
      headers: {
        // "Content-Type": "application/json"
        "Content-Type": "application/x-www-form-urlencoded"
      }
    })
      // .then(res => {
      //   res.json();
      // })
      .then(res => {
        console.log(res);
        console.log("there");
      })
      .catch(e => {
        console.log(e);
      });
    setData([
      {
        name: "Bartaco",
        coordinates: [33.7789048, -84.4094598],
        collections: [
          {
            name: "Lions",
            images: [
              "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Lion_waiting_in_Namibia.jpg/1200px-Lion_waiting_in_Namibia.jpg",
              "https://cdn.mos.cms.futurecdn.net/J9KeYkEZf4HHD5LRGf799N-320-80.jpg",
              "https://scx1.b-cdn.net/csz/news/800/2019/maasaifarmer.jpg"
            ]
          },
          {
            name: "Tigers",
            images: [
              "https://c402277.ssl.cf1.rackcdn.com/photos/18134/images/hero_small/Medium_WW226365.jpg?1574452099",
              "https://static.scientificamerican.com/blogs/cache/file/CA198B89-ECAE-49FA-82EB4688CA54EBD1_source.jpg?w=590&h=800&28D4B36B-99A8-4B17-8E6A9C0E04277A20",
              "https://www.rd.com/wp-content/uploads/2019/07/Close-up-profile-portrait-of-one-Indochinese-tiger-yawning-or-roaring-mouth-wide-open-and-showing-teeth-low-angle-view.jpg",
              "https://static01.nyt.com/images/2019/05/07/science/06SCI-TIGER1/03SCI-TIGER1-articleLarge.jpg?quality=75&auto=webp&disable=upscale",
              "https://cdn.mos.cms.futurecdn.net/TSqnkJJbXuDTgtdfQkjkcZ-320-80.jpg",
              "https://i.ytimg.com/vi/_UbDeqPdUek/maxresdefault.jpg"
            ]
          }
        ]
      },
      {
        name: "Georgia Tech",
        coordinates: [33.776033, -84.39884086],
        collections: [
          {
            name: "Students",
            images: [
              "https://ichef.bbci.co.uk/news/976/cpsprodpb/D676/production/_110220945_students.jpg"
            ]
          },
          {
            name: "Staff",
            images: [
              "https://image.freepik.com/free-photo/senior-male-professor-explaining-writing-green-chalkboard_23-2148200956.jpg"
            ]
          }
        ]
      }
    ]);
  }, []);

  return (
    <div>
      <Map data={data} />
    </div>
  );
}

export default App;
