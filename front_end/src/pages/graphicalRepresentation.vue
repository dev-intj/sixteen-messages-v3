<template>
  <Renderer ref="renderer" antialias :orbit-ctrl="{ enableDamping: true }" resize="window">
    <Camera :position="{ z: 10 }" />
    <Scene>

      <PointLight :position="{ y: 250, z: 250 }" />



    </Scene>

  </Renderer>
</template>

<script>
import initPoints  from '../utils/graphicalPointsBuilder';

export default {
    data (){
    return{
        points: initPoints()
    }
}
}

</script>