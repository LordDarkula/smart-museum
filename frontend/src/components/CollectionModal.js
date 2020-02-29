import React, { useState, useEffect } from "react";
import "../style/App.css";

import ImageMasonry from "react-image-masonry";
import { Button, Modal, ModalBody, ModalFooter } from "reactstrap";

function CollectionModal(props) {
  const [activeCollection, setActiveCollection] = useState("");
  const [activeMuseumCollections, setActiveMuseumCollections] = useState([]);

  const [buttonText, setButtonText] = useState(["View in VR"]);

  useEffect(_ => {
    prepModal();
  });

  let prepModal = _ => {
    console.log("Prepping modal");
    props.data.forEach(m => {
      if (m.name === props.activeMuseum) {
        //FIXME: Might be running extra times
        // Load current preview images
        setActiveMuseumCollections(m.collections);
        if (!activeCollection) {
          // Pre-select a collection if there isn't one selected
          setActiveCollection(m.collections[0].name);
        }
      }
    });
  };

  let exitModal = _ => {
    console.log("Cleaning up modal");
    props.setActiveMuseum("");
    // TODO: Commenting this next line might allow you to cache a collection someone hits twice (tiny improvement in speed lol)
    setActiveMuseumCollections([]);
    setActiveCollection("");
    props.toggleModal();
  };

  let startVR = _ => {
    setButtonText("Loading ...");
    //TODO: Change this to an API call
    let url = `http://127.0.0.1:5000/start/${props.activeMuseum}/${activeCollection}`;
    fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json"
      }
    })
      .then(res => {
        console.log(res.status);
        if (res.status === 200) {
          // TODO: Have another modal for "View in VR, everything loaded!"
          // Maybe have a png of someone using a VR headset
          setButtonText("View in VR");
          exitModal();
        } else {
          setButtonText("Error ...");
        }
      })
      .catch(e => {
        console.log(e);
      });
  };

  let buildTabs = _ => {
    let tabs = [];
    activeMuseumCollections.forEach((c, i) => {
      tabs.push(
        <span
          key={i}
          onClick={_ => {
            setActiveCollection(c.name);
          }}
          className={c.name === activeCollection ? "activeTab" : "tab"}
        >
          {c.name}{" "}
        </span>
      );
    });
    return tabs;
  };

  let renderImages = _ => {
    let imageURLs = [];
    activeMuseumCollections.forEach((c, i) => {
      if (activeCollection === c.name) {
        let keys = Object.keys(c.images);
        keys.forEach(key => {
          imageURLs.push(c.images[key]);
        });
      }
    });
    return <ImageMasonry imageUrls={imageURLs} numCols={3} scrollable />;
  };

  return (
    <div>
      <Modal isOpen={props.isModalOpen} toggle={exitModal} size="xl">
        <ModalBody>
          <h1>{props.activeMuseum}</h1>
          {buildTabs()}
          <div className="image-container">{renderImages()}</div>
        </ModalBody>
        <ModalFooter>
          <Button color="primary" onClick={startVR}>
            {buttonText}
          </Button>{" "}
          <Button color="secondary" onClick={exitModal}>
            Cancel
          </Button>
        </ModalFooter>
      </Modal>
    </div>
  );
}

export default CollectionModal;
