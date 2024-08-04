import React from 'react';
import VoiceRecognition from './components/VoiceCommands';
import CommandProcessor from './components/CommandProcessor';
import MapComponent from './components/MapComponent'; // Import MapComponent

const App = () => {
  const [command, setCommand] = React.useState(null);

  return (
    <div>
      <VoiceRecognition onCommand={setCommand} />
      <CommandProcessor command={command} />
      <MapComponent /> {/* Add MapComponent to render the map */}
    </div>
  );
};

export default App;
