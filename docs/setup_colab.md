# Guia de Execução no Google Colab

## Pré-requisitos

- Conta Google (gratuita)
- Navegador web moderno
- Sem necessidade de GPU ou instalação local

---

## 1. Abrindo o Notebook

### Opção A — Link Direto

Clique no botão abaixo para abrir o notebook diretamente no Google Colab:

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-xhoU_3Jg7MbrsmIES2Aezv0-_A90FT6)

### Opção B — Via GitHub

1. Acesse [colab.research.google.com](https://colab.research.google.com)
2. Clique em **Arquivo > Abrir notebook**
3. Selecione a aba **GitHub**
4. Cole: `renatoork/tts-acessibilidade-pt-br`
5. Selecione `modelscompare_v5_1903-2.ipynb`

---

## 2. Configurando o Runtime

> ⚠️ **IMPORTANTE**: O experimento foi projetado para rodar em **CPU**. Não é necessário GPU.

1. No menu superior, clique em **Runtime > Alterar tipo de runtime**
2. Em **Acelerador de hardware**, selecione **Nenhum (CPU)**
3. Clique em **Salvar**

Isso garante que os resultados sejam reprodutíveis e democraticamente acessíveis.

---

## 3. Estrutura das Células

O notebook está organizado em células progressivas:

| Célula | Conteúdo |
|--------|----------|
| **Célula 1** | Instalação de dependências do sistema (`espeak-ng`, `ffmpeg`) |
| **Célula 2** | Instalação dos pacotes Python (coqui-tts, kokoro-onnx, piper-tts, jiwer, whisper etc.) |
| **Célula 3** | Verificação de versões (`transformers==4.57.1`, `huggingface-hub==0.36.0`) |
| **Célula 4** | Download dos modelos (Piper ONNX, Kokoro ONNX + voices; XTTS baixa ao carregar) |
| **Célula 5** | Imports e configuração inicial |
| **Célula 6** | Carregamento dos 3 modelos TTS + Whisper ASR |
| **Célula 7** | Funções de síntese (`run_piper`, `run_kokoro`, `run_xtts`) + teste rápido |
| **Célula 8** | Corpus de teste estruturado (14 categorias, 140 frases) |
| **Células 9+** | Benchmark completo, análise WER, gráficos, exportação de relatórios |

---

## 4. Executando o Notebook

1. **Execute as células em ordem** (de cima para baixo).
2. Use **Ctrl+Enter** para executar a célula atual, ou **Shift+Enter** para executar e avançar.
3. Alternativamente, use **Runtime > Executar tudo** para rodar todas as células de uma vez.

### ⚠️ Tempos Esperados

| Etapa | Tempo aproximado |
|-------|:---------------:|
| Instalação de dependências (Células 1-3) | 3-8 min |
| Download dos modelos (Célula 4) | 5-15 min (depende da internet) |
| Carregamento dos modelos (Célula 6) | 2-5 min |
| Benchmark completo (Células 9+) com 420 sínteses | 2-4 horas |

> **Atenção**: O benchmark completo é demorado em CPU (especialmente o XTTS v2, com ~42s por frase). Para testes rápidos, use apenas as primeiras categorias ou reduza o corpus.

---

## 5. Primeira Execução — Download de Modelos

Na primeira execução, os modelos são baixados automaticamente (~2,2 GB total):

| Modelo | Tamanho | Local de download |
|--------|:-------:|-------------------|
| XTTS v2 | ~1,8 GB | HuggingFace (automático via coqui-tts) |
| Piper `pt_BR-cadu-medium` | ~63 MB | HuggingFace rhasspy/piper-voices |
| Kokoro ONNX + voices | ~326 MB | GitHub thewh1teagle/kokoro-onnx |

Os arquivos são armazenados temporariamente no ambiente Colab. **Cada nova sessão faz o download novamente** (comportamento normal do Colab gratuito).

---

## 6. Interpretando os Outputs

### Durante a Síntese

```
[Piper] Frase: "Bom dia!" | Latência: 0.87s | WER: 0.0
[Kokoro] Frase: "Bom dia!" | Latência: 6.2s | WER: 0.0
[XTTS] Frase: "Bom dia!" | Latência: 38.5s | WER: 0.0
```

### Resultados Finais

O notebook gera:
- **Tabelas resumo** com WER médio e latência por modelo
- **Gráficos** de comparação (boxplots, barras)
- **CSV** com todos os resultados em `results/`
- **Relatório DOCX** formatado

---

## 7. Erros Comuns

| Erro | Solução |
|------|---------|
| `espeak-ng: command not found` | Execute a Célula 1 novamente |
| `CUDA out of memory` | Confirme que está usando CPU (Runtime > Alterar tipo de runtime) |
| `ModuleNotFoundError: No module named 'TTS'` | Execute a Célula 2 novamente e reinicie o runtime |
| Download interrompido | Execute a Célula 4 novamente |
| Sessão desconectada | Normal no Colab gratuito após inatividade — reconecte e re-execute a partir da Célula 5 |

---

## 8. Salvando os Resultados

Para não perder os resultados após o encerramento da sessão:

```python
# Montar o Google Drive (opcional)
from google.colab import drive
drive.mount('/content/drive')

# Copiar resultados para o Drive
import shutil
shutil.copytree('results/', '/content/drive/MyDrive/tts-resultados/')
```

Ou faça o download diretamente pelo painel de arquivos do Colab (ícone de pasta na barra lateral).
