# Discord Bot Boiler Plate

Discord.py 2.0 Boiler Plate with Docker containerization and docker-compose for orchestration. It is setup to allow for two different environments (dev/prod).

- Cogs
- Slash Commands
- Json Configs
- Docker & Docker Compose setup.

## Requirements

- docker
- docker-compose
- update config.json files with the following items
    - BOT_TOKEN: the bots access token. found in discord developer portal
    - GUILD_ID: the guild's id. found in GUI by right clicking the guild photo and copy id
    - APP_ID: bot application id. found in the discord developer portal

## Setup

```sh
# build docker image. working directory must in the same directory as dockerfile
docker build -t dockerbot:latest .

# start the bot to view the logs for dev environment.
docker-compose --file dev.docker-compose.yml up

# start the bot in the background for production environment
docker-compose --file prod.docker-compose.yml up -d

```

