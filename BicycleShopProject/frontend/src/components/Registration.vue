<template>
    <div class="d-flex justify-content-center align-items-center" style="height: auto;">
        <div class="w-25 my-form">
            <h1 class="text-center">Rejestracja</h1>
            <b-form @submit.prevent="onSubmit">
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

export default {
    setup() {
        const form = ref({
            email: '',
            password: '',
            passwordConfirm: '',
        });

        const onSubmit = () => {
            if (form.value.password !== form.value.passwordConfirm) {
                alert('Hasła nie są takie same!');
                return;
            }

            console.log(form.value);
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