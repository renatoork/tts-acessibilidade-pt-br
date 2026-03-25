# Justificativa de Seleção dos Modelos TTS

Este documento detalha os critérios e a fundamentação acadêmica que orientaram a seleção dos três modelos de síntese de voz (*Text-to-Speech*) avaliados neste trabalho.

---

## 1. Critérios de Seleção

A definição dos modelos candidatos partiu de uma pesquisa exploratória sobre o ecossistema de TTS open source com suporte ao português brasileiro. A seleção final considerou os seguintes critérios:

| Critério | Descrição | Relevância |
|----------|-----------|------------|
| **Open source** | Código-fonte e pesos disponíveis publicamente | Reprodutibilidade acadêmica e auditabilidade |
| **Suporte nativo a pt-BR** | Modelo treinado ou com *voicepack* específico para português brasileiro | Qualidade e naturalidade na língua-alvo da pesquisa |
| **Execução offline** | Funciona sem conexão com internet ou APIs externas | Independência tecnológica; privacidade dos dados |
| **Execução em CPU** | Viável em ambiente sem GPU (ex.: Google Colab gratuito) | Democratização do acesso — qualquer pessoa pode reproduzir |
| **Arquitetura neural moderna** | Baseado em redes neurais profundas recentes | Qualidade mínima necessária para uso em leitura acessível |
| **Diversidade arquitetural** | Cada modelo representa uma abordagem arquitetural distinta | Comparação academicamente mais rica e representativa |

---

## 2. Modelos Descartados e Justificativa

Os modelos abaixo foram considerados na fase exploratória, mas **excluídos** da avaliação final pelos motivos indicados:

| Modelo | Motivo da exclusão |
|--------|--------------------|
| **gTTS** (Google TTS) | Wrapper da API do Google Translate TTS; requer conexão com internet; não é um modelo real de síntese neural |
| **edge-tts** (Microsoft Edge) | Wrapper da API de TTS da Microsoft; requer conexão com internet; não é um modelo distribuível offline |
| **Bark** (Suno AI) | Computacionalmente muito pesado para execução em CPU; tempos de síntese inviáveis no escopo da pesquisa; sem foco em pt-BR nativo |
| **Meta MMS** (`facebook/mms-tts-por`) | Qualidade inferior para pt-BR em testes preliminares; documentação e comunidade limitadas no período de realização dos experimentos |
| **eSpeak-NG** | Voz robótica baseada em regras fonológicas; naturalidade insuficiente para uso em leitura prolongada no contexto de acessibilidade |
| **Festival / MBROLA** | Síntese concatenativa; qualidade de voz significativamente inferior às arquiteturas neurais modernas; inadequada para o contexto de acessibilidade |

---

## 3. Modelos Selecionados

### 3.1 XTTS v2 (Coqui AI)

**Por que foi selecionado:**
O XTTS v2 é o modelo de maior qualidade perceptual entre os avaliados. Suporta nativamente o português brasileiro como um dos seus 17 idiomas e dispõe de *voicepacks* dedicados. É amplamente referenciado em literatura sobre TTS multilingual e síntese de voz para acessibilidade.

**Critério de destaque:**
Representa o estado da arte em qualidade de síntese — relevante como referência de teto de qualidade na comparação.

**Arquitetura:**
Modelo autoregressivo baseado em **GPT** (geração token a token) combinado com o vocoder **HiFiGAN** para conversão espectral → áudio. Permite clonagem de voz *zero-shot* a partir de amostras curtas de áudio de referência.

**Paper de referência:**
> Casanova, E. et al. *XTTS: A Massively Multilingual Zero-Shot Text-to-Speech Model*. INTERSPEECH, 2024.
> Disponível em: https://www.isca-archive.org/interspeech_2024/casanova24_interspeech.pdf

---

### 3.2 Piper (Rhasspy)

**Por que foi selecionado:**
O Piper foi desenvolvido especificamente para execução local e offline em dispositivos com recursos limitados (inclusive Raspberry Pi). Possui modelos treinados para pt-BR (`pt_BR-cadu-medium`) e apresenta a menor latência entre os modelos avaliados, tornando-o ideal para cenários de acessibilidade em tempo real.

**Critério de destaque:**
Representa o polo de eficiência computacional — fundamental para avaliar a viabilidade de implantação em dispositivos de baixo custo.

**Arquitetura:**
Baseado na arquitetura **VITS** (*Variational Inference Text-to-Speech*), que combina autoencoder variacional (VAE), fluxos normalizadores e síntese adversarial em um único modelo *end-to-end*.

**Paper de referência:**
> Kim, J. et al. *Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech*. ICML, 2021.
> Disponível em: https://arxiv.org/abs/2106.06103

---

### 3.3 Kokoro (Hexgrad)

**Por que foi selecionado:**
O Kokoro oferece um equilíbrio entre qualidade e eficiência, com apenas 82 milhões de parâmetros e exportação em formato ONNX (~326 MB), viabilizando execução eficiente em CPU. Possui *voicepacks* explícitos para pt-BR (`pf_dora` — voz feminina; `pm_alex` — voz masculina) e apresentou o menor WER médio nos experimentos deste trabalho.

**Critério de destaque:**
Combina boa qualidade perceptual com eficiência computacional razoável — ponto de equilíbrio entre XTTS v2 (alta qualidade, alta latência) e Piper (baixa latência, qualidade moderada).

**Arquitetura:**
Baseado na arquitetura **StyleTTS 2**, que utiliza difusão de estilo (*style diffusion*) e treinamento adversarial com modelos de linguagem de fala de grande escala para aproximar a qualidade da voz humana.

**Paper de referência:**
> Li, Y. A. et al. *StyleTTS 2: Towards Human-Level Text-to-Speech through Style Diffusion and Adversarial Training with Large Speech Language Models*. NeurIPS, 2023.
> Disponível em: https://arxiv.org/abs/2306.07691

---

## 4. Diversidade Arquitetural

Um dos pilares desta pesquisa é a **diversidade arquitetural**: cada modelo selecionado representa uma abordagem fundamentalmente diferente para o problema de síntese de voz, o que torna a comparação academicamente mais rica e representativa do panorama atual.

| Abordagem | Modelo | Arquitetura base | Características |
|-----------|--------|-----------------|-----------------|
| **1. Autoregressiva** | XTTS v2 | GPT + HiFiGAN | Geração sequencial token a token; alta qualidade; maior latência |
| **2. Variacional** | Piper | VITS | Inferência paralela *end-to-end*; extremamente leve e rápido |
| **3. Difusão de Estilo** | Kokoro | StyleTTS 2 | Difusão de estilo com LLM de fala; equilíbrio qualidade/eficiência |

Essa diversidade garante que as conclusões do estudo não sejam enviesadas por uma única abordagem técnica, permitindo analisar como diferentes paradigmas arquiteturais afetam métricas objetivas (WER, latência) e a viabilidade de uso em sistemas de acessibilidade.

---

## 5. Texto Sugerido para o TCC

O trecho abaixo pode ser copiado e adaptado para a **seção de metodologia** do trabalho de conclusão de curso:

> A seleção dos modelos seguiu critérios de: (i) disponibilidade como software livre; (ii) suporte nativo ao português brasileiro; (iii) capacidade de execução offline e em CPU, visando a democratização do acesso; e (iv) representatividade de diferentes arquiteturas neurais modernas. Foram selecionados três modelos: XTTS v2 (Casanova et al., 2024), baseado em arquitetura autoregressiva GPT com vocoder HiFiGAN; Piper (Rhasspy, 2024), baseado na arquitetura VITS (Kim et al., 2021); e Kokoro (Hexgrad, 2025), baseado na arquitetura StyleTTS 2 (Li et al., 2023). Modelos que dependem de APIs proprietárias (gTTS, edge-tts), que apresentaram qualidade insuficiente (eSpeak-NG, Festival) ou que se mostraram inviáveis para execução em CPU (Bark) foram excluídos da avaliação.

---

*Consulte também: [docs/referencias.md](referencias.md) para a lista completa de referências bibliográficas em formato ABNT NBR 6023:2018.*
