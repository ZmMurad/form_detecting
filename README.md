## Тестовый проект для вакансии
### Технологии:
- Django
- MongoDB
- Docker
- Docker-compose

#### О сервисе
- MongoDB база данных
- FormDetecting (сервис формы)




### Развертывание
Перед началом убедитесь что у вас есть docker
```
docker volume create mongodata
```
```sh
docker-compose up -d --build
```