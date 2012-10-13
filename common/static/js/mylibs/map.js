 var map;
  var markersArray = [];
  var locArray = [];
  var thePoly;
  var available=true;
  var geocoder = null;
  var markerscount=0;
  var l1m;
  var l2m;
  var center;
  var centermarker;
  var coordperm=0.0000429126282;

  var clientid="2LMPRCIPRWUSR0AWLRL4M4SYRA5XG4XY2L4TJ2BM3GXAI5XJ";
  var clientsecret="EXBXRD5J4V4V2OIH0GZN5XROZKUDML4RKARB0WPMFQPFRBFU";


var initialLocation;
var siberia = new google.maps.LatLng(60, 105);
var newyork = new google.maps.LatLng(40.69847032728747, -73.9514422416687);
var Timisoara = new google.maps.LatLng(45.758122, 21.231852);
var Incubator = new google.maps.LatLng(45.751641, 21.216823);
var browserSupportFlag =  new Boolean();

function initialize() {
  geocoder = new google.maps.Geocoder();
  var myOptions = {
    zoom: 12,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };

  map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);

  if(navigator.geolocation) {  // Try W3C Geolocation (Preferred)
    browserSupportFlag = true;
    navigator.geolocation.getCurrentPosition(function(position) {
      initialLocation = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
      map.setCenter(initialLocation);
    }, function() {
      handleNoGeolocation(browserSupportFlag);
    });
  } else if (google.gears) {  // Try Google Gears Geolocation
    browserSupportFlag = true;
    var geo = google.gears.factory.create('beta.geolocation');
    geo.getCurrentPosition(function(position) {
      initialLocation = new google.maps.LatLng(position.latitude,position.longitude);
      map.setCenter(initialLocation);
    }, function() {
      handleNoGeoLocation(browserSupportFlag);
    });
  }
   else {  // Browser doesn't support Geolocation
    browserSupportFlag = false;
    handleNoGeolocation(browserSupportFlag);
  }

  function handleNoGeolocation(errorFlag) {
    if (errorFlag == true) {
      alert("Geolocation service failed, so here's the place we started programming in to make you feel better.");
      initialLocation = Incubator;
    } else {
      alert("Your browser doesn't support geolocation. We've placed you in the city that created it all *smiley face*");
      initialLocation = Timisoara;
    }
    map.setCenter(initialLocation);
    map.setMapTypeId(google.maps.MapTypeId.HYBRID);
    map.setZoom(19);

  }
    google.maps.event.addListener(map, 'click', function(event){addMarker(event.latLng);});
}




  function codeAddress() {
   var address = document.getElementById("address").value;
   geocoder.geocode( { 'address': address}, function(results, status) {
     if (status == google.maps.GeocoderStatus.OK) {
       map.setCenter(results[0].geometry.location);
     } else {
       alert("We are sorry, we were not able to find the location you were looking for.");
     }
   });
 }





  function makepolygon(){
     locArray.length = 0;
      for(var i in markersArray){
        locArray.push(markersArray[i].position);
      }

      thePoly = new google.maps.Polygon({
            paths: locArray,
            strokeColor: "#060606",
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: "#0F0F0F",
            fillOpacity: 0.35,
            draggable: true
          });

          thePoly.setMap(map);
      available=false;
      

  }

  function getsides(){
      var l1;
      var l2;
      l1=markersArray[2].position.lng()-markersArray[0].position.lng();
      l2=markersArray[2].position.lat()-markersArray[0].position.lat();
      if(l1<0){l1=-l1;}
      if(l2<0){l2=-l2;}
      l1m=(l1*2)/coordperm;
      l2m=(l2*2*8)/(5*coordperm);
  }


  function calc_area(){
      var AREA;
      getsides();
      AREA=l1m*l2m;
      alert("The area is "+AREA+" square ditches");

  }

  var venues = [];

  function getvalue(){
      var response;
      var med;
      var value=0;
      getsides();
      med=(l1m+l2m)/2;
      $.get("https://api.foursquare.com/v2/venues/search?ll="+center.lat()+","+center.lng()+"&client_id="+clientid+"&client_secret="+clientsecret,
              function (response){
                  $.each(response.response.groups[0].items,function (i,el){
                         if(el.location.distance<=med){
                             var loc=new google.maps.LatLng(el.location.lat,el.location.lng);
                             var mr=new google.maps.Marker({
                                 position: loc,
                                 map: map,
                                 draggable: false,
                                 title:el.name
                                 });
                            venues.push(mr);
                             value++;
                             console.log(el.name,": ",el.location.distance);
                         }
                  });
             console.log("total with ",med,": ",value);
              },
              "json"
              );

  }


  function get_center(){
      var lonc;
      var latc;
      lonc=(markersArray[0].position.lng()+markersArray[2].position.lng())/2;
      latc=(markersArray[0].position.lat()+markersArray[2].position.lat())/2;
      center = new google.maps.LatLng(latc,lonc);
      centermarker=new google.maps.Marker({
         position: center,
         map: map,
         draggable: false
        });
  }


  function addMarker(location) {
        marker = new google.maps.Marker({
         position: location,
         map: map,
         draggable: true
        });
        markersArray[markerscount]=marker;
        markerscount++;
  }

  function clearOverlays() {
    if (markersArray) {
      for (i in markersArray) {
        markersArray[i].setMap(null);
      }
    }
  }

  function showOverlays() {
    if (markersArray) {
      for (i in markersArray) {
        markersArray[i].setMap(map);
      }
    }
  }


  function deletevenues() {
    if (venues) {
      for (i in venues) {
        venues[i].setMap(null);
      }
     venues.length = 0;
    }
  }

  function deleteMarkers() {
    if (markersArray) {
      for (i in markersArray) {
        markersArray[i].setMap(null);
      }
      markersArray.length = 0;
      markerscount=0;
      centermarker.setMap(null);

    }
  }

  function deletePolys(){
      if(thePoly){
         thePoly.setMap(null);
         available=true;
     }
  }

