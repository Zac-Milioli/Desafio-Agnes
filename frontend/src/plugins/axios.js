import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:5000', // URL base para todas as requisições
  timeout: 10000, // Tempo limite para a requisição
  headers: {
    'Content-Type': 'application/json'
  }
});

export default instance;