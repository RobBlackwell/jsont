#!/usr/bin/env bash

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent" \
  -H 'Content-Type: application/json' \
  -H "X-goog-api-key:$GEMINI_API_KEY" \
  -X POST \
    -d '{
    "contents": [
        {
        "parts": [
            {
              "text": "Given an RGB hex value of #FF0000, tell me the corresponding name of the colour. Just state the colour name with no extraneous text."
            }
        ]
        }
    ]
    }'

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent" \
  -H 'Content-Type: application/json' \
  -H "X-goog-api-key:$GEMINI_API_KEY" \
  -X POST \
    -d '{
    "contents": [
        {
        "parts": [
            {
              "text": "Given an RGB hex value of #FFA500, tell me the corresponding name of the colour. Just state the colour name with no extraneous text."
            }
        ]
        }
    ]
    }'

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent" \
  -H 'Content-Type: application/json' \
  -H "X-goog-api-key:$GEMINI_API_KEY" \
  -X POST \
    -d '{
    "contents": [
        {
        "parts": [
            {
              "text": "Given an RGB hex value of #FFFF00, tell me the corresponding name of the colour. Just state the colour name with no extraneous text."
            }
        ]
        }
    ]
    }'

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent" \
  -H 'Content-Type: application/json' \
  -H "X-goog-api-key:$GEMINI_API_KEY" \
  -X POST \
    -d '{
    "contents": [
        {
        "parts": [
            {
              "text": "Given an RGB hex value of #00FF00, tell me the corresponding name of the colour. Just state the colour name with no extraneous text."
            }
        ]
        }
    ]
    }'

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent" \
  -H 'Content-Type: application/json' \
  -H "X-goog-api-key:$GEMINI_API_KEY" \
  -X POST \
    -d '{
    "contents": [
        {
        "parts": [
            {
              "text": "Given an RGB hex value of #0000FF, tell me the corresponding name of the colour. Just state the colour name with no extraneous text."
            }
        ]
        }
    ]
    }'

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent" \
  -H 'Content-Type: application/json' \
  -H "X-goog-api-key:$GEMINI_API_KEY" \
  -X POST \
    -d '{
    "contents": [
        {
        "parts": [
            {
              "text": "Given an RGB hex value of #8F00FF, tell me the corresponding name of the colour. Just state the colour name with no extraneous text."
            }
        ]
        }
    ]
    }'

