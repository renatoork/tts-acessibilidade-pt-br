# ANÁLISE E DISCUSSÃO DOS RESULTADOS

---

## 1. VISÃO GERAL DO BENCHMARK

O presente capítulo analisa os resultados obtidos no benchmark comparativo entre três sistemas de *Text-to-Speech* (TTS) de código aberto com suporte ao português brasileiro: **Kokoro**, **Piper** e **XTTS v2**. O experimento totalizou **420 sínteses** (3 modelos × 140 frases × 14 categorias linguísticas), executadas em ambiente de CPU exclusiva (*CPU-only*) no Google Colab, sem aceleração por GPU, de modo a simular condições de uso acessível e de baixo custo computacional.

A metodologia de avaliação adotou o paradigma de transcrição reversa: cada áudio gerado pelos modelos TTS foi transcrito automaticamente pelo *Whisper* (OpenAI), e o texto transcrito foi comparado com o texto original por meio da métrica *Word Error Rate* (WER), calculada pela biblioteca `jiwer`. Essa abordagem é amplamente adotada na literatura de avaliação objetiva de sistemas TTS quando avaliações perceptivas com ouvintes humanos (*Mean Opinion Score* — MOS) não são viáveis na escala do experimento.

### Tabela 1 — Resumo Geral por Modelo

| Modelo | Qtde. sínteses | Latência média (s) | Latência DP | WER médio | WER DP |
|--------|---------------:|-------------------:|------------:|----------:|-------:|
| Piper  | 140            | 0,5541             | 0,2762      | 0,1848    | 0,2010 |
| Kokoro | 140            | 4,2818             | 2,3184      | 0,1767    | 0,2233 |
| XTTS   | 140            | 25,8830            | 14,5340     | 0,2078    | 0,2379 |

Os dados evidenciam um *trade-off* marcante: o Piper é o mais rápido (latência média de 0,55 s) porém com WER levemente superior ao Kokoro; o Kokoro apresenta o menor WER (0,1767) com latência intermediária (~4,3 s); e o XTTS, apesar de ser o modelo mais expressivo arquiteturalmente, apresenta a pior combinação de latência (~25,9 s) e WER (0,2078) no ambiente CPU-only.

---

## 2. ESTATÍSTICAS DESCRITIVAS

A Tabela 2 apresenta o conjunto completo de estatísticas descritivas calculadas para os três modelos, incluindo medidas de tendência central, dispersão, coeficiente de variação (CV), intervalos de confiança a 95% (IC95), taxa de sínteses com WER igual a zero, *throughput* médio em caracteres por segundo e *Character Error Rate* (CER).

### Tabela 2 — Estatísticas Descritivas Completas

| Métrica                         | Piper   | Kokoro  | XTTS    |
|---------------------------------|--------:|--------:|--------:|
| **WER médio**                   | 0,1848  | 0,1767  | 0,2078  |
| WER mediana                     | 0,1250  | 0,1180  | 0,1291  |
| WER desvio padrão               | 0,2010  | 0,2233  | 0,2379  |
| WER mínimo                      | 0,0     | 0,0     | 0,0     |
| WER máximo                      | 1,0     | 1,8     | 1,8     |
| WER CV (%)                      | 108,8   | 126,4   | 114,5   |
| WER IC95 inferior               | 0,1515  | 0,1397  | 0,1684  |
| WER IC95 superior               | 0,2181  | 0,2137  | 0,2472  |
| **Latência média (s)**          | 0,554   | 4,282   | 25,883  |
| Latência mediana (s)            | 0,492   | 3,690   | 22,483  |
| Latência desvio padrão          | 0,276   | 2,318   | 14,534  |
| Latência mínima (s)             | 0,165   | 1,021   | 7,349   |
| Latência máxima (s)             | 1,732   | 12,654  | 77,450  |
| Latência CV (%)                 | 49,8    | 54,1    | 56,2    |
| Latência IC95 inferior (s)      | 0,508   | 3,898   | 23,475  |
| Latência IC95 superior (s)      | 0,600   | 4,666   | 28,291  |
| **Taxa WER zero (%)**           | 25,7    | 31,4    | 21,4    |
| **Throughput médio (char/s)**   | 123,06  | 16,09   | 2,73    |
| **CER médio**                   | 0,0895  | 0,0821  | 0,1224  |

**Análise das métricas:**

- **WER médio e mediana:** A mediana do WER é substancialmente inferior à média em todos os modelos (ex.: Piper: 0,125 vs. 0,1848), indicando distribuição assimétrica à direita — a maioria das frases é sintetizada com boa inteligibilidade, mas um subconjunto de frases problemáticas eleva a média.

- **Coeficiente de variação (CV):** Os valores de CV para WER superam 100% nos três modelos, o que reflete alta heterogeneidade entre categorias linguísticas. Isso indica que o WER médio isolado é insuficiente para caracterizar o desempenho — a análise por categoria (Seção 5) é essencial.

- **Intervalos de confiança (IC95):** Os IC95 para WER dos modelos se sobrepõem parcialmente (Piper: [0,1515; 0,2181], Kokoro: [0,1397; 0,2137], XTTS: [0,1684; 0,2472]), sugerindo que as diferenças entre Piper e Kokoro podem não ser estatisticamente robustas — hipótese confirmada pelos testes estatísticos (Seção 7).

- **Latência CV:** O CV da latência do XTTS (56,2%) é o mais alto entre os modelos, refletindo a alta variabilidade do tempo de síntese por frase, característica inerente à arquitetura GPT autoregressiva.

- **Taxa WER zero:** O Kokoro lidera com 31,4% das frases transcritas sem nenhum erro, seguido pelo Piper (25,7%) e XTTS (21,4%). Esse indicador é especialmente relevante para acessibilidade, pois representa a proporção de sínteses consideradas perfeitas pelo avaliador automático.

- **Throughput:** O Piper gera em média 123,06 caracteres por segundo, contra 16,09 do Kokoro e apenas 2,73 do XTTS — ratios que têm implicações diretas para aplicações em tempo real.

---

## 3. ANÁLISE DE INTELIGIBILIDADE (WER)

A *Word Error Rate* (WER) é a métrica primária utilizada para avaliar a inteligibilidade dos sistemas TTS neste estudo. O WER representa a proporção de palavras incorretamente transcritas em relação ao total de palavras da referência, sendo calculado como:

> WER = (S + D + I) / N

onde S = substituições, D = deleções, I = inserções e N = número total de palavras na referência.

### 3.1 Comparação Global de WER

Os três modelos apresentam WER médio entre 17,67% e 20,78%:

- **Kokoro:** WER = **0,1767** (melhor desempenho)
- **Piper:** WER = **0,1848** (+0,81 p.p. em relação ao Kokoro)
- **XTTS:** WER = **0,2078** (+3,11 p.p. em relação ao Kokoro)

Para o contexto de acessibilidade, um WER de ~18% significa que, em média, aproximadamente 1 em cada 5 palavras pode ser transcrita incorretamente pelo Whisper. Considerando que o Whisper também comete erros próprios (que se somam aos do TTS), o WER efetivo percebido pelo usuário final tende a ser menor do que os valores absolutos sugerem.

A diferença entre Kokoro e Piper (0,0081) é pequena em termos absolutos e, como demonstrado na Seção 7, não é estatisticamente significativa (p = 1,0 no teste de Dunn). Isso implica que, para efeitos práticos de inteligibilidade, ambos os modelos são equivalentes.

### 3.2 Character Error Rate (CER)

O *Character Error Rate* (CER) complementa o WER ao avaliar erros no nível de caracteres, sendo mais sensível a erros em palavras curtas ou siglas:

| Modelo | CER médio |
|--------|----------:|
| Kokoro | 0,0821    |
| Piper  | 0,0895    |
| XTTS   | 0,1224    |

O Kokoro apresenta novamente o melhor desempenho (CER 0,0821), seguido de perto pelo Piper (0,0895). O XTTS apresenta CER significativamente superior (0,1224), o que indica maior taxa de erros em nível de caracteres — possivelmente relacionada à geração de inserções espúrias (ver Seção 6).

### 3.3 Taxa de Sínteses Perfeitas (WER Zero)

A taxa de WER zero indica a proporção de frases em que a transcrição gerada pelo Whisper coincide exatamente com o texto original:

| Modelo | Taxa WER zero (%) |
|--------|------------------:|
| Kokoro | 31,4              |
| Piper  | 25,7              |
| XTTS   | 21,4              |

O Kokoro alcançou transcrição perfeita em 44 de 140 frases (31,4%), demonstrando robustez na síntese de voz em português brasileiro. O XTTS ficou atrás com 21,4%, refletindo maior propensão a erros de articulação e inserções.

### 3.4 Implicações para Acessibilidade

Para usuários com deficiência visual que dependem de leitores de tela, ou para pessoas com dificuldades de leitura que utilizam TTS como auxílio cognitivo, a inteligibilidade é o critério mais crítico. Um WER próximo a 18% pode, em cenários práticos, ser tolerável para sínteses de frases curtas e de uso cotidiano, mas se torna problemático em contextos que exigem precisão absoluta, como leitura de bulas de medicamentos, contratos ou informações médicas. Nesses casos, a taxa de WER zero ganha relevância central.

---

## 4. ANÁLISE DE LATÊNCIA (VELOCIDADE DE SÍNTESE)

A latência de síntese é o tempo decorrido entre o início do processamento de um texto e a disponibilização do áudio correspondente. Em aplicações de acessibilidade, especialmente aquelas que exigem resposta em tempo real (como leitores de tela e interfaces conversacionais), a latência é frequentemente um requisito mais crítico do que a qualidade da voz.

### 4.1 Comparação Global de Latência

| Modelo | Latência média (s) | Mediana (s) | Mínima (s) | Máxima (s) |
|--------|-------------------:|------------:|-----------:|-----------:|
| Piper  | 0,554              | 0,492       | 0,165      | 1,732      |
| Kokoro | 4,282              | 3,690       | 1,021      | 12,654     |
| XTTS   | 25,883             | 22,483      | 7,349      | 77,450     |

As razões de latência são expressivas:

- O **XTTS é aproximadamente 46,7× mais lento que o Piper** (25,883 / 0,554 ≈ 46,7)
- O **XTTS é aproximadamente 6,0× mais lento que o Kokoro** (25,883 / 4,282 ≈ 6,0)
- O **Kokoro é aproximadamente 7,7× mais lento que o Piper** (4,282 / 0,554 ≈ 7,7)

A latência mínima do XTTS (7,349 s) é superior à latência máxima observada para o Piper (1,732 s), o que demonstra que mesmo para as frases mais curtas e simples, o XTTS impõe um atraso mínimo que inviabiliza aplicações em tempo real sem aceleração por GPU.

### 4.2 Throughput

O *throughput*, expresso em caracteres por segundo, oferece uma perspectiva normalizada da velocidade de síntese independente do comprimento das frases:

| Modelo | Throughput médio (char/s) | Razão vs. Piper |
|--------|-------------------------:|----------------:|
| Piper  | 123,06                   | 1,0×            |
| Kokoro | 16,09                    | 0,13×           |
| XTTS   | 2,73                     | 0,02×           |

O Piper gera texto falado a uma taxa ~7,6× superior ao Kokoro e ~45× superior ao XTTS. Esses números contextualizam claramente por que o Piper é o modelo de referência para aplicações de acessibilidade em tempo real.

### 4.3 Implicações para Acessibilidade em Tempo Real

Para que um sistema TTS seja percebido como "tempo real" pelo usuário, a latência deve ser inferior a aproximadamente 300 ms para respostas interativas, ou inferior a 1-2 segundos para leitura de textos. Apenas o **Piper** atende consistentemente a esse limiar (latência mediana de 492 ms). O Kokoro, com latência mediana de 3,69 s, pode ser aceitável para leitura de textos longos, audiolivros ou conteúdo pré-gerado. O XTTS, com latência mediana de 22,5 s em CPU, é inadequado para qualquer aplicação interativa sem GPU.

A diferença de latência entre os modelos é **estatisticamente significativa** (Kruskal-Wallis: H = 370,4574, p < 0,001), conforme detalhado na Seção 7.

---

## 5. ANÁLISE POR CATEGORIA LINGUÍSTICA

O corpus de avaliação foi estruturado em **14 categorias linguísticas** com 10 frases cada, cobrindo fenômenos fonéticos, morfossintáticos e de uso que representam desafios específicos para sistemas TTS em português brasileiro.

### Tabela 3 — WER e Latência por Modelo e Categoria

| Categoria                      | Piper WER | Piper Lat (s) | Kokoro WER | Kokoro Lat (s) | XTTS WER | XTTS Lat (s) |
|-------------------------------|----------:|--------------:|-----------:|---------------:|---------:|-------------:|
| curtas_objetivas              | 0,1083    | 0,236         | 0,1033     | 1,668          | 0,1833   | 10,185       |
| datas_horarios                | 0,1142    | 0,552         | 0,0688     | 4,615          | 0,1527   | 26,153       |
| enderecos_urls_emails         | 0,3306    | 0,592         | 0,5079     | 4,137          | 0,4219   | 27,423       |
| ingles_e_code_switching       | 0,2614    | 0,430         | 0,1701     | 3,270          | 0,2151   | 20,945       |
| interrogativas_e_exclamativas | 0,1355    | 0,408         | 0,1619     | 3,074          | 0,1567   | 15,694       |
| longas_narrativas             | 0,1036    | 1,427         | 0,0467     | 11,699         | 0,0740   | 70,177       |
| medias_informativas           | 0,0874    | 0,646         | 0,0357     | 5,095          | 0,1506   | 30,965       |
| nomes_internacionais          | 0,5089    | 0,399         | 0,3970     | 3,272          | 0,3190   | 20,150       |
| nomes_proprios_brasileiros    | 0,2236    | 0,408         | 0,1369     | 3,154          | 0,2694   | 17,417       |
| numeros_medidas_moedas        | 0,1104    | 0,588         | 0,1968     | 4,343          | 0,1879   | 25,346       |
| pontuacao_e_pausas            | 0,1938    | 0,476         | 0,2354     | 3,506          | 0,1786   | 21,425       |
| regionalismos_e_girias        | 0,0889    | 0,451         | 0,1163     | 3,082          | 0,1898   | 19,124       |
| siglas_e_abreviacoes          | 0,1699    | 0,495         | 0,1521     | 3,643          | 0,2186   | 23,549       |
| termos_tecnicos_academicos    | 0,1503    | 0,651         | 0,1451     | 5,389          | 0,1918   | 33,807       |

### Tabela 4 — Ranking por Categoria (melhor modelo em WER e Latência)

| Categoria                      | Melhor WER (modelo) | Melhor WER (valor) | Melhor Latência (modelo) | Melhor Lat. (s) |
|-------------------------------|--------------------:|-------------------:|-------------------------:|----------------:|
| curtas_objetivas              | Kokoro              | 0,1033             | Piper                    | 0,236           |
| datas_horarios                | Kokoro              | 0,0688             | Piper                    | 0,552           |
| enderecos_urls_emails         | Piper               | 0,3306             | Piper                    | 0,592           |
| ingles_e_code_switching       | Kokoro              | 0,1701             | Piper                    | 0,430           |
| interrogativas_e_exclamativas | Piper               | 0,1355             | Piper                    | 0,408           |
| longas_narrativas             | Kokoro              | 0,0467             | Piper                    | 1,427           |
| medias_informativas           | Kokoro              | 0,0357             | Piper                    | 0,646           |
| nomes_internacionais          | XTTS                | 0,3190             | Piper                    | 0,399           |
| nomes_proprios_brasileiros    | Kokoro              | 0,1369             | Piper                    | 0,408           |
| numeros_medidas_moedas        | Piper               | 0,1104             | Piper                    | 0,588           |
| pontuacao_e_pausas            | XTTS                | 0,1786             | Piper                    | 0,476           |
| regionalismos_e_girias        | Piper               | 0,0889             | Piper                    | 0,451           |
| siglas_e_abreviacoes          | Kokoro              | 0,1521             | Piper                    | 0,495           |
| termos_tecnicos_academicos    | Kokoro              | 0,1451             | Piper                    | 0,651           |

### 5.1 Distribuição de Vitórias por WER

- **Kokoro vence em WER em 8 categorias** (57,1%): curtas_objetivas, datas_horarios, ingles_e_code_switching, longas_narrativas, medias_informativas, nomes_proprios_brasileiros, siglas_e_abreviacoes, termos_tecnicos_academicos
- **Piper vence em WER em 4 categorias** (28,6%): enderecos_urls_emails, interrogativas_e_exclamativas, numeros_medidas_moedas, regionalismos_e_girias
- **XTTS vence em WER em 2 categorias** (14,3%): nomes_internacionais, pontuacao_e_pausas

**O Piper vence em latência em todas as 14 categorias (100%).**

### 5.2 Categorias Problemáticas

As categorias com WER mais elevado em todos os modelos merecem atenção especial:

- **enderecos_urls_emails:** WER médio de ~0,42 (Piper: 0,3306; Kokoro: 0,5079; XTTS: 0,4219). Endereços eletrônicos, URLs e e-mails contêm caracteres especiais (@, /, .) e palavras em inglês que desafiam os sistemas de pronúncia em português. Este é o pior desempenho do Kokoro em qualquer categoria.

- **nomes_internacionais:** WER médio de ~0,41 (Piper: 0,5089; Kokoro: 0,3970; XTTS: 0,3190). Nomes de origem estrangeira apresentam regras de pronúncia divergentes do português, e a transcrição pelo Whisper pode grafar diferentemente do texto original, penalizando o WER mesmo quando a pronúncia está aceitável.

### 5.3 Categorias com Melhor Desempenho

- **medias_informativas:** Kokoro alcança WER de apenas 0,0357 — o melhor resultado individual do benchmark. Frases informativas de comprimento médio, com vocabulário comum, parecem representar o cenário ideal para o modelo.

- **longas_narrativas:** Surpreendentemente, as frases mais longas apresentam WER baixo (Kokoro: 0,0467; XTTS: 0,0740; Piper: 0,1036), possivelmente porque textos mais longos fornecem mais contexto fonético e são mais facilmente reconhecidos pelo Whisper.

- **datas_horarios:** Kokoro apresenta WER de 0,0688, indicando excelente pronúncia de datas e horários em português.

---

## 6. ANÁLISE DE ERROS — TIPOS DE ERRO

A análise dos tipos de erro de WER (substituições, deleções e inserções) oferece *insights* qualitativos sobre os padrões de falha de cada modelo TTS.

### Tabela 5 — Distribuição de Tipos de Erro

| Modelo | Subst. (S) | Del. (D) | Ins. (I) | Total erros | S (%) | D (%) | I (%) | Total palavras | Acertos (%) |
|--------|----------:|---------:|---------:|------------:|------:|------:|------:|---------------:|------------:|
| Piper  | 347       | 11       | 59       | 417         | 83,2  | 2,6   | 14,1  | 1.553          | 73,1        |
| Kokoro | 327       | 9        | 59       | 395         | 82,8  | 2,3   | 14,9  | 1.553          | 74,6        |
| XTTS   | 360       | 11       | 77       | 448         | 80,4  | 2,5   | 17,2  | 1.571          | 71,5        |

### 6.1 Substituições — O Tipo de Erro Dominante

As **substituições** representam entre 80,4% e 83,2% de todos os erros, sendo o tipo de erro predominante nos três modelos. Uma substituição ocorre quando uma palavra é pronunciada de forma que o Whisper a transcreve como uma palavra diferente da referência. Esse padrão é característico de erros de pronúncia parcial, onde o modelo TTS sintetiza um som próximo mas não idêntico ao correto — situação comum com palavras estrangeiras, nomes próprios e termos técnicos.

Para acessibilidade, substituições são os erros de maior impacto semântico: enquanto uma deleção pode ser percebida como pausa ou engasgo, uma substituição pode alterar completamente o significado do enunciado.

### 6.2 Inserções — Padrão de "Alucinação" no XTTS

O XTTS apresenta a maior taxa de **inserções** (17,2%, total de 77 inserções), contra 14,1% do Piper e 14,9% do Kokoro. Inserções ocorrem quando o modelo sintetiza sons adicionais não presentes no texto de referência — comportamento análogo às "alucinações" observadas em modelos de linguagem generativos. A arquitetura GPT autoregressiva do XTTS v2, que gera tokens de áudio sequencialmente baseando-se em contexto anterior, é mais propensa a esse tipo de erro do que as arquiteturas determinísticas do Piper (VITS) e Kokoro (StyleTTS2).

### 6.3 Deleções — Impacto Reduzido

As **deleções** representam apenas 2,3% a 2,6% dos erros em todos os modelos, sendo o tipo menos frequente. Uma deleção ocorre quando o modelo omite uma palavra ou sílaba, resultando em silêncio ou pausa inesperada. Esse padrão é relativamente raro e pode estar associado a palavras muito curtas ou átonas que o modelo "engole" na síntese.

### 6.4 Taxa de Acertos Global

A taxa de acertos por palavra (corretamente transcrita pelo Whisper) é:

- **Kokoro:** 74,6% (1.158 de 1.553 palavras)
- **Piper:** 73,1% (1.136 de 1.553 palavras)
- **XTTS:** 71,5% (1.123 de 1.571 palavras)

Esses valores indicam que, em contexto real de uso, cerca de 3 em cada 4 palavras são inteligíveis de acordo com o avaliador automático, com margem de superioridade para o Kokoro.

---

## 7. TESTES ESTATÍSTICOS

Para verificar a significância estatística das diferenças observadas entre os modelos, foram aplicados testes não-paramétricos, adequados à natureza assimétrica e potencialmente não-normal das distribuições de WER e latência.

### Tabela 6 — Resultados dos Testes Estatísticos

| Teste                     | Métrica  | Estatística (H/ρ) | p-valor    | Significativo (p < 0,05) |
|---------------------------|----------|------------------:|------------|:------------------------:|
| Kruskal-Wallis            | WER      | H = 2,1391        | 0,3432     | Não                      |
| Kruskal-Wallis            | Latência | H = 370,4574      | < 0,001    | **Sim**                  |
| Dunn (Piper vs. Kokoro)   | WER      | —                 | 1,0        | Não                      |
| Dunn (Piper vs. Kokoro)   | Latência | —                 | < 0,001    | **Sim**                  |
| Dunn (Kokoro vs. XTTS)    | WER      | —                 | 0,4309     | Não                      |
| Dunn (Kokoro vs. XTTS)    | Latência | —                 | < 0,001    | **Sim**                  |
| Dunn (Piper vs. XTTS)     | WER      | —                 | 1,0        | Não                      |
| Dunn (Piper vs. XTTS)     | Latência | —                 | < 0,001    | **Sim**                  |
| Spearman (Piper)          | Npal×WER | ρ = −0,1278       | 0,1323     | Não                      |
| Spearman (Kokoro)         | Npal×WER | ρ = −0,2233       | 0,0080     | **Sim**                  |
| Spearman (XTTS)           | Npal×WER | ρ = −0,0935       | 0,2720     | Não                      |

### 7.1 Kruskal-Wallis para WER

O teste de Kruskal-Wallis aplicado ao WER resultou em H = 2,1391 e p = 0,3432, **não rejeitando a hipótese nula** de que as distribuições de WER dos três modelos são equivalentes. Em termos práticos, isso significa que **os três modelos não diferem significativamente em termos de inteligibilidade** quando avaliados sobre o corpus completo de 140 frases.

Esse resultado é relevante: embora existam diferenças numéricas nos WER médios (0,1767 a 0,2078), essas diferenças não são estatisticamente distinguíveis da variabilidade aleatória do experimento. A heterogeneidade dentro de cada modelo (CV > 100%) supera a variabilidade entre modelos.

### 7.2 Kruskal-Wallis para Latência

O teste de Kruskal-Wallis para latência produziu H = 370,4574 e p < 0,001 (arredondado para zero na precisão numérica utilizada), **rejeitando a hipótese nula** com altíssima significância. Os três modelos diferem dramaticamente em termos de velocidade de síntese — resultado esperado dadas as diferenças arquiteturais fundamentais entre VITS (Piper), StyleTTS2 (Kokoro) e GPT+HiFiGAN (XTTS).

### 7.3 Testes Post-Hoc de Dunn para Latência

O teste de Dunn com correção de Bonferroni confirmou que **todas as três comparações par a par de latência são estatisticamente significativas** (p < 0,001):

- Piper vs. Kokoro: diferença de ~3,7 s em média, p < 0,001
- Kokoro vs. XTTS: diferença de ~21,6 s em média, p < 0,001
- Piper vs. XTTS: diferença de ~25,3 s em média, p < 0,001

Para WER, nenhuma comparação par a par foi significativa (p ≥ 0,4309), confirmando que os modelos são estatisticamente equivalentes em inteligibilidade.

---

## 8. CORRELAÇÃO ENTRE TAMANHO DA FRASE E ERROS

O teste de correlação de Spearman foi aplicado para investigar se existe relação entre o número de palavras de uma frase (*NumPalavras*) e seu WER. A hipótese intuitiva seria que frases mais longas são mais difíceis de sintetizar e transcrever, resultando em maior WER.

### 8.1 Resultados

Os resultados do Spearman (Tabela 6) revelam um padrão contrário à intuição inicial:

- **Kokoro:** ρ = −0,2233, p = 0,008 — **correlação negativa significativa**
- **Piper:** ρ = −0,1278, p = 0,1323 — correlação negativa não significativa
- **XTTS:** ρ = −0,0935, p = 0,2720 — correlação negativa não significativa

### 8.2 Interpretação

O único modelo que apresentou correlação estatisticamente significativa foi o **Kokoro**, com correlação negativa de intensidade fraca a moderada (ρ = −0,2233). Isso indica que, para o Kokoro, **frases mais longas tendem a apresentar WER menor** — resultado aparentemente contraintuitivo, mas explicável por diversos mecanismos:

1. **Contexto fonético:** Frases mais longas fornecem mais contexto para o modelo de síntese, permitindo melhor modelagem de prosódia e coarticulação.

2. **Efeito de diluição de erros:** Uma única substituição ou inserção em uma frase de 30 palavras tem impacto percentual menor no WER do que o mesmo erro em uma frase de 5 palavras.

3. **Natureza do corpus:** As categorias com frases mais longas (longas_narrativas, medias_informativas) tendem a usar vocabulário comum e fonologia mais regular do português, enquanto categorias com frases curtas (enderecos_urls_emails, nomes_internacionais) contêm termos tecnicamente difíceis.

A ausência de correlação significativa para Piper e XTTS sugere que esses modelos são relativamente robustos ao comprimento da frase em termos de WER, embora por razões diferentes: o Piper é determinístico e estável; o XTTS tem variabilidade alta que mascara a tendência.

---

## 9. TRADE-OFF QUALIDADE × VELOCIDADE

A escolha do modelo TTS ideal para uma aplicação de acessibilidade não pode ser baseada em uma única métrica. A Tabela 7 sintetiza as principais métricas comparativas para apoiar decisões de projeto.

### Tabela 7 — Síntese Comparativa Final

| Métrica                   | Piper       | Kokoro     | XTTS       | Melhor      |
|---------------------------|-------------|------------|------------|-------------|
| WER médio                 | 0,1848      | **0,1767** | 0,2078     | Kokoro      |
| Latência média (s)        | **0,554**   | 4,282      | 25,883     | Piper       |
| Throughput (char/s)       | **123,06**  | 16,09      | 2,73       | Piper       |
| CER médio                 | 0,0895      | **0,0821** | 0,1224     | Kokoro      |
| Taxa WER zero (%)         | 25,7        | **31,4**   | 21,4       | Kokoro      |
| Acertos por palavra (%)   | 73,1        | **74,6**   | 71,5       | Kokoro      |
| Vitórias WER (categorias) | 4           | **8**      | 2          | Kokoro      |
| Vitórias latência (cat.)  | **14**      | 0          | 0          | Piper       |
| Custo computacional       | **Baixo**   | Médio      | Alto       | Piper       |

**Recomendações por cenário de uso:**

- **Tempo real / interativo (leitores de tela, semáforos sonoros):** Piper — único modelo com latência compatível com tempo real em CPU
- **Conteúdo de média duração (e-learning, newsletters):** Kokoro — melhor WER com latência tolerável para pré-geração
- **Conteúdo longo / expressivo / com GPU disponível:** XTTS — arquitetura mais expressiva, mas requer GPU para uso prático
- **Ambiente offline embarcado (IoT, dispositivos sem internet):** Piper — modelo ONNX leve (~63 MB), adequado para hardware limitado

---

## 10. APLICAÇÕES PRÁTICAS — CENÁRIOS DE USO

Com base nos resultados quantitativos do benchmark, é possível mapear cenários de aplicação concretos para cada modelo, considerando suas respectivas vantagens comparativas.

### 10.1 Piper — Aplicações de Tempo Real e Baixo Custo

O Piper é recomendado para cenários que exigem **resposta imediata** e funcionamento em hardware limitado:

1. **Leitores de tela para deficientes visuais:** Com latência mediana de 492 ms, o Piper permite leitura de elementos de interface sem atraso perceptível, sendo adequado para substituir soluções comerciais em sistemas operacionais de código aberto.

2. **Semáforos e sinais sonoros urbanos:** Dispositivos embarcados em infraestrutura urbana (semáforos acessíveis, totens de informação) podem executar o Piper localmente, sem necessidade de conectividade à internet.

3. **Terminais de autoatendimento:** Quiosques de banco, saúde e serviços públicos podem integrar o Piper para atender usuários com dificuldades de leitura, processando solicitações em tempo real.

4. **Notificações em tempo real:** Sistemas de alerta (emergências, transportes públicos) que precisam sintetizar mensagens dinâmicas com latência mínima.

5. **Dispositivos IoT acessíveis:** O modelo ONNX do Piper (~63 MB) pode ser executado em microcontroladores com Linux embarcado (Raspberry Pi e similares), viabilizando assistentes de voz offline para pessoas com deficiência.

6. **Audiodescrição ao vivo:** Sistemas de audiodescrição para transmissões ao vivo ou eventos presenciais, onde o atraso deve ser minimizado para sincronização com o conteúdo visual.

### 10.2 Kokoro — Conteúdo Educativo e Informativo

O Kokoro é recomendado para aplicações que valorizam **qualidade da síntese** e onde alguma latência é tolerável:

1. **Plataformas de e-learning acessíveis:** Conversão de material didático escrito em áudio de alta qualidade para estudantes com dislexia ou deficiência visual, onde o conteúdo é pré-gerado antes da aula.

2. **Audiolivros em português brasileiro:** Narração automatizada de livros digitais, especialmente textos narrativos e informativos, onde o Kokoro demonstrou WER de apenas 0,0467 em longas_narrativas.

3. **Chatbots com interface de voz:** Assistentes virtuais para atendimento ao cidadão em portais governamentais, onde respostas pré-processadas podem ser geradas com qualidade superior.

4. **Podcasts automatizados de acessibilidade:** Geração de versões em áudio de notícias, boletins e comunicados institucionais para distribuição em plataformas de podcast acessíveis.

5. **Materiais de apoio em LIBRAS digital:** Complemento sonoro para conteúdos em Língua Brasileira de Sinais, onde a sincronização não é crítica mas a qualidade da pronúncia importa.

6. **Leitura de relatórios e documentos longos:** Para usuários que precisam "ouvir" documentos extensos, o Kokoro oferece a melhor combinação de inteligibilidade e naturalidade da voz.

### 10.3 XTTS v2 — Síntese Expressiva com Recursos Avançados

O XTTS v2 é recomendado para aplicações que valorizam **expressividade** e **personalização de voz**, especialmente quando GPU está disponível:

1. **Preservação de voz para condições degenerativas (ELA):** A clonagem de voz zero-shot do XTTS é particularmente relevante para usuários diagnosticados com Esclerose Lateral Amiotrófica (ELA) ou outras condições que causam perda progressiva da fala. O modelo pode ser treinado com amostras de voz gravadas enquanto o paciente ainda consegue falar, gerando uma voz sintética personalizada para uso posterior com comunicadores alternativos.

2. **Audiolivros com voz autoral:** Permitir que autores preservem sua voz para narrar seus próprios livros digitalmente, criando uma experiência mais autêntica para o leitor e dispensando a contratação de locutores profissionais.

3. **Contação de histórias interativas para crianças:** A maior expressividade prosódica do XTTS, aliada à capacidade de simular diferentes vozes, é adequada para aplicações educativas infantis onde a qualidade narrativa importa mais que a velocidade.

4. **Sistemas de comunicação alternativa e aumentativa (CAA):** Dispositivos de alta tecnologia para pessoas com paralisia cerebral ou outras condições que impedem a fala, onde a naturalidade da voz gerada é prioritária e a latência pode ser tolerada.

5. **Produção de conteúdo audiovisual acessível:** Geração de audiodescrição e legendas faladas para vídeos, documentários e produções cinematográficas, onde o tempo de processamento não é um impeditivo.

6. **Locução multilíngue e code-switching:** O XTTS apresentou o melhor WER na categoria nomes_internacionais (0,3190), indicando maior capacidade de lidar com termos e nomes de origem estrangeira — útil para conteúdos técnicos, científicos ou jornalísticos com alta incidência de estrangeirismos.

---

## 11. MATRIZ COMPARATIVA FINAL

A Tabela 8 apresenta uma avaliação qualitativa dos três modelos em critérios técnicos e de aplicabilidade, sintetizando as principais conclusões do benchmark.

### Tabela 8 — Matriz de Adequação por Critério

| Critério                      | Piper        | Kokoro       | XTTS v2      |
|-------------------------------|:------------:|:------------:|:------------:|
| Uso em tempo real (CPU)       | Excelente    | Limitado     | Inadequado   |
| Operação offline/embarcado    | Excelente    | Bom          | Limitado     |
| Leitura prolongada            | Bom          | Excelente    | Bom          |
| Clonagem de voz               | Não suporta  | Não suporta  | Excelente    |
| Nomes/estrangeirismos         | Adequado     | Bom          | Melhor       |
| Custo computacional           | Muito baixo  | Baixo        | Alto         |
| Expressividade emocional      | Básica       | Moderada     | Alta         |
| Tamanho do modelo             | ~63 MB       | ~326 MB      | ~1,8 GB      |
| Suporte nativo pt-BR          | Sim          | Sim          | Sim          |
| Reprodutibilidade (ONNX)      | Sim          | Sim          | Parcial      |

**Interpretação da matriz:**

- O **Piper** se destaca como a solução mais **pragmática e escalável** para acessibilidade em contextos de recursos limitados. Sua portabilidade (ONNX, ~63 MB), velocidade e adequação para tempo real tornam-no a escolha natural para a maioria dos casos de uso de acessibilidade digital no Brasil.

- O **Kokoro** representa o **ponto ótimo** entre qualidade e velocidade para conteúdo pré-gerado. Com o melhor WER do benchmark e qualidade de voz superior ao Piper (segundo avaliação qualitativa), é ideal para plataformas educativas e de entretenimento acessível.

- O **XTTS v2** oferece capacidades únicas (clonagem de voz, expressividade) que nenhum outro modelo do benchmark suporta, mas sua utilidade prática em ambiente CPU é severamente limitada. Com acesso a GPU, o perfil de adequação do XTTS mudaria significativamente, tornando-o competitivo também em latência.

---

## 12. LIMITAÇÕES DO ESTUDO

A interpretação dos resultados deve considerar as limitações metodológicas que delimitam o escopo das conclusões:

### 12.1 Ambiente CPU-Only

Todos os experimentos foram executados exclusivamente em CPU no Google Colab, sem aceleração por GPU. Essa escolha foi deliberada para simular condições de uso acessível e de baixo custo, mas afeta desproporcionalmente o XTTS v2, cuja arquitetura GPT autoregressiva foi otimizada para execução em GPU. Estimativas informais sugerem que o XTTS com GPU poderia reduzir sua latência em um fator de 10× a 20×, alterando substancialmente as conclusões sobre sua viabilidade para uso em tempo real.

### 12.2 Avaliação Exclusivamente Automática

O estudo não incluiu avaliação perceptiva humana (*Mean Opinion Score* — MOS), que é o padrão-ouro para qualidade subjetiva de voz. O WER mede inteligibilidade objetiva, mas não captura aspectos como naturalidade, entonação, ritmo e qualidade estética da voz, que são igualmente relevantes para a experiência do usuário em aplicações de acessibilidade.

### 12.3 Escopo de Modelos Avaliados

Apenas três modelos TTS foram avaliados. O ecossistema de TTS de código aberto inclui outros modelos relevantes (como MMS da Meta, StyleTTS2, Bark, entre outros) que não foram incluídos por limitações de tempo e escopo. A conclusão de que "o Kokoro tem o melhor WER" é válida apenas no contexto dos três modelos avaliados.

### 12.4 Corpus de Avaliação

O corpus de 140 frases, organizado em 14 categorias com 10 frases cada, é representativo das principais categorias linguísticas do português brasileiro, mas não é exaustivo. Variedades regionais, neologismos, termos médicos especializados e outros fenômenos não contemplados podem apresentar resultados diferentes. Além disso, o corpus foi construído especificamente para este estudo e não foi validado por especialistas em linguística.

### 12.5 Viés do Transcritor Whisper

O uso do Whisper como transcritor automático introduz um viés sistemático: o WER calculado reflete não apenas os erros do modelo TTS, mas também os erros e tendências do próprio Whisper. O Whisper foi treinado predominantemente em dados do inglês e pode ter desempenho inferior em português brasileiro para determinados fonemas ou padrões prosódicos, penalizando modelos que sintetizam esses padrões de forma não convencional mas perfeitamente inteligível para um ouvinte humano nativo.

---

> **Nota metodológica:** Todos os resultados numéricos apresentados neste capítulo foram extraídos diretamente dos arquivos CSV gerados pelo pipeline de avaliação automatizada disponível no repositório público do projeto (`results/`). A reprodutibilidade completa do experimento é possível a partir do notebook `modelscompare_v5_1903-2.ipynb`, com as instruções de setup documentadas em `docs/setup_colab.md`.
