# 📝 Textos de Teste

Esta pasta contém os textos utilizados para testar e avaliar os modelos TTS (Text-to-Speech) nos experimentos desta pesquisa.

---

## 📄 Arquivo Principal

**`frases.txt`** — Conjunto de frases em português brasileiro para uso como entrada nos modelos TTS.

---

## 🎯 Critérios de Seleção das Frases

As frases foram selecionadas para cobrir diferentes aspectos que um modelo TTS precisa lidar bem para ser útil em contextos de acessibilidade:

### 1. Diversidade de Comprimento

| Categoria | Número de Palavras | Objetivo |
|-----------|:-----------------:|---------|
| **Curtas** | 5–10 | Testar resposta rápida e naturalidade em frases simples |
| **Médias** | 15–25 | Testar prosódia e fluência em frases completas |
| **Longas** | 30+ | Testar consistência de qualidade em textos extensos |

### 2. Diversidade de Conteúdo

| Tipo | Exemplos | Por que Importa |
|------|----------|-----------------|
| **Frases cotidianas** | "O sol nasceu cedo hoje." | Base de naturalidade |
| **Notificações de sistema** | "Arquivo salvo com sucesso." | Uso em leitores de tela |
| **Números e dados** | CPF, temperatura, tamanho de arquivo | Pronúncia de números |
| **Siglas e abreviações** | TTS, RTF, GB, Hz | Expansão de siglas |
| **Frases de acessibilidade** | Direções, alertas de segurança | Aplicação real do projeto |

### 3. Critérios de Qualidade das Frases

- ✅ Ortografia correta (português brasileiro padrão)
- ✅ Representativas do uso real em tecnologia assistiva
- ✅ Cobertura de diferentes estruturas sintáticas
- ✅ Inclusão de pontuação variada (vírgulas, pontos, interrogações)
- ✅ Uso de vocabulário técnico relevante à área

---

## 📊 Estatísticas do Conjunto de Frases

| Categoria | Quantidade |
|-----------|:----------:|
| Frases curtas (5–10 palavras) | 10 |
| Frases médias (15–25 palavras) | 7 |
| Frases longas (30+ palavras) | 3 |
| Frases com números/siglas | 7 |
| Frases de acessibilidade | 6 |
| **Total** | **33** |

---

## 🔧 Como Usar nos Experimentos

```python
def carregar_frases(caminho="textos_teste/frases.txt"):
    """
    Carrega as frases de teste ignorando comentários e linhas em branco.
    
    Returns:
        Lista de strings com as frases
    """
    frases = []
    with open(caminho, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            # Ignora linhas em branco e comentários (que começam com #)
            if linha and not linha.startswith("#"):
                frases.append(linha)
    return frases

# Uso
frases = carregar_frases()
print(f"Total de frases carregadas: {len(frases)}")

# Sintetizar todas as frases com um modelo
for i, frase in enumerate(frases, start=1):
    resultado = sintetizar_e_medir("meu_modelo", func_sintetizar, frase)
    salvar_audio(resultado["audio"], resultado["sr"], f"outputs/frase_{i:02d}.wav")
```

---

## ➕ Como Adicionar Novas Frases

Para contribuir com novas frases ao conjunto de teste, edite o arquivo `frases.txt` seguindo estas diretrizes:

1. Adicione a frase na seção temática apropriada
2. Prefixe seções novas com `# --- TÍTULO ---`
3. Use linhas em branco para separar seções
4. Linhas começando com `#` são tratadas como comentários
5. Evite frases com erros ortográficos ou gramaticais
6. Prefira frases que representem situações reais de uso em acessibilidade
