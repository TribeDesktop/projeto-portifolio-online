
# API de Disciplinas

Esta API permite a criação, leitura, atualização e exclusão (CRUD) de disciplinas de um banco de dados MySQL. A API foi desenvolvida utilizando `urllib` e se comunica com a tabela `disciplinas`.

## Endereço Base

```
http://localhost:8080
```

## Endpoints

### 1. Listar todas as disciplinas

**Descrição**: Retorna todas as disciplinas cadastradas no banco de dados.

- **Método**: `GET`
- **URL**: `/`

#### Exemplo de resposta:

```json
[
  {
    "disciplinaID": 1,
    "nomeDisciplina": "Matemática",
    "siglaDisciplina": "MAT101",
    "aulasSemanaisDisciplina": 5,
    "aulasTotaisSemestreDisciplina": 80,
    "cargaHorariaDisciplina": 60,
    "ementa": "Introdução à álgebra e geometria.",
    "turmaID": 1,
    "cursoID": 2
  }
]
```

### 2. Obter uma disciplina por ID

**Descrição**: Retorna uma disciplina específica, baseada no `disciplinaID`.

- **Método**: `GET`
- **URL**: `/?disciplinaID={id}`

#### Parâmetros:

- `disciplinaID` (obrigatório): O ID da disciplina.

#### Exemplo de resposta:

```json
{
  "disciplinaID": 1,
  "nomeDisciplina": "Matemática",
  "siglaDisciplina": "MAT101",
  "aulasSemanaisDisciplina": 5,
  "aulasTotaisSemestreDisciplina": 80,
  "cargaHorariaDisciplina": 60,
  "ementa": "Introdução à álgebra e geometria.",
  "turmaID": 1,
  "cursoID": 2
}
```

### 3. Criar uma nova disciplina

**Descrição**: Cria uma nova disciplina no banco de dados.

- **Método**: `POST`
- **URL**: `/`
- **Corpo da requisição (JSON)**:

```json
{
  "nomeDisciplina": "Matemática",
  "siglaDisciplina": "MAT101",
  "aulasSemanaisDisciplina": 5,
  "aulasTotaisSemestreDisciplina": 80,
  "cargaHorariaDisciplina": 60,
  "ementa": "Introdução à álgebra e geometria.",
  "turmaID": 1,
  "cursoID": 2
}
```

#### Exemplo de resposta:

```json
{
  "message": "Disciplina criada com sucesso."
}
```

### 4. Atualizar uma disciplina

**Descrição**: Atualiza os dados de uma disciplina existente.

- **Método**: `PUT`
- **URL**: `/`
- **Corpo da requisição (JSON)**:

```json
{
  "disciplinaID": 1,
  "nomeDisciplina": "Matemática Avançada",
  "siglaDisciplina": "MAT102",
  "aulasSemanaisDisciplina": 6,
  "aulasTotaisSemestreDisciplina": 90,
  "cargaHorariaDisciplina": 70,
  "ementa": "Álgebra avançada e geometria.",
  "turmaID": 1,
  "cursoID": 2
}
```

#### Exemplo de resposta:

```json
{
  "message": "Disciplina atualizada com sucesso."
}
```

### 5. Deletar uma disciplina

**Descrição**: Exclui uma disciplina do banco de dados.

- **Método**: `DELETE`
- **URL**: `/?disciplinaID={id}`

#### Parâmetros:

- `disciplinaID` (obrigatório): O ID da disciplina a ser excluída.

#### Exemplo de resposta:

```json
{
  "message": "Disciplina deletada com sucesso."
}
```

## Códigos de Resposta

- `200 OK`: A requisição foi bem-sucedida.
- `201 Created`: Recurso criado com sucesso.
- `400 Bad Request`: Dados inválidos foram fornecidos na requisição.
- `404 Not Found`: Disciplina não encontrada.
- `500 Internal Server Error`: Ocorreu um erro no servidor.

## Exemplo de Uso

### 1. Obter todas as disciplinas:

```bash
curl -X GET http://localhost:8080
```

### 2. Obter uma disciplina por ID:

```bash
curl -X GET http://localhost:8080?disciplinaID=1
```

### 3. Criar uma nova disciplina:

```bash
curl -X POST http://localhost:8080 \
-H "Content-Type: application/json" \
-d '{
  "nomeDisciplina": "Matemática",
  "siglaDisciplina": "MAT101",
  "aulasSemanaisDisciplina": 5,
  "aulasTotaisSemestreDisciplina": 80,
  "cargaHorariaDisciplina": 60,
  "ementa": "Introdução à álgebra e geometria.",
  "turmaID": 1,
  "cursoID": 2
}'
```

### 4. Atualizar uma disciplina:

```bash
curl -X PUT http://localhost:8080 \
-H "Content-Type: application/json" \
-d '{
  "disciplinaID": 1,
  "nomeDisciplina": "Matemática Avançada",
  "siglaDisciplina": "MAT102",
  "aulasSemanaisDisciplina": 6,
  "aulasTotaisSemestreDisciplina": 90,
  "cargaHorariaDisciplina": 70,
  "ementa": "Álgebra avançada e geometria.",
  "turmaID": 1,
  "cursoID": 2
}'
```

### 5. Excluir uma disciplina:

```bash
curl -X DELETE http://localhost:8080?disciplinaID=1
```
