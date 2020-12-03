<h1 align="center">PLP</h1>
Repositório para salvar códigos de PLP


## 📝 REOs

- [REO 2 - Python](#python)


## <h1><a name = "python">🐍 Reo 2 - Python</a></h1> 
<!--ts-->
  * [Configurações](#reo2Configurações)
    * [Ambiente virtual](#ambienteVirtualPython)
    * [Extensões para VsCode](#extensoesParaVsCodePython)
    * [settings.json](#settings.jsonPython)
  * [Aulas](#reo2Aulas)
    * [Videoaula de introdução ao Python: GCC198](#aula01)
    * [Paradigma Imperativo : Variáveis e Tipos de Dados](#aula02)
    * [Paradigma Imperativo : Avaliação de Expressões e Controle de Fluxo](#aula03)
    * [Paradigma Imperativo : Subprogramas](#aula04)
<!--te-->

<a name="reo2Configurações">Configurações</a>
<!--ts-->
  * <a name = "ambienteVirtualPython">Ambiente Virtual</a>
    * Windows
      ```cmd
      py -3 -m venv venv
      ```
    * Linux e Mac
      ```bash
      python3 -m venv venv
      venv/bin/activate 
      deactivate
      ```
  * <a name = "extensoesParaVsCodePython">Extensões para VSCode: </a>
    * Code Runner
    * Python ( Microsoft )
    * Python Test Explorer  for Visual Studio Code
    * Python Preview
    * Python Docstring Generator
  * <a name="settings.jsonPython"/>settings.json<a/>
        <p>Na pasta do projeto, crie uma pasta chamada .vscode e dentro dela um arquivo chamado settings.json</p>
    * Windows 
      ```Json
      {
        "python.pythonPath": "venv\\Scripts\\python.exe",
        "code-runner.executorMap": {
          "python": "venv\\Scripts\\python.exe",
        },
        "code-runner.ignoreSelection": true,
        "code-runner.runInTerminal": true,
        "python.linting.mypyEnabled": true,
        "python.linting.flake8Enabled": true,
        "python.testing.unittestEnabled": true,
        "[python]": {
          "editor.formatOnSave": true
        }
      }
      ```
    * Linux
      ```Json
      {
        "python.pythonPath": "venv/bin/python",
        "code-runner.executorMap": {
          "python": "venv/bin/python",
        },
        "code-runner.ignoreSelection": true,
        "code-runner.runInTerminal": true,
        "python.linting.mypyEnabled": true,
        "python.linting.flake8Enabled": true,
        "python.testing.unittestEnabled": true,
        "[python]": {
          "editor.formatOnSave": true
        }
      }
      ```
<!--te-->
   
<a name="reo2Aulas">Aulas</a>
<!--ts-->
  * <a name="aula01">Videoaula de introdução ao Python: GCC198</a>
  
    * [Conditionals](#aula01Conditionals)
    * [Interations](#aula01Interations)
    * [Exceptions](#aula01Exceptions)
    * [Files](#aula01Files)
    #

    * <a name="aula01Conditionals">Conditionals</a>

      ```Python
      valor = input("Digite um valor")
      valor = int(valor)
      if ((valor % 2 ) == 0):
        print('Número par')
      else:
        print('Número ímpar')
      ```
      > <p> Digite um número 2 </p>Número par 
      
      ```Python
      valor = int(input("Digite um valor"))
      
      if valor == 0:
        print('Zero!')
      elif valor % 2  == 0:
        print('Número par')
      else:
        print('Número ímpar')
      ```
      > <p> Digite um número 0</p>Zero! 
      
      ```Python
      valor = int(input("Digite um valor"))
      
      msg = 'par' if valor % 2 == 0 else 'ímpar'
      print(msg)
      ```
      > <p>Digite um número 2</p>par

    * <a name="aula01Interations">Interations</a>

      ```Python
      for i in range(10):
        print(i)
      ```
      >0<p>1<p>2<p>3<p>4<p>5<p>6<p>7<p>8<p>9

      ```Python
      for i in range(5,10):
        print(i)
      ```
      >5<p>6<p>7<p>8<p>9
      
      ```Python
      blacklist = ["palavrão","palavrona","palavreadão"]
      for palavra in blacklist:
        print("Palavra proibida: {}".format(palavra))
      ```
      >Palavra proibida: palavrão<p>Palavra proibida: palavrona<p>Palavra proibida: pavreadão
      
      ```Python
      blacklist = ["palavrão","palavrona","palavreadão"]
      texto = input("Digite uma frase: ")
      palavras = texto.split()
      for palavra in palavras:
        if palavra.lower() in blacklist:
          print("A palavra {} é proibida!".format(palavra))
      ```
      >Digite uma frase: Oi, palavrão tal<p>A palavra palavrão é proibida!
    
    * <a names="aula01Exceptions">Exceptions</a>

      ```Python
      try:
        valor = int(input("Digite um número"))
        if valor == 0:
          print('Zero!')
        elif valor % 2 == 0:
          print('Número par')
        else:
          print('Número ímpar')
      except:
        print('Valor digitado não é um número!')
      ```
      >Digite um número a<p>Valor digitado não é um número!

    * <a name="aula01Files">Files</a> 

      ```Python
      try:
        valor = int(input("Digite um número"))
        if valor == 0:
          print('Zero!')
        elif valor % 2 == 0:
          print('Número par')
        else:
          print('Número ímpar')
      except:
        print('Valor digitado não é um número!')
      ```
      >Digite um número a<p>Valor digitado não é um número!
  * <a name="aula02">Paradigma Imperativo : Variáveis e Tipos de Dados</a>
  * <a name="aula03">Paradigma Imperativo : Avaliação de Expressões e Controle de Fluxo</a>
  * <a name="aula04">Paradigma Imperativo : Subprogramas</a>

<!--te-->
