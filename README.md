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

# Initial Deploy:


```bash
# install fly.io cli and login
curl -L https://fly.io/install.sh | sh
flyctl auth login

#
flyctl secrets set BOT_TOKEN=<THE_BOT_TOKEN>
flyctl launch
```