# 🎵 Amostras de Áudio

Esta pasta destina-se ao armazenamento de amostras de áudio geradas pelos modelos TTS durante os experimentos.

---

## ⚠️ Aviso Importante sobre Tamanho de Arquivos

Arquivos de áudio podem ser muito grandes para o Git convencional. Por isso:

- **Arquivos `.wav`, `.mp3`, `.ogg`** estão listados no `.gitignore` e **não serão versionados**
- Para compartilhar amostras de áudio, use uma das alternativas abaixo

---

## 🗂️ Convenção de Nomenclatura

Os arquivos de áudio devem seguir o padrão:

```
{modelo}_{frase_id}_{variante}.wav
```

**Exemplos:**
```
gtts_01_frase_curta.wav
coqui_xtts_05_acessibilidade.wav
bark_10_expressivo.wav
meta_mms_03_numeros.wav
piper_07_pontuacao.wav
edge_tts_02_neutra.wav
```

---

## 📤 Como Compartilhar Amostras de Áudio

### Opção 1 — Google Drive (recomendado para o Colab)

```python
# No Google Colab, salve no Drive e compartilhe o link
from google.colab import drive
drive.mount("/content/drive")

import shutil
shutil.copy("saida.wav", "/content/drive/MyDrive/tts-amostras/")
```

### Opção 2 — Git LFS (Large File Storage)

Para versionar amostras representativas pequenas no repositório:

```bash
# Instalar Git LFS
git lfs install

# Rastrear arquivos de áudio
git lfs track "audio_samples/*.wav"
git add .gitattributes
git commit -m "Configurar Git LFS para arquivos de áudio"
```

> 📌 **Nota:** O Git LFS tem limites de armazenamento no GitHub gratuito (1 GB total, 1 GB de banda/mês).

### Opção 3 — Links externos

Inclua links para audios hospedados externamente (Google Drive, SoundCloud, etc.) no notebook correspondente.

---

## 📋 Amostras Planejadas

Após a execução dos experimentos, as amostras representativas serão catalogadas aqui:

| Arquivo | Modelo | Frase | Observação |
|---------|--------|-------|------------|
| `gtts_01.wav` | gTTS | Frase curta #1 | — |
| `edge_tts_01.wav` | edge-tts | Frase curta #1 | Voz FranciscaNeural |
| `coqui_xtts_01.wav` | Coqui XTTS-v2 | Frase curta #1 | — |
| `bark_01.wav` | Bark | Frase curta #1 | — |
| `meta_mms_01.wav` | Meta MMS | Frase curta #1 | — |
| `piper_01.wav` | Piper | Frase curta #1 | Modelo faber-medium |

---

> 🔬 *As amostras serão disponibilizadas conforme os experimentos forem concluídos.*
