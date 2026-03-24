# Resultados

Esta pasta armazena os arquivos exportados pelo notebook após a execução do benchmark completo.

## Arquivos Esperados

| Arquivo | Descrição |
|---------|-----------|
| `benchmark_results.csv` | Resultados brutos: modelo, categoria, frase, latência, WER |
| `summary_by_model.csv` | Resumo agregado por modelo (latência média, WER médio) |
| `summary_by_category.csv` | Resumo agregado por categoria |
| `relatorio_tts.docx` | Relatório formatado em Word com tabelas e análises |

## Como Gerar os Arquivos

Execute o notebook `modelscompare_v5_1903-2.ipynb` até o final. As células de análise (Célula 9 em diante) exportam automaticamente os resultados para esta pasta.

> **Nota**: Os arquivos CSV e DOCX não estão versionados no repositório (ver `.gitignore`) pois são gerados pelo notebook. Execute o notebook para obtê-los.
