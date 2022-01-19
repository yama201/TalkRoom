# chat/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    # 接続時処理
    def connect(self):
        self.accept()

    # 切断時処理
    def disconnect(self, close_code):
        pass

    # メッセージ受信時処理
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))