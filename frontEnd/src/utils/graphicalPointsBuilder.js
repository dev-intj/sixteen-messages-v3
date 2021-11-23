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

  const vertex = []

  // generate vertices
  const vertices = [];

  for (let iy = 0; iy < heightSegments; iy++) {

    const v = iy / heightSegments;

    for (let ix = 0; ix < widthSegments; ix++) {

      const u = ix / widthSegments;

      // inside sphere calculations
      if (sliceSegments > 0 ){
      for (let iz = 0; iz < sliceSegments; iz++) {

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

        vertices.push(...vertex);
      }
    }
  }

  //array cleaner from 0,0,0
  for (let vi = 0; vi < vertices.length; vi++) {
    if (vertices[vi][0] == 0 && vertices[vi][1] == 0 && vertices[vi][2] == 0){
        vertices.splice(vi,1)
    }
  }

  //random calculations
  const max_random = 40;
  const max_random_x = 40;
  const max_random_y= 40;
  const max_random_z = 40;

  for (let vi = 0; vi < vertices.length; vi++) {
    let random_x = Math.ceil(Math.random() * max_random) * (Math.round(Math.random()) ? 1 : -1)
    let random_y = Math.ceil(Math.random() * max_random) * (Math.round(Math.random()) ? 1 : -1)
    let random_z = Math.ceil(Math.random() * max_random) * (Math.round(Math.random()) ? 1 : -1)
    vertices[vi][0] += random_x
    vertices[vi][1] += random_y
    vertices[vi][2] += random_z
  }
  //maybe I should spawn one message on the 0,0,0 that will act as creator message
  return vertices;
}

export default sphereConstruct;