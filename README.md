## English description

This is the repo of my solution to the *Arithmetic Formatter* project from the **Scientific Computing with Python** course from freeCodeCamp. Portuguese version down below.

### Assignment

Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:
```
  235
+  52
-----
```

Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to `True`, the answers should be displayed.

### For example

Function Call:
```py
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

Output:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Function Call:
```py
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

Output:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

### Rules

The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will **return** a **string** that describes an error that is meaningful to the user.  


* Situations that will return an error:
  * If there are **too many problems** supplied to the function. The limit is **five**, anything more will return:
    `Error: Too many problems.`
  * The appropriate operators the function will accept are **addition** and **subtraction**. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be:
    `Error: Operator must be '+' or '-'.`
  * Each number (operand) should only contain digits. Otherwise, the function will return:
    `Error: Numbers must only contain digits.`
  * Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be:
    `Error: Numbers cannot be more than four digits.`
*  If the user supplied the correct format of problems, the conversion you return will follow these rules:
    * There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.
    * Numbers should be right-aligned.
    * There should be four spaces between each problem.
    * There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)

### Development

Write your code in `arithmetic_arranger.py`. For development, you can use `main.py` to test your `arithmetic_arranger()` function. Click the "run" button and `main.py` will run.

### Testing 

The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

### Submitting

Copy your project's URL and submit it to freeCodeCamp.

-------------------------------------------------------------------------------------------

## Descrição em português

Esse é o repositório com a minha solução para o projeto *Arithmetic Formatter* do curso **Scientific Computing with Python** do freeCodeCamp. A tradução do README em inglês é livre e feita por mim.

### Tarefa

Alunos do Ensino Fundamental geralmente montam os seus problemas de aritmética verticalmente para facilitar a solução. Por exemplo, "253 + 52" se torna:

```
  235
+  52
-----
```

Crie uma função que recebe uma lista de strings que são problemas aritméticos e retorna os problemas organizados verticalmente e lado a lado. A função deve receber um segundo argumento opcional; quando o segundo argumento estiver setado para `True`, as respostas devem ser exibidas.

### Por exemplo

Chamada da função:
```py
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

Output:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Chamada da função:
```py
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

Output:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

### Regras

A função retornará a conversão correta se os problemas fornecidos estiverem adequadamente formatados; do contrário, **retornará** uma **string** que descreve um erro significativo para o usuário.


* Situações que retornarão erro:
  * Se há **problemas demais** fornecidos para a função. O limite são **cinco**, qualquer coisa a mais retornará:
    `Error: Too many problems.`
  * Os operadores adequados que a função aceitará são **adição** e **subtração**. Multiplicação e divisão retornarão um erro. Outras operações não mencionados aqui não precisarão ser testados. O error retornado será:
    `Error: Operator must be '+' or '-'.`
  * Cada número (operand) deve conter apenas dígitos. Do contrário, a função retornará:
    `Error: Numbers must only contain digits.`
  * Cada operando tem um máximo de 4 dígitos de largura. Do contrário, a string de erro retornada será:
    `Error: Numbers cannot be more than four digits.`
* Se o usuário forneceu os problemas no formato correto, a conversão que você retornará deve seguir as seguintes regras:
    * Deve haver um único espaço entre o operador e o mais longo dos dois operandos, o operador estará na mesma linha do segundo operando, ambos os operandos estarão na mesma ordem fornecida (o primeiro no topo e o segundo embaixo).
    * Números devem estar alinhados à direita.
    * Devem haver 4 espaçoes entre cada problema.
    * Devem haver traços no final de cada problema. Eles devem percorrer todo o comprimento de cada problema individual (vide exemplo acima).

### Desenvolvimento

Escreva seu código em `arithmetic_arranger.py`. Para desenvolvimento, você pode usar `main.py` para testar a sua função `arithmetic_arranger()`. Clique no botão "run" e `main.py` irá rodar.

### Testando

Os testes unitários para este projeto estão em `test_module.py`. Importamos os testes de `test_module.py` para `main.py` para a sua conveniência. Os testes rodarão automaticamente sempre que você clicar no botão "run".

The unit tests for this project are in . We imported the tests from  for your convenience. The tests will run automatically whenever you hit the "run" button.

### Submissão

Copie a URL do projeto e submeta-a ao freeCodeCamp.
