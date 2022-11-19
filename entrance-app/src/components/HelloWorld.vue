<template>
  <div class="container">
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/minty/bootstrap.min.css"
      integrity="sha384-H4X+4tKc7b8s4GoMrylmy2ssQYpDHoqzPa9aKXbDwPoPUA3Ra8PA5dGzijN+ePnH"
      crossorigin="anonymous"
    />
    <h1 class="text-center">Welcome Home App</h1>
    <b-form>
      <b-form-group id="input-group-1" label="Name:" label-for="Name">
        <b-form-input
          id="Name"
          type="text"
          placeholder="Enter Your Name"
          required
          v-model="name.Name"
        ></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-2" label="Pictures:" label-for="input-2">
        <b-form-file
          v-model="file"
          placeholder="Upload Pictures"
          multiple
          v-on:input="onClick()"
        >
          ></b-form-file
        >
      </b-form-group>
      <b-form-group id="input-group-3" label="Song Name:" label-for="songName">
        <b-form-input
          id="Name"
          type="text"
          placeholder="Enter Song Name"
          v-model="songName.Song"
          required
        ></b-form-input>
      </b-form-group>
      <div class="text-center">
        <b-button @click="onTest()" type="submit" size="lg" variant="primary"
          >Submit</b-button
        >
      </div>
    </b-form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "HelloWorld",
  data() {
    return {
      file: [],
      filesAccumulated: [],
      ip: "http://192.168.0.105:3000/",
      name: { Name: "" },
      songName: { Song: "" },
    };
  },
  methods: {
    onClick() {
      this.file.forEach((thisFile) => {
        this.filesAccumulated.push(thisFile);
      });
    },
    onTest() {
      const fd = new FormData();
      for (let i = 0; i < this.filesAccumulated.length; i++) {
        fd.append("image", this.filesAccumulated[i]);
      }
      fd.append("name", this.name.Name);
      fd.append("song", this.songName.Song);
      axios
        .post(this.ip + "handle", fd)
        .then((response) => console.log(response.data));
    },
  },
};
</script>
