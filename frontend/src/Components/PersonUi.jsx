import React from "react";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";

function PersonUi({ person }) {
  return (
    <Card style={{ width: "18rem" }}>
      <Card.Img variant="top" src={person.img} />
      <Card.Body>
      <Card.Title>{person.name}</Card.Title>
        <Card.Title>{person.post}</Card.Title>
        <Card.Text>{person.specialization}</Card.Text>
        {/* <Button variant="primary">Go somewhere</Button> */}
      </Card.Body>
    </Card>
  );
}

export default PersonUi;
