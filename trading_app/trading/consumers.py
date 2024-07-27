import json
from channels.generic.websocket import AsyncWebsocketConsumer


class TradingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "trading",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "trading",
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data['type'] == 'move_order':
            price = data['price']
            await self.channel_layer.group_send(
                "trading",
                {
                    "type": "order_message",
                    "message": {
                        'type': 'move_order',
                        'price': price
                    }
                }
            )

    async def order_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps(message))