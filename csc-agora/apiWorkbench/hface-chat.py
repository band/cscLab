from easyllm.clients import huggingface

# helper to build llama2 prompt
huggingface.prompt_builder = "llama2"

response = huggingface.ChatCompletion.create(
    model="meta-llama/Llama-2-70b-chat-hf",
    messages=[
        {"role": "system", "content": "\nYou are a helpful assistant speaking like a pirate. argh!"},
        {"role": "user", "content": "What is the sun?"},
    ],
    temperature=0.9,
    top_p=0.6,
    max_tokens=256,
)

print(response)
