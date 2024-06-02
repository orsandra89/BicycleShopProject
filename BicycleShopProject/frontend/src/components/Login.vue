<template>
    <div class="d-flex justify-content-center align-items-center" style="height: auto;">
        <div class="w-25 my-form">
            <h1 class="text-center">Logowanie</h1>
            <b-alert variant="danger" v-model="showErrorAlert" dismissible>
                Nieprawidłowy email lub hasło.
            </b-alert>
            <b-alert variant="success" v-model="showSuccessAlert" dismissible>
                Pomyślnie zalogowano.
            </b-alert>
            <b-form @submit.prevent="onSubmit">
                <b-form-group label="Email">
                    <b-form-input type="email" v-model="form.username" required></b-form-input>
                </b-form-group>
                <b-form-group label="Hasło">
                    <b-form-input type="password" v-model="form.password" required></b-form-input>
                </b-form-group>
                <b-button type="submit" variant="primary">Zaloguj</b-button>
            </b-form>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

export default {
    setup() {
        const form = ref({
            username: '',
            password: '',
        });
        const showErrorAlert = ref(false);
        const showSuccessAlert = ref(false);
        const router = useRouter();

        const onSubmit = async () => {
            try {
                const response = await axios.post('/login/', form.value);
                console.log(response.data);
                if (response.data.message === 'User logged in successfully') {
                    localStorage.setItem('user', JSON.stringify(response.data));
                    showSuccessAlert.value = true;
                    setTimeout(() => {
                        router.push({ name: 'Main' }).then(() => window.location.reload());
                    }, 1000);
                } else {
                    showErrorAlert.value = true;
                }
            } catch (error) {
                console.error(error);
                showErrorAlert.value = true;
            }
        };

        return { form, onSubmit, showErrorAlert, showSuccessAlert };
    },
};
</script>

<style scoped>
.my-form {
    margin-top: 0;
    margin-bottom: 0;
}
</style>