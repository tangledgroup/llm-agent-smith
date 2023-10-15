import os
import base64
import asyncio

import dill
import aiohttp

from smith import smith_prompt, smith_suffix, smith_max_tokens

HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', 5000))

async def main():
    req = {
        'prompt': smith_prompt,
        'suffix': base64.b64encode(dill.dumps(smith_suffix)).decode(),
        'n_ctx': 4096,
        'max_tokens': smith_max_tokens,
        'temperature': 0.1,
    }
    print(req)

    async with aiohttp.ClientSession() as session:
        async with session.post(f'http://{HOST}:{PORT}/api/text-completion', json=req) as resp:
            res = await resp.json()
            print(res)

if __name__ == '__main__':
    asyncio.run(main())
