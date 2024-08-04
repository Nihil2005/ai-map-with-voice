import React, { useEffect, useRef } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

const CommandProcessor = ({ command }) => {
    const mapRef = useRef(null);
    const mapInstance = useRef(null);

    useEffect(() => {
        if (!mapInstance.current) {
            mapInstance.current = L.map(mapRef.current).setView([20, 0], 2);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 19,
            }).addTo(mapInstance.current);
        }
    }, []);

    useEffect(() => {
        if (command) {
            processCommand(command);
        }
    }, [command]);

    const processCommand = async (command) => {
        const lowerCaseCommand = command.toLowerCase();
        if (lowerCaseCommand.includes('go to')) {
            const place = lowerCaseCommand.replace('go to', '').trim();
            try {
                const response = await fetch(`https://nominatim.openstreetmap.org/search?q=${place}&format=json`);
                const data = await response.json();
                if (data && data.length > 0) {
                    const { lat, lon } = data[0];
                    mapInstance.current.setView([lat, lon], 10);
                } else {
                    alert('Place not found');
                }
            } catch (error) {
                console.error('Error in geocoding:', error);
            }
        } else if (lowerCaseCommand.includes('zoom in')) {
            mapInstance.current.zoomIn();
        } else if (lowerCaseCommand.includes('zoom out')) {
            mapInstance.current.zoomOut();
        }
    };

    return <div id="map" ref={mapRef} style={{ width: '100%', height: '600px' }}></div>;
};

export default CommandProcessor;
