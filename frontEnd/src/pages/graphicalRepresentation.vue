<template>
  <Renderer
    ref="renderer"
    antialias
    :orbit-ctrl="{ enableDamping: true }"
    resize="window"
  >
    <Camera :position="{ z: 10 }" />
    <Scene>
      <PointLight :position="{ y: 250, z: 250 }" />

        <div v-for="item in gpoints" :key="item.message">
         
          <Sphere :position="{ x: item[0], y: item[1], z: item[2] }" > 
           <LambertMaterial />
          </Sphere>
        </div>

    </Scene>
  </Renderer>
</template>

<script>
import initPoints from "../utils/graphicalPointsBuilder";

export default {
  data() {
    //default settings are 1,8,6
    const gpoints = initPoints(20,12,10,3);

    console.log(gpoints);
    return {
      gpoints
    };
  },
};
</script>