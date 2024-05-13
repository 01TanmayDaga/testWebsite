import { useEffect, useState } from "react";
import "./App.css";
import PersonUi from "./Components/PersonUi";
import axios from "axios";

function App() {
  const [data, setData] = useState([]);
  const config = {
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS"
    }
  };

  axios
    .get("http://localhost:8000/aboutpage/api",config)
    .then((res) => {
      res = res.data;
      setData(res);
    })
    .catch((err) => {
      console.log(err);
    });

  return (
    <div
      className="container"
      style={{
        display: "grid",
        gridTemplateRows: "repeat(3, minmax(0, 1fr))",
      }}
    >
      {data.map((ele) => {
        return <PersonUi person={ele} />;
      })}
    </div>
  );
}

export default App;
