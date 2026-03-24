# Amostras de Áudio

Esta pasta é destinada a armazenar amostras de áudio geradas pelos 3 modelos TTS avaliados.

## Estrutura Sugerida

```
audio_samples/
├── kokoro/
│   ├── curtas_objetivas_01.wav
│   ├── longas_narrativas_01.wav
│   └── ...
├── piper/
│   ├── curtas_objetivas_01.wav
│   ├── longas_narrativas_01.wav
│   └── ...
└── xtts_v2/
    ├── curtas_objetivas_01.wav
    ├── longas_narrativas_01.wav
    └── ...
```

## Nota

Os arquivos WAV não estão versionados no repositório (ver `.gitignore`) pois podem ocupar vários GB de espaço. Para gerar as amostras, execute o notebook `modelscompare_v5_1903-2.ipynb`.

## Como Adicionar Amostras

Se você quiser compartilhar amostras de áudio representativas, considere:

1. Selecionar **1-2 frases por categoria** de cada modelo
2. Converter para formato comprimido (MP3, OGG) para reduzir o tamanho
3. Nomear os arquivos de forma descritiva: `{modelo}_{categoria}_{numero}.wav`

> ⚠️ Certifique-se de que as amostras não contenham dados sensíveis ou que violem direitos autorais.
