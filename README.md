# Arrgbot

## Help

simply run `!help` in to see all available commands

## Add Bot to your Server:

[invite link](https://discord.com/api/oauth2/authorize?client_id=775774321318297630&permissions=8&scope=bot)

## Setup:
```bash
virtualenv --python=/usr/bin/python3.8 ~/.envs/arrgbot/
source ~/.envs/arrgbot/bin/activate

cd /mnt/d/dev/arrgbot
pip install -U -r arrgbot/requirements.txt
```

## Run:
```bash
export PYTHONPATH=.
export BOT_TOKEN="<BOT TOKEN>"
python arrgbot/main.py
```

## Deploy
```bash
ssh tomato
cd ~/arrgbott
git pull
docker-compose --env-file /arrgbot_env -p arrgbot up --build -d
```
