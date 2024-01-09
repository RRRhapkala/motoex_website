window.onload = init;


function init() {
  const map = new ol.Map({
    view: new ol.View({
      center: [2339014.595662489, 6841950.467177815],
      zoom: 9,
      minZoom: 4,
      maxZoom: 20,
    }),
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM(),
      }),
    ],
    target: 'js-map',
  });

  map.on('click', function (e) {
    console.log(e.coordinate);
  });

  const coordinates = [2339014.595662489, 6841950.467177815]; //выбранные координаты
  addIconToMap(coordinates, map, markerImagePath);
}

function addIconToMap(coordinates, map, markerImagePath) {
  const iconStyle = new ol.style.Style({
    image: new ol.style.Icon({
      anchor: [0.5, 1],
      src: markerImagePath,
    }),
  });

  const iconFeature = new ol.Feature({
    geometry: new ol.geom.Point(coordinates),
  });

  iconFeature.setStyle(iconStyle);

  const vectorSource = new ol.source.Vector({
    features: [iconFeature],
  });

  const vectorLayer = new ol.layer.Vector({
    source: vectorSource,
  });

  map.addLayer(vectorLayer);
}
