# 📈 Resultados dos Experimentos

Esta pasta armazena os resultados gerados pelos experimentos de avaliação dos modelos TTS.

---

## 📁 Organização dos Arquivos

```
results/
├── metricas/
│   ├── resultados_comparativos.csv     # Tabela geral com todas as métricas
│   ├── rtf_por_modelo.csv              # RTF de cada modelo por frase
│   ├── tempo_sintese.csv               # Tempo de síntese detalhado
│   └── uso_recursos.csv                # Uso de GPU/RAM por modelo
│
├── graficos/
│   ├── comparativo_rtf.png             # Gráfico comparativo de RTF
│   ├── comparativo_latencia.png        # Gráfico comparativo de latência
│   ├── comparativo_qualidade.png       # Gráfico de qualidade (MOS)
│   └── uso_vram.png                    # Gráfico de uso de VRAM
│
└── README.md                           # Este arquivo
```

---

## 📊 Formato dos Arquivos CSV

Os arquivos CSV seguem o seguinte esquema de colunas:

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `modelo` | string | Nome do modelo TTS |
| `frase_id` | int | ID da frase de teste |
| `texto` | string | Texto sintetizado |
| `tempo_s` | float | Tempo de síntese em segundos |
| `duracao_s` | float | Duração do áudio gerado em segundos |
| `rtf` | float | Real-Time Factor |
| `ram_usada_gb` | float | RAM utilizada durante a síntese (GB) |
| `vram_usada_gb` | float | VRAM utilizada durante a síntese (GB) |
| `mos` | float | Mean Opinion Score (1–5, avaliação subjetiva) |
| `inteligibilidade` | float | Percentual de inteligibilidade (0–100%) |

---

## 🔬 Status dos Experimentos

> 🔜 *Os resultados serão adicionados conforme os experimentos forem concluídos.*

| Notebook | Modelo | Status |
|----------|--------|--------|
| `01_gtts_basico.ipynb` | gTTS | ⏳ Pendente |
| `02_edge_tts.ipynb` | edge-tts | ⏳ Pendente |
| `03_coqui_tts_xtts.ipynb` | Coqui XTTS-v2 | ⏳ Pendente |
| `04_bark_tts.ipynb` | Bark | ⏳ Pendente |
| `05_meta_mms.ipynb` | Meta MMS | ⏳ Pendente |
| `06_piper_tts.ipynb` | Piper | ⏳ Pendente |
| `07_comparativo_modelos.ipynb` | Todos | ⏳ Pendente |

---

## 💡 Notas

- Os resultados numéricos podem variar conforme o hardware utilizado (GPU T4 no Colab, CPU local, etc.)
- Os arquivos de áudio gerados **não são armazenados aqui** (ver `audio_samples/README.md`)
- Para reproduzir os resultados, execute os notebooks na ordem indicada
