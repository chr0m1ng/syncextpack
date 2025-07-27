# Guia de Instalação Manual de Aplicativos

Este guia mostra como instalar aplicativos manualmente no Ford SYNC 2 usando o Total Commander. Usaremos o AutoKit como exemplo - um aplicativo que permite executar CarPlay e Android Auto.

## Por que Instalação Manual?

- **Maior controle**: Você pode ver exatamente o que está sendo instalado
- **Resolução de problemas**: Mais fácil de diagnosticar problemas
- **Flexibilidade**: Pode instalar qualquer aplicativo, não apenas os predefinidos
- **Aprendizagem**: Entenda como o sistema SYNC 2 funciona internamente

## Pré-requisitos

1. **Total Commander para Windows** - Navegador de arquivos dual-pane
   - Download: [https://www.ghisler.com/](https://www.ghisler.com/)
   - **Por que Total Commander**: Interface dual-pane torna mais fácil copiar arquivos entre diretórios

2. **Pen drive formatado em FAT32** (8GB+ recomendados)

3. **Arquivos do aplicativo preparados** (AutoKit usado como exemplo)

## Fluxo de Trabalho com Total Commander

### Configuração Inicial

1. **Abra o Total Commander**
2. **Configure os painéis**:
   - **Painel esquerdo**: Navegue até os arquivos do seu aplicativo
   - **Painel direito**: Navegue até seu pen drive

### Estrutura de Arquivos do AutoKit

Para o AutoKit, você precisa dos seguintes arquivos preparados:

```text
AutoKit/
├── AutoKitPlugin.dll          # Plugin DLL (gerado por create_plugin_dll.py)
├── autokit.exe               # Executável principal do AutoKit
├── autokit_config.xml        # Arquivo de configuração
└── outros_arquivos_do_autokit/  # Arquivos adicionais conforme necessário
```

## Processo de Instalação Passo a Passo

### Etapa 1: Criar Plugin DLL

Primeiro, crie o plugin DLL usando nosso script Python:

```bash
python3 create_plugin_dll.py AutoKit /SyncExtendedPack/Apps/Media/AutoKit/autokit.exe
```

Isto cria `AutoKitPlugin.dll` que será usado mais tarde.

### Etapa 2: Configurar Estrutura de Diretórios no Pen Drive

No **painel direito** do Total Commander (pen drive):

1. **Criar diretório principal**:
   - Pressione `F7` ou clique com o botão direito → "Novo" → "Pasta"
   - Nome: `SyncExtendedPack`

2. **Navegar para dentro de SyncExtendedPack**:
   - Duplo clique em `SyncExtendedPack`

3. **Criar subdiretório Apps**:
   - Pressione `F7`, nome: `Apps`
   - Navegar para dentro: duplo clique em `Apps`

4. **Criar subdiretório Media**:
   - Pressione `F7`, nome: `Media`
   - Navegar para dentro: duplo clique em `Media`

5. **Criar diretório do aplicativo**:
   - Pressione `F7`, nome: `AutoKit`
   - Navegar para dentro: duplo clique em `AutoKit`

**Caminho final**: `D:\SyncExtendedPack\Apps\Media\AutoKit\` (onde D: é seu pen drive)

### Etapa 3: Copiar Arquivos do Aplicativo

No **painel esquerdo** do Total Commander (arquivos fonte):

1. **Navegar até seus arquivos do AutoKit**
2. **Selecionar todos os arquivos do AutoKit**:
   - `Ctrl+A` para selecionar tudo
   - Ou segurar `Ctrl` e clicar em arquivos específicos

3. **Copiar para o pen drive**:
   - Pressione `F5` ou clique no botão "Copiar"
   - Total Commander copiará do painel esquerdo para o direito
   - Confirme a operação de cópia

### Etapa 4: Configurar Plugin DLL

1. **Navegar de volta ao diretório raiz do pen drive** no painel direito
2. **Criar diretório windows**:
   - Pressione `F7`, nome: `windows`
   - Navegar para dentro: duplo clique em `windows`

3. **Copiar plugin DLL**:
   - No painel esquerdo: navegar até onde está `AutoKitPlugin.dll`
   - Selecionar `AutoKitPlugin.dll`
   - Pressione `F5` para copiar para `D:\windows\`

### Etapa 5: Arquivos de Configuração (se necessário)

Alguns aplicativos precisam de arquivos de configuração XML adicionais:

1. **Para definições de menu**: Pode precisar modificar arquivos XML existentes
2. **Para configurações de aplicativo**: Criar arquivos de configuração personalizados

**Exemplo de configuração do AutoKit** (`autokit_config.xml`):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <app name="AutoKit">
        <path>/SyncExtendedPack/Apps/Media/AutoKit/autokit.exe</path>
        <description>CarPlay and Android Auto</description>
    </app>
</configuration>
```

## Estrutura Final do Pen Drive

Seu pen drive deve ficar assim:

```text
D:\ (Pen Drive)
├── SyncExtendedPack/
│   └── Apps/
│       └── Media/
│           └── AutoKit/
│               ├── autokit.exe
│               ├── autokit_config.xml
│               └── outros_arquivos_do_autokit...
└── windows/
    └── AutoKitPlugin.dll
```

## Instalação no Veículo

### Usando o Pen Drive

1. **Inserir pen drive** no veículo
2. **Navegar para Menu SYNC → Configurações → Geral → Atualização do Sistema**
3. **Selecionar "Instalar"** quando solicitado
4. **Aguardar a instalação** completar (pode levar vários minutos)
5. **Reinicializar o sistema** quando solicitado

### Verificação da Instalação

Após reinicializar:

1. **Verificar novo item de menu**: AutoKit deve aparecer nos menus de aplicativos
2. **Testar funcionalidade**: Tentar executar o aplicativo
3. **Verificar logs de erro**: Olhar mensagens de erro se algo não funcionar

## Resolução de Problemas

### Aplicativo Não Aparece no Menu

**Possíveis causas**:

- Plugin DLL não instalado corretamente
- Caminho do executável incorreto no DLL
- Arquivos de configuração em falta

**Soluções**:

1. **Verificar plugin DLL**:
   - Confirmar que `AutoKitPlugin.dll` está em `/windows/`
   - Recriar usando `create_plugin_dll.py` com caminho correto

2. **Verificar estrutura de arquivos**:
   - Confirmar que o aplicativo está no caminho especificado no DLL
   - Usar Total Commander para navegar e verificar todos os arquivos

### Aplicativo Aparece Mas Não Executa

**Possíveis causas**:

- Executável corrompido ou incompatível
- Dependências em falta
- Problemas de permissão

**Soluções**:

1. **Verificar arquivos do aplicativo**:
   - Recopy todos os arquivos usando Total Commander
   - Confirmar que nenhum arquivo foi corrompido durante a transferência

2. **Verificar dependências**:
   - Certificar-se de que todas as bibliotecas necessárias estão incluídas
   - Verificar se o aplicativo funciona em ambiente de teste primeiro

### Plugin DLL Não Reconhecido

**Possíveis causas**:

- DLL gerado incorretamente
- Arquitetura errada (precisa ser Windows CE ARM)
- Assinatura DLL inválida

**Soluções**:

1. **Regenerar DLL**:

   ```bash
   python3 create_plugin_dll.py AutoKit /SyncExtendedPack/Apps/Media/AutoKit/autokit.exe
   ```

2. **Verificar formato DLL**:
   - DLL deve ser Windows CE PE32 para ARM
   - Nosso script `create_plugin_dll.py` cuida disso automaticamente

## Dicas do Total Commander

### Navegação Rápida

- **Tab**: Alternar entre painéis esquerdo e direito
- **Ctrl+R**: Atualizar visualização
- **Alt+F1/F2**: Mudar unidade no painel esquerdo/direito
- **Ctrl+U**: Trocar painéis

### Operações de Arquivo

- **F5**: Copiar arquivos (esquerdo → direito)
- **F6**: Mover arquivos
- **F7**: Criar nova pasta
- **F8**: Deletar arquivos/pastas
- **Ctrl+A**: Selecionar todos os arquivos

### Visualização de Arquivos

- **F3**: Visualizar arquivo (modo somente leitura)
- **F4**: Editar arquivo
- **Ctrl+M**: Mudar atributos de arquivo

## Instalação de Outros Aplicativos

Este mesmo processo funciona para qualquer aplicativo:

1. **Obter arquivos do aplicativo**
2. **Criar plugin DLL apropriado** usando `create_plugin_dll.py`
3. **Usar Total Commander** para organizar arquivos no pen drive
4. **Seguir estrutura de diretórios** apropriada
5. **Instalar no veículo** via pen drive

### Exemplos de Estruturas de Caminho

Para diferentes tipos de aplicativos:

- **Aplicativo de mídia**: `/SyncExtendedPack/Apps/Media/[NomeApp]/`
- **Aplicativo de navegação**: `/SyncExtendedPack/Apps/Nav/[NomeApp]/`
- **Ferramentas**: `/SyncExtendedPack/Apps/Tools/[NomeApp]/`

## Automatização

Embora este guia cubra instalação manual, você também pode usar nossos scripts automatizados:

```bash
# Construir pacote completo com AutoKit incluído
python3 build_pack.py SEU_APIM_SERIAL saida.bin 0 UpdateService AutoKit Player_EN Reboot
```

A instalação manual é útil para:

- **Aprender** como o sistema funciona
- **Depurar** problemas
- **Personalizar** instalações
- **Instalar** aplicativos únicos não suportados pelos scripts automatizados

## Segurança e Backup

### Antes de Instalar

1. **Fazer backup** do firmware original do SYNC
2. **Anotar** a versão atual do sistema
3. **Verificar** compatibilidade do aplicativo

### Durante a Instalação

1. **Não desligar** o veículo durante a instalação
2. **Manter** o motor funcionando ou bateria carregada
3. **Não remover** o pen drive até a instalação estar completa

### Após a Instalação

1. **Testar** todas as funcionalidades básicas do SYNC
2. **Verificar** se o aplicativo funciona conforme esperado
3. **Manter** backup do pen drive de instalação para futuras referências
