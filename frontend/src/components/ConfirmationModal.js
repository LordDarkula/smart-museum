import React, { useState } from "react";
import "../style/App.css";

import { Button, Modal, ModalBody, ModalFooter } from "reactstrap";

function ConfirmationModal(props) {
  const [isModalOpen, setIsModalOpen] = useState(true);

  let toggleModal = _ => {
    setIsModalOpen(!isModalOpen);
    window.location.reload();
  };

  return (
    <div>
      <Modal isOpen={isModalOpen} toggle={toggleModal} size="xl">
        <ModalBody>
          <h1>{props.success ? "Your VR Experience is Ready" : "Uh oh ..."}</h1>
          <p>
            {props.success
              ? "Place the phone in the Google Cardboard and interact with the gesture detector."
              : "There was an error creating your VR experience. Please check your network connection."}
          </p>
          <div className="modal-img">
            <img
              style={{ width: "50%" }}
              src={
                props.success
                  ? require("../images/mark.png")
                  : require("../images/sad.png")
              }
              alt="emoji"
            />
          </div>
          {/* TODO: Throw in an image of VR person PNG */}
        </ModalBody>
        <ModalFooter>
          <Button color="primary" onClick={toggleModal}>
            Ok
          </Button>{" "}
        </ModalFooter>
      </Modal>
    </div>
  );
}

export default ConfirmationModal;
