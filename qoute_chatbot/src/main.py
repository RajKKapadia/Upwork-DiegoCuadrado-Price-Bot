from flask import Flask, request

from qoute_chatbot.helper.conversation import get_location
from qoute_chatbot.helper.twilio_api import send_message
from qoute_chatbot.helper.utils import get_price
from qoute_chatbot.logger import logging

logger = logging.getLogger(__name__)


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return 'OK', 200


@app.route('/twilio', methods=['POST'])
def twilio():
    try:
        logger.info('A new twilio request...')
        data = request.form.to_dict()
        query = data['Body']
        sender_id = data['From']

        location_info = get_location(query)

        if location_info['status'] == 1 and location_info['location'] != -1:
            response = get_price(location_info['location'])
        else:
            response = 'I did not get the location very clearly, can you rephrase that.'

        logger.info(f'Sender -> {sender_id}')
        logger.info(f'Query -> {query}')
        logger.info(f'Response -> {response}')

        send_message(sender_id, response)
        logger.info('Request success.')
    except:
        logger.info('Request failed.')
        pass

    return 'OK', 200
