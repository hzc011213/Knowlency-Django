import json

import requests
from django.shortcuts import render, redirect

messages_history = []


def chat(request):
    try:
        global messages_history

        if request.method == 'POST':
            message = request.POST.get('message_input')

            # Add user's message to the history
            user_message_data = {
                'role': 'user',
                'content': message
            }
            messages_history.append(user_message_data)

            # Sending an HTTP request to the specified server
            url = 'http://13.55.198.181:4399/'
            assistant_response = requests.post(url, data=json.dumps(messages_history))

            # Check if the request was successful
            if assistant_response.status_code == 200:
                assistant_response_data = {
                    'role': 'assistant',
                    'content': assistant_response.text
                }
                messages_history.append(assistant_response_data)
            else:
                error_data = {
                    'role': 'assistant',
                    'content': 'Error: Unable to fetch the response'
                }
                messages_history.append(error_data)

            return redirect('chat:chat')

        context = {
            'messages_history': messages_history
        }
        return render(request, 'chat/chat.html', context)

    except:
        return "Error"


# Clear the in-memory list
def clear_history(request):
    global messages_history
    messages_history = []
    return redirect('chat:chat')
