# Rodar a API em uma imagem docker

Na raiz:

## Construindo a imagem:
```
docker build -t lanchonete-da-rua .
```

## Subindo a aplicação + DB:
```
docker compose up
```

## Conferir se aplicação está de pé:
```
http://localhost:5000/
```

### Recomendamos tambem:
[Instalação utilizando k8s](./k8s.md)

[Overview da API](../overview.md)

### Siga em frente:
[Endpoints da aplicação](../endpoints/endpoints.md)