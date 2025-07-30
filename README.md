### Dev mode

1. Создать `.env.dev` по образцу `.env.example`
2. `docker-compose -f docker-compose.dev.yml up --build`

`docker-compose -f docker-compose.dev.yml down -v` остановка с удалением volumes

### Prod mode

1. Создать `.env.prod` по образцу `.env.example`
2. `docker-compose -f docker-compose.prod.yml up --build`