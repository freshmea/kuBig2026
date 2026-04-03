// cc -o mqttPub mqttPub.c -lpaho-mqtt3c

#include "MQTTClient.h"
#include <stdio.h>
#include <string.h>

#define DEFAULT_ADDRESS "tcp://127.0.0.1:1883"
#define DEFAULT_CLIENT_ID "kubig-student"
#define DEFAULT_TOPIC "school/test"
#define DEFAULT_MESSAGE "hello mqtt"

int main(int argc, char *argv[])
{
    MQTTClient client;
    MQTTClient_connectOptions conn_opts = MQTTClient_connectOptions_initializer;
    MQTTClient_message pubmsg = MQTTClient_message_initializer;
    const char *address = argc > 1 ? argv[1] : DEFAULT_ADDRESS;
    const char *clientId = argc > 2 ? argv[2] : DEFAULT_CLIENT_ID;
    const char *topic = argc > 3 ? argv[3] : DEFAULT_TOPIC;
    const char *message = argc > 4 ? argv[4] : DEFAULT_MESSAGE;

    MQTTClient_create(&client, address, clientId, MQTTCLIENT_PERSISTENCE_NONE, NULL);
    if (MQTTClient_connect(client, &conn_opts) != MQTTCLIENT_SUCCESS)
    {
        printf("접속 실패: broker=%s client_id=%s\n", address, clientId);
        return -1;
    }

    pubmsg.payload = (void *)message;
    pubmsg.payloadlen = (int)strlen(pubmsg.payload);
    pubmsg.qos = 1;
    MQTTClient_publishMessage(client, topic, &pubmsg, NULL);

    printf("메시지 전송 완료: topic=%s message=%s\n", topic, message);
    MQTTClient_disconnect(client, 10000);
    MQTTClient_destroy(&client);
    return 0;
}
