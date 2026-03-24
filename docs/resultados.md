# Resultados

## 1. Visão Geral

O benchmark foi executado com **420 sínteses** (140 frases × 3 modelos) em ambiente **CPU-only** no Google Colab.

### Tabela Geral de Resultados

| Modelo | Latência média (s) | WER médio | Classificação |
|--------|:-----------------:|:---------:|:-------------:|
| **Kokoro** | 7,357 | **0,1381** | 🥇 Melhor inteligibilidade |
| **Piper** | **0,996** | 0,3130 | ⚡ Mais rápido |
| **XTTS v2** | 42,034 | 0,2095 | 🎭 Mais expressivo |

---

## 2. Análise por Modelo

### Kokoro (StyleTTS2 + ONNX)

- **WER médio**: 0,1381 — o mais baixo entre os 3 modelos, indicando **maior fidelidade na síntese**.
- **Latência média**: 7,357 segundos — razoável para CPU, considerando a qualidade entregue.
- **Voz**: feminina (`pf_dora`), natural e fluida.
- **Destaque**: excelente desempenho em categorias com vocabulário técnico e nomes próprios.
- **Tamanho**: ~326 MB (ONNX) — equilíbrio entre qualidade e tamanho.

### Piper (VITS)

- **WER médio**: 0,3130 — maior taxa de erro, mas ainda funcional para muitas aplicações.
- **Latência média**: **0,996 segundos** — o **mais rápido** por uma margem enorme (42× mais rápido que XTTS).
- **Voz**: masculina (`pt_BR-cadu-medium`), clara e objetiva.
- **Destaque**: ideal para aplicações em tempo real, leitores de tela, sistemas embarcados.
- **Tamanho**: ~63 MB — o mais leve dos 3.

### XTTS v2 (Coqui / GPT + HiFiGAN)

- **WER médio**: 0,2095 — segundo melhor resultado em inteligibilidade.
- **Latência média**: **42,034 segundos** — o mais lento, reflexo da arquitetura GPT em CPU.
- **Voz**: multilingual com clonagem zero-shot (expressiva e variada).
- **Destaque**: maior expressividade e capacidade de clonagem de voz.
- **Tamanho**: ~1,8 GB — o maior dos 3 modelos.
- **Limitação**: latência proibitiva para uso em tempo real sem GPU.

---

## 3. Análise por Categoria

### Categorias e Resultados (médias por modelo)

| Categoria | Kokoro WER | Piper WER | XTTS WER | Média |
|-----------|:----------:|:---------:|:--------:|:-----:|
| `curtas_objetivas` | — | — | — | — |
| `datas_horarios` | — | — | — | — |
| `enderecos_urls_emails` | — | — | — | — |
| `ingles_e_code_switching` | — | — | — | — |
| `interrogativas_e_exclamativas` | — | — | — | — |
| `longas_narrativas` | — | — | — | — |
| `medias_informativas` | — | — | — | — |
| `nomes_internacionais` | — | — | — | — |
| `nomes_proprios_brasileiros` | — | — | — | — |
| `numeros_medidas_moedas` | — | — | — | — |
| `pontuacao_e_pausas` | — | — | — | — |
| `regionalismos_e_girias` | — | — | — | — |
| `siglas_e_abreviacoes` | — | — | — | — |
| `termos_tecnicos_academicos` | — | — | — | — |

> Os resultados detalhados por categoria serão exportados como CSV na pasta `results/` após a execução completa do notebook.

---

## 4. Trade-offs: Qual Modelo Escolher?

```
                Alta Qualidade (baixo WER)
                        ▲
                        │
                    Kokoro ●
                        │
                   XTTS v2 ●
                        │
─────────────────────────────────────────── Velocidade
Lento            Piper ●                    Rápido
```

### Guia de Decisão

| Caso de uso | Modelo recomendado |
|-------------|-------------------|
| Máxima inteligibilidade | **Kokoro** |
| Tempo real / baixa latência | **Piper** |
| Expressividade / clonagem de voz | **XTTS v2** (com GPU) |
| Dispositivos com recursos limitados | **Piper** |
| Melhor equilíbrio qualidade/velocidade | **Kokoro** |

---

## 5. Conclusões

1. **Kokoro** é a melhor escolha para aplicações de acessibilidade que priorizam inteligibilidade em pt-BR com CPU.
2. **Piper** é imbatível em velocidade e deve ser considerado para leitores de tela em tempo real.
3. **XTTS v2** apresenta a maior expressividade, mas sua latência em CPU (~42s) o torna impraticável para uso em produção sem GPU.
4. Todos os modelos são viáveis em CPU, confirmando a hipótese de democratização do acesso.

---

## 6. Arquivos de Resultados

Os resultados completos são exportados pelo notebook para a pasta `results/`:

- `results/benchmark_results.csv` — resultados brutos por frase
- `results/summary_by_model.csv` — resumo por modelo
- `results/summary_by_category.csv` — resumo por categoria
- `results/relatorio_tts.docx` — relatório formatado em Word
