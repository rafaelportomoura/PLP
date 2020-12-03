<h1 align="center">PLP</h1>
Repositório para salvar códigos de PLP


## 📝 REOs

- [REO 2 - Python](#python)


## <h1><a name = "python">🐍 Reo 2 - Python</a></h1> 
Configurações 
  * [Ambiente virtual](#ambienteVirtualPython)
  * [Extensões para VsCode](#extensoesParaVsCodePython)
  * [settings.json](#settings.jsonPython)


  * # <h4> <a name = "ambienteVirtualPython">Ambiente Virtual</a></h4>
    * Windows
      ```bash
      py -3 -m venv venv
      ```
    * Linux e Mac
      ```bash
      python3 -m venv venv
      venv/bin/activate 
      deactivate
      ```
  * # <h4> <a name = "extensoesParaVsCodePython">Extensões para VSCode: </a></h4>
    - Code Runner
    - Python ( Microsoft )
    - Python Test Explorer  for Visual Studio Code
    - Python Preview
    - Python Docstring Generator
 
  * #  <h4><a name="settings.jsonPython"/>settings.json<a/>
    Na pasta do projeto, crie uma pasta chamada .vscode e dentro dela um arquivo chamado settings.json
    * Windows 
      ```
      {
        "python.pythonPath": "venv\\Scripts\\python.exe",
        "code-runner.executorMap": {
          "python": "venv\\Scripts\\python.exe",
        },
        "code-runner.ignoreSelection": true,
        "code-runner.runInTerminal": true,
        "python.linting.mypyEnabled": true,
        "python.linting.flake8Enabled": true,
        "python.testing;unittestEnabled": true,
        "[python]": {
          "editor.formatOnSave": true
        }
      }
      ```
    * Linux
      ```
      {
        "python.pythonPath": "venv/bin/python",
        "code-runner.executorMap": {
          "python": "venv/bin/python",
        },
        "code-runner.ignoreSelection": true,
        "code-runner.runInTerminal": true,
        "python.linting.mypyEnabled": true,
        "python.linting.flake8Enabled": true,
        "python.testing;unittestEnabled": true,
        "[python]": {
          "editor.formatOnSave": true
        }
      }
      ```
    #     
<p color="#FFFFFF">Aulas</p>

