from datetime import datetime

from flask import Flask, request

from qoute_chatbot.helper.conversation import get_location
from qoute_chatbot.helper.azure_conversation import azure_chat_completion
from qoute_chatbot.helper.twilio_api import send_message
from qoute_chatbot.helper.utils import get_price, generate_messages
from qoute_chatbot.helper.database_api import create_user, update_messages, get_user\

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return 'OK', 200


@app.route('/twilio', methods=['POST'])
def twilio():
    try:
        print('A new twilio request...')
        data = request.form.to_dict()
        query = data['Body']
        sender_id = data['From']
        user_name = data['ProfileName']

        user = get_user(sender_id)

        # create chat_history from the previous conversations
        if user:
            messages = generate_messages(user['messages'][-2:], query)
        else:
            messages = generate_messages([], query)

        parameters = get_location(query)

        print(query)
        print(sender_id)
        print(parameters)

        if parameters['status'] == 1 and parameters['location'] != -1 and parameters['quantity'] != -1:
            response = get_price(parameters['location'], parameters['quantity'])
        elif parameters['status'] == 1 and parameters['location'] != -1 and parameters['quantity'] == -1:
            response = get_price(parameters['location'])
        else:
            response = azure_chat_completion(messages)

        print(response)

        if user:
            update_messages(sender_id, query,
                            response, user['messageCount'])
        else:
            # if not create
            message = {
                'query': query,
                'response': response,
                'createdAt': datetime.now().strftime('%d/%m/%Y, %H:%M')
            }
            user = {
                'userName': user_name,
                'senderId': sender_id,
                'messages': [message],
                'messageCount': 1,
                'mobile': sender_id.split(':')[-1],
                'channel': 'WhatsApp',
                'is_paid': False,
                'created_at': datetime.now().strftime('%d/%m/%Y, %H:%M')
            }
            create_user(user)
        send_message(sender_id, response)
        print('Request success.')
    except:
        print('Request failed.')
        pass

    return 'OK', 200
