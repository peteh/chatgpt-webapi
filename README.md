# chatgpt-webapi
This project uses pyChatGPT to provide an API endpoint similar to the official text completion endpoint.

## API endpoints

### Endpoint /v1/completions

The requests and responses are somewhat compatible to OpenAI's official API for text completions.

Request (POST):

```json
{
   "model":"text-davinci-003", # not interpreted
   "prompt": "What are you doing ChatGPT?", 
   "max_tokens":100, # not interpreted
   "temperature":1 # not intepreted
}
```

Response:

```json
{
    "choices":[
        {"text":"I am currently running on a computer, processing and generating text based on the prompts given to me by users like you. Is there something specific you would like me to help you with?\n\n"
        }
    ]
}
```

### Endpoint /v1/reset

This is not an official endpoint from OpenAI but it let's you reset the conversation you are currently in. 

## Docker

I haven't managed to run this in docker yet.
