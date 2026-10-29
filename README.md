# Lista de tarefas

Aplicativo de terminal para adicionar e acompanhar tarefas. É possível
consultar a lista, marcar tarefas como concluídas e remover as concluídas.

## Requisitos

- Python 3.7 ou superior
- Nenhuma dependência externa

## Como executar

No terminal, acesse a pasta do projeto e execute:

```bash
python lista_tarefas.py
```

Em alguns sistemas, use `python3` no lugar de `python`.
A saída é configurada como UTF-8 quando o terminal oferece suporte.

## Como usar

1. **Ver tarefas:** mostra todas as tarefas e indica quais foram concluídas.
2. **Adicionar nova tarefa:** solicita uma descrição não vazia.
3. **Marcar tarefa como concluída:** permite escolher entre as tarefas
   pendentes.
4. **Remover tarefa concluída:** permite escolher entre as tarefas concluídas.
5. **Sair:** encerra o programa.

Entradas inválidas são avisadas sem encerrar o programa. As tarefas ficam
somente na memória durante a execução e não são salvas ao sair.

## Executar os testes

Execute na pasta do projeto:

```bash
python -m unittest -v
```

## Estrutura

- `lista_tarefas.py`: aplicação e operações da lista.
- `test_lista_tarefas.py`: testes automatizados com a biblioteca padrão `unittest`.

## 👨‍💻 Autor

### Diego Francisco da Silva

Desenvolvedor Front-End em formação e estudante de Engenharia de Software.

- **[Site Empresa](https://diegofranciscodasilva.github.io/dev-software-web/)**: dev.software.web Site Empresa
- **[LinkedIn](https://www.linkedin.com/in/diego-francisco-da-silva/)**: diego-francisco-da-silva
- **[GitHub](https://github.com/diegofranciscodasilva)**: diegofranciscodasilva
- **[Instagram](https://www.instagram.com/diego_francisco_da_silva/)**: @diego_francisco_da_silva
- **[Instagram](https://www.instagram.com/dev.software.web/)**: @dev.software.web

---

Feito com ❤️ por Diego.
