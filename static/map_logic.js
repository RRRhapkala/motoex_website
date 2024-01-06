window.onload = init;

function init(){
  const map = new ol.Map({
    view: new ol.View({
      center: [2339014.595662489, 6841950.467177815], 
      zoom: 9, 
      minZoom: 4,
      maxZoom: 20 
    }),
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM
      })
    ],
    target: 'js-map'
  })

map.on('click', function(e){
  console.log(e.coordinate)
})
}
