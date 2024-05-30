from requests import HTTPError, post, get, codes
from datetime import datetime
from time import sleep

'''
Problem 3: Transaction Broadcasting and Monitoring Client
Description:
Your task is to develop a module/class in a programming language of your choice that interacts with an HTTP
server. This client module will enable the broadcasting of a transaction and subsequently monitor its status
until finalization.
Requirements:
Create a client module that is designed to be integrated into another application, with the following capabilities:
1. Broadcast Transaction: Construct a JSON payload and send a POST request to
`https://mock-node-wgqbnxruha-as.a.run.app/broadcast`. The payload structure is as follows:
{
"symbol": "string", // Transaction symbol, e.g., BTC
"price": uint64, // Symbol price, e.g., 100000
"timestamp": uint64 // Timestamp of price retrieval
}
Example payload and server response:
// Payload
{
"symbol": "ETH",
"price": 4500,
"timestamp": 1678912345
}
// Server response
{
"tx_hash": "e97ae379d666eed7576bf285c451baf9f0edba93ce718bf15b06c8a85d07b8d1"
}
2. Transaction Status Monitoring: Utilize the transaction hash obtained from the response to periodically
issue GET requests to `https://mock-node-wgqbnxruha-as.a.run.app/check/<tx_hash>`. The response will be
plaintext indicating the transaction status, which can be one of the following:
- `CONFIRMED`: Transaction has been processed and confirmed
- `FAILED`: Transaction failed to process
- `PENDING`: Transaction is awaiting processing
- `DNE`: Transaction does not exist
An example response is shown below:
{
"tx_status": "CONFIRMED"
}
'''

URL = 'https://mock-node-wgqbnxruha-as.a.run.app'
HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
MAX_PENDING = 30
TIME_SLEEP = 1

def fetch_transaction_status(tx_id: str) -> tuple:
    res = get(url=f'{URL}/check/{tx_id}', headers=HEADERS)
    if res.status_code != codes["ok"]:
        return "Some error happen in server", res.status_code
    else:
        tx_status = res.json().get("tx_status")
        return tx_status, res.status_code

def main(coin: str, price: int) -> str:
    body = {
        "symbol": coin,
        "price": price,
        "timestamp": int(datetime.now().timestamp())
    }
    try:
        res = post(url=f'{URL}/broadcast', json=body, headers=HEADERS)
    except HTTPError as e:
        return f'Request create transaction error: {e=}'
    else:
        message = res.json()
        transaction_id = message.get("tx_hash")
        round = 0
        message, status = fetch_transaction_status(transaction_id)
        while round < MAX_PENDING and message == "PENDING" and status == codes["ok"]:
            message, status = fetch_transaction_status(transaction_id)
            round += 1
            sleep(TIME_SLEEP)
        if message == "PENDING":
            return f"{transaction_id} status Waiting Timeout"
        return f"{transaction_id} status {message}"


if __name__ == '__main__':
    print(f'Input type coin: ')
    coin = input()
    print(f'Input price: ')
    price = int(input())
    print(f'Result create transaction: {main(coin, price)}')