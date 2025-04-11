// Example: App.js
import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [msg, setMsg] = useState("");

  useEffect(() => {
    axios.get("http://localhost:5003/api/hello")
      .then(res => setMsg(res.data.message));
  }, []);

  return <div>{msg}</div>;
}

export default App;
