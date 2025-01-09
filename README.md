# Projeto CVM-ETL

Este repositório contém uma estrutura padrão para iniciar um projeto na área de Dados. Abaixo, você encontrará uma descrição de cada pasta e arquivo presente no repositório.

## Estrutura de Pastas

### `.github/workflows`
Contém os arquivos de configuração para a integração contínua e deploy (CI/CD). São definidos os fluxos de trabalho que automatizam testes, builds e outros processos.

### `.vscode`
Esta pasta contém configurações específicas do Visual Studio Code (VSCode), como configurações de formatação e linting para facilitar o desenvolvimento.

### `app`
A pasta **app** contém a lógica principal do projeto. Aqui, você encontrará os scripts que realizam as operações de extração, transformação e carregamento de dados, como a conexão com fontes de dados, transformação de dados e carregamento para o destino.

### `docs`
A pasta **docs** contém toda a documentação do projeto. Normalmente, inclui informações sobre como usar, desenvolver, e contribuir para o projeto. Também pode conter especificações técnicas e manuais de uso.

### `tests`
A pasta **tests** contém os testes automatizados do projeto. São definidos testes para garantir que o código do projeto funcione corretamente e que as transformações de dados sejam realizadas com precisão.

### `.gitignore`
Este arquivo contém uma lista de arquivos e diretórios que devem ser ignorados pelo Git. Isso é útil para evitar que arquivos temporários, como logs, binários ou configurações locais, sejam versionados no repositório.

### `.python-version`
Este arquivo especifica a versão do Python que deve ser utilizada no ambiente virtual do projeto. Ele ajuda a garantir que o projeto seja executado com a versão correta do Python, independentemente do ambiente em que está sendo desenvolvido.

### `README.md`
Este arquivo contém a documentação inicial sobre o projeto. Ele serve como guia para desenvolvedores e outros colaboradores, explicando o propósito do repositório, como configurá-lo e usá-lo, além de outras informações úteis.

### `mkdocs.yml`
O arquivo de configuração do MkDocs. MkDocs é uma ferramenta estática para criar sites de documentação. Este arquivo define a estrutura e o conteúdo do site de documentação do projeto.

### `poetry.lock`
Este arquivo é gerado automaticamente quando se utiliza o **Poetry** para gerenciar dependências. Ele garante que as versões das dependências instaladas sejam consistentes em todos os ambientes, registrando as versões exatas das bibliotecas que foram instaladas.

### `pre-commit-config.yaml`
Arquivo de configuração para o **Pre-commit**, que define hooks (gatilhos) para rodar ferramentas de verificação de código, como linters e formatadores, antes de cada commit. Isso ajuda a garantir a qualidade do código e a consistência entre os colaboradores.

### `pyproject.toml`
Este arquivo contém as configurações do projeto, incluindo as dependências do Python, como o **Poetry** para gerenciamento de pacotes, além de outras configurações relacionadas ao projeto. Ele é usado pelo Poetry para gerenciar dependências e a versão do projeto.

## Como rodar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/cvm-etl.git
   cd cvm-etl
