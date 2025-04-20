# Frequently asked Questions and additional use cases

## TTS: Text-To-Speech (read alout answers including reasoning)
You can get the answers read alout. In the settings->Audio you can change the languages and the playback speed. But dont expect too much. Speakers are system speakers from your browser. Microsofts edge browser supports many different and less robotic voices, if you are interested in the read alout content give edge browser a try. I like the voice `Microsoft AndrewMultilingual ONine United States` with a quicker playback speed also sound even more natural.

## LLM integration into IDEs like VScode
Open VScode, install the extension 'Continue'. Open the extension (on the left side). It asks you to sign in or use locally only. On the bottom you can click 'configure manually'. This opens the 'config.json' where you can add the models you want to use. You can add these lines:
```
# name: Local Assistant
# version: 1.0.0
# schema: v1
models:
  - name: deepseek-r1:32b
    provider: ollama
    model: deepseek-r1:32b
    roles:
      - chat
    apiBase: http://ocean:11434 
```
Alternatively, you can also click and navigate through the menu to add models yourself. It is important to point to the local Ollama API at http://ocean:11434 (which stays the same for all the local models).
deepseek-r1:32b is now enabled for chat (roles: chat).

### Autocompletion
Deepseek-r1:32b is very slow in thinking and not really practical for autocompletion. There exists dedicated models for this task. I tried starcoder2:15b in 2025 and the suggestions are fast but not really related to the surrounding content. No comparison to Github Copilot, so i disabled this feature again. Feel free to report your experiences. 

```
models:
  - name: inline suggestions with starcoder2:15b
    provider: ollama
    model: starcoder2:15b
    roles:
      - autocomplete
    apiBase: http://ocean:11434 
```

## Models for image generation
Image generation models are quite proprietary and require different interfaces not (always) available in the webUI. I didnt find a good and compatible. Feel free to test some yourself and please report the usage.

## Directly propt Ollama (not recommended)
You can use the ollama API directly, too but the output is rather non human readable. However, integrating this API endpoint in Vscode might be handy (see above)

Example query from the terminal to the API endpoint of ollama
```
curl http://ocean:11434/api/generate -d '{ "model": "deepseek-r1:32b", "prompt": "What is water made of?" }'
```
