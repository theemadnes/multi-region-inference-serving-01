# multi-region-inference-serving-01
Playing around with serving an LLM app across multiple region using GKE

### setting up Cloud Workstations

```
gcloud beta workstations configs update config-lpuvfdv9 \
  --cluster=cluster-lpqhjitt --region=us-central1 --machine-type=n1-standard-8 \
  --accelerator-type=nvidia-tesla-p4 --accelerator-count=1
```
