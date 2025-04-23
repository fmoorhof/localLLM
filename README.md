# localLLM
Locally host LLMs and serve them via OpenWebUI.

## Install with Docker
```
docker-compose up
# docker-compose down  # shutdown the service
```
Access the chat interface at: http://localhost:3000.
Additional models can be simply selected via the WebUI or from the terminal: `docker exec -it ollama ollama pull deepseek-r1:1.5b`. Check available models [here](https://ollama.com/search).
The Ollama API can be accessed at http://localhost:11434/ and used for diverse other applications like VScode e.g. (see [faq.md](faq.md) for more use cases and advanced configurations).

## Manual install (not recommended)
Might have issues actually using the GPUs despite detected. Ollama install without user privileges is a pain. Better use docker and dont waste your time.

### Prerequisites - Install Ollama and OpenWebUI
If root access is available, install Ollama with the below command.
Choose a desired way to install [OpenWebUI](https://github.com/open-webui/open-webui).
```
curl -fsSL https://ollama.com/install.sh | sh
```

#### Personal setup example at IPB (for non root users)
Get Ollama for users (without root privileges): https://github.com/ollama/ollama/issues/2111

Select the lastest [pre-built binary](https://github.com/ollama/ollama/releases). Afterwards select the version that matches your system architecture. If you are not sure type: `uname -m` into your terminal. x86_64 means amd64 which I will use.
```
curl -L https://github.com/ollama/ollama/releases/download/v0.6.6-rc2/ollama-linux-amd64.tgz | tar -xzf - -C ~/opt/
mv ~/opt/bin/ollama ~/opt/; rm -r ~/opt/bin/
echo 'export PATH=$PATH:~/opt/' >> ~/.bashrc
echo 'export OLLAMA_MODELS=~/ollama-local' >> ~/.bashrc
source ~/.bashrc
```
```
conda create --name open-webui python=3.11
conda activate open-webui
pip install open-webui  # requires Python3.11
```

## Select and run a desired model
Select a [desired model](https://ollama.com/search). For demonstration purposes we are using `DeepSeek-R1-Distill-Qwen-32B` which is identified simply by: `deepseek-r1:32b`.
```
ollama serve
ollama run deepseek-r1:32b
```

## Serve the model with OpenWebUI
```
open-webui serve
```
In your browser you should now be able to see the interface at `http://localhost:8080`