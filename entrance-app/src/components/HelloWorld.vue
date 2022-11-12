<template>
  <div class="container">
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/minty/bootstrap.min.css"
      integrity="sha384-H4X+4tKc7b8s4GoMrylmy2ssQYpDHoqzPa9aKXbDwPoPUA3Ra8PA5dGzijN+ePnH"
      crossorigin="anonymous"
    />
    <h1 class="text-center">Placeholder</h1>
    <b-form>
      <b-form-group id="input-group-1" label="Name:" label-for="Name">
        <b-form-input
          id="Name"
          type="text"
          placeholder="Enter Your Name"
          required
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
    </b-form>
    <button @click="onTest()">adfafadfa</button>
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
      ip: "172.20.10.5:5000/",
      test: "Hello",
    };
  },
  methods: {
    click() {
      console.log(this.filesAccumulated);
    },
    onClick() {
      this.file.forEach((thisFile) => {
        console.log(thisFile);
        if (confirm(`Are you sure you want to upload ${thisFile.name}`)) {
          this.filesAccumulated.push(thisFile);
        }
      });
    },
    onTest(test) {
      axios
        .post(this.ip + "handle", test)
        .then((response) => console.log(response.data));
    },
  },
};
</script>
