import sys
from io import BytesIO

import urllib.request
import re

text = urllib.request.urlopen('http://127.0.0.1:4040').read()
url  = re.search(b'https://([A-Za-z0-9]+)\.ngrok\.io', text)

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '394874562:AAFRl4sA24DjBVUJ6sVlk4ldJryqI2t1QAs'
WEBHOOK_URL = url.group(0).decode('utf-8')+'/hook'#'https://e0a15dfe.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
		'start',
        'user',
        'english',
        'french',
		'chinese',
		'c1_play',
		'c2_play',
		'c3_play',
		'c4_play',
		'c5_play',
		'e1_play',
		'e2_play',
		'e3_play',
		'e4_play',
		'e5_play',
		'f1_play',
		'f2_play',
		'f3_play',
		'f4_play',
		'f5_play',
        'cancel'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'user',
            'conditions': 'go_user'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'english',
            'conditions': 'go_english'
        },
		{
		    'trigger': 'advance',
		    'source': 'user',
		    'dest': 'french',
		    'conditions': 'go_french'
		},
		{
		    'trigger': 'advance',
		    'source': 'user',
		    'dest': 'chinese',
		    'conditions': 'go_chinese'
		},
        {
            'trigger': 'advance',
            'source': 'chinese',
            'dest': 'c1_play',
            'conditions': 'go_play1'
        },
        {
            'trigger': 'advance',
            'source': 'chinese',
            'dest': 'c2_play',
            'conditions': 'go_play2'
        },
        {
            'trigger': 'advance',
            'source': 'chinese',
            'dest': 'c3_play',
            'conditions': 'go_play3'
        },
        {
            'trigger': 'advance',
            'source': 'chinese',
            'dest': 'c4_play',
            'conditions': 'go_play4'
        },
        {
            'trigger': 'advance',
            'source': 'chinese',
            'dest': 'c5_play',
            'conditions': 'go_play5'
        },
        {
            'trigger': 'advance',
            'source': 'english',
            'dest': 'e1_play',
            'conditions': 'go_play1'
        },
        {
            'trigger': 'advance',
            'source': 'english',
            'dest': 'e2_play',
            'conditions': 'go_play2'
        },
        {
            'trigger': 'advance',
            'source': 'english',
            'dest': 'e3_play',
            'conditions': 'go_play3'
        },
        {
            'trigger': 'advance',
            'source': 'english',
            'dest': 'e4_play',
            'conditions': 'go_play4'
        },
        {
            'trigger': 'advance',
            'source': 'english',
            'dest': 'e5_play',
            'conditions': 'go_play5'
        },
        {
            'trigger': 'advance',
            'source': 'french',
            'dest': 'f1_play',
            'conditions': 'go_play1'
        },
        {
            'trigger': 'advance',
            'source': 'french',
            'dest': 'f2_play',
            'conditions': 'go_play2'
        },
        {
            'trigger': 'advance',
            'source': 'french',
            'dest': 'f3_play',
            'conditions': 'go_play3'
        },
        {
            'trigger': 'advance',
            'source': 'french',
            'dest': 'f4_play',
            'conditions': 'go_play4'
        },
        {
            'trigger': 'advance',
            'source': 'french',
            'dest': 'f5_play',
            'conditions': 'go_play5'
        },
        {
            'trigger': 'advance',
            'source': [
                'chinese',
                'english',
                'french'
            ],
            'dest': 'cancel',
            'conditions': 'go_cancel'
        },
        {
            'trigger': 'advance',
            'source': [
	        	'c1_play',
	        	'c2_play',
        		'c3_play',
	        	'c4_play',
        		'c5_play',
        		'e1_play',
        		'e2_play',
        		'e3_play',
        		'e4_play',
        		'e5_play',
        		'f1_play',
        		'f2_play',
        		'f3_play',
        		'f4_play',
        		'f5_play'
            ],
            'dest': 'cancel',
            'conditions': 'go_finish'
        },
        {
            'trigger': 'advance',
            'source': 'cancel',
            'dest': 'user',
            'conditions': 'go_basic'
        },
        {
            'trigger': 'go_back',
            'source': 'cancel',
            'dest': 'user',
        }
    ],
    initial='start',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
