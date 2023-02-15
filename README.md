# chatgpt-webapi

This project uses pyChatGPT to provide an API endpoint similar to the official text completion endpoint.

## Dependencies

Start in the root path of the repository and create a new virtual environment.

```bash
cd app
python3 -m venv .venv
```

Activate the environment and install the dependencies

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## API endpoints

By default the server will be opened on port 8000.

### Endpoint /v1/completions

The requests and responses are somewhat compatible to OpenAI's official API for text completions.

Request (POST):

```json
{
   "model":"text-davinci-003", # not interpreted
   "prompt": "What are you doing ChatGPT?", 
   "max_tokens":100, # try to limit the number of words to this amount or less, smaller number means shorter answers
   "temperature":1 # not intepreted
}
```

Response:

```json
{
   "id":"1ea4a4b7-7bdb-4a8b-b223-2de67a9542fb", # uuid of the conversation
   "object":"text_completion",
   "created":1670734183, # currently constant
   "model":"text-davinci-003", 
   "choices":[
      {
         "text":"My name is ChatGPT. I am a highly advanced language model developed by OpenAI, designed to generate human-like text based on the input provided to me. I have been trained on a large corpus of text, allowing me to generate coherent and informative responses to a wide range of questions. I am constantly learning and improving my responses, making me a valuable resource for information and knowledge. Whether you're looking for a quick answer or in-depth information, I'm here to help.\n\n",
         "index":0,
         "logprobs":null,
         "finish_reason":"stop"
      }
   ],
   "usage":{
      "prompt_tokens":10, # words in prompt
      "completion_tokens":85, # words in response
      "total_tokens":95 # total words
   }
}
```

### Endpoint /v1/reset

This is not an official endpoint from OpenAI but it let's you reset the conversation you are currently in.

## Docker

It's possible to run it with the Dockerfile. Update the environment variables in the docker-compose.yaml file to your login credentials. Then build the container.

```bash
docker compose build
```

To run you can use

```bash
docker compose up
```
