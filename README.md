# multi-region-inference-serving-01
Playing around with serving an LLM app across multiple region using GKE

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

### download mistral 7b

```
mkdir mistral-7b
wget -O mistral-7b/mistral-7b-v0.1.Q5_K_M.gguf https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/resolve/main/mistral-7b-v0.1.Q5_K_M.gguf
```

