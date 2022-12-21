async function getrouteData() {
    // The await keyword lets js know that it needs to wait until it gets a response back to continue.
    var response = await fetch("https://maps.googleapis.com/maps/api/distancematrix/json?origins=5905%20Muddy%20Creek%20Road,%20Cincinnati,%20OH%2045233&destinations=7544%20Burlington%20Pike,%20Florence,%20KY%2041042&units=imperial&key=AIzaSyC81PU439FQUFkQ1OItr9xnXyqXaVV_dxs");
    // We then need to convert the data into JSON format.
    var coderData = await response.json();
    return coderData;
}
    
console.log(getrouteData());



function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 13,
    center: { lat: 89.1031, lng: -84.5120 },
});
const trafficLayer = new google.maps.TrafficLayer();

trafficLayer.setMap(map);
}

window.initMap = initMap;
