d3.json("TopBeerLocaations.json", function createMarkers(data) {

    var feature = data.features;
    var beerMarkers = [];
    var mark;

    for(var i = 0; i < feature.length; i++) {
        var brewery = feature[i].properties;
        var coordinates = feature[i].geometry.coordinates;
            mark = L.circle([parseFloat(coordinates[1]),parseFloat(coordinates[0])],
                {
                    fillColor: brown,
                    fillOpacity: 0.5,
                    radius: 50,
                    stroke: false
                }
            )
            beerMarkers.push(mark)
    }
    createMap(L.layerGroup(beerMarkers));
})




function createMap(beerMarkers) {

    // create the tile layer that will be the background of our map
    var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1Ijoia2pnMzEwIiwiYSI6ImNpdGRjbWhxdjAwNG0yb3A5b21jOXluZTUifQ.T6YbdDixkOBWH_k9GbS8JQ");
  
    var beerMarkers = L.layerGroup(beers)
  
    // Create the map object with options
    var myMap = L.map("map", {
      center: [40.73, -130],
      zoom: 4,
      layers: [lightmap, beerMarkers]
    });
  }