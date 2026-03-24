# Modelos TTS Avaliados

Esta pesquisa avaliou **3 modelos open source** de Text-to-Speech com suporte nativo ao português brasileiro e funcionamento offline.

---

## 1. XTTS v2 — Coqui TTS

### Visão Geral

| Atributo | Detalhe |
|----------|---------|
| **Desenvolvedor** | Coqui AI |
| **Versão** | XTTS v2 (via `coqui-tts==0.27.3`) |
| **Arquitetura** | GPT + HiFiGAN |
| **Parâmetros** | ~500M |
| **Tamanho do modelo** | ~1,8 GB |
| **Licença** | [CPML](https://coqui.ai/cpml) (uso não-comercial) |
| **Suporte ao pt-BR** | Nativo (multilingual) |
| **Voz** | Multilingual + clonagem zero-shot |

### Características Técnicas

- **Arquitetura híbrida**: componente GPT para modelagem de linguagem + HiFiGAN como vocoder.
- **Clonagem zero-shot**: com um arquivo de referência de áudio, é possível sintetizar voz imitando o falante original.
- **Multilingual**: suporta mais de 17 idiomas, incluindo pt-BR nativamente.
- **Expressividade**: produz fala com prosódia natural e variações emocionais.

### Resultado na Pesquisa

- **Latência média**: 42,034 s (CPU)
- **WER médio**: 0,2095

### Como é Carregado no Notebook

```python
from TTS.api import TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
```

O modelo é baixado automaticamente do HuggingFace (~1,8 GB) na primeira execução.

### Referências

- [GitHub — Coqui TTS](https://github.com/coqui-ai/TTS)
- [HuggingFace — XTTS v2](https://huggingface.co/coqui/XTTS-v2)

---

## 2. Piper TTS

### Visão Geral

| Atributo | Detalhe |
|----------|---------|
| **Desenvolvedor** | Rhasspy / Michael Hansen |
| **Versão** | `piper-tts==1.4.1` |
| **Arquitetura** | VITS (Variational Inference with adversarial learning for end-to-end TTS) |
| **Tamanho do modelo** | ~63 MB (`pt_BR-cadu-medium`) |
| **Licença** | MIT |
| **Suporte ao pt-BR** | Nativo (modelo dedicado) |
| **Voz** | `pt_BR-cadu-medium` — masculina |

### Características Técnicas

- **VITS end-to-end**: gera áudio diretamente do texto sem vocoder separado.
- **Extremamente leve**: modelo de ~63 MB, ideal para dispositivos embarcados e IoT.
- **Projetado para offline**: sem dependências de rede, perfeito para aplicações de acessibilidade locais.
- **ONNX runtime**: exportado em formato ONNX para portabilidade máxima.
- **Sem GPU necessária**: otimizado para CPU.

### Resultado na Pesquisa

- **Latência média**: 0,996 s (CPU) — ⚡ mais rápido dos 3 modelos
- **WER médio**: 0,3130

### Como é Carregado no Notebook

```python
from piper import PiperVoice
voice = PiperVoice.load("pt_BR-cadu-medium.onnx", config_path="pt_BR-cadu-medium.onnx.json")
```

O modelo ONNX é baixado do repositório HuggingFace do Rhasspy.

### Referências

- [GitHub — Piper](https://github.com/rhasspy/piper)
- [HuggingFace — Piper Voices](https://huggingface.co/rhasspy/piper-voices)

---

## 3. Kokoro

### Visão Geral

| Atributo | Detalhe |
|----------|---------|
| **Desenvolvedor** | thewh1teagle / hexgrad |
| **Versão** | `kokoro-onnx` (latest) |
| **Arquitetura** | StyleTTS2 |
| **Parâmetros** | 82M |
| **Tamanho do modelo** | ~326 MB (ONNX + voices) |
| **Licença** | Apache 2.0 |
| **Suporte ao pt-BR** | Nativo |
| **Voz** | `pf_dora` — feminina |

### Características Técnicas

- **StyleTTS2**: arquitetura moderna que modela o estilo de fala como difusão adversarial, produzindo qualidade próxima à voz humana.
- **82M parâmetros**: leve o suficiente para execução eficiente em CPU via ONNX Runtime.
- **ONNX exportado**: portabilidade para múltiplas plataformas sem dependência de PyTorch em runtime.
- **Vozes separadas**: arquivo `voices-v1.0.bin` contém embeddings de múltiplos falantes.
- **Melhor qualidade**: WER mais baixo entre os 3 modelos testados.

### Resultado na Pesquisa

- **Latência média**: 7,357 s (CPU)
- **WER médio**: 0,1381 — 🥇 melhor inteligibilidade

### Como é Carregado no Notebook

```python
from kokoro_onnx import Kokoro
kokoro = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin")
```

Os arquivos ONNX e voices são baixados do GitHub/HuggingFace (~326 MB total).

### Referências

- [GitHub — kokoro-onnx](https://github.com/thewh1teagle/kokoro-onnx)
- [HuggingFace — Kokoro](https://huggingface.co/hexgrad/Kokoro-82M)

---

## Comparativo Técnico

| Característica | XTTS v2 | Piper | Kokoro |
|----------------|:-------:|:-----:|:------:|
| Arquitetura | GPT+HiFiGAN | VITS | StyleTTS2 |
| Tamanho | ~1,8 GB | ~63 MB | ~326 MB |
| Parâmetros | ~500M | ~30M | 82M |
| Formato | PyTorch | ONNX | ONNX |
| Latência CPU | ~42 s | ~1 s | ~7 s |
| WER médio | 0,2095 | 0,3130 | 0,1381 |
| GPU necessária | Não (mas recomendada) | Não | Não |
| Clonagem de voz | ✅ Zero-shot | ❌ | ❌ |
| Licença | CPML | MIT | Apache 2.0 |
