# 🗣️ TTS Acessibilidade PT-BR

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-xhoU_3Jg7MbrsmIES2Aezv0-_A90FT6)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red.svg)](https://github.com/renatoork/tts-acessibilidade-pt-br)
[![Acessibilidade](https://img.shields.io/badge/Acessibilidade-♿-green.svg)](https://github.com/renatoork/tts-acessibilidade-pt-br)

> **Pesquisa acadêmica** sobre avaliação de modelos open source de **Text-to-Speech (TTS)** com suporte ao **português brasileiro**, voltada à **acessibilidade de pessoas com deficiência visual**.

Este repositório reúne scripts reprodutíveis, documentação e resultados de experimentos com modelos TTS open source executados em ambiente Google Colab, com o objetivo de identificar as melhores soluções para apoiar o acesso à leitura por pessoas com deficiência visual.

---

## 🔬 Pergunta de Pesquisa

> *Como diferentes modelos open source de Text-to-Speech (TTS) com suporte ao português brasileiro podem ser aplicados e avaliados, por meio de scripts reprodutíveis em ambiente Google Colab (ou equivalente), para apoiar a acessibilidade de pessoas com deficiência visual no acesso à leitura, considerando critérios de qualidade da síntese de voz e de viabilidade técnica de execução?*

---

## 🎯 Objetivo Geral

Avaliar modelos open source de Text-to-Speech (TTS) com suporte ao português brasileiro, por meio de scripts reprodutíveis em ambiente Google Colab (ou equivalente), quanto à qualidade da síntese de voz e à viabilidade técnica de execução, visando apoiar o acesso à leitura por pessoas com deficiência visual.

Pretende-se iniciar esses testes no Google Colab e evidenciar como esses modelos podem ser utilizados nesse contexto, considerado de grande relevância e impacto para a sociedade. Além disso, propõe-se registrar todas as etapas do processo, de modo a permitir a continuidade do estudo e contribuir positivamente para a progressão de pesquisas futuras relacionadas ao uso de modelos de áudio voltados à acessibilidade.

---

## 📋 Objetivos Específicos

1. **Identificar e selecionar** modelos open source de TTS com suporte ao português brasileiro adequados para uso em ambientes gratuitos de experimentação, como o Google Colab.
2. **Implementar scripts reprodutíveis** em notebooks (Google Colab ou equivalente) para cada modelo selecionado, documentando o fluxo necessário para gerar síntese de fala a partir de textos em português.
3. **Definir e aplicar métricas** de avaliação da síntese de voz, contemplando aspectos de qualidade perceptiva (como naturalidade e inteligibilidade) e de desempenho técnico (como tempo de processamento e uso de recursos computacionais).
4. **Comparar os modelos** avaliados quanto ao equilíbrio entre qualidade da fala gerada e viabilidade de execução em cenários de baixo custo, com foco em aplicações de acessibilidade para pessoas com deficiência visual.
5. **Organizar e disponibilizar** a documentação dos scripts, configurações e resultados obtidos, de forma a facilitar a replicação dos experimentos e o aproveitamento dos achados em futuros estudos e implementações na área de tecnologia assistiva.

---

## 🤖 Modelos Avaliados

| Modelo | Link | Suporte PT-BR | Clonagem de Voz | Local/Offline |
|--------|------|:-------------:|:---------------:|:-------------:|
| **Coqui TTS / XTTS-v2** | [GitHub](https://github.com/coqui-ai/TTS) | ✅ | ✅ Sim | ✅ Sim |
| **Meta MMS** (`facebook/mms-tts-por`) | [HuggingFace](https://huggingface.co/facebook/mms-tts-por) | ✅ | ⚠️ Parcial | ✅ Sim |
| **Bark** (`suno-ai/bark`) | [GitHub](https://github.com/suno-ai/bark) | ✅ | ✅ Sim | ✅ Sim |
| **Piper** | [GitHub](https://github.com/rhasspy/piper) | ✅ | ⚠️ Parcial | ✅ Sim |
| **gTTS** | [PyPI](https://pypi.org/project/gTTS/) | ✅ | ❌ Não | ❌ Não |
| **edge-tts** | [PyPI](https://pypi.org/project/edge-tts/) | ✅ | ❌ Não | ❌ Não |

> 📖 Veja a documentação completa de cada modelo em [`docs/modelos.md`](docs/modelos.md)

---

## 📁 Estrutura do Repositório

```
tts-acessibilidade-pt-br/
│
├── 📓 notebooks/               # Notebooks Jupyter / Google Colab
│   ├── 01_gtts_basico.ipynb
│   ├── 02_edge_tts.ipynb
│   ├── 03_coqui_tts_xtts.ipynb
│   ├── 04_bark_tts.ipynb
│   ├── 05_meta_mms.ipynb
│   ├── 06_piper_tts.ipynb
│   ├── 07_comparativo_modelos.ipynb
│   └── README.md
│
├── 📊 docs/                    # Documentação técnica
│   ├── metricas.md             # Métricas de avaliação
│   ├── modelos.md              # Detalhes dos modelos TTS
│   └── setup_colab.md          # Guia de configuração do Colab
│
├── 🐍 scripts/                 # Scripts Python utilitários
│   ├── __init__.py
│   └── utils.py
│
├── 🎵 audio_samples/           # Amostras de áudio geradas (ver .gitignore)
│   └── README.md
│
├── 📈 results/                 # Resultados dos experimentos (CSVs, gráficos)
│   └── README.md
│
├── 📝 textos_teste/            # Frases de teste em português
│   ├── frases.txt
│   └── README.md
│
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 🚀 Como Usar

### Pré-requisitos

- Python 3.8 ou superior
- pip atualizado
- (Recomendado) GPU com CUDA para modelos mais pesados

### 1. Clonar o repositório

```bash
git clone https://github.com/renatoork/tts-acessibilidade-pt-br.git
cd tts-acessibilidade-pt-br
```

### 2. Criar ambiente virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
# ou
venv\Scripts\activate           # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar os notebooks

```bash
jupyter notebook notebooks/
```

Ou abra diretamente no **Google Colab** clicando no badge abaixo:

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-xhoU_3Jg7MbrsmIES2Aezv0-_A90FT6)

---

## ☁️ Google Colab

Os experimentos foram desenvolvidos e testados no Google Colab, que oferece acesso gratuito a GPUs.

🔗 **Notebook principal:** [Abrir no Google Colab](https://colab.research.google.com/drive/1-xhoU_3Jg7MbrsmIES2Aezv0-_A90FT6)

Para instruções detalhadas de configuração do ambiente Colab, consulte [`docs/setup_colab.md`](docs/setup_colab.md).

---

## 📊 Métricas de Avaliação

Os modelos são avaliados segundo os seguintes critérios:

| Métrica | Descrição | Peso Sugerido |
|---------|-----------|:-------------:|
| **MOS** (Mean Opinion Score) | Qualidade perceptiva geral (escala 1–5) | Alto |
| **Naturalidade** | Quão natural soa a voz sintética | Alto |
| **Inteligibilidade** | % de palavras corretamente compreendidas | Alto |
| **RTF** (Real-Time Factor) | Tempo de síntese / duração do áudio | Médio |
| **Uso de GPU/RAM** | Consumo de memória durante a inferência | Médio |
| **Latência** | Tempo até iniciar a reprodução do áudio | Médio |

> 📖 Detalhamento completo em [`docs/metricas.md`](docs/metricas.md)

---

## 📈 Resultados

> 🔬 *Seção em construção — resultados serão adicionados conforme os experimentos forem concluídos.*

Os resultados comparativos dos modelos serão publicados na pasta [`results/`](results/) no formato de tabelas CSV e gráficos.

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Se você tem interesse em pesquisa de TTS, acessibilidade ou quiser adicionar um novo modelo, consulte o guia [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## 📄 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE) — sinta-se livre para usar, modificar e distribuir.

---

## 📚 Referências

- [Coqui TTS](https://github.com/coqui-ai/TTS) — TTS open source de alta qualidade
- [Meta MMS](https://huggingface.co/facebook/mms-tts-por) — Massively Multilingual Speech da Meta
- [Bark](https://github.com/suno-ai/bark) — Modelo generativo de voz da Suno AI
- [Piper](https://github.com/rhasspy/piper) — TTS rápido e leve para dispositivos embarcados
- [gTTS](https://github.com/pndurette/gTTS) — Google Text-to-Speech wrapper
- [edge-tts](https://github.com/rany2/edge-tts) — Microsoft Edge TTS wrapper
- [VITS Paper](https://arxiv.org/abs/2106.06103) — Conditional Variational Autoencoder with Adversarial Learning
- [HuggingFace TTS](https://huggingface.co/models?pipeline_tag=text-to-speech) — Hub de modelos TTS

---

## 👤 Autor

**@renatoork**

- GitHub: [@renatoork](https://github.com/renatoork)

---

## 🙏 Agradecimentos

- À comunidade **open source** pelos modelos e ferramentas disponibilizados gratuitamente
- À equipe do **Coqui TTS**, **Meta AI**, **Suno AI** e **Rhasspy** pelo excelente trabalho
- Ao **Google Colab** por tornar experimentos de IA acessíveis a pesquisadores sem hardware dedicado
- A todos os contribuidores que acreditam na **tecnologia como ferramenta de acessibilidade**

---

<p align="center">
  Feito com ❤️ para a acessibilidade 
  <br>
  <a href="https://colab.research.google.com/drive/1-xhoU_3Jg7MbrsmIES2Aezv0-_A90FT6">🔗 Abrir no Google Colab</a>
</p>
