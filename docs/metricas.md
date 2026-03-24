# 📊 Métricas de Avaliação de TTS

Este documento descreve as métricas utilizadas para avaliar e comparar os modelos de Text-to-Speech (TTS) nesta pesquisa.

---

## 1. MOS — Mean Opinion Score

### O que é

O **MOS (Mean Opinion Score)** é a métrica mais tradicional para avaliar a qualidade perceptiva de voz sintética. Consiste em avaliações subjetivas realizadas por ouvintes humanos.

### Escala

| Pontuação | Qualidade | Nível de Distorção |
|:---------:|-----------|-------------------|
| **5** | Excelente | Imperceptível |
| **4** | Bom | Ligeiramente perceptível, mas não incômodo |
| **3** | Regular | Perceptível e levemente incômodo |
| **2** | Ruim | Incômodo |
| **1** | Péssimo | Muito incômodo |

### Como Aplicar

1. Selecionar um conjunto de frases de teste (ver `textos_teste/frases.txt`)
2. Gerar o áudio com cada modelo
3. Apresentar os áudios a um grupo de ouvintes (mínimo 10 para validade estatística)
4. Solicitar que avaliem em escala de 1 a 5
5. Calcular a média das avaliações

> 📝 **Nota:** Para este estudo, pode-se usar avaliação qualitativa individual quando não houver grupo disponível, indicando a subjetividade da análise.

---

## 2. Inteligibilidade

### O que é

A **inteligibilidade** mede o percentual de palavras ou frases que um ouvinte consegue compreender corretamente a partir do áudio sintetizado.

### Como Calcular

```
Inteligibilidade (%) = (Palavras corretamente compreendidas / Total de palavras) × 100
```

### Como Aplicar

1. Sintetizar frases de teste com o modelo
2. Reproduzir o áudio para ouvintes sem mostrar o texto original
3. Solicitar que transcrevam o que ouviram
4. Comparar a transcrição com o texto original

### Referência

- **≥ 95%**: Excelente inteligibilidade
- **80–94%**: Boa inteligibilidade
- **60–79%**: Inteligibilidade moderada
- **< 60%**: Inteligibilidade baixa — inadequado para acessibilidade

---

## 3. Naturalidade

### O que é

A **naturalidade** avalia subjetivamente o quão próxima de uma voz humana real soa a voz sintética. Considera prosódia, ritmo, entonação e pausas.

### Aspectos Avaliados

| Aspecto | Descrição |
|---------|-----------|
| **Prosódia** | Variação natural de tom e ritmo |
| **Entonação** | Curvas de melodia da fala |
| **Pausas** | Pausas naturais entre frases e cláusulas |
| **Velocidade** | Taxa de fala confortável |
| **Sotaque** | Aproximação ao português brasileiro |

### Escala

Utiliza-se a mesma escala MOS (1–5), porém focada exclusivamente na naturalidade da voz, não na qualidade técnica geral.

---

## 4. RTF — Real-Time Factor

### O que é

O **RTF (Real-Time Factor)** mede a eficiência computacional do modelo, comparando o tempo necessário para sintetizar o áudio com a duração do áudio gerado.

### Fórmula

```
RTF = Tempo de síntese (s) / Duração do áudio gerado (s)
```

### Interpretação

| RTF | Interpretação |
|-----|---------------|
| **RTF < 1** | Síntese em tempo real (mais rápido que o áudio) ✅ |
| **RTF = 1** | Síntese em tempo real exato |
| **RTF > 1** | Síntese mais lenta que o tempo real ⚠️ |

### Exemplo

Se um modelo leva **2 segundos** para sintetizar um áudio de **5 segundos**:
```
RTF = 2 / 5 = 0,4  →  Excelente (mais rápido que o tempo real)
```

---

## 5. Uso de Recursos Computacionais

### GPU (VRAM)

Medição do uso de memória de vídeo durante a inferência do modelo.

```python
# Exemplo de coleta (NVIDIA)
import torch
vram_usada = torch.cuda.memory_allocated() / 1024**3  # GB
```

### RAM (Memória do Sistema)

Medição do uso de memória RAM durante a inferência.

```python
import psutil
ram_usada = psutil.virtual_memory().used / 1024**3  # GB
```

### Categorias de Hardware

| Categoria | GPU VRAM | Modelos Compatíveis |
|-----------|:--------:|---------------------|
| **Leve** | < 2 GB | gTTS, edge-tts, Piper |
| **Médio** | 2–6 GB | Meta MMS |
| **Pesado** | > 6 GB | Coqui XTTS-v2, Bark |

---

## 6. Tempo de Processamento (Latência)

### O que é

A **latência** mede o tempo decorrido desde a requisição de síntese até o início da reprodução do áudio. É um fator crítico para aplicações de acessibilidade em tempo real.

### Como Medir

```python
import time

inicio = time.time()
audio = modelo.sintetizar(texto)
fim = time.time()

latencia = fim - inicio  # em segundos
```

### Referência

| Latência | Avaliação |
|----------|-----------|
| **< 1s** | Excelente para uso em tempo real |
| **1–3s** | Adequado para a maioria dos casos |
| **3–10s** | Aceitável para leitura de textos longos |
| **> 10s** | Inadequado para uso interativo |

---

## 7. Tabela de Critérios e Pesos

Tabela resumida com os critérios e pesos sugeridos para a avaliação comparativa dos modelos:

| Critério | Peso | Justificativa |
|----------|:----:|---------------|
| **MOS / Qualidade Geral** | 25% | Principal indicador de experiência do usuário |
| **Naturalidade** | 20% | Essencial para uso prolongado (leitura de livros) |
| **Inteligibilidade** | 25% | Crítico para acessibilidade — o usuário precisa entender |
| **RTF** | 10% | Eficiência computacional |
| **Latência** | 10% | Tempo de resposta para o usuário |
| **Uso de GPU/RAM** | 10% | Viabilidade em hardware limitado (Colab gratuito) |

> 💡 **Nota:** Os pesos são sugestões para a análise comparativa e podem ser ajustados conforme o foco da avaliação.

---

## 8. Ferramentas e Bibliotecas

| Ferramenta | Uso |
|-----------|-----|
| `time` | Medição de tempo de processamento |
| `psutil` | Monitoramento de RAM |
| `torch.cuda` | Monitoramento de VRAM (GPU NVIDIA) |
| `librosa` | Análise de áudio |
| `soundfile` | Leitura/escrita de arquivos de áudio |
| `pandas` | Organização dos resultados em tabelas |
| `matplotlib` | Geração de gráficos comparativos |

---

## Referências

- ITU-T Recommendation P.800 — Methods for subjective determination of transmission quality
- [VITS Paper](https://arxiv.org/abs/2106.06103) — Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech
- [librosa Documentation](https://librosa.org/doc/latest/index.html)
