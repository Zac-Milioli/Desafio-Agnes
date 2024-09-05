<template>
  <div class="welcome">
    <h1 class="fade-in">Bem vindo!</h1>
    <button @click="goToProjects">Ir para "Meus Projetos"</button>
  </div>
</template>

<script>
export default {
  name: 'WelcomeComponent',
  methods: {
    goToProjects() {
      this.$router.push('/projects');
    }
  }
}
</script>

<style>
.welcome {
  text-align: center;
  margin-top: 50px;
}
.fade-in {
  animation: fadeIn 2s;
}
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
</style>