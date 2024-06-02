<template>
    <b-navbar toggleable="lg" type="dark">
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
            <b-navbar class="mx-auto" style="max-width: 600px;">
                <b-navbar-brand href="#" class="fw-bold"><font-awesome-icon :icon="['fas', 'bicycle']"
                        class="me-1" />SKLEP ROWEROWY</b-navbar-brand>
                <b-navbar-nav>
                    <router-link to="/" class="nav-link">Strona główna</router-link>
                    <router-link to="/sklep" class="nav-link">Sklep</router-link>
                    <router-link to="/kontakt" class="nav-link">Kontakt</router-link>
                </b-navbar-nav>
            </b-navbar>

            <b-navbar-nav>
                <router-link to="/koszyk" class="nav-link" v-if="isLoggedIn">
                    <font-awesome-icon :icon="['fas', 'shopping-basket']" class="me-1" />
                    Koszyk
                </router-link>

                <b-nav-item-dropdown right>
                    <template #button-content>
                        <font-awesome-icon :icon="['fas', 'circle-user']" class="me-1" v-if="isLoggedIn" />
                        {{ username }}
                    </template>
                    <router-link v-if="isLoggedIn" to="/user-panel" class="dropdown-item">Profil</router-link>
                    <router-link v-if="isLoggedIn" to="/order-history" class="dropdown-item">Historia
                        Zamówień</router-link>
                    <b-dropdown-item v-if="isLoggedIn && is_superuser" href="http://localhost:8000/admin">Panel
                        Admina</b-dropdown-item>
                    <router-link v-if="!isLoggedIn" to="/rejestracja" class="dropdown-item">Rejestracja</router-link>
                    <router-link v-if="!isLoggedIn" to="/logowanie" class="dropdown-item">Logowanie</router-link>
                    <b-dropdown-item v-if="isLoggedIn" @click="logout">Wyloguj</b-dropdown-item>
                </b-nav-item-dropdown>
            </b-navbar-nav>
        </b-collapse>
    </b-navbar>
</template>

<script>
export default {
    name: 'AppNavbar',
    data() {
        return {
            username: 'Zaloguj się',
            isLoggedIn: false,
            is_superuser: false,
        };
    },
    mounted() {
        const user = JSON.parse(localStorage.getItem('user'));
        if (user && user !== "undefined") {
            this.username = user.username;
            this.isLoggedIn = true;
            this.is_superuser = user.is_superuser;
        }
    },
    methods: {
        logout() {
            localStorage.removeItem('user');
            this.username = 'Zaloguj się';
            this.isLoggedIn = false;
            this.is_superuser = false;
            window.location.reload();
        }
    }
};
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