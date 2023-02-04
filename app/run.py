import falcon
import json
from wsgiref import simple_server
import re
from pyChatGPT import ChatGPT
from decouple import config

class ChatGPTResource(object):
    def __init__(self, openAIUser, openAIPass):
        self._api = ChatGPT(auth_type='openai', email=openAIUser, password=openAIPass)
    
    def on_post_completions(self, req, resp):
        prompt = req.media['prompt']

        if 'max_tokens' in req.media:
            numTokens = req.media['max_tokens']
            prompt += " - Answer in %d words or less! " % numTokens
        
        
        print("Prompt: " + prompt)
        chatResponse = self._api.send_message(prompt)
        print(chatResponse)

        tokensPrompt = len(re.findall(r'\w+', prompt))
        tokensResponse = len(re.findall(r'\w+', chatResponse['message']))
        jsonResponse = {
                "id": chatResponse['conversation_id'],
                "object":"text_completion",
                "created":1670734183,
                "model":"text-davinci-003",
                "choices":[
                    {
                        'text': chatResponse['message'],
                        "index":0,
                        "logprobs":None,
                        "finish_reason":"stop"
                    }
                ],
                "usage":{
                    "prompt_tokens":tokensPrompt,
                    "completion_tokens":tokensResponse,
                    "total_tokens":tokensPrompt + tokensResponse
                }
            }
        resp.text = json.dumps(jsonResponse)

    def on_get_reset(self, req, resp):
        self._api.reset_conversation()
        jsonResponse = {'message': 'OK'}
        resp.text = json.dumps(jsonResponse)
    
    def on_get_refresh(self, req, resp):
        self._api.refresh_chat_page()
        jsonResponse = {'message': 'OK'}
        resp.text = json.dumps(jsonResponse)
    
    def on_get_clear(self, req, resp):
        self._api.clear_conversations()
        jsonResponse = {'message': 'OK'}
        resp.text = json.dumps(jsonResponse)


if __name__ == '__main__':
    api = falcon.App()
    chatGPTEndpoint = ChatGPTResource(config('OPENAI_USER'), config('OPENAI_PASS'))
    api.add_route('/v1/completions', chatGPTEndpoint, suffix='completions')
    api.add_route('/v1/reset', chatGPTEndpoint, suffix='reset')
    api.add_route('/v1/refresh', chatGPTEndpoint, suffix='refresh')
    api.add_route('/v1/clear', chatGPTEndpoint, suffix='clear')

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