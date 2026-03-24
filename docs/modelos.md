# 🤖 Modelos TTS Avaliados

Documentação detalhada sobre cada modelo de Text-to-Speech (TTS) open source avaliado nesta pesquisa.

---

## 1. Coqui TTS / XTTS-v2

| Atributo | Detalhe |
|----------|---------|
| **Link Oficial** | [github.com/coqui-ai/TTS](https://github.com/coqui-ai/TTS) |
| **HuggingFace** | [huggingface.co/coqui/XTTS-v2](https://huggingface.co/coqui/XTTS-v2) |
| **Licença** | Coqui Public Model License 1.0 |
| **Arquitetura** | VITS + Transformer (XTTS) |
| **Suporte PT-BR** | ✅ Nativo |
| **Clonagem de Voz** | ✅ Sim (poucos segundos de áudio de referência) |
| **Uso Offline** | ✅ Sim |
| **GPU Recomendada** | ≥ 6 GB VRAM |

### Descrição

O **Coqui TTS** é uma das soluções open source de TTS mais completas disponíveis. O modelo **XTTS-v2** é capaz de:
- Síntese de voz de alta qualidade em múltiplos idiomas
- Clonagem de voz com apenas 3–6 segundos de áudio de referência
- Streaming de áudio em tempo real
- Suporte nativo ao português brasileiro

### Instalação

```bash
pip install TTS
```

### Exemplo de Uso

```python
from TTS.api import TTS

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
tts.tts_to_file(
    text="Olá! Este é um teste de síntese de voz em português brasileiro.",
    speaker_wav="referencia.wav",   # opcional: voz de referência para clonagem
    language="pt",
    file_path="saida.wav"
)
```

### ✅ Prós
- Qualidade de voz muito alta
- Suporte a clonagem de voz
- Comunidade ativa e bem documentada

### ❌ Contras
- Requer GPU com muita VRAM (≥ 6 GB)
- Tempo de carregamento inicial elevado
- Modelo grande (~2 GB)

---

## 2. Meta MMS (`facebook/mms-tts-por`)

| Atributo | Detalhe |
|----------|---------|
| **Link Oficial** | [huggingface.co/facebook/mms-tts-por](https://huggingface.co/facebook/mms-tts-por) |
| **Paper** | [arxiv.org/abs/2305.13516](https://arxiv.org/abs/2305.13516) |
| **Licença** | CC BY-NC 4.0 |
| **Arquitetura** | VITS |
| **Suporte PT-BR** | ✅ Nativo (português) |
| **Clonagem de Voz** | ⚠️ Parcial |
| **Uso Offline** | ✅ Sim |
| **GPU Recomendada** | ≥ 2 GB VRAM |

### Descrição

O **Meta MMS (Massively Multilingual Speech)** é um projeto da Meta AI que treinou modelos de TTS e ASR para mais de 1.100 idiomas, incluindo o português. É robusto e relativamente leve comparado ao XTTS.

### Instalação

```bash
pip install transformers torch
```

### Exemplo de Uso

```python
from transformers import VitsModel, AutoTokenizer
import torch
import scipy

model = VitsModel.from_pretrained("facebook/mms-tts-por")
tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-por")

texto = "Olá! Este é um teste de síntese de voz em português."
inputs = tokenizer(texto, return_tensors="pt")

with torch.no_grad():
    output = model(**inputs).waveform

scipy.io.wavfile.write("saida.wav", rate=model.config.sampling_rate, data=output.squeeze().numpy())
```

### ✅ Prós
- Leve e eficiente
- Fácil integração via HuggingFace Transformers
- Funciona bem em CPU

### ❌ Contras
- Qualidade inferior ao XTTS
- Sem clonagem de voz nativa
- Voz pode soar menos natural

---

## 3. Bark (`suno-ai/bark`)

| Atributo | Detalhe |
|----------|---------|
| **Link Oficial** | [github.com/suno-ai/bark](https://github.com/suno-ai/bark) |
| **HuggingFace** | [huggingface.co/suno/bark](https://huggingface.co/suno/bark) |
| **Licença** | MIT |
| **Arquitetura** | Transformer (GPT-like) |
| **Suporte PT-BR** | ✅ Suportado |
| **Clonagem de Voz** | ✅ Sim (voice presets) |
| **Uso Offline** | ✅ Sim |
| **GPU Recomendada** | ≥ 8 GB VRAM |

### Descrição

O **Bark** é um modelo generativo de voz da Suno AI, baseado em Transformers. É capaz de gerar fala com emoções, música de fundo, efeitos sonoros e ruídos não verbais (risos, suspiros, etc.). É o modelo mais criativo e expressivo da lista.

### Instalação

```bash
pip install bark
```

### Exemplo de Uso

```python
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

# Carrega modelos (primeira execução faz download)
preload_models()

texto = "Olá! [suspiro] Este é um teste com o Bark em português."
audio_array = generate_audio(texto)

write_wav("saida.wav", SAMPLE_RATE, audio_array)
```

### ✅ Prós
- Voz muito expressiva e natural
- Suporte a emoções, música e efeitos sonoros
- Licença MIT (uso livre)

### ❌ Contras
- Muito pesado (≥ 8 GB VRAM recomendado)
- Lento mesmo com GPU potente
- RTF geralmente > 1 (mais lento que tempo real)
- Resultados não são totalmente determinísticos

---

## 4. Piper

| Atributo | Detalhe |
|----------|---------|
| **Link Oficial** | [github.com/rhasspy/piper](https://github.com/rhasspy/piper) |
| **Licença** | MIT |
| **Arquitetura** | VITS |
| **Suporte PT-BR** | ✅ Sim (modelo específico) |
| **Clonagem de Voz** | ⚠️ Parcial (requer retreinamento) |
| **Uso Offline** | ✅ Sim |
| **GPU Recomendada** | Funciona bem em CPU |

### Descrição

O **Piper** é um sistema de TTS rápido e leve, projetado para funcionar eficientemente em dispositivos com recursos limitados (Raspberry Pi, sistemas embarcados). É ideal quando a velocidade e o baixo consumo de memória são prioridades.

### Instalação

```bash
pip install piper-tts
```

### Exemplo de Uso

```python
import wave
from piper.voice import PiperVoice

# Baixe o modelo em: https://huggingface.co/rhasspy/piper-voices/tree/main/pt/pt_BR
voice = PiperVoice.load("pt_BR-faber-medium.onnx")

with wave.open("saida.wav", "w") as wav_file:
    voice.synthesize("Olá, teste do Piper em português brasileiro.", wav_file)
```

### ✅ Prós
- Muito rápido (RTF < 0.1 em CPU)
- Baixo consumo de memória
- Funciona offline sem GPU

### ❌ Contras
- Qualidade inferior aos modelos mais pesados
- Opções de vozes em PT-BR mais limitadas
- Menos natural em frases complexas

---

## 5. gTTS (Google Text-to-Speech)

| Atributo | Detalhe |
|----------|---------|
| **Link Oficial** | [github.com/pndurette/gTTS](https://github.com/pndurette/gTTS) |
| **PyPI** | [pypi.org/project/gTTS](https://pypi.org/project/gTTS/) |
| **Licença** | MIT |
| **Arquitetura** | API Google (não open source) |
| **Suporte PT-BR** | ✅ `lang="pt"` |
| **Clonagem de Voz** | ❌ Não |
| **Uso Offline** | ❌ Requer internet |
| **GPU Recomendada** | Não necessária |

### Descrição

O **gTTS** é um wrapper Python para a API de Text-to-Speech do Google Translate. É a opção mais simples de implementar e produz voz com boa qualidade, mas depende de conexão com a internet e não é tecnicamente open source (usa serviço proprietário do Google).

### Instalação

```bash
pip install gTTS
```

### Exemplo de Uso

```python
from gtts import gTTS
import os

texto = "Olá! Este é um teste com o Google Text-to-Speech em português."
tts = gTTS(text=texto, lang="pt", slow=False)
tts.save("saida.mp3")
os.system("mpg123 saida.mp3")  # reproduz (Linux)
```

### ✅ Prós
- Extremamente simples de usar
- Boa qualidade de voz
- Suporte completo ao português brasileiro

### ❌ Contras
- Requer conexão com a internet
- Usa API proprietária (Google)
- Sem controle sobre velocidade/tom (limitado)
- Não funcional para uso offline

---

## 6. edge-tts (Microsoft Edge TTS)

| Atributo | Detalhe |
|----------|---------|
| **Link Oficial** | [github.com/rany2/edge-tts](https://github.com/rany2/edge-tts) |
| **PyPI** | [pypi.org/project/edge-tts](https://pypi.org/project/edge-tts/) |
| **Licença** | GPL-3.0 |
| **Arquitetura** | API Microsoft (não open source) |
| **Suporte PT-BR** | ✅ Vozes neurais brasileiras |
| **Clonagem de Voz** | ❌ Não |
| **Uso Offline** | ❌ Requer internet |
| **GPU Recomendada** | Não necessária |

### Descrição

O **edge-tts** é um wrapper Python não oficial para o serviço de TTS do Microsoft Edge. Oferece vozes neurais de alta qualidade em português brasileiro (ex: `pt-BR-FranciscaNeural`, `pt-BR-AntonioNeural`) sem custo adicional.

### Instalação

```bash
pip install edge-tts
```

### Exemplo de Uso

```python
import asyncio
import edge_tts

async def sintetizar():
    texto = "Olá! Este é um teste com o Microsoft Edge TTS em português brasileiro."
    communicator = edge_tts.Communicate(texto, voice="pt-BR-FranciscaNeural")
    await communicator.save("saida.mp3")

asyncio.run(sintetizar())
```

### Vozes Disponíveis em PT-BR

| Voz | Gênero | Estilo |
|-----|--------|--------|
| `pt-BR-FranciscaNeural` | Feminino | Geral |
| `pt-BR-AntonioNeural` | Masculino | Geral |

### ✅ Prós
- Vozes neurais de alta qualidade
- Sem necessidade de GPU
- Gratuito (sem chave de API)

### ❌ Contras
- Requer conexão com a internet
- Usa infraestrutura proprietária (Microsoft)
- Dependência de serviço de terceiros

---

## Comparativo Resumido

| Modelo | Qualidade | Velocidade | Offline | Facilidade | Custo de HW |
|--------|:---------:|:----------:|:-------:|:----------:|:-----------:|
| Coqui XTTS-v2 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ✅ | ⭐⭐⭐ | Alto |
| Meta MMS | ⭐⭐⭐ | ⭐⭐⭐⭐ | ✅ | ⭐⭐⭐⭐ | Médio |
| Bark | ⭐⭐⭐⭐ | ⭐⭐ | ✅ | ⭐⭐⭐ | Alto |
| Piper | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ | ⭐⭐⭐⭐ | Baixo |
| gTTS | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ❌ | ⭐⭐⭐⭐⭐ | Baixo |
| edge-tts | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ❌ | ⭐⭐⭐⭐⭐ | Baixo |
