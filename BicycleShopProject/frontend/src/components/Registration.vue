<template>
    <div class="d-flex justify-content-center align-items-center" style="height: auto;">
        <div class="w-25 my-form">
            <h1 class="text-center">Rejestracja</h1>
            <b-form @submit.prevent="onSubmit">
                <b-form-group label="Imię">
                    <b-form-input type="text" v-model="form.first_name" required></b-form-input>
                </b-form-group>
                <b-form-group label="Nazwisko">
                    <b-form-input type="text" v-model="form.last_name" required></b-form-input>
                </b-form-group>
                <b-form-group label="Email">
                    <b-form-input type="email" v-model="form.email" required></b-form-input>
                </b-form-group>
                <b-form-group label="Hasło">
                    <b-form-input type="password" v-model="form.password" required></b-form-input>
                </b-form-group>
                <b-form-group label="Powtórz hasło">
                    <b-form-input type="password" v-model="form.passwordConfirm" required></b-form-input>
                </b-form-group>
                <b-button type="submit" variant="primary">Zarejestruj</b-button>
            </b-form>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
    setup() {
        const form = ref({
            first_name: '',
            last_name: '',
            email: '',
            password: '',
            passwordConfirm: '',
        });

        const onSubmit = async () => {
            if (form.value.password !== form.value.passwordConfirm) {
                alert('Hasła nie są takie same!');
                return;
            }

            try {
                const response = await axios.post('/register/', form.value);
                console.log(response.data);
            } catch (error) {
                console.error(error);
            }
        };

        return { form, onSubmit };
    },
};
</script>

<style scoped>
.my-form {
    margin-top: 0;
    margin-bottom: 0;
}
</style>