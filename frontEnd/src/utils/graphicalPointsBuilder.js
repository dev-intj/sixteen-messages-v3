import * as threejs from '../../node_modules/three/src/Three';

function sphereConstruct(radius, widthSegments, heightSegments, sliceSegments) {

  //setting variables
  var radius = radius;
  var widthSegments = widthSegments;
  var heightSegments = heightSegments;
  var sliceSegments = sliceSegments;
  var phiStart = 0;
  var phiLength = Math.PI * 2;
  var thetaStart = 0;
  var thetaLength = Math.PI;

  widthSegments = Math.max(3, Math.floor(widthSegments));
  heightSegments = Math.max(2, Math.floor(heightSegments));

  const thetaEnd = Math.min(thetaStart + thetaLength, Math.PI);

  const vertex = new threejs.Vector3();

  //random calculations
  const random_radius = new threejs.Vector3();
  const max_random = 2;
  const min_random = -2;

  const normal = new threejs.Vector3();
  
  // generate vertices
  const vertices = [];

  for (let iy = 0; iy <= heightSegments; iy++) {

    const v = iy / heightSegments;

    for (let ix = 0; ix <= widthSegments; ix++) {

      const u = ix / widthSegments;

      // inside sphere calculations
      if (sliceSegments > 0 ){
      for (let iz = 0; iz <= sliceSegments; iz++) {

        // vertex

        let current_radius = (radius / sliceSegments) * iz + (radius * iz)
        
        vertex.x = - current_radius * Math.cos(phiStart + u * phiLength) * Math.sin(thetaStart + v * thetaLength);
        vertex.y = current_radius * Math.cos(thetaStart + v * thetaLength);
        vertex.z = current_radius * Math.sin(phiStart + u * phiLength) * Math.sin(thetaStart + v * thetaLength);
        
        vertices.push([vertex.x, vertex.y, vertex.z]);
        
      }
      }else{
        // vertex
        vertex.x = - radius * Math.cos(phiStart + u * phiLength) * Math.sin(thetaStart + v * thetaLength);
        vertex.y = radius * Math.cos(thetaStart + v * thetaLength);
        vertex.z = radius * Math.sin(phiStart + u * phiLength) * Math.sin(thetaStart + v * thetaLength);

        vertices.push([vertex.x, vertex.y, vertex.z]);
      }
    }
  }
  
  return vertices;
}

export default sphereConstruct;