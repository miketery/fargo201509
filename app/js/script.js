
            
	var main=new L.LayerGroup();
	var blocks=new L.LayerGroup();

	var tileLayer= L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
            maxZoom: 18,
        });


        var map = L.map('map', {
		center: [46.8772, -96.7894], 
		zoom: 13, 
		layers: [tileLayer,main,blocks]
	});

	var baseMaps = {
		"TileLayer": tileLayer,
	};
	var overlayMaps = {
		"Census": main,
		"Parcels": blocks
	};

	L.control.layers(baseMaps,overlayMaps).addTo(map);


        $.ajax({
	    url:"data/fargoCensus.geojson",
            }).done(function(file) {
                data = $.parseJSON(file);
                L.geoJson(data.features).addTo(main);
                console.log("OK: Loaded Fargo Census Blocks");
            });

function showParcels(number) {
        $.ajax({
	    url:"data/parcelData/"+number+".geojson",//"380170103061.geojson",
            }).done(function(file) {
                data = $.parseJSON(file);
                L.geoJson(data.features).addTo(blocks);
                console.log("OK: Success loaded parcel block");
            });
	}

function addToList(element, index, array) {
	$("#list").append("<div class=\"block\" boolean=\"0\" value=\""+element+"\">"+index+" "+element+"</div>");
}

$(document).ready(function() {
	$.ajax({
	    url:"data/files.txt",
            }).done(function(file) {
                data = $.parseJSON(file);
		data.sort();
		console.log(data);
		data.forEach(addToList);
                console.log("OK: Loaded list");
		$('.block').click(function() {
			val=$(this).html().split(" ");
			if($(this).hasClass('layerOn')) {
				console.log('layerwas already on');
			} else {
				$(this).addClass('layerOn');
				showParcels(val[1]);
			}
		});
	});

});
