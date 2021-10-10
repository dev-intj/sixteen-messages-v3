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

      <Sphere
        v-for="(item, index) in gpoints"
        :key="'item_' + index"
        :position="{ x: item[0], y: item[1], z: item[2] }"
      >
        <PhysicalMaterial color="#ffffff" />
      </Sphere>

      
    </Scene>
  </Renderer>
</template>

<script>
import initPoints from "../utils/graphicalPointsBuilder";

export default {
  data() {
    return {
      gpoints: [],
    };
  },
  mounted() {
    //default settings are 1,8,6
    this.gpoints = initPoints(15, 15, 15, 15);
    this.fetchMessages();
  },
  methods: {
    fetchCreatorMessage() {

    },
    fetchMessages() {
      // Make a request for a user with a given ID
      axios({
        url: `/api/message/`,
        method: "get",
      })
        .then((response) => {
          if (response.status == 200 || response.status == 201) {
            console.log(response.data);
          }
        })
        .catch((error) => {});
    },
  },
};
</script>