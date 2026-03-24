"""
Funções utilitárias para os experimentos de TTS.

Este módulo provê helpers para:
- Medição de tempo e recursos computacionais
- Salvamento de arquivos de áudio
- Cálculo de métricas (RTF, etc.)
- Geração de relatórios comparativos
"""

import time
import functools
import os
from typing import Callable, Any

import numpy as np
import soundfile as sf
import pandas as pd

# Importações opcionais (nem sempre disponíveis no ambiente)
try:
    import psutil
    PSUTIL_DISPONIVEL = True
except ImportError:
    PSUTIL_DISPONIVEL = False

try:
    import torch
    TORCH_DISPONIVEL = True
except ImportError:
    TORCH_DISPONIVEL = False


# =============================================================================
# Medição de tempo
# =============================================================================

def medir_tempo(func: Callable) -> Callable:
    """
    Decorator que mede o tempo de execução de uma função.

    Uso:
        @medir_tempo
        def minha_funcao():
            ...

    Retorna:
        Tuple (resultado, tempo_em_segundos)
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()
        tempo_decorrido = fim - inicio
        print(f"[{func.__name__}] Tempo de execução: {tempo_decorrido:.3f}s")
        return resultado, tempo_decorrido
    return wrapper


# =============================================================================
# Salvamento de áudio
# =============================================================================

def salvar_audio(audio: np.ndarray, sr: int, caminho: str) -> None:
    """
    Salva um array de áudio como arquivo WAV.

    Args:
        audio:   Array numpy com os dados de áudio (float32 ou int16)
        sr:      Taxa de amostragem em Hz (ex: 22050, 44100)
        caminho: Caminho de destino do arquivo (ex: 'outputs/saida.wav')
    """
    # Cria o diretório de destino se não existir
    diretorio = os.path.dirname(caminho)
    if diretorio:
        os.makedirs(diretorio, exist_ok=True)

    # Converte para float32 se necessário
    if audio.dtype != np.float32:
        audio = audio.astype(np.float32)

    # Normaliza o áudio para evitar clipping
    valor_maximo = np.max(np.abs(audio))
    if valor_maximo > 0:
        audio = audio / valor_maximo
    else:
        import warnings
        warnings.warn(
            f"O áudio a ser salvo em '{caminho}' está completamente silencioso (todos os valores são zero).",
            UserWarning,
            stacklevel=2,
        )

    sf.write(caminho, audio, sr)
    print(f"Áudio salvo em: {caminho} (taxa: {sr} Hz, duração: {len(audio)/sr:.2f}s)")


# =============================================================================
# Métricas
# =============================================================================

def calcular_rtf(tempo_sintese: float, duracao_audio: float) -> float:
    """
    Calcula o Real-Time Factor (RTF) do processo de síntese.

    RTF = tempo_de_síntese / duração_do_áudio_gerado

    RTF < 1: síntese mais rápida que o tempo real (desejável)
    RTF > 1: síntese mais lenta que o tempo real

    Args:
        tempo_sintese:  Tempo decorrido durante a síntese, em segundos
        duracao_audio:  Duração do áudio gerado, em segundos

    Returns:
        Valor do RTF (float)
    """
    if duracao_audio <= 0:
        raise ValueError("A duração do áudio deve ser maior que zero.")
    rtf = tempo_sintese / duracao_audio
    return rtf


def calcular_duracao_audio(audio: np.ndarray, sr: int) -> float:
    """
    Calcula a duração de um array de áudio em segundos.

    Args:
        audio: Array numpy com os dados de áudio
        sr:    Taxa de amostragem em Hz

    Returns:
        Duração em segundos (float)
    """
    return len(audio) / sr


# =============================================================================
# Coleta de recursos computacionais
# =============================================================================

def coletar_recursos() -> dict:
    """
    Coleta informações sobre o uso atual de recursos computacionais.

    Returns:
        Dicionário com:
        - ram_usada_gb:   Memória RAM utilizada em GB
        - ram_total_gb:   Memória RAM total em GB
        - ram_percent:    Percentual de RAM utilizada
        - vram_usada_gb:  Memória de vídeo utilizada em GB (se GPU disponível)
        - vram_total_gb:  Memória de vídeo total em GB (se GPU disponível)
        - gpu_nome:       Nome da GPU (se disponível)
    """
    recursos = {
        "ram_usada_gb": None,
        "ram_total_gb": None,
        "ram_percent": None,
        "vram_usada_gb": None,
        "vram_total_gb": None,
        "gpu_nome": None,
    }

    # Coleta uso de RAM
    if PSUTIL_DISPONIVEL:
        mem = psutil.virtual_memory()
        recursos["ram_usada_gb"] = round(mem.used / 1024**3, 2)
        recursos["ram_total_gb"] = round(mem.total / 1024**3, 2)
        recursos["ram_percent"] = mem.percent

    # Coleta uso de VRAM (GPU)
    if TORCH_DISPONIVEL and torch.cuda.is_available():
        props = torch.cuda.get_device_properties(0)
        recursos["gpu_nome"] = props.name
        recursos["vram_usada_gb"] = round(torch.cuda.memory_allocated() / 1024**3, 2)
        recursos["vram_total_gb"] = round(props.total_memory / 1024**3, 2)

    return recursos


# =============================================================================
# Wrapper genérico de síntese
# =============================================================================

def sintetizar_e_medir(modelo_nome: str, func_sintetizar: Callable, texto: str, **kwargs) -> dict:
    """
    Wrapper genérico para sintetizar voz e medir as métricas de desempenho.

    Args:
        modelo_nome:      Nome do modelo TTS (para identificação nos resultados)
        func_sintetizar:  Callable que recebe (texto, **kwargs) e retorna
                          (audio: np.ndarray, sr: int)
        texto:            Texto a ser sintetizado
        **kwargs:         Argumentos adicionais passados para func_sintetizar

    Returns:
        Dicionário com:
        - modelo:        Nome do modelo
        - texto:         Texto sintetizado
        - tempo_s:       Tempo de síntese em segundos
        - duracao_s:     Duração do áudio gerado em segundos
        - rtf:           Real-Time Factor
        - recursos:      Dicionário com uso de RAM/VRAM
        - audio:         Array numpy com o áudio gerado
        - sr:            Taxa de amostragem
    """
    recursos_antes = coletar_recursos()

    inicio = time.perf_counter()
    audio, sr = func_sintetizar(texto, **kwargs)
    fim = time.perf_counter()

    tempo_sintese = fim - inicio
    duracao_audio = calcular_duracao_audio(audio, sr)
    rtf = calcular_rtf(tempo_sintese, duracao_audio)

    recursos_depois = coletar_recursos()

    resultado = {
        "modelo": modelo_nome,
        "texto": texto,
        "tempo_s": round(tempo_sintese, 3),
        "duracao_s": round(duracao_audio, 3),
        "rtf": round(rtf, 3),
        "ram_usada_gb": recursos_depois.get("ram_usada_gb"),
        "vram_usada_gb": recursos_depois.get("vram_usada_gb"),
        "gpu_nome": recursos_depois.get("gpu_nome"),
        "audio": audio,
        "sr": sr,
    }

    print(f"\n[{modelo_nome}]")
    print(f"  Texto: '{texto[:60]}...'" if len(texto) > 60 else f"  Texto: '{texto}'")
    print(f"  Tempo de síntese: {tempo_sintese:.3f}s")
    print(f"  Duração do áudio: {duracao_audio:.3f}s")
    print(f"  RTF: {rtf:.3f} ({'✅ em tempo real' if rtf < 1 else '⚠️ mais lento que tempo real'})")

    return resultado


# =============================================================================
# Geração de relatório
# =============================================================================

def gerar_relatorio(resultados: list) -> pd.DataFrame:
    """
    Gera um DataFrame pandas com os resultados comparativos dos modelos.

    Args:
        resultados: Lista de dicionários retornados por sintetizar_e_medir()

    Returns:
        DataFrame com as colunas:
        modelo, texto, tempo_s, duracao_s, rtf, ram_usada_gb, vram_usada_gb, gpu_nome
    """
    colunas = ["modelo", "texto", "tempo_s", "duracao_s", "rtf",
               "ram_usada_gb", "vram_usada_gb", "gpu_nome"]

    # Remove a chave 'audio' e 'sr' do dicionário para o DataFrame
    dados = []
    for r in resultados:
        linha = {col: r.get(col) for col in colunas}
        dados.append(linha)

    df = pd.DataFrame(dados, columns=colunas)

    print("\n" + "=" * 60)
    print("RELATÓRIO COMPARATIVO DOS MODELOS TTS")
    print("=" * 60)
    print(df.to_string(index=False))
    print("=" * 60)

    return df
