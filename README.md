# localLLM
Locally host LLMs.

## Prerequisites - Install Ollama and OpenWebUI
If root access is available, install Ollama with the below command.
Choose a desired way to install [OpenWebUI](https://github.com/open-webui/open-webui).
```
curl -fsSL https://ollama.com/install.sh | sh
```

### Personal setup example at IPB (for non root users)
Get Ollama for users (without root priviledges): https://github.com/ollama/ollama/issues/2111

Select the lastest [pre-built binary](https://github.com/ollama/ollama/releases). Afterwards select the version that matches your system architecture. If you are not sure type: `uname -m` into your terminal. x86_64 means amd64 which I will use.
```
curl -L https://github.com/ollama/ollama/releases/download/v0.6.6-rc2/ollama-linux-amd64.tgz | tar -xzf - -C ~/opt/
mv ~/opt/bin/ollama ~/opt/; rm -r ~/opt/bin/
echo 'export PATH=$PATH:~/opt/' >> ~/.bashrc
echo 'export OLLAMA_MODELS=/scratch/global_1/ollama_models' >> ~/.bashrc
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