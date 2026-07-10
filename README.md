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
curl -L https://github.com/ollama/ollama/releases/download/v0.21.0/ollama-linux-amd64.tar.zst | tar -I zstd -xvf - -C ~/opt/
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

##### Update existing Ollama version
Select the lastest [pre-built binary](https://github.com/ollama/ollama/releases). Afterwards select the version that matches your system architecture. If you are not sure type: `uname -m` into your terminal.
```
curl -L https://github.com/ollama/ollama/releases/download/v0.21.0/ollama-linux-amd64.tar.zst | tar -I zstd -xvf - -C ~/opt/
mv ~/opt/bin/ollama ~/opt/; rm -r ~/opt/bin/
```
Troubleshooting:
```
ollama --version
```
ollama version is 0.12.5
Warning: client version is 0.21.0
I dont know what to do about that but all new features of ollama are working seamlessly, also latest models are available.

## Select and run a desired model locally
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

## Only serve LLM in a docker container
```
docker run -d --gpus=all -v /scratch/global_1/ollama_models/:/root/.ollama/models -p 11434:11434 --name ollama ollama/ollama
docker exec -it ollama ollama run qwen3.5
```

## Integrations
### Programmatic use via Python
This repository also contains examples for accessing a local LLM (Ollama) and integrating external tools (such as the MassBank3 API) from Python. The following files demonstrate these capabilities:

- **query.py**: This will print available LLM models, run a sample LLM query, and demonstrate how to fetch compound data from MassBank (tool server integration).
- **agents.py**: Provides a simple agent class that interacts with the LLM, demonstrating how to define agent roles and goals for agentic workflows.
- **tools.py**: Contains a universal Python tool for accessing the MassBank3 API, with examples for searching compounds and retrieving chemical data.

### GitHub Copilot CLI
Visual Studio Code supports running agent sessions in the background by using GitHub Copilot CLI. You can start, monitor, and manage your Copilot CLI sessions from the unified Chat view in VS Code, while the agents run autonomously on your local machine while you continue other work in the editor. Run multiple Copilot CLI sessions in parallel to tackle independent tasks simultaneously. More info [here](https://code.visualstudio.com/docs/agents/agent-types/copilot-cli)

```
docker build -t copilot -f Dockerfile-copilotCLI .
docker run --name copilot-playground-localLLM --rm -it -e COPILOT_PROVIDER_API_KEY=$OPENWEBUI_SECRET_KEY -v ./:/work copilot
```

Troubleshooting:
- replace `-v ./:` either with all your code repositories or start a container for each repo you are using it for to limit its access to other repositories.
- make sure to have the latest VScode version (or to avoid version conflicts between npm install -g @github/copilot and VScode)
- All additional specifications or requirements are listed in the corresponding Dockerfile
- make sure the SSL Certificate is once in the folder you build the image from
- make sure the SSL Certificate has the same name for `COPY` and `ENV` in the corresponding Dockerfile
- `$OPENWEBUI_SECRET_KEY` environment variable needs to be set system wide of course

Code and idea from @flange-ipb
https://github.com/ipb-halle/playground_flange/tree/main/copilot_cli

### Claude Code
Install claude code from the official website (for me i used `curl -fsSL https://claude.ai/install.sh | bash`). i used Version: 2.1.114 (default install location is: Location: ~/.local/bin/claude)
Navigate to your project where you like try Claude Code on
```
# cd your_repo
OLLAMA_CONTEXT_LENGTH=8192 ollama launch claude --model qwen3.5
```
`OLLAMA_CONTEXT_LENGTH=8192` increases the context length by 2x from 4096 (default).

For better directory structure and visual inspection of changes it is recommended to run Claude from within an IDE. VScode example.
- Get Claude Code extension, try to prompt something
- check `.vscode/settings.json` if your model is served there
- check `.vscode/Modelfile` if it contains your desired LLM
- overwrite default model claude-sonnet by local model `ollama create claude-sonnet-4-6 -f .vscode/Modelfile`
- Claude Code extension, try to prompt something
Full details and instructions adapted from this [article](https://medium.com/@mouatez.chaita/how-to-run-claude-code-vs-code-extension-locally-with-ollama-)

### n8n workflows
```
docker run -it --rm \
  -p 5678:5678 \
  -e NODE_EXTRA_CA_CERTS=/ipb-ca-bis2026.pem \
  -e N8N_SECURE_COOKIE=false \
  -v /etc/ssl/servercert/ipb_ca.bis2026.pem:/ipb-ca-bis2026.pem:ro \
  docker.n8n.io/n8nio/n8n
```