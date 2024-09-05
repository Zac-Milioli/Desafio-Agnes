<template>
  <div>
    <h1>Clientes e Atividades de {{ projectName }}</h1>
    <div>
      <h2>Clientes</h2>
      <ul>
        <li v-for="client in clients" :key="client.id">
          {{ client.nome }}
          <button @click="editClient(client)">Editar</button>
          <button @click="deleteClient(client.id)">Excluir</button>
        </li>
      </ul>
      <button @click="createClient">Criar Novo Cliente</button>
    </div>
    <div>
      <h2>Atividades</h2>
      <ul>
        <li v-for="activity in activities" :key="activity.id">
          {{ activity.nome }}
          <button @click="editActivity(activity)">Editar</button>
          <button @click="deleteActivity(activity.id)">Excluir</button>
        </li>
      </ul>
      <button @click="createActivity">Criar Nova Atividade</button>
    </div>
    <!-- Formulários de criação/edição -->
    <div v-if="showClientForm">
      <h3>{{ isEditingClient ? 'Editar Cliente' : 'Criar Cliente' }}</h3>
      <form @submit.prevent="submitClientForm">
        <input v-model="clientForm.nome" placeholder="Nome do Cliente" required />
        <button type="submit">{{ isEditingClient ? 'Salvar' : 'Criar' }}</button>
        <button @click="cancelClientForm">Cancelar</button>
      </form>
    </div>
    <div v-if="showActivityForm">
      <h3>{{ isEditingActivity ? 'Editar Atividade' : 'Criar Atividade' }}</h3>
      <form @submit.prevent="submitActivityForm">
        <input v-model="activityForm.nome" placeholder="Nome da Atividade" required />
        <button type="submit">{{ isEditingActivity ? 'Salvar' : 'Criar' }}</button>
        <button @click="cancelActivityForm">Cancelar</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ClientsActivitiesComponent',
  data() {
    return {
      projectName: '',
      clients: [],
      activities: [],
      showClientForm: false,
      showActivityForm: false,
      isEditingClient: false,
      isEditingActivity: false,
      clientForm: {
        id: null,
        nome: ''
      },
      activityForm: {
        id: null,
        nome: ''
      }
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      const projectId = this.$route.params.id;
      axios.get(`http://localhost:5000/projeto/${projectId}`)
        .then(response => {
          this.projectName = response.data.nome;
        });
      axios.get(`http://localhost:5000/projeto/${projectId}/cliente`)
        .then(response => {
          this.clients = response.data;
        });
      axios.get(`http://localhost:5000/projeto/${projectId}/atividade`)
        .then(response => {
          this.activities = response.data;
        });
    },
    createClient() {
      this.showClientForm = true;
      this.isEditingClient = false;
      this.clientForm = { id: null, nome: '' };
    },
    editClient(client) {
      this.showClientForm = true;
      this.isEditingClient = true;
      this.clientForm = { ...client };
    },
    submitClientForm() {
      const projectId = this.$route.params.id;
      if (this.isEditingClient) {
        axios.put(`http://localhost:5000/api/cliente/${this.clientForm.id}`, this.clientForm)
          .then(() => {
            this.fetchData();
            this.cancelClientForm();
          });
      } else {
        axios.post(`http://localhost:5000/api/cliente`, { ...this.clientForm, projeto_id: projectId })
          .then(() => {
            this.fetchData();
            this.cancelClientForm();
          });
      }
    },
    cancelClientForm() {
      this.showClientForm = false;
      this.clientForm = { id: null, nome: '' };
    },
    deleteClient(id) {
      axios.delete(`http://localhost:5000/api/cliente/${id}`)
        .then(() => {
          this.fetchData();
        });
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
        axios.put(`http://localhost:5000/api/atividade/${this.activityForm.id}`, this.activityForm)
          .then(() => {
            this.fetchData();
            this.cancelActivityForm();
          });
      } else {
        axios.post(`http://localhost:5000/api/atividade`, { ...this.activityForm, projeto_id: projectId })
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
      axios.delete(`http://localhost:5000/api/atividade/${id}`)
        .then(() => {
          this.fetchData();
        });
    }
  }
}
</script>