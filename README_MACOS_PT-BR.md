# Suporte do macOS para SyncExtPack Builder

## 🤖 Compatibilidade do macOS Gerada por IA

**Esta camada de compatibilidade do macOS foi inteiramente projetada e implementada pelo Claude 3.5 Sonnet** em colaboração com o mantenedor do projeto. A IA analisou o código original apenas para Windows, identificou problemas de compatibilidade e criou uma solução multiplataforma completa incluindo:

- Correções de bugs de detecção de plataforma
- Integração Docker para binários Linux
- Integração de ferramentas Homebrew  
- Equivalentes em shell script
- Scripts de configuração automatizados
- Documentação abrangente

Isso demonstra como a IA pode efetivamente modernizar e estender códigos existentes para suportar novas plataformas mantendo compatibilidade retroativa.

---

## Visão Geral

O SyncExtPack Builder agora funciona nativamente no macOS graças a:

- Bug de detecção de plataforma corrigido em `builder/utils.py`
- Wrapper Docker para o binário Linux `crypto_pack`
- Instalação Homebrew do `swfmill`
- Equivalentes em shell script dos arquivos batch do Windows

## Configuração Rápida

1. **Instalar dependências**:

   ```bash
   # Instalar Homebrew se não estiver instalado
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   
   # Instalar swfmill e Java
   brew install swfmill
   brew install openjdk
   
   # Instalar Docker Desktop
   # Baixar de: https://www.docker.com/products/docker-desktop
   ```

2. **Executar a configuração automatizada**:

   ```bash
   ./setup_macos.sh
   ```

## Uso

### Construindo Pacotes

Use o shell script ao invés do arquivo batch do Windows:

```bash
# Ao invés de build_pack.bat
./build_pack.sh SEU_APIM_SERIAL NUMERO_MAGICO

# Exemplo:
./build_pack.sh ABC12345 0
```

### Uso Direto do Python

Os scripts Python funcionam da mesma forma no macOS:

```bash
python3 build_pack.py SEU_APIM_SERIAL saida.bin 0 UpdateService Player_EN Reboot
```

## Detalhes Técnicos

### Correção da Detecção de Plataforma

Corrigido o bug crítico em `builder/utils.py` onde `'win' in sys.platform` incorretamente correspondia a `'darwin'` (macOS), fazendo-o procurar por arquivos `.exe` em sistemas Unix.

**Antes** (quebrado):

```python
if 'win' in sys.platform:  # 'win' corresponde a 'darwin'!
    PLATFORM_EXEC_FILE_POSTFIX = '.exe'
```

**Depois** (corrigido):

```python
if sys.platform.startswith('win'):  # Identifica corretamente o Windows
    PLATFORM_EXEC_FILE_POSTFIX = '.exe'
```

### Integração Docker

O wrapper `crypto_pack_docker.sh` automaticamente executa o binário Linux `crypto_pack` em um container Docker com emulação x86_64:

```bash
docker run --rm \
  --platform=linux/amd64 \
  -v "$PWD:/workspace" \
  -w /workspace \
  -u "$(id -u):$(id -g)" \
  ubuntu:20.04 \
  ./crypto_pack "$@"
```

O código Python automaticamente detecta e usa este wrapper quando disponível.

### Ferramentas Nativas

- **swfmill**: Instalado via Homebrew, link simbólico para `FlashTools/swfmill`
- **Java**: OpenJDK via Homebrew para `secureSWF.jar`

## Arquivos Adicionados

- `build_pack.sh` - Equivalente em shell script de `build_pack.bat`
- `unpack_pack.sh` - Equivalente em shell script de `unpack_pack.bat`
- `crypto_pack_docker.sh` - Wrapper Docker para `crypto_pack`
- `setup_macos.sh` - Script de configuração automatizada
- `README_MACOS_PT-BR.md` - Esta documentação

## Compatibilidade

- **macOS**: ✅ Suporte completo (Apple Silicon e Intel)
- **Linux**: ✅ Deve funcionar (não testado mas projetado para compatibilidade)  
- **Windows**: ✅ Funcionalidade original preservada

## Solução de Problemas

### Problemas com Docker

Se você receber erros "Docker not found":

1. Instale o Docker Desktop
2. Certifique-se de que o Docker está executando
3. Teste com: `docker --version`

### Problemas com Java

Se você receber erros "Java Runtime not found":

1. Instale o OpenJDK: `brew install openjdk`
2. Adicione ao PATH: `export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"`

### Problemas de Permissão

Se você receber erros de permissão:

1. Torne os scripts executáveis: `chmod +x *.sh`
2. Verifique as permissões do Docker nas configurações do Docker Desktop

## Contribuindo

Ao contribuir para o suporte do macOS:

1. Teste em Macs Apple Silicon e Intel se possível
2. Certifique-se de que a compatibilidade com Windows seja preservada
3. Atualize este README para quaisquer novos recursos ou requisitos
