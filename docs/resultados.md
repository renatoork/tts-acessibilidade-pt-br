# Resultados

## 1. Visão Geral

O benchmark foi executado com **420 sínteses** (140 frases × 3 modelos) em ambiente **CPU-only** no Google Colab.

### Tabela Geral de Resultados

| Modelo | Latência média (s) | WER médio | Classificação |
|--------|:-----------------:|:---------:|:-------------:|
| **Kokoro** | 4,282 | **0,1767** | 🥇 Melhor inteligibilidade |
| **Piper** | **0,554** | 0,1848 | ⚡ Mais rápido |
| **XTTS v2** | 25,883 | 0,2078 | 🎭 Mais expressivo |

---

## 2. Análise por Modelo

### Kokoro (StyleTTS2 + ONNX)

- **WER médio**: 0,1767 — o mais baixo entre os 3 modelos, indicando **maior fidelidade na síntese**.
- **Latência média**: 4,282 segundos — razoável para CPU, considerando a qualidade entregue.
- **Voz**: feminina (`pf_dora`), natural e fluida.
- **Destaque**: excelente desempenho em categorias com vocabulário técnico e nomes próprios.
- **Tamanho**: ~326 MB (ONNX) — equilíbrio entre qualidade e tamanho.

### Piper (VITS)

- **WER médio**: 0,1848 — taxa de erro próxima ao Kokoro e funcional para diversas aplicações.
- **Latência média**: **0,554 segundos** — o **mais rápido** por uma margem enorme (~46× mais rápido que XTTS).
- **Voz**: masculina (`pt_BR-cadu-medium`), clara e objetiva.
- **Destaque**: ideal para aplicações em tempo real, leitores de tela, sistemas embarcados.
- **Tamanho**: ~63 MB — o mais leve dos 3.

### XTTS v2 (Coqui / GPT + HiFiGAN)

- **WER médio**: 0,2078 — o maior WER entre os três modelos no ambiente CPU-only.
- **Latência média**: **25,883 segundos** — o mais lento, reflexo da arquitetura GPT em CPU.
- **Voz**: multilingual com clonagem zero-shot (expressiva e variada).
- **Destaque**: maior expressividade e capacidade de clonagem de voz.
- **Tamanho**: ~1,8 GB — o maior dos 3 modelos.
- **Limitação**: latência proibitiva para uso em tempo real sem GPU.

---

## 3. Análise por Categoria

### Categorias e Resultados (médias por modelo)

| Categoria | Kokoro WER | Piper WER | XTTS WER | Média |
|-----------|:----------:|:---------:|:--------:|:-----:|
| `curtas_objetivas` | 0,1033 | 0,1083 | 0,1833 | 0,1317 |
| `datas_horarios` | 0,0688 | 0,1142 | 0,1527 | 0,1119 |
| `enderecos_urls_emails` | 0,5079 | 0,3306 | 0,4219 | 0,4202 |
| `ingles_e_code_switching` | 0,1701 | 0,2614 | 0,2151 | 0,2155 |
| `interrogativas_e_exclamativas` | 0,1619 | 0,1355 | 0,1567 | 0,1514 |
| `longas_narrativas` | 0,0467 | 0,1036 | 0,0740 | 0,0748 |
| `medias_informativas` | 0,0357 | 0,0874 | 0,1506 | 0,0912 |
| `nomes_internacionais` | 0,3970 | 0,5089 | 0,3190 | 0,4083 |
| `nomes_proprios_brasileiros` | 0,1369 | 0,2236 | 0,2694 | 0,2100 |
| `numeros_medidas_moedas` | 0,1968 | 0,1104 | 0,1879 | 0,1650 |
| `pontuacao_e_pausas` | 0,2354 | 0,1938 | 0,1786 | 0,2026 |
| `regionalismos_e_girias` | 0,1163 | 0,0889 | 0,1898 | 0,1317 |
| `siglas_e_abreviacoes` | 0,1521 | 0,1699 | 0,2186 | 0,1802 |
| `termos_tecnicos_academicos` | 0,1451 | 0,1503 | 0,1918 | 0,1624 |

> Dados extraídos diretamente do arquivo `results/resumo_por_modelo_categoria.csv`.

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

---

## 7. Análises Avançadas

O notebook `notebooks/analise_avancada.ipynb` expande a análise com métricas derivadas,
testes estatísticos e visualizações avançadas — tudo calculado a partir do CSV existente,
**sem necessidade de reexecutar o benchmark**.

### Novas Métricas Calculadas

| Métrica | Descrição |
|---|---|
| **Throughput (char/s)** | Caracteres sintetizados por segundo (`len(texto) / latência`) |
| **CER** | Character Error Rate via `jiwer.cer()` |
| **WER zero (%)** | Percentual de frases com acerto perfeito (WER = 0) |
| **Log Latência** | `log1p(latência)` para visualizações em escala logarítmica |

### Testes Estatísticos Disponíveis

- **Kruskal-Wallis** para WER e Latência entre os 3 modelos
- **Teste post-hoc de Dunn** (Bonferroni) para comparação par-a-par: Piper×Kokoro, Kokoro×XTTS, Piper×XTTS
- **Correlação de Spearman** entre NumPalavras e WER por modelo

### Novos Arquivos Gerados

**CSVs expandidos** (pasta `results/`):
- `results/resultados_expandidos.csv` — DataFrame completo com as novas colunas
- `results/estatisticas_descritivas.csv` — tabela completa de estatísticas por modelo
- `results/testes_estatisticos.csv` — resultados de todos os testes estatísticos
- `results/ranking_por_categoria.csv` — vencedor por categoria em WER e Latência
- `results/analise_erros.csv` — contagem de substituições, deleções e inserções por modelo

**Gráficos** (pasta `results/`):
- `results/scatter_wer_vs_latencia.png` — dispersão WER × Latência (tamanho ∝ NumPalavras)
- `results/violin_wer.png` — distribuição completa de WER por modelo
- `results/violin_latencia.png` — distribuição completa de Latência por modelo
- `results/heatmap_wer_modelo_categoria.png` — heatmap WER por modelo × categoria
- `results/heatmap_latencia_modelo_categoria.png` — heatmap Latência por modelo × categoria
- `results/barras_tipos_erro.png` — substituições, deleções e inserções empilhadas por modelo
- `results/radar_comparativo.png` — radar chart com 5 eixos normalizados
- `results/scatter_wer_vs_numpalavras.png` — WER × NumPalavras com linha de tendência

### Como Executar

```bash
# Ambiente local
jupyter notebook notebooks/analise_avancada.ipynb

# Google Colab
# Faça upload do arquivo notebooks/analise_avancada.ipynb e do CSV results/resultados_tts_tcc.csv
```
