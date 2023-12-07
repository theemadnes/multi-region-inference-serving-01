# multi-region-inference-serving-01
Playing around with serving an LLM app across multiple region using GKE

### setting up Cloud Workstations

```
gcloud beta workstations configs update config-lpuvfdv9 \
  --cluster=cluster-lpqhjitt --region=us-central1 --machine-type=n1-standard-8 \
  --accelerator-type=nvidia-tesla-p4 --accelerator-count=1


# install linux homebrew 

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

test -d ~/.linuxbrew && eval "$(~/.linuxbrew/bin/brew shellenv)"
test -d /home/linuxbrew/.linuxbrew && eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
echo "eval \"\$($(brew --prefix)/bin/brew shellenv)\"" >> ~/.bashrc


# set up github
ssh-keygen -t ed25519 -C "your_email@example.com"
cat ~/.ssh/id_ed25519.pub
```

