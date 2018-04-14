function init() {
    DropdownPopulate()
}

function DropdownPopulate() {
    var url = '/names';
    d3.json(url, function(error, response){
        if (error) {
            return console.warn(error);
        }
    for(var i=0; i<response.length; i++) {
        var sel = document.getElementById('dropdown');
            var opt = document.createElement('option');
            opt.text = response[i];
            opt.value = response[i];
            sel.appendChild(opt);
        }
    });
}

function updateBeerInfo(beer) {
    var name = document.getElementById('beername');
    var style = document.getElementById('beerstyle');
    var brewery = document.getElementById('breweryname');
    var glass = document.getElementById('glass');
    var food_1 = document.getElementById('pairing1');
    var food_2 = document.getElementById('pairing2');
    var food_3 = document.getElementById('pairing3');
    var queryURL = "/advice/" + beer;
    d3.json(queryURL, function (error, response) {
        if (error) return console.warn(error);
        Object.keys(response).forEach(function(key) {
        name.innerText +=  "name:" + response[beer_name];
        style.innerText +=  "style:" + response[beer_style];
        brewery.innerText +=  "brewed by:" + response[brewery_name];
        food_1.src = "" //img paths based on style
        food_2.src = ""
        food_3.src = ""
        })
    });
}

init()