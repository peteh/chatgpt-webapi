import falcon
import json
from wsgiref import simple_server

from pyChatGPT import ChatGPT
from decouple import config

class ChatGPTResource(object):
    def __init__(self, openAIUser, openAIPass):
        self._api = ChatGPT(auth_type='openai', email=openAIUser, password=openAIPass)
    
    def handlePrompt(self, prompt):
        print("Prompt: " + prompt)
        chatResponseCall = self._api.send_message(prompt)
        chatResponse = chatResponseCall['message']
        print("Response: " + chatResponse)
        return chatResponse 
    
    def on_get_completions(self, req, resp):
        prompt = "Hello World"
        chatResponse = self.handlePrompt(prompt)
        jsonResponse = {'choices': [{'text': chatResponse} ]}
        resp.text = json.dumps(jsonResponse)

    def on_post_completions(self, req, resp):
        prompt = req.media["prompt"]
        chatResponse = self.handlePrompt(prompt)
        jsonResponse = {'choices': [{'text': chatResponse} ]}
        resp.text = json.dumps(jsonResponse)

    def on_get_reset(self, req, resp):
        self._api.reset_conversation()
        jsonResponse = {'message': 'OK'}
        resp.text = json.dumps(jsonResponse)


if __name__ == '__main__':
    api = falcon.App()
    chatGPTEndpoint = ChatGPTResource(config('OPENAI_USER'), config('OPENAI_PASS'))
    api.add_route('/v1/completions', chatGPTEndpoint, suffix='completions')
    api.add_route('/v1/reset', chatGPTEndpoint, suffix='reset')

    try:
        httpd = simple_server.make_server('', 8000, api)
    except Exception as e:
        #logger.error(f"Couldn't start Server: {e}")
        #return 1
        exit(1)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()