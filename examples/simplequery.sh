#!/bin/bash
curl http://127.0.0.1:8000/v1/completions \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer [Your API Key]" \
  -d '{
  "model": "text-davinci-003",
  "prompt": "What is your name?",
  "max_tokens": 10,
  "temperature": 1.0
}' \
--insecure