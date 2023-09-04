
## Rodando em k8s

**Pré requisitos**
- minikube instalado, caso não tenha só baixar uilizando esse [link](https://minikube.sigs.k8s.io/docs/start/)
- helm instalado, caso não tenha só baixar uilizando esse [link](https://helm.sh/docs/intro/install/)
- docker instalado, caso não tenha só baixar uilizando esse [link](https://docs.docker.com/engine/install/)  

O Primeiro passo vai ser inicializar o seu ambiente kubernetes, com esse comando:
```shell
minikube start
```

Proximo passo vai ser criar apontar o docker-cli para a Engine do minikube assim facilitando na hora do build, pois o k8s já terá acesso a imagem. 
Caso seu SO seja linux ou MacOs:
```shell
eval $(minikube docker-env)
```
Caso seja Windows:
```shell
minikube docker-env
```  

Agora vamos fazer o build da imagem a partir do Dockerfile
```shell
docker build -t lanchonete-da-rua .
```
    
Como ja buildamos a imagem nos passos anteriores, a próxima coisa que voce irá fazer é o build da imagem que será enviar a imagem docker para o seu ambiente kubernetes, utlizando o comando abaixo:
```shell
minikube image load lanchonete-da-rua
```

Com o seu ambiente já inicializado e com a imagem da aplicação disponivel podermos prosseguir com a preparação do nosso helm chart personalizado. Entre na pasta `deploy` e rode o seguinte comando para levantar as dependencias do nosso chart.
``` shell
 helm dependency build
```

Caso você queira validar o que está sendo criado e quais yamls estão sendo gerados, pode rodar o comando abaixo, senão pode pular para o próximo comando.
```shell
helm template lanchonete-de-rua .
```

E para finalizar a criação dos nossos pods pode instalar o chart no seu ambiente
```shell
helm install lanchonete-de-rua .
```
**para testar ambiente k8s**

Para testar se a nossa aplicação subiu vamos usar o `kubeclt`, para disparar comandos contra o cluster.

* Comandos: 
    - validar se os pods subiram
      ```shell
        kubectl get pods
      ```
    - conseguir bater na api
      ```shell
        kubectl port-forward deployment/lanchonete-de-rua-deployment 5000:5000
      ```
    - validar criação das secrets
      ```shell
        kubectl get secrets
      ```


### Recomendamos tambem:
[Instalação utilizando docker](./Docker.md)

[Overview da API](../overview.md)

### Siga em frente:
[Endpoints da aplicação](../endpoints/endpoints.md)