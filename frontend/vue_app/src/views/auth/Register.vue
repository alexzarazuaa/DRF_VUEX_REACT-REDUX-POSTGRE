<template>
  <section>
    <form @submit.prevent="onSubmit">
      <h1>Sign Up</h1>
      <div class="container">
        <label for="username"><b>Username</b></label>
        <input
          class="form-control form-control-lg"
          type="text"
          v-model="username"
          placeholder="Username"
          required
        />

        <label for="email"><b>Email</b></label>
        <input
          class="form-control form-control-lg"
          type="email"
          v-model="email"
          placeholder="Email"
          required
        />

        <label for="psw"><b>Password</b></label>
        <input
          class="form-control form-control-lg"
          type="password"
          v-model="password"
          placeholder="password"
          required
        />

        <div class="clearfix">
          <router-link :to="{ name: 'Home' }">
            <button type="button" class="cancelbtn">Cancel</button></router-link
          >
          <button class="signupbtn">Sign Up</button>
        </div>
      </div>
    </form>
  </section>
</template>

<script>
import { mapState } from "vuex";
import { ActionsType } from "@/store/actions.type";

export default {
  name: "Register",
  data() {
    return {
      username: "",
      email: "",
      password: "",
    };
  },
  computed: {
    ...mapState({
      errors: (state) => state.auth.errors,
    }),
  },
  methods: {
    onSubmit() {
      this.$store
        .dispatch(ActionsType.REGISTER, {
          email: this.email,
          password: this.password,
          username: this.username,
        })
        .then((response) => {
          console.log(response)
          this.$router.push({ name: "Home" });
        })
        .catch((response) => {
          response.data.errors.email
            ? alert(response.data.errors.email)
            : alert(response.data.errors.username);
        });
    },
  },
};
</script>

<style>
body {
  font-family: Arial, Helvetica, sans-serif;
}
* {
  box-sizing: border-box;
}

/* Full-width input fields */
input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

/* Add a background color when the inputs get focus */
input[type="text"]:focus,
input[type="password"]:focus {
  background-color: #ddd;
  outline: none;
}

/* Set a style for all buttons */
button {
  background-color: #4caf50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.9;
}

button:hover {
  opacity: 1;
}

/* Extra styles for the cancel button */
.cancelbtn {
  padding: 14px 20px;
  background-color: #f44336;
}

/* Float cancel and signup buttons and add an equal width */
.cancelbtn,
.signupbtn {
  float: left;
  width: 50%;
}

/* Add padding to container elements */
.container {
  padding: 16px;
}

/* The Modal (background) */
.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: #474e5d;
  padding-top: 50px;
}

/* Modal Content/Box */
.modal-content {
  background-color: #fefefe;
  margin: 5% auto 15% auto; /* 5% from the top, 15% from the bottom and centered */
  border: 1px solid #888;
  width: 80%; /* Could be more or less, depending on screen size */
}

/* Style the horizontal ruler */
hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}

/* The Close Button (x) */
.close {
  position: absolute;
  right: 35px;
  top: 15px;
  font-size: 40px;
  font-weight: bold;
  color: #f1f1f1;
}

.close:hover,
.close:focus {
  color: #f44336;
  cursor: pointer;
}

/* Clear floats */
.clearfix::after {
  content: "";
  clear: both;
  display: table;
}

/* Change styles for cancel button and signup button on extra small screens */
@media screen and (max-width: 300px) {
  .cancelbtn,
  .signupbtn {
    width: 100%;
  }
}
</style>
