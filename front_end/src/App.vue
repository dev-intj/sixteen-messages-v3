<template>
  <Renderer ref="renderer" antialias :orbit-ctrl="{ enableDamping: true }" resize="window">
    <Camera :position="{ z: 10 }" />
    <Scene>

      <PointLight :position="{ y: 250, z: 250 }" />

      <Sphere>
        <LambertMaterial />
      </Sphere>

    </Scene>
    
  </Renderer>
</template>

<script>
export default {
  mounted() {
  }
}
</script>

<style>
body {
  margin: 0;
}
canvas {
  display: block;
}
</style>
