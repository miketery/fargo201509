
            
	var census=new L.LayerGroup();
	var parcels=new L.LayerGroup();
	var mailSt=new L.LayerGroup();
	var owner=new L.LayerGroup();
	var topOwner=new L.LayerGroup();
	var topAcres=new L.LayerGroup();

	var tileLayer= L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
            maxZoom: 18,
        });


        var map = L.map('map', {
		center: [46.8772, -96.7894], 
		zoom: 13, 
		layers: [tileLayer,census,parcels,mailSt,owner,topOwner]
	});

	var baseMaps = {
		"TileLayer": tileLayer,
	};
	var overlayMaps = {
		"Census": census,
		"Parcels": parcels,
		"MailSt": mailSt,
		"Owner": owner,
		"topOwner": topOwner,
		"topAcres": topAcres
	};

	L.control.layers(baseMaps,overlayMaps).addTo(map);

	function style(feature) {
		return {
			fillColor: getColor(feature.properties.TotalValue),
			weight: 2,
			opacity: .3,
			color: 'white',
			dashArray: '1',
			fillOpacity: 0.7
		};
	}

	function getColor(d) {
	    return d > 300000 ? '#D7301F' :
		   d > 200000  ? '#FC8D59' :
		   d > 100000  ? '#FDCC8A' :
			      '#FEF0D9';
	}


        $.ajax({
	    url:"data/fargoCensus.geojson",
            }).done(function(file) {
                data = $.parseJSON(file);
                L.geoJson(data.features).addTo(census);
                console.log("OK: Loaded Fargo Census Blocks");
            });

function showParcels(number,layer) {
        $.ajax({
	    url:"data/parcelData/"+number+".geojson",//"380170103061.geojson",
            }).done(function(file) {
                data = $.parseJSON(file);
		/*if(data.length)
			L.geoJson(data).addTo(blocks);
		else*/
		L.geoJson(data.features, {style: style}).addTo(layer);
                console.log("OK: Success loaded parcel block "+number);
            });
	}

function topAcresA(number,layer) {
	console.log("topacres");
	console.log(number);
        $.ajax({
	    url:"data/topAcres/"+number+".geojson",//"380170103061.geojson",
            }).done(function(file) {
                data = $.parseJSON(file);
		/*if(data.length)
			L.geoJson(data).addTo(blocks);
		else*/
		L.geoJson(data.features).addTo(layer);
                console.log("OK: Success loaded parcel block "+number);
            });
	}


function addToListA(element, index, array) {
	$("#list").append("<div class=\"block mailSt\" boolean=\"0\" value=\""+element+"\">MailSt"+index+" "+element+"<span class=\"hide\">"+element+"</span></div>");
}
function addToListB(element, index, array) {
	$("#list").append("<div class=\"block topOwner\" boolean=\"0\" value=\""+element+"\">"+element+"<span class=\"hide\">"+element+"</span></div>");
}
function addToListC(element, index, array) {
	$("#list").append("<div class=\"block topAcres\" boolean=\"0\" value=\""+element+"\">"+element+"<span class=\"hide\">"+element+"</span></div>");
}

function addToList(element, index, array) {
	$("#list").append("<div class=\"block parcel\" boolean=\"0\" value=\""+element+"\">"+index+"<span class=\"hide\">"+element+"</span></div>");
	$("#list").append("<div class=\"block owner\" boolean=\"0\" value=\""+element+"\">C"+index+"<span class=\"hide\">c"+element+"</span></div>");
}

$(document).ready(function() {
	arr=["NDparcels","MNparcels","OutOfStateParcels"];
	arr.forEach(addToListA);

	arr=["NDSU DEPT #3000","FARGO PUBLIC SCHOOL DISTRICT 1","CITY OF FARGO","MERITCARE HOSPITAL",
	"INNOVIS HEALTH LLC","INREIT PROPERTIES LLLP","SANFORD NORTH","WEST ACRES DEVELOPMENT CO",
	"MATRIX PROPERTIES CORP","NDSU DEVELOPMENT FOUNDATION","MUNICIPAL AIRPORT AUTHORITY","N D S U",
	"PARK DISTRICT OF THE CITY OF FARGO","DAKOTA UPREIT LTD PTSHP","FARGO PUBLIC SCHOOL DISTRICT",
	"BETHANY ON 42ND","CASS COUNTY","WAL-MART REAL ESTATE BUSINESS TRUST","CASE EQUIPMENT CORP",
	"DAKOTA PARK LTD PTSHP","MERITCARE MEDICAL GROUP","IRET PROPERTIES LTD PTSHP","1709 25 AVENUE SOUTH LLC",
	"UNITED STATES OF AMERICA","WATERFORD AT HARWOOD GROVES LLC","SCHEELS ALL SPORTS, INC","NDSU",
	"U S OF AMERICA","CARDINAL I G COMPANY","BLUE CROSS BLUE SHIELD OF ND","GREAT PLAINS SOFTWARE O C , INC",
	"FARGO HOUSING AUTHORITY"]
	//arr.forEach(addToListB);

	arr=["NDSU DEPT #3000","NORTH DAKOTA AIR NATIONAL GUARD","PARK DISTRICT OF THE CITY OF FARGO","MUNICIPAL AIRPORT AUTHORITY","CITY OF FARGO","NDSU"]

	//arr.forEach(addToListC);

	$.ajax({
	    url:"data/files.txt",
            }).done(function(file) {
                data = $.parseJSON(file);
		data.sort();
		console.log(data);
		data.forEach(addToList);
                console.log("OK: Loaded list");
		$('.block').click(function() {
			val=$(this).find("span").html();//#.split(" ");
			console.log(val)
			if($(this).hasClass('layerOn')) {
				console.log('layerwas already on');
			} else {
				$(this).addClass('layerOn');
				if($(this).hasClass('parcel'))
					showParcels(val,parcels);//[1]);
				else if($(this).hasClass('mailSt'))
					showParcels(val,mailSt);//[1]);
				else if($(this).hasClass('topOwner'))
					showParcels(val,topOwner);//[1]);
				else if($(this).hasClass('owner'))
					showParcels(val,owner);//[1]);
				else if($(this).hasClass('topAcres'))
					topAcresA(val,topAcres);//[1]);
			}
		});
	});

});
