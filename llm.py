__all__ = ['text_completion']

from llama_cpp import Llama

def text_completion(model_path: str,
                    prompt: str,
                    suffix: str | None=None,
                    n_ctx: int=4096,
                    max_tokens: int=512,
                    temperature: float=0.1) -> str:
    print('DEBUG text_completion: [begin]', model_path, prompt, suffix, n_ctx, max_tokens, temperature, '[end]')
    llm = Llama(model_path=model_path, n_ctx=n_ctx, verbose=False)
    output = llm(prompt, suffix=suffix, max_tokens=max_tokens, temperature=temperature, echo=False)
    return output['choices'][0]['text']
