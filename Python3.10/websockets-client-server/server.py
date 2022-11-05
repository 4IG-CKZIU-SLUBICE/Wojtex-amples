import asyncio
import websockets
import json
from random import random
from copy import deepcopy

from Client import Client


async def main(websocket):
    clients = []
    json_data_for_new_client = {'Connected': True, 'ID': None}
    
    async for data in websocket:
        json_data = json.loads(data) 
        
        if json_data['type'] == 'connect':
            clients.append(Client(random(), json_data['name']))
            
            last_index = len(clients) - 1

            print('New client connected.')
            print(clients[last_index].desc())
            
            new_client_json_data = deepcopy(json_data_for_new_client)
            new_client_json_data['ID'] = clients[last_index].client_id
            await websocket.send(json.dumps(new_client_json_data))
            
            continue
        

        if json_data['type'] == 'desc':
            print('Client requested for Description...')
            
            for client in clients:
                if client.client_id == json_data['ID']:
                    desc_json_data = {'type': 'desc', 'desc': str(client.desc())}
                   
                    print(f'Send description for client ID: {client.client_id}...')

                    await websocket.send(json.dumps(desc_json_data))
                    break
            
                print(client.client_id, json_data['ID'])

            continue


        if json_data['type'] == 'disconnect':
            print('type == disconnect')
            for i, client in enumerate(clients):
                print(i)
                if client.client_id == json_data['ID']:
                    print('Disconnecting client...')
                    print(client.desc())

                    del clients[i]
                    break
            
            continue

async def InitServer():
    async with websockets.serve(main, 'localhost', 8001):
        await asyncio.Future()


if __name__ == '__main__':
    clients = []
    asyncio.run(InitServer())
