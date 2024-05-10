<template>
    <b-navbar toggleable="lg" type="dark">
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
            <b-navbar class="mx-auto" style="max-width: 600px;">
                <b-navbar-brand href="#">Sklep rowerowy</b-navbar-brand>
                <b-navbar-nav>
                    <b-nav-item href="/">Strona główna</b-nav-item>
                    <b-nav-item href="/sklep">Sklep</b-nav-item>
                    <b-nav-item href="/kontakt">Kontakt</b-nav-item>
                </b-navbar-nav>
            </b-navbar>

            <b-navbar-nav>
                <b-nav-item-dropdown right>
                    <template #button-content>
                        <em>Użytkownik</em>
                    </template>
                    <b-dropdown-item href="#">Profil</b-dropdown-item>
                    <b-dropdown-item href="#">Wyloguj</b-dropdown-item>
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
.b-nav-item {
    margin-right: 10px;
}

.b-navbar {
    background-color: #FFD700;
}
</style>