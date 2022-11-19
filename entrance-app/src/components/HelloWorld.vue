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
        <b-button @click="onButtonClick()" size="lg" variant="primary"
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
    //Post json name object to server with request headers
    postName() {
      axios
        .post(this.ip + "name", this.name, {
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },

    //Post json object to server with request headers
    postSongName() {
      axios
        .post(this.ip + "songName", this.songName, {
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then((response) => {
          console.log(response);
        });
    },
    //Post files from filesAccumulated to server with request headers
    postFiles() {
      let formData = new FormData();
      for (let i = 0; i < this.filesAccumulated.length; i++) {
        formData.append("image", this.filesAccumulated[i]);
      }

      axios
        .post(this.ip + "files", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          console.log(response);
        });
    },
    async onButtonClick() {
      //Create form data to uplaod to server
      this.postName();
      await new Promise((r) => setTimeout(r, 30));
      this.postFiles();
      //Sleep for 30 milliseconds
      await new Promise((r) => setTimeout(r, 30));
      this.postSongName();
    },
  },
};
</script>
