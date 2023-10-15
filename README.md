# llm-agent-smith

Download in local directory Mistral-based models for `llama.cpp`:

1) Mistral-7B-v0.1-GGUF
https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/blob/main/mistral-7b-v0.1.Q5_K_M.gguf

2) zephyr-7B-alpha-GGUF
https://huggingface.co/TheBloke/zephyr-7B-alpha-GGUF/blob/main/zephyr-7b-alpha.Q5_K_M.gguf

```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt --force-reinstall --upgrade --no-cache-dir
```

```bash
HOST=0.0.0.0 PORT=5000 MODEL_PATH="mistral-7b-v0.1.Q5_K_M.gguf" python -B server.py
```

```bash
HOST=0.0.0.0 PORT=5001 MODEL_PATH="zephyr-7b-alpha.Q5_K_M.gguf" python -B server.py
```

```bash
python -B client.py
```

## References

* [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
* [llama-cpp-python documentation](https://llama-cpp-python.readthedocs.io)
* [llama.cpp](https://github.com/ggerganov/llama.cpp)
* [Tangled Group, Inc](https://tangledgroup.com)
* https://github.com/abetlen/llama-cpp-python/blob/f30aa2012613df1e90e29f78e181a92366494ca6/llama_cpp/llama.py#L904
* https://github.com/abetlen/llama-cpp-python/blob/f30aa2012613df1e90e29f78e181a92366494ca6/llama_cpp/llama.py#L1295