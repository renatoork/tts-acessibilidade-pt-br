# ☁️ Guia de Configuração — Google Colab

Este guia descreve o passo a passo para configurar o ambiente Google Colab e executar os experimentos de TTS desta pesquisa.

---

## 🔗 Notebook Principal

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-xhoU_3Jg7MbrsmIES2Aezv0-_A90FT6)

---

## 1. Acessar o Google Colab

1. Acesse [colab.research.google.com](https://colab.research.google.com)
2. Faça login com sua conta Google
3. Abra o notebook desejado:
   - Via link direto (badge acima)
   - Via **File > Open notebook > GitHub** e cole a URL do repositório

---

## 2. Habilitar GPU

O Google Colab oferece acesso gratuito a GPUs (T4), essencial para modelos pesados como XTTS e Bark.

### Passo a passo:

1. No menu superior, clique em **Runtime** (ou **Ambiente de execução**)
2. Selecione **Change runtime type** (ou **Alterar tipo de ambiente de execução**)
3. Em **Hardware accelerator**, selecione **GPU**
4. Clique em **Save** (ou **Salvar**)

> ⚠️ **Atenção:** O Colab gratuito tem limite de horas de GPU por sessão. Salve o progresso regularmente no Google Drive.

### Verificar se a GPU está ativa:

```python
import torch
print(f"GPU disponível: {torch.cuda.is_available()}")
print(f"GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'Nenhuma'}")
```

---

## 3. Instalar Dependências

No início de cada notebook, execute a célula de instalação:

```python
# Instalar dependências do projeto
!pip install -q TTS bark gTTS edge-tts piper-tts transformers
!pip install -q librosa soundfile matplotlib pandas tqdm psutil
```

> 💡 O `-q` suprime a saída verbose do pip, deixando o notebook mais limpo.

### Para modelos específicos:

```python
# Coqui XTTS-v2
!pip install -q TTS

# Meta MMS
!pip install -q transformers torch

# Bark
!pip install -q bark

# Piper
!pip install -q piper-tts

# gTTS
!pip install -q gtts

# edge-tts
!pip install -q edge-tts
```

---

## 4. Montar o Google Drive

Para salvar os resultados e áudios gerados entre sessões, monte o Google Drive:

```python
from google.colab import drive
drive.mount("/content/drive")
```

Você será redirecionado para autorizar o acesso. Após a autorização:

```python
import os

# Criar pasta para os resultados no Drive
PASTA_RESULTADOS = "/content/drive/MyDrive/tts-acessibilidade-resultados"
os.makedirs(PASTA_RESULTADOS, exist_ok=True)

# Subpastas
os.makedirs(f"{PASTA_RESULTADOS}/audios", exist_ok=True)
os.makedirs(f"{PASTA_RESULTADOS}/metricas", exist_ok=True)

print(f"Pasta criada: {PASTA_RESULTADOS}")
```

---

## 5. Clonar o Repositório (opcional)

Se quiser acessar os scripts utilitários e textos de teste diretamente no Colab:

```python
# Clonar o repositório
!git clone https://github.com/renatoork/tts-acessibilidade-pt-br.git
%cd tts-acessibilidade-pt-br

# Instalar dependências do repositório
!pip install -q -r requirements.txt
```

---

## 6. Verificar Ambiente

Após a configuração, verifique se tudo está funcionando corretamente:

```python
import torch
import psutil
import platform

print("=" * 50)
print("INFORMAÇÕES DO AMBIENTE")
print("=" * 50)
print(f"Python: {platform.python_version()}")
print(f"PyTorch: {torch.__version__}")
print(f"GPU disponível: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    vram = torch.cuda.get_device_properties(0).total_memory / 1024**3
    print(f"VRAM total: {vram:.1f} GB")

ram = psutil.virtual_memory().total / 1024**3
print(f"RAM total: {ram:.1f} GB")
print("=" * 50)
```

---

## 7. Salvar Resultados

### Salvar áudio gerado no Drive

```python
import shutil

def salvar_no_drive(arquivo_local, nome_arquivo, pasta_drive):
    """Copia um arquivo local para o Google Drive."""
    destino = os.path.join(pasta_drive, nome_arquivo)
    shutil.copy(arquivo_local, destino)
    print(f"Arquivo salvo em: {destino}")

# Exemplo de uso
salvar_no_drive("saida.wav", "coqui_tts_amostra.wav", f"{PASTA_RESULTADOS}/audios")
```

### Salvar métricas em CSV

```python
import pandas as pd

# Após coletar as métricas dos experimentos
resultados = [
    {"modelo": "Coqui XTTS-v2", "rtf": 0.35, "latencia_s": 2.1, "vram_gb": 5.8},
    {"modelo": "Meta MMS", "rtf": 0.12, "latencia_s": 0.8, "vram_gb": 1.2},
    # ...
]

df = pd.DataFrame(resultados)
caminho_csv = f"{PASTA_RESULTADOS}/metricas/resultados_comparativos.csv"
df.to_csv(caminho_csv, index=False)
print(f"Métricas salvas em: {caminho_csv}")
```

---

## 8. Dicas e Boas Práticas

### Evitar desconexão por inatividade

```python
# Execute esta célula para evitar que o Colab desconecte por inatividade
# (funciona no navegador Chrome)
from IPython.display import display, Javascript

display(Javascript('''
function conectar() {
    document.querySelector("#connect").click();
}
setInterval(conectar, 60000);
'''))
```

### Verificar uso de memória

```python
# Durante a execução, monitore o uso de memória
def verificar_memoria():
    if torch.cuda.is_available():
        vram_usada = torch.cuda.memory_allocated() / 1024**3
        vram_total = torch.cuda.get_device_properties(0).total_memory / 1024**3
        print(f"VRAM: {vram_usada:.2f} / {vram_total:.1f} GB")
    
    ram = psutil.virtual_memory()
    print(f"RAM: {ram.used / 1024**3:.2f} / {ram.total / 1024**3:.1f} GB ({ram.percent}%)")

verificar_memoria()
```

### Limpar cache entre modelos

```python
# Após usar cada modelo, limpe a memória da GPU
import gc

def limpar_memoria():
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    print("Memória liberada.")

limpar_memoria()
```

---

## 9. Solução de Problemas Comuns

### "CUDA out of memory"

```python
# Reduza o batch size ou use um modelo menor
# Limpe a memória antes de carregar um novo modelo
torch.cuda.empty_cache()
gc.collect()
```

### "No module named 'TTS'"

```python
# Reinstale o pacote
!pip install -q TTS
import importlib
import TTS
importlib.reload(TTS)
```

### "Drive não montado"

```python
# Remonte o Drive
from google.colab import drive
drive.flush_and_unmount()
drive.mount("/content/drive", force_remount=True)
```

---

## Recursos Adicionais

- [Documentação do Google Colab](https://colab.research.google.com/notebooks/intro.ipynb)
- [Tutorial de GPU no Colab](https://colab.research.google.com/notebooks/gpu.ipynb)
- [Google Drive no Colab](https://colab.research.google.com/notebooks/io.ipynb)
