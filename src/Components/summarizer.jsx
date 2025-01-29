import React, { useState } from "react";
import axios from "axios";

const Summarizer = () => {
    const [text, setText] = useState("");
    const [summary, setSummary] = useState("");
    const [type, setType] = useState("medium");

    const handleSummarize = async () => {
        try {
            const response = await axios.post("http://127.0.0.1:5000/summarize", {
                text,
                type,
            });
            setSummary(response.data.summary);
        } catch (error) {
            console.error("Error summarizing text", error);
        }
    };

    return (
        <div>
            <textarea
                rows="10"
                cols="50"
                placeholder="Enter text to summarize"
                onChange={(e) => setText(e.target.value)}
            ></textarea>
            <select onChange={(e) => setType(e.target.value)}>
                <option value="short">Short</option>
                <option value="medium">Medium</option>
                <option value="detailed">Detailed</option>
            </select>
            <button onClick={handleSummarize}>Summarize</button>
            <p>{summary}</p>
        </div>
    );
};

export default Summarizer;
