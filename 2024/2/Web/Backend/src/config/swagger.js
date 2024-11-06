import swaggerJSDoc from 'swagger-jsdoc';
import swaggerUi from 'swagger-ui-express';
import express from 'express';

const options = {
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'ProjetoPO API',
      version: '1.0.0',
      description: 'API para gerenciamento de alunos',
    },
    servers: [
      {
        url: 'http://localhost:3000', // Substitua pela URL da sua aplicação
      },
    ],
  },
  apis: ['./src/routes/*.js', './src/models/*.js'], // Arquivos para gerar a documentação
};

const swaggerSpec = swaggerJSDoc(options);

const swaggerDocs = (app) => {
  app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec));
};

export default swaggerDocs;
