# 🤝 Guia de Contribuição

Obrigado pelo interesse em contribuir com o projeto **TTS Acessibilidade PT-BR**! 🗣️♿

Este projeto é uma pesquisa acadêmica aberta e toda contribuição da comunidade é bem-vinda, seja reportando bugs, sugerindo melhorias, adicionando novos modelos ou melhorando a documentação.

---

## 📋 Índice

- [Como Reportar Bugs](#-como-reportar-bugs)
- [Como Sugerir Melhorias](#-como-sugerir-melhorias)
- [Como Adicionar um Novo Modelo TTS](#-como-adicionar-um-novo-modelo-tts)
- [Padrão de Commits](#-padrão-de-commits)
- [Código de Conduta](#-código-de-conduta)

---

## 🐛 Como Reportar Bugs

1. **Verifique se o bug já foi reportado** na [lista de issues](https://github.com/renatoork/tts-acessibilidade-pt-br/issues)
2. Se não encontrar um issue existente, [abra um novo](https://github.com/renatoork/tts-acessibilidade-pt-br/issues/new)
3. Inclua no report:
   - **Descrição clara** do problema
   - **Passos para reproduzir** o bug
   - **Comportamento esperado** vs. **comportamento atual**
   - **Ambiente** (Python version, SO, GPU, Colab ou local)
   - **Mensagens de erro** completas (stack trace)
   - **Versões dos pacotes** relevantes (`pip freeze`)

### Template de Bug Report

```markdown
**Descrição:**
[Descreva o bug de forma clara e concisa]

**Passos para Reproduzir:**
1. ...
2. ...
3. ...

**Comportamento Esperado:**
[O que deveria acontecer]

**Comportamento Atual:**
[O que acontece de fato]

**Ambiente:**
- Python: 3.x.x
- PyTorch: x.x.x
- Colab / Local: ...
- GPU: ...

**Mensagem de Erro:**
```
[Cole o traceback aqui]
```
```

---

## 💡 Como Sugerir Melhorias

1. [Abra um novo issue](https://github.com/renatoork/tts-acessibilidade-pt-br/issues/new) com a tag `enhancement`
2. Descreva a melhoria proposta:
   - **Motivação**: Por que essa melhoria é útil?
   - **Solução proposta**: Como você imagina que deveria funcionar?
   - **Alternativas consideradas**: Outras abordagens que você avaliou

---

## 🤖 Como Adicionar um Novo Modelo TTS

Para adicionar suporte a um novo modelo TTS ao projeto:

### 1. Crie o notebook do modelo

Na pasta `notebooks/`, crie um arquivo seguindo o padrão de nomenclatura:

```
NN_nome_do_modelo.ipynb
```

O notebook deve conter as seções padrão (veja `notebooks/README.md`).

### 2. Documente o modelo

Adicione uma seção ao arquivo `docs/modelos.md` com:

- Nome e link oficial do modelo
- Arquitetura (VITS, Transformer, etc.)
- Suporte ao português brasileiro
- Requisitos de hardware
- Exemplo de instalação e uso
- Prós e contras

### 3. Atualize o README

No `README.md` principal, adicione o modelo à tabela de modelos avaliados.

### 4. Abra um Pull Request

Envie um PR com as mudanças, incluindo na descrição:
- Por que esse modelo é relevante para o contexto de acessibilidade
- Requisitos e limitações
- Resultados preliminares (se disponíveis)

---

## 📝 Padrão de Commits

Este projeto adota o padrão [Conventional Commits](https://www.conventionalcommits.org/).

### Formato

```
<tipo>(<escopo>): <descrição curta em português>

[corpo opcional]

[rodapé opcional]
```

### Tipos Aceitos

| Tipo | Uso |
|------|-----|
| `feat` | Nova funcionalidade ou novo modelo |
| `fix` | Correção de bug |
| `docs` | Alterações na documentação |
| `refactor` | Refatoração de código sem mudança de comportamento |
| `test` | Adição ou correção de testes |
| `chore` | Tarefas de manutenção (atualização de deps, etc.) |
| `notebook` | Adição ou atualização de notebook |

### Exemplos

```bash
# Adicionar novo modelo
git commit -m "feat(notebooks): adicionar notebook para modelo Whisper TTS"

# Corrigir bug em utils.py
git commit -m "fix(scripts): corrigir cálculo de RTF quando duração é zero"

# Atualizar documentação
git commit -m "docs(metricas): adicionar métrica de WER (Word Error Rate)"

# Adicionar dados de teste
git commit -m "chore(textos): adicionar frases técnicas de computação para teste"
```

---

## 🌐 Código de Conduta

Este projeto segue o princípio de que **tecnologia deve ser inclusiva e acessível a todos**.

### Nossos Valores

- **Respeito**: Trate todos os colaboradores com respeito e cordialidade
- **Inclusão**: Acolha pessoas de todos os níveis de experiência e background
- **Acessibilidade**: Lembre-se que o objetivo final é ajudar pessoas com deficiência visual
- **Colaboração**: Compartilhe conhecimento e ajude outros colaboradores

### Comportamentos Inaceitáveis

- Linguagem ou imagens ofensivas
- Assédio de qualquer natureza
- Discriminação por gênero, raça, orientação sexual, deficiência ou qualquer outro atributo
- Spam ou autopromoção excessiva

### Como Reportar Violações

Se você presenciar ou for vítima de comportamento inadequado, entre em contato com o mantenedor do projeto via GitHub.

---

## 🙏 Agradecimentos

Todo contribuidor que tiver um PR aceito será adicionado à seção de **Agradecimentos** no `README.md`.

Juntos podemos tornar a tecnologia de síntese de voz mais acessível para todos! 🚀
