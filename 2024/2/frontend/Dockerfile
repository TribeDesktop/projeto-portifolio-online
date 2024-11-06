FROM node:20.17.0-alpine3.20


WORKDIR /app


COPY package*.json ./


RUN npm install --production


COPY . .


EXPOSE 5173


CMD ["node", "app.js"]
