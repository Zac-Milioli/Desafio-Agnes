<template>
  <div class="page-container">
    <div class="header-bar">
      <h1>Clientes e Atividades</h1>
    </div>
    <div class="content">
      <div class="column">
        <h2>Clientes</h2>
        <!-- Conteúdo relacionado aos clientes -->
      </div>
      <div class="column">
        <h2>Atividades</h2>
        <!-- Conteúdo relacionado às atividades -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ClientsActivitiesComponent',
  data() {
    return {
      showActivityForm: false,
      isEditingActivity: false,
      activityForm: { id: null, nome: '' }
    };
  },
  methods: {
    fetchData() {
      // Implementação da função fetchData
    },
    createActivity() {
      this.showActivityForm = true;
      this.isEditingActivity = false;
      this.activityForm = { id: null, nome: '' };
    },
    editActivity(activity) {
      this.showActivityForm = true;
      this.isEditingActivity = true;
      this.activityForm = { ...activity };
    },
    submitActivityForm() {
      const projectId = this.$route.params.id;
      if (this.isEditingActivity) {
        this.$axios.put(`/api/atividade/${this.activityForm.id}`, this.activityForm)
          .then(() => {
            this.fetchData();
            this.cancelActivityForm();
          });
      } else {
        this.$axios.post(`/api/atividade`, { ...this.activityForm, projeto_id: projectId })
          .then(() => {
            this.fetchData();
            this.cancelActivityForm();
          });
      }
    },
    cancelActivityForm() {
      this.showActivityForm = false;
      this.activityForm = { id: null, nome: '' };
    },
    deleteActivity(id) {
      this.$axios.delete(`/api/atividade/${id}`)
        .then(() => {
          this.fetchData();
        });
    }
  }
}
</script>

<style scoped>
html, body {
  margin: 0;
  padding: 0;
  height: 100%;
}

.page-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.header-bar {
  background-color: #0078d4; /* Azul da Microsoft */
  color: white;
  padding: 10px 20px;
}

.header-bar h1 {
  margin: 0;
  font-size: 1.5em;
}

.content {
  display: flex;
  flex: 1;
  padding: 20px;
}

.column {
  flex: 1;
  padding: 10px;
}

button {
  background-color: #0078d4; /* Azul da Microsoft */
  color: white;
  border: none;
  padding: 10px; /* Reduzido o tamanho dos botões */
  font-size: 1em;
  cursor: pointer;
  border-radius: 0; /* Tornar os botões quadrados */
  margin: 10px; /* Aumentar as margens dos botões */
}

button:hover {
  background-color: #005a9e; /* Azul mais escuro ao passar o mouse */
}
</style>