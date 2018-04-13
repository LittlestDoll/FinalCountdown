function init() {
    DropdownPopulate()
}

function DropdownPopulate() {
    var url = '/names';
    d3.json(url, function(error, response){
        if (error) {
            return console.warn(error);
        }
        var sel = document.getElementById('selBeer');
        for(var i=0; i<response.length; i++) {
            var opt = document.createElement('option');
            opt.innerHTML = response[i];
            opt.value = response[i];
            sel.appendChild(opt);
        }
    });
}

init()