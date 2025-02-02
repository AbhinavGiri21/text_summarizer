import React, { useState, useEffect } from "react";
import axios from "axios";
import "./summarizer.css";

const loadingMessages = [
    "Summarizing your text...",
    "This will take some time...",
    "Getting ready...",
    "Processing your request...",
    "Almost done...",
    "Hang tight, we're on it...",
    "Just a moment...",
    "Finalizing the details...",
    "Bringing it all together...",
    "Loading your summary..."
];

const SummarizerUpload = () => {
    const [text, setText] = useState("");
    const [summary, setSummary] = useState("");
    const [message, setMessage] = useState("");
    const [loading, setLoading] = useState(false);
    const [loadingText, setLoadingText] = useState(loadingMessages[0]);

    useEffect(() => {
        let interval;
        if (loading) {
            let index = 0;
            interval = setInterval(() => {
                index = (index + 1) % loadingMessages.length;
                setLoadingText(loadingMessages[index]);
            }, 2000);
        } else {
            clearInterval(interval);
        }
        return () => clearInterval(interval);
    }, [loading]);

    const handleSummarize = async () => {
        if (!text) {
            setMessage("Please enter some text to summarize.");
            return;
        }

        setLoading(true);
        const requestData = {
            text: text,
            type: "medium",
        };

        try {
            const response = await axios.post('http://127.0.0.1:5000/summarize', requestData);
            setSummary(response.data.summary);
        } catch (error) {
            console.error('Error summarizing text:', error);
            setMessage('Error summarizing text');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="container">
            {loading && (
                <div className="loading-overlay">
                    <p className="loading-text">{loadingText}</p>
                </div>
            )}
            <h1>Text Summarizer Tool</h1>
            <div className="summarizer-container">
                <div className="textareas">
                    <textarea
                        className="text-area"
                        placeholder="Enter text to summarize"
                        value={text}
                        onChange={(e) => setText(e.target.value)}
                    ></textarea>
                    <textarea
                        className="text-area"
                        placeholder="Summary will appear here"
                        value={summary}
                        readOnly
                    ></textarea>
                </div>
                <div className="controls">
                    <select onChange={(e) => setSummary(e.target.value)}>
                        <option value="short">Short</option>
                        <option value="medium">Medium</option>
                        <option value="detailed">Detailed</option>
                    </select>
                    <button onClick={handleSummarize}>Summarize</button>
                </div>
            </div>

            {message && <p>{message}</p>}
        </div>
    );
};

export default SummarizerUpload;
