import os
import json
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from datetime import datetime
from decouple import config

TOPIC_NAME = config('TOPIC_NAME')
SUB_NAME = config('SUB_NAME')
CONNECTION_STRING = config('CONNECTION_STRING')

class ServiceBusManager:
    def __init__(self):
        """
        Inicializa as configurações da conexão com o Service Bus.
        """

        self.connection_string = CONNECTION_STRING
        self.topic_name = TOPIC_NAME
        self.subscription_name = SUB_NAME

        if not self.connection_string or not self.topic_name or not self.subscription_name:
            raise ValueError("CONNECTION_STRING, TOPIC_NAME e SUB_NAME devem estar definidas no .env")

    def send_message(self, body_content):
        """
        Envia uma única mensagem ao tópico especificado.
        body_content: Conteúdo deve estar em formato de dicionário.
        """

        with ServiceBusClient.from_connection_string(self.connection_string) as client:
            with client.get_topic_sender(self.topic_name) as sender:
                message = ServiceBusMessage(json.dumps(body_content), content_type="application/json")
                
                if body_content:
                    body_content['datetime'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                    message = ServiceBusMessage(json.dumps(body_content), content_type="application/json")
                    sender.send_messages(message)
                    print(f"[MENSAGEM ENVIADA] para o tópico: {self.topic_name}")
                else:
                    raise ValueError("Mensagem vazia!")

    def send_array_of_messages(self, messages_array):
        """
        Envia várias mensagens ao tópico especificado.
        messages_array: Conteúdo deve estar em formato de lista.
        """

        with ServiceBusClient.from_connection_string(self.connection_string) as client:
            with client.get_topic_sender(self.topic_name) as sender:
                messages = []
                for msg in messages_array:
                    msg['datetime'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                    messages.append(ServiceBusMessage(json.dumps(msg), content_type="application/json"))

                sender.send_messages(messages)
                print(f"[MENSAGENS ENVIADAS] para o tópico: {self.topic_name}")

def main():
    sb_manager = ServiceBusManager()

    # Exemplo de como podemos enviar uma mensagem ao serviceBus:
    #sb_manager.send_message(
    #    {"id": 1, "name": "Gabriel"}
    #)

    # Exemplo de como podemos enviar várias mensagens ao serviceBus:
    sb_manager.send_array_of_messages([
        {"id": 1},
        {"id": 7},
        {"id": 8},
    ])


if __name__ == "__main__":
    main()
