# Resultados

Esta pasta armazena os arquivos exportados pelo notebook após a execução do benchmark completo.

## Arquivos Existentes

| Arquivo | Descrição |
|---------|-----------|
| `resultados_tts_tcc.csv` | Resultados brutos do benchmark: 420 sínteses (3 modelos × 140 frases × 14 categorias) |
| `resumo_por_modelo.csv` | Resumo agregado por modelo (latência média, WER médio) |
| `resumo_por_categoria.csv` | Resumo agregado por categoria |
| `resumo_por_modelo_categoria.csv` | Resumo por modelo e categoria combinados |
| `corpus_teste_tcc.csv` | Corpus das 140 frases utilizadas no benchmark |
| `graficos_tcc/` | Gráficos gerados pelo notebook principal |

## Arquivos Gerados por `notebooks/analise_avancada.ipynb`

### CSVs Expandidos

| Arquivo | Descrição |
|---------|-----------|
| `resultados_expandidos.csv` | DataFrame completo com novas colunas: Throughput, CER, WER_zero, Log_Latencia |
| `estatisticas_descritivas.csv` | Tabela de estatísticas por modelo: média, mediana, dp, CV, IC 95%, taxa WER zero, CER |
| `testes_estatisticos.csv` | Resultados de Kruskal-Wallis, Dunn post-hoc e Spearman por modelo |
| `ranking_por_categoria.csv` | Vencedor (menor WER e menor Latência) por categoria |
| `analise_erros.csv` | Contagem de substituições (S), deleções (D) e inserções (I) por modelo |

### Gráficos Avançados

| Arquivo | Descrição |
|---------|-----------|
| `scatter_wer_vs_latencia.png` | Dispersão WER × Latência com tamanho ∝ NumPalavras |
| `violin_wer.png` | Distribuição completa de WER por modelo (violin plot) |
| `violin_latencia.png` | Distribuição completa de Latência por modelo (violin plot) |
| `heatmap_wer_modelo_categoria.png` | Heatmap WER médio por modelo × categoria |
| `heatmap_latencia_modelo_categoria.png` | Heatmap Latência média por modelo × categoria |
| `barras_tipos_erro.png` | Barras empilhadas: substituições, deleções e inserções por modelo |
| `radar_comparativo.png` | Radar chart comparativo com 5 eixos normalizados |
| `scatter_wer_vs_numpalavras.png` | WER × NumPalavras com linha de tendência por modelo |

## Como Gerar os Arquivos

### Notebook principal (benchmark)
Execute o notebook `modelscompare_v5_1903-2.ipynb` até o final. As células de análise exportam automaticamente os resultados para esta pasta.

### Notebook de análise avançada
Execute o notebook `notebooks/analise_avancada.ipynb`. Ele lê `resultados_tts_tcc.csv` e gera todos os arquivos listados na seção "Gerados por analise_avancada.ipynb" acima.

> **Nota**: Os arquivos CSV e PNG não estão versionados no repositório (ver `.gitignore`) pois são gerados pelos notebooks. Execute os notebooks para obtê-los.
