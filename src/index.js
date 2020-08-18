import { GoogleMapsOverlay } from '@deck.gl/google-maps';
import { HexagonLayer } from '@deck.gl/aggregation-layers';
import { HeatmapLayer } from '@deck.gl/aggregation-layers';


const sourceData = './monthlyData.json';


const heatmap = () => new HeatmapLayer({
      id: 'heat',
      data: sourceData,
      getPosition: d => [d.Longitude, d.Latitude],
      getWeight: d => d.avgT,
      radiusPixels: 60,
});
const hexagon = () => new HexagonLayer({
    id: 'hex',
    data: sourceData,
    getPosition: d => [d.Longitude, d.Latitude],
    getElevationWeight: d => d.totalPP,
    elevationScale: 100,
    extruded: true,
    radius: 1609,         
    opacity: 0.6,        
    coverage: 0.88,
    lowerPercentile: 50
});
window.initMap = () => {

    const map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -22.0, lng: 29.0},
        zoom: 5,
    });
    
}
const overlay = new GoogleMapsOverlay({
    layers: [
        heatmap(),
        hexagon()
    ],
});


overlay.setMap(map);