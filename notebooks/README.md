# 📓 Notebooks

Esta pasta contém os notebooks Jupyter / Google Colab com os experimentos de síntese de voz para cada modelo TTS avaliado.

## 🔗 Notebook Principal no Google Colab

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-xhoU_3Jg7MbrsmIES2Aezv0-_A90FT6)

---

## 📋 Convenções de Nomenclatura

Os notebooks seguem o padrão `NN_nome_do_modelo.ipynb`, onde `NN` é um número sequencial com dois dígitos. Isso garante a ordem de execução sugerida e facilita a navegação.

## 📚 Notebooks Planejados

| Arquivo | Modelo | Descrição |
|---------|--------|-----------|
| `01_gtts_basico.ipynb` | gTTS | Teste básico com Google Text-to-Speech — wrapper simples, requer internet |
| `02_edge_tts.ipynb` | edge-tts | Teste com Microsoft Edge TTS — vozes neurais, requer internet |
| `03_coqui_tts_xtts.ipynb` | Coqui TTS / XTTS-v2 | Modelo de alta qualidade, multi-voz, suporte a clonagem de voz |
| `04_bark_tts.ipynb` | Bark (Suno AI) | Modelo generativo expressivo, suporta emoções e ruídos |
| `05_meta_mms.ipynb` | Meta MMS | Massively Multilingual Speech da Meta AI, robusto |
| `06_piper_tts.ipynb` | Piper | TTS rápido e leve, ideal para dispositivos com poucos recursos |
| `07_comparativo_modelos.ipynb` | Todos | Comparação lado a lado de todos os modelos com métricas |

---

## 🗂️ Estrutura Interna de Cada Notebook

Cada notebook deve seguir a estrutura abaixo para manter consistência e reprodutibilidade:

```
1. 🔧 Configuração do Ambiente
   - Instalação das dependências
   - Importações
   - Configuração de caminhos

2. 🤖 Carregamento do Modelo
   - Download dos pesos (se necessário)
   - Inicialização do modelo

3. 🗣️ Síntese de Voz
   - Síntese a partir de frases de teste (textos_teste/frases.txt)
   - Reprodução/download do áudio gerado

4. 📊 Avaliação
   - Medição de tempo de processamento
   - Coleta de uso de GPU/RAM
   - Cálculo do RTF (Real-Time Factor)

5. 💾 Salvamento dos Resultados
   - Exportar métricas para CSV
   - Salvar amostras de áudio (com aviso de tamanho)

6. 📝 Conclusões do Experimento
   - Observações sobre qualidade, naturalidade e limitações
```

---

## 💡 Como Executar

### Google Colab (recomendado)

1. Acesse o notebook desejado no GitHub
2. Clique no badge "Open in Colab" ou use o menu **File > Open in Colab**
3. No Colab, ative a GPU: **Runtime > Change runtime type > GPU**
4. Execute as células na ordem (`Ctrl+F9` ou **Runtime > Run all**)

### Localmente

```bash
# Na raiz do repositório
pip install -r requirements.txt
jupyter notebook notebooks/
```

---

## ⚠️ Observações Importantes

- **Modelos pesados** (Coqui XTTS, Bark) requerem GPU com pelo menos 6 GB de VRAM
- **Modelos leves** (gTTS, edge-tts, Piper) funcionam bem em CPU
- Os arquivos de áudio gerados **não são versionados** (ver `.gitignore`) — use o Google Drive para persistência no Colab
- Sempre execute o notebook `07_comparativo_modelos.ipynb` por último, pois ele depende dos resultados dos notebooks anteriores
