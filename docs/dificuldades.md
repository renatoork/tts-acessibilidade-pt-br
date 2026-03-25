# 📋 Diário Completo de Dificuldades e Soluções

## Projeto: TTS Acessibilidade PT-BR — Notebook `modelscompare_v5_1903-2.ipynb`

> Cronologia reconstruída a partir de dois históricos de interação com IA (GitHub Copilot), cobrindo o período de desenvolvimento do notebook entre 2024-2026.

---

## 🔴 Categoria 1 — Ambiente de Execução e Versões do Python

### 1.1 Incompatibilidade do Python 3.12 no Google Colab

- **Problema**: O Google Colab atualizou seu runtime padrão para **Python 3.12**, o que gerou quebra de compatibilidade com modelos de TTS projetados para Python 3.9/3.10. Erros de `RuntimeError` indicavam que bibliotecas legadas não suportavam a nova versão.
- **Solução**: Identificação da necessidade de utilizar o fork da comunidade (`coqui-tts`) que suporta versões recentes, ou alternativamente realizar o downgrade do runtime do Colab para a versão 2025.10 (Python 3.11).
- **Impacto no TCC**: Demonstra como a evolução rápida do ecossistema de IA pode comprometer a reprodutibilidade de experimentos.

### 1.2 Dependências de sistema operacional ausentes no Colab

- **Problema**: O Coqui TTS (XTTS v2) depende do `espeak-ng` como backend de fonemas, e o processamento de áudio precisa do `ffmpeg`. O Colab não os tem pré-instalados.
- **Solução**: Célula 1 do notebook executa `apt-get install espeak-ng ffmpeg` antes de qualquer instalação Python.
- **Erro típico**: `espeak-ng: command not found` → resolver re-executando a Célula 1.

---

## 🔴 Categoria 2 — Conflitos e Transições de Bibliotecas Python

### 2.1 Descontinuação do pacote `TTS` original (Coqui AI)

- **Problema**: O pacote original `TTS` no PyPI foi descontinuado em dezembro de 2023, tornando-se incompatível com as novas versões do PyTorch e do Python. O comando `pip install TTS` falhava ou não encontrava distribuições compatíveis.
- **Solução**: Migração completa para o pacote `coqui-tts` (`pip install coqui-tts==0.27.3`), garantindo que o namespace `TTS` fosse preservado no código (importações como `from TTS.api import TTS` continuam funcionando), mas utilizando binários modernos mantidos pela comunidade.
- **Impacto no TCC**: Exemplifica como projetos open source podem ser descontinuados e depender de forks comunitários para sobreviver.

### 2.2 Conflitos de versão entre transformers/huggingface-hub

- **Problema**: O `coqui-tts` tem dependências pesadas (`torch`, `transformers`, `huggingface-hub`) que conflitam com versões pré-instaladas no Colab. Instalar tudo junto causava erros de incompatibilidade.
- **Solução**: Célula 2 desinstala versões conflitantes e reinstala com versões pinadas (`transformers==4.57.1`, `huggingface-hub==0.36.0`). Célula 3 faz **verificação explícita** das versões carregadas no ambiente.
- **Erro típico**: `ModuleNotFoundError: No module named 'TTS'` → re-executar Célula 2 + reiniciar runtime.

### 2.3 Erros de compilação do OpenAI Whisper no Python 3.12

- **Problema**: A instalação do Whisper via `pip` padrão falhava no estágio de "building wheel". O erro `subprocess-exited-with-error` era causado pela falta de ferramentas de build compatíveis com Rust ou por dependências como `tiktoken` sem wheels pré-compiladas para Python 3.12.
- **Solução**: Instalação direta do repositório Git oficial do Whisper (`pip install git+https://github.com/openai/whisper.git`), que contém correções de compatibilidade em tempo real.

---

## 🔴 Categoria 3 — Mudanças de API nos Modelos TTS

### 3.1 Mudança na estrutura de atributos do Piper TTS (v1.3 → v1.4+)

- **Problema**: A atualização da biblioteca `piper-tts` da versão 1.3 para 1.4+ alterou a forma como os metadados do modelo são acessados. O erro `AttributeError: 'PiperVoice' object has no attribute 'sample_rate'` ocorria porque a taxa de amostragem foi movida para dentro de um objeto de configuração.
- **Solução**: Ajuste da chamada para `piper_voice.config.sample_rate` e alteração do construtor para o método de fábrica `PiperVoice.load(model_path, config_path)`.
- **Impacto no TCC**: Ilustra como mesmo atualizações menores de biblioteca podem quebrar código funcional.

### 3.2 Cada modelo TTS tem interface de código completamente diferente

- **Problema**: Não existe padrão entre os modelos TTS — XTTS usa `TTS.api`, Piper usa `PiperVoice`, Kokoro usa `kokoro_onnx.Kokoro`. Cada um gera áudio de forma diferente.
- **Solução**: Criamos funções wrapper padronizadas (`run_piper()`, `run_kokoro()`, `run_xtts()`) que recebem texto e retornam caminho do áudio + tempo de execução, uniformizando a interface para o loop de benchmark.

---

## 🔴 Categoria 4 — Download e Integridade de Dados

### 4.1 Hugging Face entregando HTML em vez de arquivos binários

- **Problema**: Ao utilizar `wget` para baixar modelos e arquivos de configuração (`.json`), o servidor do Hugging Face frequentemente entregava páginas HTML (a interface visual do repositório) em vez do conteúdo bruto. Isso causava `JSONDecodeError` ao tentar ler os arquivos.
- **Solução**: Implementação de URLs de resolução direta com o parâmetro `?download=true` (ex: `https://huggingface.co/.../resolve/v1.0.0/pt_BR-cadu-medium.onnx?download=true`), forçando o download dos arquivos binários.

### 4.2 Downloads de ~2,2 GB instáveis no Colab gratuito

- **Problema**: Os 3 modelos somam ~2,2 GB (XTTS 1,8 GB + Kokoro 326 MB + Piper 63 MB). Downloads podem falhar por timeout ou instabilidade de rede. Além disso, **cada nova sessão do Colab perde os arquivos**.
- **Solução**: Célula 4 faz downloads separados com verificação de existência e tamanho (`os.path.exists` + `os.path.getsize`), evitando re-downloads desnecessários caso a célula seja re-executada. XTTS baixa automaticamente ao carregar via `TTS.api`.

---

## 🔴 Categoria 5 — Lógica de Implementação e Erros de Código

### 5.1 Erros de sintaxe em estruturas de dados

- **Problema**: Erros de `SyntaxError` ao tentar inicializar listas de resultados e funções de modelos de forma incompleta (ex: `resultados =` sem valor, tuplas malformadas).
- **Solução**: Correção da sintaxe de declaração de listas vazias (`resultados = []`) e listas de tuplas (`modelos_funcs = [("Nome", funcao)]`) para permitir que o loop de avaliação percorresse todos os modelos sem interrupções.

### 5.2 XTTS v2 requer áudio de referência para clonagem zero-shot

- **Problema**: O XTTS v2 exige um arquivo de áudio de referência (`speaker_wav`) para gerar voz. Se o arquivo não existisse, a síntese falhava.
- **Solução**: A função `run_xtts()` verifica se o arquivo de referência existe; caso contrário, gera automaticamente um usando o Piper (o modelo mais rápido) antes de prosseguir com a síntese XTTS.

---

## 🔴 Categoria 6 — Seleção e Justificativa Acadêmica dos Modelos

### 6.1 Escolher quais modelos avaliar entre dezenas de opções

- **Problema**: Existem muitos modelos TTS open source. Precisávamos de critérios claros e academicamente defensáveis.
- **Solução**: Definimos 6 critérios objetivos de seleção: (1) Open source, (2) Suporte nativo a pt-BR, (3) Execução offline, (4) Execução em CPU, (5) Arquitetura neural moderna, (6) Diversidade arquitetural. Eliminamos gTTS/edge-tts (wrappers de API), Bark (pesado demais), MMS (qualidade inferior em pt-BR).
- **Resultado**: 3 modelos representando 3 paradigmas: XTTS v2 (GPT+HiFiGAN), Piper (VITS), Kokoro (StyleTTS2).

### 6.2 Falta de referências bibliográficas para fundamentar as escolhas

- **Problema**: As escolhas dos modelos precisavam de papers para o TCC, e o aluno não havia anotado as referências.
- **Solução**: Pesquisamos e identificamos os papers de cada modelo (Casanova et al./Interspeech 2024, Kim et al./ICML 2021, Li et al./NeurIPS 2023, Radford et al./OpenAI 2022) e formatamos em ABNT NBR 6023:2018.

---

## 🔴 Categoria 7 — Execução do Benchmark e Resultados

### 7.1 Latência proibitiva do XTTS v2 em CPU

- **Problema**: O XTTS v2 usa arquitetura GPT autoregressiva — cada frase levava em média **42 segundos** em CPU. O benchmark de 140 frases tomava ~1,6 horas só para o XTTS.
- **Solução**: Mantivemos no benchmark (relevante academicamente), documentamos a limitação e sugerimos reduzir o corpus para testes rápidos.
- **Achado para o TCC**: XTTS v2 é impraticável para uso em tempo real sem GPU.

### 7.2 Sessão do Colab desconectando durante benchmark longo

- **Problema**: O benchmark completo (420 sínteses) levava 2-4 horas. O Colab gratuito desconecta por inatividade (~90 min).
- **Solução**: Salvamento incremental dos resultados + opção de montar Google Drive + documentação de como retomar a partir da Célula 5.

### 7.3 Ausência de corpus padronizado para TTS em pt-BR

- **Problema**: Não existia corpus de teste para TTS em português brasileiro com foco em acessibilidade.
- **Solução**: Construímos corpus com **14 categorias** e **140 frases** cobrindo: curtas/médias/longas, números, datas, nomes próprios, siglas, regionalismos, termos técnicos, code-switching, pontuação.

---

## 🔴 Categoria 8 — Documentação e Organização

### 8.1 Falta de registro do processo durante o desenvolvimento

- **Problema**: O aluno foi resolvendo problemas sem anotar decisões e dificuldades. Na hora de escrever o TCC, não tinha registro.
- **Solução**: Reconstruímos o histórico a partir das conversas com IA, commits e estrutura do notebook. Criamos `docs/` completa.
- **Aprendizado**: **Sempre manter um diário de pesquisa desde o início.**

---

## 💡 Parágrafo consolidado para o TCC (seção "Dificuldades e Limitações")

> *Durante o desenvolvimento do experimento, diversas dificuldades técnicas foram encontradas e superadas, evidenciando os desafios inerentes à pesquisa reprodutível com modelos de Inteligência Artificial em rápida evolução. As principais incluem: (1) a atualização do Google Colab para Python 3.12, que gerou incompatibilidades com bibliotecas legadas, exigindo a migração do pacote descontinuado `TTS` para o fork comunitário `coqui-tts`; (2) conflitos de versão entre `transformers` e `huggingface-hub`, resolvidos com pinagem explícita de dependências; (3) a mudança de API na biblioteca `piper-tts` entre as versões 1.3 e 1.4, que alterou o acesso à taxa de amostragem do modelo; (4) falhas de download no Hugging Face, que entregava páginas HTML em vez de arquivos binários, resolvidas com URLs de resolução direta; (5) erros de compilação do Whisper no Python 3.12, mitigados pela instalação via repositório Git; (6) latência elevada do modelo XTTS v2 em CPU (~42s por frase), inerente à arquitetura GPT autoregressiva; (7) instabilidade da sessão do Colab gratuito durante benchmarks longos, mitigada com salvamento incremental; e (8) ausência de corpus padronizado para avaliação de TTS em pt-BR, resolvida com a criação de um conjunto de 140 frases em 14 categorias. Essas dificuldades reforçam a importância da documentação detalhada e do uso de formatos portáveis como ONNX, que são menos dependentes de versões específicas de frameworks.*
