import React from "react";
import FileUpload from "./Components/fileupload";
import Summarizer from "./Components/summarizer";

function App() {
  return (
    <div className="App">
      <h1>Text Summarizer Tool</h1>
      <FileUpload />
      <Summarizer />
    </div>
  );
}

export default App;
