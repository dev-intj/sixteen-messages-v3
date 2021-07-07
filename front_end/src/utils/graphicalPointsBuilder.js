import * as threejs from '../../node_modules/three/src/Three';

const v = new threejs.Vector3();

function randomPointInSphere( radius ) {
	
  const x = threejs.Math.randFloat( -1, 1 );
  const y = threejs.Math.randFloat( -1, 1 );
  const z = threejs.Math.randFloat( -1, 1 );
  const normalizationFactor = 1 / Math.sqrt( x * x + y * y + z * z );

  v.x = x * normalizationFactor * radius;
  v.y = y * normalizationFactor * radius;
  v.z = z * normalizationFactor * radius;

  return v;
}

function initPoints() {
  
  var positions = [];
  
  for (var i = 0; i < 50000; i ++ ) {
    
    var vertex = randomPointInSphere( 50 );
    positions.push( [vertex.x, vertex.y, vertex.z] );
    
  }
  return positions;
}

export default initPoints;