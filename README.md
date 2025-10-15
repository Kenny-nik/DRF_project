# DRF_project

## О проекте

**DRF Project** — это веб-приложение на основе Django REST Framework для выполнения домашнего задания

## Быстрый старт

Следуйте этим шагам для настройки и запуска проекта локально:

### Предварительные требования
*   Docker
*   Docker Compose

### Установка и запуск

1.  Клонируйте репозиторий:
    ```bash
    git clone https://github.com/Kenny-nik/DRF_project.git
    cd DRF_project
    ```

2.  Запустите приложение:
    ```bash
    docker-compose up -d
    ```
    Флаг `-d` запускает контейнеры в фоновом режиме.

### Проверка работоспособности

После запуска проверьте статус сервисов:

1.  **Django API:** Откройте в браузере http://localhost:8000
2.  **Flower Dashboard:** Откройте http://localhost:5555 для мониторинга задач Celery
3.  **Проверьте статус контейнеров:**
    ```bash
    docker-compose ps
    ```
4.  **Просмотрите логи конкретного сервиса:**
    ```bash
    docker-compose logs web
    docker-compose logs celery_worker
    docker-compose logs celery_beat
    ```



