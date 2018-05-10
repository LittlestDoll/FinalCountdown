// function init() {
//     DropdownPopulate()
// }

// function DropdownPopulate() {
//     var url = '/names';
//     d3.json(url, function(error, response){
//         if (error) {
//             return console.warn(error);
//         }
//     for(var i=0; i<response.length; i++) {
//         var sel = document.getElementById('dropdown');
//             var opt = document.createElement('option');
//             opt.text = response[i];
//             opt.value = response[i];
//             sel.appendChild(opt);
//         }
//     });
// }

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

        name.innerText =  "name:" + response["beer_name"];
        style.innerText =  "style:" + response["beer_style"];
        brewery.innerText =  "brewed by:" + response["brewery_name"];
        //glass.src = "static/glasses/" + pairlookup(response["beer_style"], glassimg);
        food_1.src = "static/pairings/" + pairlookup(response["beer_style"], pairing1img); //img paths based on style
        food_2.src = "static/pairings/" + pairlookup(response["beer_style"], pairing2img); 
        food_3.src = "static/pairings/" + pairlookup(response["beer_style"], pairing3img); 
    });
}

function pairlookup(style, ref) {
    var data = require('static/js/beer_styles.json');
    var output = data.style.ref;

    return output;
}

function optionChanged() {
    var name = document.getElementById('dropdown').value;
    updateBeerInfo(name);
}

$(document).ready(function() {
    $(".js-data-ajax").select2({
      ajax: {
        url: "/beer_search",
        dataType: 'json',
        delay: 250,
        data: function (params) {
          return {
            query: params.term
          };
        },
        processResults: function (data, params) {
            return {
                "results": data.map(function(beer) {
                    return {
                        id: beer,
                        text: beer
                    };
                }),
                "pagination": {
                    "more": false
                }
            }
        },
        cache: true
      },
      placeholder: 'Search for a beer',
      escapeMarkup: function (markup) { return markup; }, // let our custom formatter work
      minimumInputLength: 1,
    });
});
