from llama_cpp import Llama

model_path = "/Users/alexmattson/Documents/Projects/multi-region-inference-serving-01/models/llama-2-7b-chat/ggml-model-f16_q4_0.bin"
model = Llama(model_path = model_path,
              n_ctx = 2048,            # context window size
              n_gpu_layers = 1,        # enable GPU
              use_mlock = True)        # enable memory lock so not swap


prompt = """
[INST]<<SYS>>
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.

What is the best way to learn programming?
[/INST]
"""

output = model(prompt = prompt, max_tokens = 120, temperature = 0.2)
print(output)