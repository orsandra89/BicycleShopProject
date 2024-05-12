<template>
    <div class="user-panel">
      <h2>Panel użytkownika</h2>
      <form @submit.prevent="submitForm">
        <div>
          <label for="name">Imię:</label>
          <input id="name" v-model="user.name" type="text" required>
        </div>
        <div>
          <label for="surname">E-Mail:</label>
          <input id="surname" v-model="user.Email" type="text" required>
        </div>
        <div>
          <label for="address">Adres:</label>
          <input id="address" v-model="user.address" type="text" required>
        </div>
        <div>
          <label for="postalCode">Kod pocztowy:</label>
          <input id="postalCode" v-model="user.postalCode" type="text" required>
        </div>
        <div>
          <label for="phone">Telefon:</label>
          <input id="phone" v-model="user.phone" type="text" required>
          <p v-if="errors.phone" class="error">{{ errors.phone }}</p>
        </div>
        <div>
          <label for="password">Hasło:</label>
          <input id="password" v-model="user.password" type="password" required>
        </div>
        <button type="submit">Zaktualizuj dane</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'UserPanel',
    data() {
      return {
        user: {
          name: '',
          Email: '',
          address: '',
          postalCode: '',
          phone: '',
          password: ''
        },
        errors: {
          phone: null,
        }
      };
    },
    methods: {
      validatePhone() {
        const phonePattern = /^[0-9]{9}$/;
        if (!this.user.phone) {
          this.errors.phone = 'Phone number is required.';
        } else if (!phonePattern.test(this.user.phone)) {
          this.errors.phone = 'Phone number is invalid.';
        } else {
          this.errors.phone = null;
        }
      },
      submitForm() {
        this.validatePhone();
        if (!this.errors.phone) {
          this.updateUser();
        }
      },
      updateUser() {
        // Update user logic here
        console.log(this.user);
      }
    }
  };
  </script>
  
  <style scoped>
  .user-panel {
    width: 300px;
    margin: auto;
    background-color: #f8f8f8;
    border-radius: 15px;
    box-shadow: 0px 0px 15px 0px rgba(0,0,0,0.1);
    padding: 30px;
    font-family: 'Arial', sans-serif;
  }
  
  .user-panel form div {
    margin-bottom: 25px;
  }
  
  .user-panel form input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 16px;
  }
  
  .user-panel form button {
    width: 100%;
    padding: 15px;
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 5px;
    font-size: 16px;
    transition: background-color 0.3s ease;
  }
  
  .user-panel form button:hover {
    background-color: #45a049;
  }
  
  .error {
    color: red;
    font-weight: bold;
    margin-top: 10px;
  }
  </style>