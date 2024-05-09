<template>
    <footer class="footer">
      <div class="container">
        <div class="row">
          <div class="col-md-4">
            <h3>Kontakt</h3>
            <p>Adres: 1234 Ulica Rowerowa</p>
            <p>Telefon: 123-456-789</p>
            <p>Email: kontakt@skleprowerowy.com</p>
          </div>
          <div class="col-md-4">
            <h3>O nas</h3>
            <p>Jesteśmy pasjonatami rowerów od ponad 10 lat. Nasz sklep oferuje szeroki wybór rowerów i akcesoriów dla każdego typu rowerzysty.</p>
          </div>
          <div class="col-md-4">
            <h3>Linki</h3>
            <ul>
              <li><a href="#">Strona główna</a></li>
              <li><a href="#">Oferta</a></li>
              <li><a href="#">Kontakt</a></li>
            </ul>
          </div>
        </div>
        <hr>
        <div class="row">
          <div class="col-md-12">
            <p class="text-center">© 2024 Sklep Rowerowy. Wszelkie prawa zastrzeżone.</p>
          </div>
        </div>
      </div>
    </footer>
  </template>
  
  <script>
  export default {
    name: 'AppFooter'
  }
  </script>
  
  <style scoped>
  .footer {
    background-color: #f8f9fa;
    padding: 40px 0;
  }
  
  .footer h3 {
    color: #333;
  }
  
  .footer p {
    color: #666;
  }
  
  .footer ul {
    list-style: none;
    padding: 0;
  }
  
  .footer ul li {
    margin-bottom: 10px;
  }
  
  .footer ul li a {
    color: #666;
    text-decoration: none;
  }
  
  .footer ul li a:hover {
    color: #333;
  }
  
  .text-center {
    text-align: center;
  }
  </style>
  