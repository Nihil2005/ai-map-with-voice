import React, { useEffect, useState } from 'react';

const VoiceCommands = ({ onCommand }) => {
    const [spokenText, setSpokenText] = useState('');

    useEffect(() => {
        if (!('webkitSpeechRecognition' in window)) {
            alert('Your browser does not support speech recognition.');
            return;
        }

        const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.continuous = true;
        recognition.interimResults = false;
        recognition.lang = 'en-US';

        recognition.onresult = (event) => {
            const lastResult = event.results[event.results.length - 1];
            if (lastResult.isFinal) {
                const command = lastResult[0].transcript.trim();
                setSpokenText(command);
                onCommand(command);
            }
        };

        recognition.start();

        return () => recognition.stop();
    }, [onCommand]);

    return (
        <div>
            <p>Spoken Text: {spokenText}</p>
        </div>
    );
};

export default VoiceCommands;
