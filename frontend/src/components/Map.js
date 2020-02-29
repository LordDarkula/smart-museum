import React, { useState } from "react";
import "../style/App.css";
import GoogleMapReact from "google-map-react";

import MapMarker from "./MapMarker";
import CollectionModal from "./CollectionModal";

function Map(props) {
  const [activeMuseum, setActiveMuseum] = useState("");

  // Centered on Georgia Tech
  const [center] = useState({ lat: 33.776033, lng: -84.39884086 });
  const [zoom] = useState(15);

  // For modal in map marker
  const [isModalOpen, setIsModalOpen] = useState(false);
  const toggleModal = _ => {
    setIsModalOpen(!isModalOpen);
  };

  const dropPins = _ => {
    let markers = [];
    props.data.forEach(museum => {
      markers.push(
        <MapMarker
          lat={museum.coordinates[0]}
          lng={museum.coordinates[1]}
          name={museum.name}
          toggleModal={toggleModal}
          activeMuseum={activeMuseum}
          setActiveMuseum={setActiveMuseum}
        />
      );
    });
    return markers;
  };

  return (
    <div>
      <div style={{ height: "100vh", width: "100%" }}>
        <GoogleMapReact
          defaultCenter={center}
          defaultZoom={zoom}
          bootstrapURLKeys={{
            key: "AIzaSyBJ4VRIYNr-uMXPBN0BAgdeGrkU9SSypRs",
            language: "en"
          }}
        >
          {dropPins()}
        </GoogleMapReact>
      </div>
      {/* Collection Modal */}
      <CollectionModal
        isModalOpen={isModalOpen}
        toggleModal={toggleModal}
        data={props.data}
        activeMuseum={activeMuseum}
        setActiveMuseum={setActiveMuseum}
      />
    </div>
  );
}

export default Map;
