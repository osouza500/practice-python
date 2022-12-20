# Practice Python
## Exercício 6
A tarefa é pedir uma string ao usuário e printar se o input é um palíndromo ou não. 
## Minha solução
Usei o método **replace()** para eliminar os espaços da string (caso seja uma frase).

O loop **for** itera sobre  essa string. A cada iteração, um caractere é adicionado a uma lista vazia,
começando pelo último por meio de um operador de índice com valor negativo que decresce a cada iteração.

Ao cabo do loop, converti o conteúdo da lista em string a partir do método **join()**. O resultado é a palavra/frase
inserida pelo usuário, porém ao contrário.

Por fim, o conteúdo de amabs as variáveis são comparadas a partir de uma instrução **if/else** e o resultado é printado.
