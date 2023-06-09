# Telegram Mailman
### Proxy-service to hide original HTTP responses from Telegram API

---

Environment variables:\
`BOT_API_TOKEN` - Telegram Bot API Key 

---

### Important clarification: message sending is only performed on behalf of the bot, in which the message recipient is authenticated.

API has only one HTTP method:

POST `/send_message`

```json
{
  "chat_id": "string",
  "message": "string"
}
```

If the message was successfully delivered, the server will return the status code `200`\
In any other case `500` and will provide information about the problem in the server logs