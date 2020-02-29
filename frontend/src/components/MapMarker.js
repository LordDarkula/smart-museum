import React from "react";
import "../style/marker.css";

function MapMarker(props) {
  return (
    <div>
      <div
        className="pin bounce"
        // Set by default to a red color
        style={{ backgroundColor: "#e74c3c", cursor: "pointer" }}
        title={props.name}
        onClick={_ => {
          props.setActiveMuseum(props.name);
          props.toggleModal();
        }}
      />
      <div className="pulse" />
    </div>
  );
}

export default MapMarker;
