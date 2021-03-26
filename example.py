async def app(scope, receive, send):
    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello, world!',
    })
 

import uvicorn

if __name__ == "__main__":
    uvicorn.run("example:app", host="0.0.0.0", port=5000, log_level="info")
