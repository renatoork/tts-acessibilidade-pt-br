# 🗣️ TTS Acessibilidade PT-BR — Avaliação Comparativa de Modelos Open Source

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-xhoU_3Jg7MbrsmIES2Aezv0-_A90FT6)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red.svg)](https://github.com/renatoork/tts-acessibilidade-pt-br)

Pesquisa acadêmica que compara **3 modelos TTS open source** (XTTS v2, Piper e Kokoro) com suporte offline ao português brasileiro, avaliados por **WER** (Word Error Rate via Whisper ASR) e **latência em CPU**, visando apoiar a **acessibilidade de pessoas com deficiência visual**.

---

## 📋 Pergunta de Pesquisa

> Como diferentes modelos open source de Text-to-Speech (TTS) com suporte ao português brasileiro podem ser aplicados e avaliados, por meio de scripts reprodutíveis em ambiente Google Colab (ou equivalente), para apoiar a acessibilidade de pessoas com deficiência visual no acesso à leitura, considerando critérios de qualidade da síntese de voz e de viabilidade técnica de execução?

---

## 🎯 Objetivo Geral

Avaliar modelos open source de TTS com suporte ao português brasileiro, por meio de scripts reprodutíveis em Google Colab, quanto à **qualidade da síntese de voz** e **viabilidade técnica**, visando apoiar o acesso à leitura por pessoas com deficiência visual.

### Objetivos Específicos

1. **Identificar e selecionar** modelos open source de TTS com suporte ao português brasileiro adequados para uso em ambientes gratuitos de experimentação, como o Google Colab.
2. **Implementar scripts reprodutíveis** em notebooks (Google Colab ou equivalente) para cada modelo selecionado, documentando o fluxo necessário para gerar síntese de fala a partir de textos em português.
3. **Definir e aplicar métricas** de avaliação da síntese de voz, contemplando aspectos de qualidade (inteligibilidade via WER) e desempenho técnico (latência de CPU).
4. **Comparar os modelos** avaliados quanto ao equilíbrio entre qualidade da fala gerada e viabilidade de execução em cenários de baixo custo, com foco em aplicações de acessibilidade para pessoas com deficiência visual.
5. **Organizar e disponibilizar** a documentação dos scripts, configurações e resultados obtidos, de forma a facilitar a replicação dos experimentos e o aproveitamento dos achados em futuros estudos na área de tecnologia assistiva.

---

## 🤖 Modelos Avaliados

Foram testados **3 modelos open source** com suporte nativo offline ao português brasileiro. Modelos como gTTS, edge-tts, Bark e MMS não foram incluídos devido a restrições de tempo e/ou ausência de suporte offline adequado ao pt-BR.

| Modelo | Arquitetura | Tamanho | Voz (pt-BR) | Licença |
|--------|-------------|---------|-------------|---------|
| **XTTS v2** (Coqui) | GPT + HiFiGAN | ~1.8 GB | Multilingual + clonagem zero-shot | CPML |
| **Piper** | VITS | ~63 MB | `pt_BR-cadu-medium` (masculina) | MIT |
| **Kokoro** | StyleTTS2 (82M params) | ~326 MB (ONNX) | `pf_dora` (feminina) | Apache 2.0 |

---

## 📚 Corpus de Teste

O corpus foi estruturado em **14 categorias** com **10 frases cada**, totalizando **140 frases** e **420 sínteses** (140 frases × 3 modelos).

| # | Categoria | Quantidade | Média de Palavras |
|---|-----------|:----------:|:-----------------:|
| 0 | `curtas_objetivas` | 10 | 3,9 |
| 1 | `datas_horarios` | 10 | 12,1 |
| 2 | `enderecos_urls_emails` | 10 | 9,1 |
| 3 | `ingles_e_code_switching` | 10 | 9,6 |
| 4 | `interrogativas_e_exclamativas` | 10 | 8,7 |
| 5 | `longas_narrativas` | 10 | 28,2 |
| 6 | `medias_informativas` | 10 | 13,0 |
| 7 | `nomes_internacionais` | 10 | 8,3 |
| 8 | `nomes_proprios_brasileiros` | 10 | 7,9 |
| 9 | `numeros_medidas_moedas` | 10 | 9,9 |
| 10 | `pontuacao_e_pausas` | 10 | 8,8 |
| 11 | `regionalismos_e_girias` | 10 | 8,6 |
| 12 | `siglas_e_abreviacoes` | 10 | 9,9 |
| 13 | `termos_tecnicos_academicos` | 10 | 11,4 |
| **Total** | | **140** | — |

---

## 📊 Métricas de Avaliação

- **WER (Word Error Rate)**: calculado via transcrição automática com OpenAI Whisper (`base`) e comparação com o texto original usando a biblioteca `jiwer`. Menor WER = melhor inteligibilidade.
- **Latência (s)**: tempo de CPU necessário para sintetizar cada frase. Medido em ambiente **CPU-only** (sem GPU) para garantir reprodutibilidade democrática — qualquer pessoa com uma conta gratuita no Google Colab pode reproduzir os experimentos.

> **Por que CPU e não GPU?** O objetivo é democratizar o acesso: qualquer pessoa com uma conta Google pode reproduzir estes experimentos sem custo adicional.

---

## 🏆 Resultados

| Modelo | Latência média (s) | WER médio | Destaque |
|--------|:-----------------:|:---------:|----------|
| **Kokoro** | 7,357 | **0,1381** | ✅ Melhor inteligibilidade |
| **Piper** | **0,996** | 0,3130 | ✅ Mais rápido |
| **XTTS v2** | 42,034 | 0,2095 | Mais expressivo, porém mais lento |

**Análise:**
- 🥇 **Kokoro** apresentou o melhor WER (0,1381), indicando maior fidelidade na síntese de fala.
- ⚡ **Piper** foi o mais rápido (~1s por frase), ideal para aplicações em tempo real.
- 🎭 **XTTS v2** é o mais expressivo com clonagem zero-shot, mas apresentou a maior latência em CPU (~42s).

Para análise detalhada por categoria, veja [`docs/resultados.md`](docs/resultados.md).

---

## 🗂️ Estrutura do Repositório

```
tts-acessibilidade-pt-br/
├── modelscompare_v5_1903-2.ipynb  ← Notebook principal da pesquisa
├── requirements.txt                ← Dependências Python
├── .gitignore
├── LICENSE
├── README.md
├── CONTRIBUTING.md
├── docs/
│   ├── metodologia.md              ← Metodologia detalhada
│   ├── modelos.md                  ← Detalhes dos 3 modelos
│   ├── resultados.md               ← Análise completa dos resultados
│   └── setup_colab.md              ← Guia de execução no Colab
├── results/
│   └── README.md                   ← Placeholder para CSVs e gráficos
└── audio_samples/
    └── README.md                   ← Placeholder para amostras de áudio
```

---

## 🚀 Como Reproduzir

### Opção 1: Google Colab (Recomendado)

1. Acesse o notebook diretamente: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-xhoU_3Jg7MbrsmIES2Aezv0-_A90FT6)
2. **NÃO é necessário GPU** — use o runtime padrão (CPU)
3. Execute as células em ordem
4. A primeira execução baixa ~2,2 GB de modelos (XTTS v2, Piper, Kokoro)

Para mais detalhes, veja o guia [`docs/setup_colab.md`](docs/setup_colab.md).

### Opção 2: Execução Local

```bash
# Pré-requisitos do sistema
sudo apt-get install espeak-ng ffmpeg

# Clone o repositório
git clone https://github.com/renatoork/tts-acessibilidade-pt-br.git
cd tts-acessibilidade-pt-br

# Instale as dependências Python
pip install -r requirements.txt

# Abra o notebook
jupyter notebook modelscompare_v5_1903-2.ipynb
```

> ⚠️ **Atenção**: A execução local requer ~4 GB de RAM e ~3 GB de espaço em disco para os modelos.

---

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologia |
|-----------|-----------|
| Linguagem | Python 3.12+ |
| Deep Learning | PyTorch |
| TTS — XTTS v2 | [Coqui TTS](https://github.com/coqui-ai/TTS) 0.27.3 |
| TTS — Piper | [Piper TTS](https://github.com/rhasspy/piper) 1.4.1 |
| TTS — Kokoro | [Kokoro ONNX](https://github.com/thewh1teagle/kokoro-onnx) |
| ASR (WER) | [OpenAI Whisper](https://github.com/openai/whisper) (`base`) |
| Métricas WER | [jiwer](https://github.com/jitsi/jiwer) 3.0.4 |
| Áudio | soundfile 0.13.1 |
| Análise | Pandas, Matplotlib |
| Ambiente | Google Colab (CPU) |

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE) — Copyright 2026 Renato Arruda.

> **Atenção sobre licenças dos modelos:**
> - XTTS v2 usa a licença **CPML** (restrições para uso comercial)
> - Piper usa licença **MIT**
> - Kokoro usa licença **Apache 2.0**

---

## 👤 Autor
**Rafael Soares** - [@RafaelSoares19](https://github.com/RafaelSoares19)
**Raphael Henrique** - [@RHSantos08](https://github.com/RHSantos08)
**Renato Arruda** — [@renatoork](https://github.com/renatoork)

---

## 📚 Referências

- [Coqui TTS — GitHub](https://github.com/coqui-ai/TTS)
- [Piper TTS — GitHub](https://github.com/rhasspy/piper)
- [Kokoro ONNX — GitHub](https://github.com/thewh1teagle/kokoro-onnx)
- [OpenAI Whisper — GitHub](https://github.com/openai/whisper)
- [XTTS v2 — HuggingFace](https://huggingface.co/coqui/XTTS-v2)
- [Piper pt_BR-cadu-medium — HuggingFace](https://huggingface.co/rhasspy/piper-voices)
- [jiwer — Métricas WER](https://github.com/jitsi/jiwer)
- [Notebook no Google Colab](https://colab.research.google.com/drive/1-xhoU_3Jg7MbrsmIES2Aezv0-_A90FT6)
