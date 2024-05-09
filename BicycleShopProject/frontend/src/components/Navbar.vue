<template>
    <v-app>
        <v-app-bar app color="deep-purple accent-4" dark>
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
            <v-toolbar-title>Bicycle Shop</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn text color="white" href="/">Home</v-btn>
            <v-btn text color="white" href="/shop">Shop</v-btn>
            <v-btn text color="white" href="/contact">Contact</v-btn>
        </v-app-bar>

        <v-navigation-drawer v-model="drawer" app>
            <v-list-item>
                <v-list-item-content>
                    <v-list-item-title class="title">Navigation</v-list-item-title>
                </v-list-item-content>
            </v-list-item>

            <v-divider></v-divider>

            <v-list dense>
                <v-list-item link href="/">
                    <v-list-item-icon>
                        <v-icon>mdi-home</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title>Home</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>

                <v-list-item link href="/shop">
                    <v-list-item-icon>
                        <v-icon>mdi-store</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title>Shop</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>

                <v-list-item link href="/contact">
                    <v-list-item-icon>
                        <v-icon>mdi-email</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title>Contact</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
    </v-app>
</template>

<script>
export default {
    name: 'AppNavbar',
    data: () => ({
        drawer: false,
    }),
}
</script>

<style scoped>
.v-btn {
    margin-right: 10px;
}
</style>