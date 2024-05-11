<template>
    <b-navbar toggleable="lg" type="dark">
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
            <b-navbar class="mx-auto" style="max-width: 600px;">
                <b-navbar-brand href="#">Sklep rowerowy</b-navbar-brand>
                <b-navbar-nav>
                    <router-link to="/" class="nav-link">Strona główna</router-link>
                    <b-nav-item href="/sklep">Sklep</b-nav-item>
                    <router-link to="/kontakt" class="nav-link">Kontakt</router-link>
                </b-navbar-nav>
            </b-navbar>

            <b-navbar-nav>
                <b-nav-item-dropdown right>
                    <template #button-content>
                        <em>Użytkownik</em>
                    </template>
                    <b-dropdown-item href="#">Profil</b-dropdown-item>
                    <b-dropdown-item href="#">Wyloguj</b-dropdown-item>
                    <b-dropdown-item href="/rejestracja">Rejestracja</b-dropdown-item>
                    <b-dropdown-item href="/logowanie">Logowanie</b-dropdown-item>
                </b-nav-item-dropdown>
            </b-navbar-nav>
        </b-collapse>
    </b-navbar>
</template>

<script>
export default {
    name: 'AppNavbar',
}
</script>

<style scoped>
.b-nav-item,
.nav-link {
    margin-right: 10px;
}

.b-navbar {
    background-color: #FFD700;
}
</style>