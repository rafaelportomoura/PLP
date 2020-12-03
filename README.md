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
      //NO VENV
      pip install wheel
      ```
    * Linux e Mac
      ```bash
      python3 -m venv venv
      //NO VENV
      venv/bin/activate 
      pip install wheel
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
  * <b><a name="aula01">Videoaula de introdução ao Python: GCC198</a></b>

    * [Conditionals](#aula01Conditionals)
    * [Interations](#aula01Interations)
    * [Exceptions](#aula01Exceptions)
    * [Files](#aula01Files)
    * [CommandArguments](#aula01CommandArguments)
    * [Extras](#aula01Extras)
    #

    * <b><a name="aula01Conditionals">Conditionals</a></b>

      *  [Vídeo-aula de introdução ao Python : GCC198](https://www.youtube.com/watch?v=zyCu32zRPFw&list=PLhBit65YoreOHcv9evI-uEXJUUeR3wOEM&index=3&ab_channel=ERICKGALANIMAZIERO)

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

    * <b><a name="aula01Interations">Interations</a></b>

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
    
    * <b><a names="aula01Exceptions">Exceptions</a></b>

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

    * <b><a name="aula01Files">Files</a></b>
      <p>dataset.csv : 
        <p>7,8,9<p>3,4,5<p>2,4,1<p>90,89,20<p>8,4,12

      ```Python
      xs = []
      ys = []
      zs = []
      with open('dataset.csv','r') as file:
        lines = file.readlines()
        for line in lines:
          x, y, z = line.split(',')
          xs.append(x)
          ys.append(y)
          zs.append(z)
      
      print(xs)
      print(ys)
      print(zs)
      ```
      >['7', '3', '2', '90', '8']<p>['8', '4', '4', '89', '4']<p>['9\n', '5\n', '1\n', '20\n', '12']
      
      ```Python
      xs = []
      ys = []
      zs = []
      with open('dataset.csv','r') as file:
        lines = file.readlines()
        for line in lines:
          x, y, z = line.split(',')
          xs.append(x)
          ys.append(y)
          zs.append(z.strip())
      
      print(xs)
      print(ys)
      print(zs)
      ```
      >['7', '3', '2', '90', '8']<p>['8', '4', '4', '89', '4']<p>['9', '5', '1', '20', '12']

    * <b><a name="aula01CommandArguments">Command Arguments</a></b>
      * python_example1.py 
        
        ```Python
        import sys

        caminho_do_arquivo = sys.argv[1] #o sys.argv[0] é o nome do próprio arquivo python

        xs = []
        ys = []
        zs = []

        with open(caminho_do_arquivo,  'r') as file:
          lines = file.readlines()
          for line in lines:
            x, y, z = line.split(', ')
            xs.append(x)
            ys.append(y)
            zs.append(z.strip())

        print(xs)
        print(ys)
        print(zs)
        ```
      * A chamada é feita por terminal de comando<p>python3 python_example1.py dataset.csv
        >['7', '3', '2', '90', '8']<p>['8', '4', '4', '89', '4']<p>['9', '5', '1', '20', '12']

    * <b><a name="aula01Extras">Extras</a></b>
    
      ```Python
      numeros = [1, 10, 100, 1000, 2, 20, 200]
      print(sum(numeros))
      print(max(numeros))
      print(min(numeros))
      ```
      >1333<p>1000<p>1

      
      ```Python
      numeros = [1, 10, 100, 1000, 2, 20, 200]
      print("Média da lista", sum(numeros)/len(numeros))
      ```
      >190.42857142857142



  * <b><a name="aula02">Paradigma Imperativo : Variáveis e Tipos de Dados</a></b>
  
      *  [Vídeo-aula Paradigma Imperativo : Variáveis e Tipos de Dados](https://www.youtube.com/watch?v=ixgq1igka04&list=PLhBit65YoreOHcv9evI-uEXJUUeR3wOEM&index=4&ab_channel=ERICKGALANIMAZIERO)
      * [Slide Variáveis e tipos de dados](https://drive.google.com/file/d/16eCZZyFb7y4OKCbyoKi-tf8mOBlD2284/view?usp=sharing)

      ```Python
      my_string = 'Hello, World!'
      my_flt = 45.06
      my_bool = 5 > 9
      my_list = ['item1','item2']
      my_tuple = ('item1','item2')
      my_dict = {'letter':'g','number':7}
      ```

  * <b><a name="aula03">Paradigma Imperativo : Avaliação de Expressões e Controle de Fluxo</a></b>
  
      *  [Paradigma Imperativo : Avaliação de Expressões e Controle de Fluxo](https://www.youtube.com/watch?v=SXqOHgvQBfo&list=PLhBit65YoreOHcv9evI-uEXJUUeR3wOEM&index=5&ab_channel=ERICKGALANIMAZIERO)
      
      * [Avaliações de expressões e controle de fluxo](https://drive.google.com/file/d/1_ohN2hIh6nSqq-Pyl2W7fvFvajyrUAhW/view?usp=sharing)

  * <b><a name="aula04">Paradigma Imperativo : Subprogramas</a></b>

      *  [Paradigma Imperativo : Subprogramas](https://www.youtube.com/watch?v=IBVEJx5Hfzo&list=PLhBit65YoreOHcv9evI-uEXJUUeR3wOEM&index=6&ab_channel=ERICKGALANIMAZIERO)
      
      * [Subprogramas](https://drive.google.com/file/d/1SuvBqQdD7KhYc7GiGW8z6nM0ef3hLZcL/view?usp=sharing)

      ```Python
      def subprograma(a,b,c):
        print(a + b + c)
      ```
      * Recursao
        
      ```Python
      def fatorial(n):
        if (n <= 1):
          return 1
        else: 
          return (n * fatorial(n-1))
      ```

<!--te-->
