<template>
  <div>
    <h1>Meus Projetos</h1>
    <div v-for="status in projectStatuses" :key="status">
      <h2>{{ status }}</h2>
      <ul>
        <li v-for="project in filteredProjects(status)" :key="project.id">
          <span @click="goToClientsActivities(project)">{{ project.nome }}</span>
          <button @click="editProject(project)">Editar</button>
          <button @click="deleteProject(project.id)">Excluir</button>
        </li>
      </ul>
    </div>
    <button @click="showCreateProjectForm">Criar Novo Projeto</button>

    <!-- Formulário de Criação/Edição de Projeto -->
    <div v-if="showForm">
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
import axios from 'axios';

export default {
  name: 'ProjectsComponent',
  data() {
    return {
      projects: [],
      projectStatuses: ['Concluído', 'Cancelado', 'Em andamento'],
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
      axios.get('/api/projects')
        .then(response => {
          this.projects = response.data;
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
      axios.post('/api/projects', this.form)
        .then(() => {
          this.fetchProjects();
          this.showForm = false;
        });
    },
    editProject(project) {
      this.form = { ...project };
      this.showForm = true;
      this.isEditing = true;
    },
    updateProject() {
      axios.put(`/api/projects/${this.form.id}`, this.form)
        .then(() => {
          this.fetchProjects();
          this.showForm = false;
        });
    },
    deleteProject(id) {
      axios.delete(`/api/projects/${id}`)
        .then(() => {
          this.fetchProjects();
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