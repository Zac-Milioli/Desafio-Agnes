<template>
  <div class="projects-container">
    <h1>Meus Projetos</h1>
    <button class="create-button" @click="showCreateProjectForm">Criar Projeto</button>

    <div v-for="status in projectStatuses" :key="status" class="status-section">
      <h2>{{ status }}</h2>
      <div class="cards-container">
        <div v-for="project in filteredProjects(status)" :key="project.id" class="project-card">
          <div @click="goToClientsActivities(project)" class="card-content">
            <h3>{{ project.nome }}</h3>
            <p>Status: {{ project.status }}</p>
          </div>
          <div class="card-actions">
            <button @click="editProject(project)">Editar</button>
            <button @click="deleteProject(project.id)">Excluir</button>
          </div>
        </div>
      </div>
    </div>

    <div v-if="showForm" class="form-container">
      <h2>{{ isEditing ? 'Editar Projeto' : 'Criar Novo Projeto' }}</h2>
      <form @submit.prevent="isEditing ? updateProject() : createProject()">
        <label for="nome">Nome:</label>
        <input type="text" v-model="form.nome" required />

        <label for="status">Status:</label>
        <select v-model="form.status" required>
          <option v-for="status in projectStatuses" :key="status" :value="status">{{ status }}</option>
        </select>

        <button type="submit">{{ isEditing ? 'Salvar' : 'Criar' }}</button>
        <button type="button" @click="cancelForm">Cancelar</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProjectsComponent',
  data() {
    return {
      projects: [],
      projectStatuses: ['Em andamento', 'Concluído', 'Cancelado'],
      showForm: false,
      isEditing: false,
      form: {
        id: null,
        nome: '',
        status: ''
      }
    };
  },
  created() {
    this.fetchProjects();
  },
  methods: {
    fetchProjects() {
      this.$axios.get('/projeto')
        .then(response => {
          this.projects = response.data;
        })
        .catch(error => {
          console.error('Erro ao buscar projetos:', error);
        });
    },
    filteredProjects(status) {
      return this.projects.filter(project => project.status === status);
    },
    goToClientsActivities(project) {
      this.$router.push(`/projects/${project.id}/clients-activities`);
    },
    showCreateProjectForm() {
      this.resetForm();
      this.showForm = true;
      this.isEditing = false;
    },
    createProject() {
      this.$axios.post('/api/projeto', this.form)
        .then(() => {
          this.fetchProjects();
          this.showForm = false;
        })
        .catch(error => {
          console.error('Erro ao criar projeto:', error);
        });
    },
    editProject(project) {
      this.form = { ...project };
      this.showForm = true;
      this.isEditing = true;
    },
    updateProject() {
      this.$axios.put(`/api/projeto/${this.form.id}`, this.form)
        .then(() => {
          this.fetchProjects();
          this.showForm = false;
        })
        .catch(error => {
          console.error('Erro ao atualizar projeto:', error);
        });
    },
    deleteProject(id) {
      this.$axios.delete(`/api/projeto/${id}`)
        .then(() => {
          this.fetchProjects();
        })
        .catch(error => {
          console.error('Erro ao excluir projeto:', error);
        });
    },
    cancelForm() {
      this.showForm = false;
    },
    resetForm() {
      this.form = {
        id: null,
        nome: '',
        status: ''
      };
    }
  }
}
</script>

<style scoped>
.projects-container {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #333;
  padding: 20px;
}

.create-button {
  background-color: #0078d4;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  margin-bottom: 20px;
}

.create-button:hover {
  background-color: #005a9e;
}

.status-section {
  margin-bottom: 40px;
}

.cards-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.project-card {
  background-color: #f3f2f1;
  border: 1px solid #e1dfdd;
  border-radius: 4px;
  padding: 20px;
  width: 300px;
  cursor: pointer;
}

.project-card:hover {
  background-color: #e1dfdd;
}

.card-content {
  margin-bottom: 10px;
}

.card-actions {
  display: flex;
  justify-content: space-between;
}

.card-actions button {
  background-color: #0078d4;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
}

.card-actions button:hover {
  background-color: #005a9e;
}

.form-container {
  background-color: #f3f2f1;
  border: 1px solid #e1dfdd;
  border-radius: 4px;
  padding: 20px;
  width: 300px;
  margin-top: 20px;
}

.form-container form {
  display: flex;
  flex-direction: column;
}

.form-container label {
  margin-bottom: 5px;
}

.form-container input,
.form-container select {
  margin-bottom: 10px;
  padding: 5px;
  border: 1px solid #e1dfdd;
  border-radius: 4px;
}

.form-container button {
  background-color: #0078d4;
  color: white;
  border: none;
  padding: 10px;
  cursor: pointer;
}

.form-container button:hover {
  background-color: #005a9e;
}
</style>