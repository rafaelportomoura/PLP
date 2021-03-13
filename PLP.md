<h1 align="center">PLP</h1>
Repositório para salvar códigos de PLP


## 📝 REOs

- [REO 2 - Paradigma Imperativo](#paradigmaimperativo)
- [REO 3 - Paradigma Orientado a Objetos](#paradigmaOrientadoAObjetos)
- [REO 4 - Paradigma Funcional](#paradigmaFuncional)


<h1><a name = "paradigmaimperativo">🐍 Reo 2 - Paradigma Imperativo</a></h1> 
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
  * [Atividade Avaliativa](#reo2AtividadeAvaliativa)
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
<a name="reo2AtividadeAvaliativa">Atividade Avaliativa</a>
<!--ts-->
  * Sobre
    * Programa pra rodar o coeficiente da correlação de Pearson
  * Rodar
  
      ```cmd
      py -3 atividade_avaliativa_Rafael_Porto_reo2 teste.txt
      ```
<!--te-->

# <a name="paradigmaOrientadoAObjetos"></a> 🐍 Reo 3 - Paradigma Orientado a Objetos

* ### Aulas
  * #### [Paradigma Orientado a Objetos : Conceitos iniciais](#reo3aula1)
  * #### [Paradigma Orientado a Objetos : Encapsulamento](#reo3aula2)
  * #### [Paradigma Orientado a Objetos : Herança e Composição](#reo3aula3)
  * #### [Paradigma Orientado a Objetos : Polimorfismo](#reo3aula4)

* ### [Python](#reo3Python)

* ### [Atividade Avaliativa](#reo3atividadeAvaliativa)


## <a name="reo3aula1"></a> **Paradigma Orientado a Objetos : Conceitos iniciais**


[Video Aula](https://youtu.be/lIp_sSmD3hg)

### **Conjunto de princípios**
 * Orientam a criação de sistemas computacionais, objetos que interagem entre si.  

Em termos de LPs, conceitos formais surgem com Simula 67, sendo consolidados com Smalltalk (primeira linguagem orientada a objetos).  

Popularizado com a difusão de interfaces gráficas de usuários (GUIs)
 * Surgimento de ferramentas com suporte para desenvolvimento de aplicações gráficas (C++, FoxPro, Delphi). 

Suportado por várias linguagens (ex: Python, Ruby, C#)
 * Atualmente sua maior expressão comercial é dada pelo Java

### **Pilares da OO**

Conceitos fundamentais (pilares) que norteiam o desenvolvimento OO:
 * Abstração;
 * Encapsulamento;
 * Herança;
 * Polimorfismo.

### **Abstração**
Representação de uma entidade do mundo real, com seu comportamento e características.  
"Modelos Mentais"
 * Classes;
 * Objetos;
 * Métodos;
 * Atributos;

**Classes**: 
Uma classe pode ser entendida como um módulo ou uma estrutura de dados abstrata.  
Uma visão mais ampla pode levar à seguinte definição:  
 * Uma classe é um tipo abstrato de dados, que reúne objetos com características similares.
 * O comportamento destes objetos é descrito pelo conjunto de métodos disponíveis.
 * O conjunto de atributos da classe descrevem as características de um objeto.

![Classes](img/classesReo3.png)

**********

**Objetos**:  
Um objeto pode ser entendido como um ser, lugar, evento, coisa ou conceito do mundo real que possa ser aplicável a um sistema.  
É comum que haja objetos diferentes com características semelhantes. Esses objetos são agrupados em classes.  
Classes são um agrupamento de objetos com características similares!  
Objetos são entidades (instâncias) únicas de uma classe!

![Objetos](img/objetosReo3.png)

************

**Atributos**:  
Um atributo é uma característica de um grupo de entidades do mundo real, agrupados em uma classe.  
Um atributo pode ser um valor simples (um inteiro, por exemplo) ou estruturas complexas (um outro objeto, por exemplo).  

![Atributos](img/atributosReo3.png)

Atributos de classe  
 * Em geral, os atributos pertencem a cada objeto instanciado, ou seja, a cada novo instanciação de uma mesma classe, cada instância pode ter valores distintos para cada atributo.
 * Atributos de classe são definidos para terem o mesmo valor para todas as instâncias de uma classe.

![Atributos de classe](img/atributosDeClasseReo3.png)

***************

**Métodos**  
Semelhante a uma função, é a implementação de uma ação da entidade representada pela classe;  
Conjunto de métodos define o comportamento dos objetos de uma classe.  

![Métodos](img/MétodosReo3.png)

******************

**Construtores**  
É um método especial para a criação e inicialização de uma nova instância de uma classe.  
Um construtor inicializa um objeto e suas variáveis, cria quaisquer outros objetos de que ele precise, garantindo que ele seja configurado corretamente quando criado.  
Na maioria das LPs, o construtor é um método que tem o mesmo nome da classe, que geralmente é chamado quando um objeto da classe é declarado ou instanciado.  

![Construtores](img/ConstrutoresReo3.png)
![Construtores](img/Construtores2Reo3.png)

****************

**Destrutores**  
De forma similar aos construtores, os destrutores são métodos fundamentais das classes, sendo geralmente chamados quando termina o tempo de vida do objeto.  
Em algumas linguagens como C++, ocupam um papel tão importante quanto os construtores, por conta da necessidade de desalocação de memória.  
Em outras linguagens como Java, o Garbage Collector (Coletor Automático de Lixo) faz esse papel, desalocando aquilo que não é mais utilizado. Há o método `finalize()`, mas raramente é utilizado (há dúvidas se sempre funciona, inclusive).  
Tanto os construtores, quanto os destrutores são métodos que não precisam ser definidos em Orientação a Objetos em Python, caso o comportamento esperado seja o padrão.  
Geralmente, define-se o construtor para a passagem de argumentos na criação do objeto. Já o destrutor não se costuma definir.  
Caso seja necessário realizar algum procedimento na destruição do objeto, define-se o método destrutor, como será exemplificado.  

![Destrutores](img/DestrutoresReo3.png)
![Destrutores](img/Destrutores2Reo3.png)

Garbage Collection em Java  
 * Em C++ a memória é alocada e desalocada explicitamente
 * Java possui gerenciamento automático de memória, realizado pela JVM  
   * Evita vazamento de memória e bugs de ponteiros 
   * Consome recursos computacionais quanto à decisão de desalocação
   * É um processo "não determinístico"

****

## <a name="reo3aula2"></a> **Paradigma Orientado a Objetos : Encapsulamento**  
[Video Aula](https://youtu.be/thvtKowe85E)  

Na programação Orientada a Objetos, é desejável e, muitas vezes, muito importante, que os atributos dos objetos tenham o devido nível e forma de acesso externo ao objeto.  
Para isso, é necessário definir a visibilidade dos atributos e métodos de um objeto.  
Como 'dono' dos atributos, um objeto é o mais indicado para lidar com seus atributos e métodos e não o cenário externo, como outros objetos.  
O encapsulamento permite maior controle e validação dos dados de um objeto  

### Encapsulamento  
É importante evitar que atributos de uma classe sejam diretamente acessíveis de fora da classe.
```Python 
class Conta:
  def __init__(self):
    self.saldo = 0

c1 = Conta()
c1.saldo = 100000
```  
![Atributos](img/EncapsulamentoAtributoVisivel.png)
Para acessar esses atributos, métodos são definidos   
  * permitem maior controle dos valores, como validação dos dados

### **Visibilidade**  
A visibilidade é utilizada para indicar o nível de acesso de um determinado atributo ou método;  
Os três modos distintos são:  
  * Público:
    * Objetos de quaisquer classes podem ter acesso a atributos, ou métodos, públicos;
  * Privado:
    * Apenas a classe que define atributos ou métodos privados pode ter acesso a eles;
  * Protegido:
    * Apenas a classe e suas subclasses podem ter acesso a atributos e métodos protegidos;

![Atributos](img/EncapsulamentoAtributoPrivadoPython.png)
![Atributos](img/EncapsulamentoAtributosPython.png)

Em Python é possível definir atributos, no momento da execução: 
![Atributos](img/EncapsulamentoDefinindoAtributosPython.png)
![Atributos](img/EncapsulamentoDefinindoAtributosPython2.png)

### **Getters e Setters**  
São métodos específicos para acesso aos atributos de uma classe, principalmente os atributos privado.  
Como padrão na comunidade de programadores, são nomeados com os prefixos 'ser_' ou 'get_' para ajustar ou obter os valores dos atributos.  
Permitem validação e formatação dos valores dos atributos antes de serem acessados ou alterados fora do objeto.  
São métodos, geralmente, públicos  

### **Troca de Mensagens**  
Na Orientação a Objetos, os objetos interagem pela troca de mensagens, e, nesse contexto, os métodos getters e setters desempenham papel importante e frequente. 
<h3 align="center"><em>Cada objeto sabe os atributos que têm e, portanto, têm métodos para alterá-los adequadamente</em></h3>  

### **Padrões de Projeto de Software**
Sáo soluções gerai para problemas que ocorrem com frequência na programação.  
Um desses padrões é chamado *'Decorator'*
  * Esse padrão adiciona comportamento a um método ou objeto em tempo de execução.

No python: 
**Decorators** @property e @attr.setter  
**@property** decora os métodos getters  
**@attribute_name.setter**, os métodos setters  
Não se utiliza os prefixos 'get_' e 'set_'  
Os métodos têm o nome do atributo a ser manipulado   
  * Polimorfismo

![Decorators](img/EncapsulamentoPropertyAndSetter.png)

**Decorator**  
**@classmethod** define métodos de classe  
@classmethod recebe uma referência à classe (geralmente chamado de cls) como primeiro parâmetro implícito (semelhante ao self, referência ao objeto)  

![Decorators](img/EncapsulamentoClassMethod.png)




****

## <a name="reo3aula3"></a> **Paradigma Orientado a Objetos : Herança e Composição**

### **HERANÇA OO**  
Mecanismo que permite que características comuns a diversas classes sejam organizadas em uma classe base e que, a partir dessa, outras possam ser criadas, herdando a classe base. 
<div align="center"><img src="img/herancaOO.png"/></div>  

A classe derivada (ou subclasse) mantém as características herdadas e acrescenta o que for de sua exclusividade. 
<div align="center"><img src="img/herancaOOjava.png"/></div>

A classe derivada (ou subclasse) mantém as características herdadas e acrescenta o que for de sua exclusividade.  
<p align="center">Python</p>

```Python 
class Pessoa: 
  def__init__(self,nome):
    self.nome = nome
  
class Paciente(Pessoa):
  def __init__(self,nome, med_id):
    super().__init__(nome)
    self.med_id = med_id

class Medico(Pessoa):
  def __init__(self,nome,id_func):
    super().__init__(nome)
    self.id_func = id_func
```
<div align="center"><img src="img/herancaOOpython.png"/></div>

### **CLASSE ABSTRATA**
Uma classe abstrata contém métodos abstratos, ou seja, que não têm implementação  
As classes que herdarem a classe abstrata são obrigados a realizar a implementação dos métodos abstratos da classe abstrata  
Uma classe abstrata, com métodos abstratos não pode ser diretamente instanciada  
<div align="center"><img src="img/herancaOOclasseAbstrata.png"/></div>
<div align="center"><img src="img/herancaOOclasseAbstrata2.png"/></div>

### **DUCK TYPING**  
Estilo de codificação, em linguagens dinamicamente tipadas, em que define-se classes e métodos sem se importar com o tipo das variáveis.  
<p align="center">Importa-se com o comportamento, não com o tipo</p>
<p align="center">se anda como pato, nada como um pato e faz quack como um pato, então provavelmente é um pato</p>

Por ser uma linguagem não tipada, ou seja, não se define o tipo das variáveis, os argumentos de métodos não são tipados e podem receber qualquer tipo de dados.   
Obviamente, as expressão com tais argumentos devem envolver operadores que consigam lidar com os valores fornecidos.  
Para se certificar que uma variável é um tipo esperado, o Python fornece algumas funções úteis: 
  * **type()** recebe como parâmetro uma variável e retorna o tipo da mesma
  * **isinstance()** recebe dois parâmetros: variável e tipo esperado. Retorna True se a variável é do tipo indicado e False caso contrário

```Python
class A: 
  pass

>> a = A()

>> isinstance(a,A)
True

>> type(a)
<class '__main__.A'>
```

### **HERANÇA MÚLTIPLA**  
Uma classe pode herdar de mais de uma classe seus atributos e métodos  
Java não suporta  
C++ e Python suportam herança múltipla  

<div align="center"><img src="img/herancaOOmúltiplaClock.png"/></div>
<div align="center"><img src="img/herancaOOmúltiplaCalendar.png"/></div>
<div align="center"><img src="img/herancaOOmúltiplaCalendarClock.png"/></div>


### **PROBLEMA DO DIAMANTE**  
O problema do Diamante (devido à forma geométrica da ilustração ao lado) pode ocorrer na herança múltipla  

```Python  
class A:
  def m(self):
    print("m of A called")
class B(A):
  def m(self):
    print("m of B called")
class C(A): 
  def m(self):
    print("m of C called")

class D(B,C):
  pass
```

Considere as classes A, B, C e D, a cima, o que acontece no seguinte trecho do código? 
```Python
d = D()
d.m()
```
<span style="color: orange;">Qual método m() será invocado, da classe A,B ou C?</span>   
A resolução da ambiguidade depende da MRO (MethodResolutionOrder) de cada linguagem  
Leia em https://www.python.org/download/releases/2.3/mro/ADBC



****

## <a name="reo3aula4"></a> **Paradigma Orientado a Objetos : Polimorfismo**

[Video aula](https://youtu.be/L5VFek5PDEg)

Habilidade de apresentar a mesma interface para formas diferentes, tipos diferentes de dados
  * Por exemplo, métodos polimórficos podem aceitar tipos de dados diferentes e, dependendo dos mesmos ter comportamentos diferentes;

<div align="center"><img src="img/polimorfismo1.png"/></div>
<div align="center"><img src="img/polimorfismo2.png"/></div>

### **Sobrescrita, sobrecarga, substituição**  
Relacionadas ao polimorfismo, temos algumas variações são bem similares, veja:  
  * **Sobrescrita**: Método com mesmo nome, quantidade de parâmetros (e/ou tipos de parâmetros)
  * **Sobrecarga**: Método com mesmo nome, mas quantidade e tipos de parâmetros diferentes
  * **Substituição**: Quando uma subclasse reescreve um método definido na superclasse

### **Sobrecarga**  
O mecanismo chamado de sobrecarga (*overloading*) é utilizado quando se deseja que dois métodos de uma mesma classe possam ter o mesmo nome, desde que suas listas de parâmetros sejam diferentes, constituindo assim uma assinatura diferente de cada método.  
A sobrecarga não gera conflito pois o compilador é capaz de detectar qual método deve ser escolhido a partir da análise dos tipos de argumentos do método.  
A sobrecarga é uma aplicação do polimorfismo na Orientação a Objetos.  
<div align="center"><img src="img/polimorfismoSobrecarga.png"/></div>

**Métodos *mágicos*, em Python**  
Em Python, um inteiro, ponto-flutuante, string, lista, dicionários, etc. São tratados como objetos. Inclusive, essas 'classes base' podem ser herdadas, como veremos mais adiante.  
Portanto, vários operadores pode ser sobrecarregados para operar em todos esses tipos de dados e, inclusive, sobre objetos criados por um programador.  
Isso é feito através dos métodos mágicos.  
Veja a tabela a seguir, que lista os operadores, tanto aritméticos quanto lógicos, e seus respectivos métodos mágicos para sobrecarga.
<div align="center"><img src="img/polimorfismoSobrecargaMetodosMagicos.png"/></div>
<div align="center"><img src="img/polimorfismoSobrecarga2.png"/></div>
<div align="center"><img src="img/polimorfismoSobrecarga3.png"/></div>
<div align="center"><img src="img/polimorfismoSobrecarga4.png"/></div>

<div align="center"><img src="img/polimorfismo3.png"/></div>
<div align="center"><img src="img/polimorfismo4.png"/></div>
<div align="center"><img src="img/polimorfismo5.png"/></div>
<div align="center"><img src="img/polimorfismo6.png"/></div>
<div align="center"><img src="img/polimorfismo7.png"/></div>
<div align="center"><img src="img/polimorfismo8.png"/></div>
****

## <a name="reo3Python"></a> **Paradigma Orientado a Objetos : Python**

Conceitos Iniciais: 

Definição de classe:   
```Python
class Pessoa: 
  def __init__(self,cpf,nome): 
    self.cpf = cpf
    self.nome = nome
```
Objetos: 
```Python
p1 = Pessoa('123.456.789-10', 'João da Silva')
```
Atributos são o `self.cpf` e `self.nome`  
Atributos de classe nesse exemplo seria o `__total_pessoas`  
```Python
class Pessoa: 
  __total_pessoas = 0
  def __init__(self,cpf,nome): 
    self.cpf = cpf
    self.nome = nome
    Pessoa.__total_pessoas += 1
  def get_total_pessoas(self): 
    return Pessoa.__total_pessoas

p1 = Pessoa('123.456.789-10', 'Bissexto')
print(p1.get_total_pessoas()) #erro
print(Pessoa.get_total_pessoas(p1)) #OK
``` 
> 1  

Métodos
```Python
from datetime import datetime
class Pessoa:
  def __init__(self,cpf,nome, data_nascimento):
    d, m, a = data_nascimento.split("/")
    self.cpf = cpf
    self.nome = nome
    self.data_nascimento = datetime(a,m,d)

  def get_data_nascimento(self):
    return self.data_nascimento.strftime("%x")
```
Construtores 
```Python
class Medicamento:
  def __init__(self, nome):
    self.nome = nome
```
Destrutores  
```Python
class A: 
  def __del__(self):
    print("A has been destroyed")

minhaClasse = A()
del minhaClasse
```
> A has been destroyed


Visibilidade de atributos 
```Python
class A(): 
  def__init__(self):
    self.__priv = "I am private"
    self._prot = "I am protected"
    self.pub = "I am public"
```

Limitanto os atributos 
```Python
class Conta:
  _slots__=('_Conta__saldo')
  def __init__(self): 
    self.__saldo = 0 

c1 = Conta()
c1.new_saldo = 100000 #Erro
c1._Conta__saldo = 100000 #permitido
```
Decorators 
```Python
class Conta: 
  _slots__ = ('_Conta__saldo')
  def __init__(self): 
    self.__saldo = 0  
  @property  
  def saldo(self):
    return 'R$ {0:.2f}'.format(self.__saldo)
  @saldo.setter 
  def saldo(self, novo_saldo):
    if novo_saldo > 0:
      self.__saldo = novo_saldo
    else:
      raise Exception()
  @classmethod 
  def contas_instanciadas(cls):
    return '{} contas ativas'.format(cls.__contas)

c1 = Conta()
c1.saldo = 100 # chama setter  
c1.saldo  # chama getter
# R$ 100     
c1.saldo = -100 #Exception
print(Conta.contas_instanciadas()) 
c2 = Conta()
print(c2.contas_instanciadas()) 
```
> 1 contas ativas  
> 2 contas ativas   

Herança em OO  
```Python 
class Pessoa: 
  def__init__(self,nome):
    self.nome = nome
  
class Paciente(Pessoa):
  def __init__(self,nome, med_id):
    super().__init__(nome)
    self.med_id = med_id

class Medico(Pessoa):
  def __init__(self,nome,id_func):
    super().__init__(nome)
    self.id_func = id_func
```
***

<h1><a name = "paradigmaFuncional"> Reo 4 - Paradigma Funcional
</a></h1> 

* Aulas 
  * [Aula 1 - Paradigma Funcional : Introdução](#paradigmaFuncionalAula1)
  * [Haskell](#paradigmaFuncionalHaskell)

* [Atividade Avaliativa](#paradigmaFuncionalAtividadeAvaliativa)


<a name = "paradigmaFuncionalAula1"></a>

## **Paradigma Funcional : Introdução**
[video-aula](https://youtu.be/1NNTy7X9Q18)

<center style="margin: 40px 0 20px 0;">

## **Introdução**

</center>

O paradigma funcional trata a computação como avaliação de funções matemáticas.  

Esse estilo de programação é suportado por linguagens de programação funcional, ou linguagens aplicativas.  

Linguagens funcionais possuem alto nível de abstração e estilo declarativo: especifica-se o que deve ser computado ao invés de como.  

Alguns exemplos de linguagens funcionais: LISP, Scheme, ML e Haskell.2

<center style="margin: 10px 0 10px 0;">

  ![Linguagens](img/paradigmaFuncionalLinguagens.png)

</center>


<center style="margin: 40px 0 20px 0;">

## **Funções matemáticas**

</center>

Uma função matemática é um mapeamento de membros de um conjunto, chamado de conjunto **domínio**, para outro, chamado de conjunto **imagem**.  

As funções são geralmente aplicadas a um elemento em particular do conjunto domínio, fornecido como um **parâmetro** para a função.  

Uma função leva a, ou retorna, um elemento do conjunto imagem.  

Em funções matemáticas, a ordem de avaliação de suas expressões de mapeamento é controlada por recursão e expressões condicionais, e não por sequência e repetição iterativa, como nas linguagens imperativas

<center>

  ![Linguagens](img/paradigmaFuncionalFunçõesMatemáticas.png)
  ![Linguagens](img/paradigmaFuncionalFunçõesMatemáticas2.png)

</center>

<center style="margin: 40px 0 20px 0;">

## **Fundamentos da Programação Funcional - I**

</center>

O objetivo do projeto de uma linguagem de programação funcional é **mimetizar funções matemáticas ao máximo possível**.  

Em uma linguagem imperativa, uma expressão é avaliada e o resultado é armazenado em uma **posição de memória**, representada como uma variável em um programa.   

Uma linguagem de **programação puramente funcional não usa variáveis**, nem sentenças de atribuição. Sem variáveis, as construções de iteração não são possíveis, já que elas são controladas por variáveis


<center style="margin: 40px 0 20px 0;">

## **Fundamentos da Programação Funcional - II**

</center>

Na programação funcional, as repetições devem ser especificadas com recursão em vez de estruturas de repetição.  

Uma linguagem funcional fornece:  

* um conjunto de **funções primitivas**; 
* um conjunto de **formas funcionais** para construir funções complexas a partir das funções primitivas; 
* uma **operação de aplicação de função**; 
* alguma estrutura ou **estruturas para representar dados**


<center style="margin: 40px 0 20px 0;">

## **Transparência Referencial**

</center>

Programa funcional não tem ’estado’  
Não tem atribuição: o programador não precisa se preocupar com variáveis  

Dada uma função, podemos substituí-la por seu valor de retorno sem causar impacto na aplicação

O resultado de uma função é determinado unicamente por seus valores de entrada. Coisa alguma fora da função pode afetar a sua saída.  

<center style="font-size: 15px;">
Isso é não tem efeito colateral!!
</center>

<center style="margin: 40px 0 20px 0;">

## **Uso da recursão**

</center>

Principal causa da perda de performance, pois é computacionalmente caro realizar a recursão.  

Se recursão for *de cauda* interpretador por mudar para iteração. 

<center style="font-size: 15px;color: darkorange;font-weight: 600;">
Pesquise o que significa recursão de cauda
</center>

<center style="font-size: 15px;">

Indicado é sempre tentar **recursão de cauda**

</center>

<center style="margin: 40px 0 20px 0;">

## **Funções Simples**

</center>

```Haskell
cube(x) ≡ x * x *x, x ∈ ℝ
cube: ℝ → ℝ
```

<center>

  ![Funções Simples](img/paradigmaFuncionalFunçõesSimples.png)

</center>

<center style="margin: 40px 0 20px 0;">

## **Funções Lambda**

</center>

Alonzo Church, 1941, especificou funções não nomeadas

```Haskell
λ(x)𝑥∗𝑥∗𝑥
(λ(x)𝑥∗𝑥∗𝑥(2)
```
Resulta em 8

<center>

  ![Funções Lambda](img/paradigmaFuncionalFunçõesLambda.png)

</center>

<center>

## **Formas Funcionais**

</center>

Nem tudo se resolve com funções simples, como a função cubo. Então, as linguagens funcionais permitem as funções de ordem superior. Exemplos:
* Composição de funções
* Aplicar-a-todos


### **Composição de funções**


```Haskell
ℎ ≡ 𝑓°𝑔

𝑓(𝑥) ≡ 𝑥+2
𝑔(𝑥) ≡ 3∗𝑥

ℎ(𝑥) ≡ 𝑓(𝑔(𝑥))
ℎ(𝑥) ≡ (3∗𝑥)+2
```

<center>

  ![Funções Lambda](img/paradigmaFuncionalComposiçãoDeFunções.png)

</center>


### **Aplicar a todos**

Denotada como α recebe uma única função como parâmetro e uma lista de argumentos

```Haskell
𝑓(𝑥) ≡ 𝑥∗𝑥
α(𝑓,(2,3,4))
```
Resulta em (4,9,16)


<a name = "paradigmaFuncionalAtividadeAvaliativa"></a>


<center style="margin: 40px 0 20px 0;">

## **A primeira linguagem funcional**

</center>

LISP está para Fortran, como Funcional está para Imperativo, no histórico das linguagens de programação

Mas, inclui recursos imperativos: variáveis e, portanto, não pode ser considerada uma linguagem puramente funcional

### **LISP: Tipos e Estruturas de dados**

Em LISP, os dados podem ser:  
◇Átomos, ou  
◇Listas 
* Desprovidos de tipos  

◇Exemplos de Listas em LISP
* (A BC D)
* (A (BC) D(E (FG)))

### **LISP: Primeiro interpretador**

LISP usa a Notação-M que foi definida para a linguagem FORTRAN
* Notação-M para linguagem de máquina (máquina IBM 704)  
 
Função EVAL é o Interpretador LISP, definido em 1965
* Tem grande relação com o estudo da computabilidade, que vocês estudarão na disciplina Teoria da Computação

Convenção Cambridge Polonesa definia a seguinte sintaxe para os comandos LISP
```LISP
(nome_funcao param_1 ... param_n)
(+ 5 7)
(nome_funcao(LAMBDA(arg_1, ..., arg_n) expressao))
```

### **Scheme**

É um dialeto de LISP, surgiu no MIT em 1970, com as seguintes vantagens:
* Tamanho pequeno
* Escopo estático
* Sintaxe simples
* Bom para fins didáticos

### **Scheme: Interpretador**

Laço infinito de leitura-avaliação-escrita: Lê o comando, faz a sua avaliação (execução) e retorna o resultado

Isso é feito pela função EVAL 
1. Cada expressão de parâmetro é avaliada 
2. Função primitiva é aplicada aos parâmetros 
3. Valor resultante é mostrado

### **Scheme: Funções Numéricas Primitivas**

* +, -, /, e * são os operadores aritméticos
* \* -> 1 (se inserir apenas o operador *, Schemeretorna 1)
* \+ -> 0 (se inserir apenas o +, retorna 0, porque?)
* Considere os seguintes comandos e retornos:   
  * (* 3 7) retorna 21  
  * (-15 7 2)retorna 6  
  * (-24 (* 4 3))retorna 12

### **Scheme: definição de funções**

Baseado na notação LAMBDA

* `(LAMBDA(x)(* x x))`
* `((LAMBDA(x)(* x x))7)`
  * Resulta em 49
  * x é variável vinculada e nunca muda na expressão

* DEFINE é utilizado para vincular nome a um valor ou expressão
  * Não define variável!
  * Pode criar constante
* `(DEFINE símbolo expressão)`  
* `(DEFINE pi 3.14159)`  
* `(DEFINE two_pi(* 2 pi))`

### **Scheme: Função de saída**
* `(DISPLAY expressão)`
  * Como o print do Python
* `(NEWLINE)`

### **Scheme: Predicado numérico**

<div style="margin: 20px 0 20px 0;display: flex; flex-direction: row;justify-content: center;">

  <div style="padding-top: 100px;margin-right: 50px;">
    <h3>Retorna valor<br>booleano:<br>◇#T<br>◇#F</h3>
  </div>

  <table width="50%" >
    <tr>
      <th style="background: black; color: white;border: 1px solid rgb(155,155,155);">
        Função
      </th>
      <th style="background: black; color: white;border: 1px solid rgb(155,155,155);">
        Significado
      </th>
    </tr>
    <tr>
      <td style="background: rgb(200,200,200); color: black ;border: 1px solid rgb(155,155,155);">
        =
      </td>
      <td style="background: rgb(200,200,200); color: black ;border: 1px solid rgb(155,155,155);">
        Igual
      </td>
    </tr>
    <tr>
      <td style="background: white; color: black ;border: 1px solid rgb(155,155,155);">
        <>
      </td>
      <td style="background: white; color: black ;border: 1px solid rgb(155,155,155);">
        Diferente
      </td>
    </tr>
    <tr>
      <td style="background: rgb(200,200,200); color: black ;border: 1px solid rgb(155,155,155);">
        >
      </td>
      <td style="background: rgb(200,200,200); color: black ;border: 1px solid rgb(155,155,155);">
        Maior que
      </td>
    </tr>
    <tr>
      <td style="background: white; color: black ;border: 1px solid rgb(155,155,155);">
        <
      </td>
      <td style="background: white; color: black ;border: 1px solid rgb(155,155,155);">
        Menor que
      </td>
    </tr>
    <tr>
      <td style="background: rgb(200,200,200); color: black ;border: 1px solid rgb(155,155,155);">
        >=
      </td>
      <td style="background: rgb(200,200,200); color: black ;border: 1px solid rgb(155,155,155);">
        Maior ou igual a
      </td>
    </tr>
    <tr>
      <td style="background: white; color: black ;border: 1px solid rgb(155,155,155);">
        <=
      </td>
      <td style="background: white; color: black ;border: 1px solid rgb(155,155,155);">
        Menor ou igual a
      </td>
    </tr>
    <tr>
      <td style="background: rgb(200,200,200); color: black ;border: 1px solid rgb(155,155,155);">
        EVEN?
      </td>
      <td style="background: rgb(200,200,200); color: black ;border: 1px solid rgb(155,155,155);">
        É numero par?
      </td>
    </tr>
    <tr>
      <td style="background: white; color: black ;border: 1px solid rgb(155,155,155);">
        ODD?
      </td>
      <td style="background: white; color: black ;border: 1px solid rgb(155,155,155);">
        É número ímpar?
      </td>
    </tr>
    <tr>
      <td style="background: rgb(200,200,200); color: black ;border: 1px solid rgb(155,155,155);">
        ZERO?
      </td>
      <td style="background: rgb(200,200,200); color: black ;border: 1px solid rgb(155,155,155);">
        É zero?
      </td>
    </tr>
  </table>

</div>

### **Scheme: Controle de fluxo**

<div style="display: flex;flex-direction: row;margin-bottom: 20px;">

  <div align="center" style="background: rgb(255,249,204); height: 80px;padding-top: 11px;border: 2px solid rgb(244,219,7); margin-right: 20px;margin-top: 30px;">
    Exemplo da<br>função factorial,<br>em Scheme
  </div>

```Scheme
(IF predicado expressão_ então expressão_senão)
(DEFINE (factorial n)
  (IF (= n0)
    1
    (* n(factorial(- n 1)))))
  )
)
```

</div>


### **Scheme: Funções de lista**

<div style="display: flex;flex-direction: row;margin-bottom: 20px;margin-top: 10px;">

  <div align="center" style="background: rgb(255,249,204);min-width: 100px;height: 115px;padding-top: 5px;border: 2px solid rgb(244,219,7); margin-right: 20px;margin-top: 30px;font-size: 14px;line-height: 15px">

  `DEFINE`<br>Retorna o<br>segundo,<br>elemento da<br>lista `lst`<br>Consegue ver<br> isso?
  </div>

  <div>

  Uso principal das primeiras linguagens funcionais foi o processamento de listas   
  Então a linguagem tem *seletores* para listas:  
  * `CAR`: retorna o primeiro elemento da lista
  * `CDR`: retorna a lista menos o primeiro elemento
  * `(DEFINE (second lst) (CAR (CDR lst)))`
  
  </div>

</div>

### **Scheme: QUOTE**

Evita que um parâmetro seja avaliado

<div style="display: flex;flex-direction: row;margin-bottom: 20px;margin-top: 10px;">


  <div>

  * `(QUOTE A)`
    * `A
  </div>

  <div align="center" style="background: rgb(255,249,204);min-width: 110px;height: 62px;padding-top: 10px;border: 2px solid rgb(244,219,7); margin-LEFT: 20px;font-size: 14px;line-height: 15px">

  Retorna A, sem<br>saber o que A<br>seja
  </div>

</div>

* `(QUOTE (A B C))`
  * `(A B C)

## **Atividade Avaliativa**
[Paradigma Funcional : Exemplos em Haskell](https://youtu.be/NKQUtbwHrMo)