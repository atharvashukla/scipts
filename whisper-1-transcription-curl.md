Whisper 1 Transcription with curl:

```sh
curl -X POST "https://api.openai.com/v1/audio/transcriptions" \
  -H "Authorization: Bearer API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@input.m4a" \
  -F "model=whisper-1" \
  -F "response_format=vtt"
```
