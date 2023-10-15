import os
import base64

import dill
from aiohttp import web

from llm import text_completion

HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', 5000))
MODEL_PATH = os.getenv('MODEL_PATH', 'mistral-7b-v0.1.Q5_K_M.gguf')

routes = web.RouteTableDef()

@routes.post('/api/text-completion')
async def post_api_text_completion(request):
    req = await request.json()
    model_path = req.get('model_path', MODEL_PATH)
    prompt = req['prompt']
    suffix = dill.loads(base64.b64decode(req['suffix'])) if 'suffix' in req else None
    n_ctx = req['n_ctx']
    max_tokens = req['max_tokens']
    temperature = req['temperature']

    # execute llm text_completion
    text = text_completion(model_path, prompt, suffix, n_ctx, max_tokens, temperature)

    res = {'text': text}
    return web.json_response(res)

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app, host=HOST, port=PORT)