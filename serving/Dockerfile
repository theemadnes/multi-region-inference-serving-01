FROM python:3.12.1-slim

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

RUN addgroup --system appuser && adduser --system appuser --ingroup appuser
USER appuser

ENTRYPOINT [ "python" ]

CMD [ "-u -m vllm.entrypoints.openai.api_server --tensor-parallel-size 1 --gpu-memory-utilization 0.9 --max-model-len 15000 --host 0.0.0.0 --model mistralai/Mistral-7B-Instruct-v0.2" ]