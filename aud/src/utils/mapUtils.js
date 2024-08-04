export const mapCommands = (command) => {
    switch (command) {
        case 0:
            return { zoom: 15 };  // Example command
        case 1:
            return { center: [51.505, -0.09] };  // Example command
        default:
            return {};
    }
};
