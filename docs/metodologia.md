# Metodologia

## 1. Seleção dos Modelos

### Critérios de Seleção

Para esta pesquisa, foram adotados os seguintes critérios de seleção dos modelos TTS:

1. **Suporte nativo ao português brasileiro** — o modelo deve ser capaz de sintetizar pt-BR sem necessitar de adaptações externas.
2. **Funcionamento offline** — o modelo deve rodar localmente, sem depender de APIs externas, garantindo privacidade e reprodutibilidade.
3. **Open source** — código e pesos disponíveis publicamente.
4. **Viabilidade em CPU** — deve ser possível executar em ambiente Google Colab gratuito (sem GPU).

### Modelos Selecionados

Com base nesses critérios, foram selecionados **3 modelos**:

| Modelo | Justificativa |
|--------|---------------|
| **XTTS v2** (Coqui) | Modelo multilingual de alta qualidade com clonagem zero-shot; suporte nativo ao pt-BR |
| **Piper** | Modelo VITS extremamente leve (~63 MB), projetado para execução offline em dispositivos com recursos limitados |
| **Kokoro** | Modelo moderno baseado em StyleTTS2, exportado em ONNX (~326 MB), com excelente qualidade para pt-BR |

### Modelos Não Testados e Justificativas

Os modelos a seguir foram considerados, mas **não incluídos** nesta pesquisa:

- **gTTS (Google TTS)**: depende de API online, não funciona offline — viola o critério de independência de conectividade.
- **edge-tts (Microsoft)**: também depende de API online.
- **Bark (Suno AI)**: exige GPU para tempo de síntese razoável; inviável em CPU no escopo deste estudo.
- **MMS (Meta)**: suporte ao pt-BR incompleto e setup complexo no período de realização dos testes.

> **Nota**: As exclusões se devem principalmente a restrições de tempo e às limitações de ambiente (CPU only). Esses modelos podem ser objeto de estudos futuros.

---

## 2. Corpus de Teste

### Estrutura

O corpus foi construído para cobrir a diversidade linguística do português brasileiro em contextos reais de uso por pessoas com deficiência visual. São **140 frases** organizadas em **14 categorias** com **10 frases cada**.

| # | Categoria | Descrição | Média de Palavras |
|---|-----------|-----------|:-----------------:|
| 0 | `curtas_objetivas` | Frases curtas do cotidiano | 3,9 |
| 1 | `datas_horarios` | Expressões temporais, dias e horas | 12,1 |
| 2 | `enderecos_urls_emails` | Endereços físicos, URLs e e-mails | 9,1 |
| 3 | `ingles_e_code_switching` | Termos em inglês intercalados no discurso | 9,6 |
| 4 | `interrogativas_e_exclamativas` | Perguntas e exclamações | 8,7 |
| 5 | `longas_narrativas` | Frases longas e descritivas | 28,2 |
| 6 | `medias_informativas` | Frases informativas de tamanho médio | 13,0 |
| 7 | `nomes_internacionais` | Nomes próprios estrangeiros | 8,3 |
| 8 | `nomes_proprios_brasileiros` | Nomes próprios brasileiros | 7,9 |
| 9 | `numeros_medidas_moedas` | Números, unidades e valores monetários | 9,9 |
| 10 | `pontuacao_e_pausas` | Frases com pontuação variada e pausas | 8,8 |
| 11 | `regionalismos_e_girias` | Expressões regionais e gírias do pt-BR | 8,6 |
| 12 | `siglas_e_abreviacoes` | Siglas e abreviações comuns | 9,9 |
| 13 | `termos_tecnicos_academicos` | Vocabulário técnico e acadêmico | 11,4 |

**Total**: 140 frases × 3 modelos = **420 sínteses**

### Critérios de Composição

- Cada frase foi elaborada para testar aspectos específicos da síntese de voz.
- As categorias cobrem desde vocabulário simples até estruturas linguísticas mais complexas.
- A diversidade temática reflete casos de uso reais para pessoas com deficiência visual (leitura de notícias, documentos, e-mails, navegação na web etc.).

---

## 3. Métricas de Avaliação

### WER — Word Error Rate

O **WER** mede a taxa de erro por palavra entre o texto sintetizado (após transcrição automática) e o texto original:

```
WER = (S + D + I) / N
```

Onde:
- **S** = substituições
- **D** = deleções
- **I** = inserções
- **N** = total de palavras no texto de referência

**Pipeline de cálculo**:
1. Síntese do texto pelo modelo TTS → arquivo WAV
2. Transcrição do WAV pelo **OpenAI Whisper** (`base`)
3. Comparação entre transcrição e texto original via biblioteca **jiwer**

> Menor WER = melhor inteligibilidade da síntese.

### Latência (tempo de CPU)

Medido em segundos, representa o tempo total de processamento para sintetizar cada frase em **CPU pura** (sem aceleração GPU).

```python
import time
inicio = time.time()
# síntese da frase...
latencia = time.time() - inicio
```

---

## 4. Por que CPU e não GPU?

A execução em **CPU** foi uma escolha intencional e alinhada ao objetivo de democratização:

- O Google Colab gratuito **não garante** acesso a GPU — sessões com GPU têm tempo limitado e fila de espera.
- Qualquer pessoa com uma conta Google pode reproduzir este experimento **gratuitamente e sem restrições**.
- Reflete o cenário real de muitos desenvolvedores e pesquisadores em contextos de baixo recurso.
- Permite avaliar a **viabilidade real** dos modelos para implementações em dispositivos como Raspberry Pi, computadores de entrada ou servidores sem GPU.

---

## 5. Pipeline de Avaliação

```
Texto de entrada (corpus)
        │
        ▼
┌───────────────────┐
│  Modelo TTS       │  (Piper / Kokoro / XTTS v2)
│  síntese em CPU   │
└───────────────────┘
        │
        ▼ WAV (áudio sintetizado)
┌───────────────────┐
│  OpenAI Whisper   │  transcrição automática (modelo base)
│  (ASR)            │
└───────────────────┘
        │
        ▼ Texto transcrito
┌───────────────────┐
│  jiwer            │  cálculo de WER
│  (métricas)       │
└───────────────────┘
        │
        ▼
   WER + Latência → Análise e Gráficos (Pandas, Matplotlib)
```

---

## 6. Ambiente de Execução

| Componente | Detalhe |
|------------|---------|
| Plataforma | Google Colab |
| Tipo de runtime | CPU (sem GPU) |
| Python | 3.12 |
| Sistema operacional | Ubuntu (Colab padrão) |
| Dependências do sistema | `espeak-ng`, `ffmpeg` |
| Framework de áudio | `soundfile` 0.13.1 |
| ASR | OpenAI Whisper `base` |
| Métricas | `jiwer` 3.0.4 |
