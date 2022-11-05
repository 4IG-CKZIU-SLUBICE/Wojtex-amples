import asyncio
import websockets
import json

import Client

async def main():
    async with websockets.connect('ws://localhost:8001') as connection:

        json_data_to_send = [{'type': 'connect', 'name': 'Jakiś Typ'},
                             {'type': 'desc', 'ID': None},
                             {'type': 'disconnect', 'ID': None}]

        await connection.send(json.dumps(json_data_to_send[0]))
        json_data = await connection.recv()
        json_data = json.loads(json_data)
        print(json_data)

        client_id = json_data['ID']

        json_data_to_send[1].update(ID = client_id)
        print(json_data_to_send[1])

        await connection.send(json.dumps(json_data_to_send[1]))
        json_data = await connection.recv()
        print(json.loads(json_data))
    
        print('disconnecting...')
        json_data_to_send[2].update(ID = client_id)
        await connection.send(json.dumps(json_data_to_send[2]))

asyncio.get_event_loop().run_until_complete(main())
