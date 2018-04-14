d3.json("static/JS/TopBeersLocation.json", function createMarkers(data) {

    var beerMarkers = [];
    var mark;
    console.log(data)

    for(var i = 0; i < data.Features.length; i++) {
        var brewery = data.Features[i].name;
        var beer = data.Features[i].beername;
        var style = data.Features[i].style;
        var rating = data.Features[i].rating

            mark = L.circle([data.Features[i].latitude,data.Features[i].longitude],
                {
                    fillColor: 'brown',
                    fillOpacity: 0.5,
                    radius: 20000,
                    stroke: false
                }
            )
            console.log(mark)
            beerMarkers.push(mark.bindPopup("<h1>Beer: "+beer+"</h1> <hr> <h2>Style: "+style+"</h2>  <h2>Brewery: "+brewery+"</h2>  <h2>Rating: "+rating+"</h2>"))
    }
    createMap(L.layerGroup(beerMarkers));
})




function createMap(beerMarkers) {

    // create the tile layer that will be the background of our map
    var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoicnJ3b2xiZXIiLCJhIjoiY2pkd2drY203MDVtbzJ3bzF2NXUxdnNqayJ9.vzgFq7GgYJFYIJoCWDyu7g");

  
    // Create the map object with options
    var myMap = L.map("map", {
      center: [42.73, -100],
      zoom: 4,
      layers: [lightmap, beerMarkers]
    });
  }

