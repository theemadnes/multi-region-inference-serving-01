# setup for using Gemma demo 

https://cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-gpu-vllm

### steps 

```
export HF_TOKEN=hf_xxx # make sure to request access to Gemma model on HF https://huggingface.co/google/gemma-2b-it

kubectl create secret generic hf-secret \
--from-literal=hf_api_token=$HF_TOKEN \
--dry-run=client -o yaml | kubectl apply -f -

kubectl apply -f vllm-2b-it.yaml

kubectl port-forward service/llm-service 8000:8000

USER_PROMPT="Tell me about Manchester United"

curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
    "prompt": "${USER_PROMPT}",
    "temperature": 0.90,
    "top_p": 1.0,
    "max_tokens": 128
}
EOF

USER_PROMPT="Tell me about Manchester United"

curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
    "prompt": "${USER_PROMPT}",
    "temperature": 0.90,
    "top_p": 1.0,
    "max_tokens": 1024
}
EOF

# run in a loop
while true; do 
curl -X POST http://localhost:8000/generate \
    -H "Content-Type: application/json" \
    -d @- <<EOF
{
    "prompt": "${USER_PROMPT}",
    "temperature": 0.90,
    "top_p": 1.0,
    "max_tokens": 1024
}
EOF
done
```