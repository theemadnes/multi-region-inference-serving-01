# multi-region-inference-serving-01
Playing around with serving an LLM app across multiple region using GKE

### setting up GCE instance

helpful links:
- https://learn.canceridc.dev/cookbook/virtual-machines/using-vs-code-with-gcp-vms


```
export PROJECT=e2m-private-test-01
export IMAGE_FAMILY=tf-ent-latest-gpu
export ZONE=us-central1-a
export INSTANCE_NAME=llm-test-01
export NETWORK=default

gcloud compute firewall-rules create --project=$PROJECT --network=$NETWORK default-allow-ssh --allow=tcp:22

gcloud compute instances create $INSTANCE_NAME \
  --project=$PROJECT \
  --zone=$ZONE \
  --machine-type=g2-standard-8 \
  --boot-disk-size=200GB \
  --image-family=$IMAGE_FAMILY \
  --image-project=deeplearning-platform-release \
  --maintenance-policy=TERMINATE \
  --accelerator="type=nvidia-l4,count=1" \
  --metadata="install-nvidia-driver=True"

# turn on remote SSH
gcloud --project $PROJECT compute config-ss
```

### setting up Cloud Workstation

```
# using workstation with n1-standard-8 & T4 GPU
# install linux homebrew 

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

test -d ~/.linuxbrew && eval "$(~/.linuxbrew/bin/brew shellenv)"
test -d /home/linuxbrew/.linuxbrew && eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
echo "eval \"\$($(brew --prefix)/bin/brew shellenv)\"" >> ~/.bashrc


# set up github
ssh-keygen -t ed25519 -C "your_email@example.com"
cat ~/.ssh/id_ed25519.pub

# test
```

### install ollama and test mistral

```
brew install ollama
ollama serve
ollama run mistral
```

### setting up vllm to test

```
cd serving
python3 -m venv .
source bin/activate
pip install -r requirements.txt
#git config --global credential.helper store
#huggingface-cli login

python -u -m vllm.entrypoints.openai.api_server \
       --tensor-parallel-size 1 \
       --gpu-memory-utilization 0.9 \
       --max-model-len 15000 \
       --host 0.0.0.0 \
       --model mistralai/Mistral-7B-Instruct-v0.2

python -u -m vllm.entrypoints.openai.api_server \
       --tensor-parallel-size 2 \
       --host 0.0.0.0 \
       --dtype half \
       --model mistralai/Mistral-7B-Instruct-v0.2

python -u -m vllm.entrypoints.openai.api_server \
       --host 0.0.0.0 \
       --dtype half \
       --max-num-batched-tokens 32768 \
       --max-num-seqs 2048 \
       --model mistralai/Mistral-7B-Instruct-v0.2

python -u -m vllm.entrypoints.openai.api_server \
       --host 0.0.0.0 \
       --dtype half \
       --tensor-parallel-size 2 \
       --model mistralai/Mistral-7B-Instruct-v0.2

python -u -m vllm.entrypoints.openai.api_server \
       --host 0.0.0.0 \
       --dtype half \
       --tensor-parallel-size 2 \
       --gpu-memory-utilization 1.0 \
       --model meta-llama/Llama-2-7b-chat-hf

python -u -m vllm.entrypoints.openai.api_server \
       --host 0.0.0.0 \
       --dtype half \
       --model mistralai/Mistral-7B-v0.1
```

### test

```
curl http://localhost:8000/v1/models -s | jq

curl http://localhost:8000/v1/completions -s \
       -H "Content-Type: application/json" \
       -d '{
              "model": "mistralai/Mistral-7B-Instruct-v0.2",
              "prompt": "San Francisco is a",
              "max_tokens": 100,
              "temperature": 0
       }' | jq
```