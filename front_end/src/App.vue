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
    const renderer = this.$refs.renderer
    const box = this.$refs.box.mesh
    renderer.onBeforeRender(() => {
      box.rotation.x += 0.01
    })

    // scene
    const geometry = new THREE.SphereGeometry( 5, 32, 32 );
    const material = new THREE.MeshBasicMaterial( {color: 0xffff00} );
    const sphere = new THREE.Mesh( geometry, material );
    scene.add( sphere );
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
