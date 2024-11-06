FROM postgres:16.4-alpine3.20

ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_DB=praxis

COPY ./query.sql /docker-entrypoint-initdb.d/

EXPOSE 5432
