# Guia de Instalação do SyncExtPack

Passos para instalar no seu Ford SYNC 2.

> **⚠️ Recomendação**: É recomendado atualizar seu Ford SYNC 2 para a versão de firmware 3.10 antes de instalar o SyncExtPack. Veja o [Guia de Instalação de Firmware](FIRMWARE_INSTALLATION_PT-BR.md) para instruções de atualização.

## Requisitos

- **Pen Drive**: USB 2.0, máximo 32GB, formatado como FAT32 MBR
- **Número de Série APIM**: Encontre no seu carro

## Passo 1: Obter o Número de Série APIM

Vá para: **Menu → Configurações → Geral → Sobre o SYNC** e anote o número de série APIM (exemplo: `XV31M13H`)

## Passo 2: Escolher Script de Build

Baseado no seu sistema operacional:

- **Windows**: Use `build_pack.bat`
- **macOS/Linux**: Use `build_pack.sh`

## Passo 3: Configurar Apps para Instalar

1. Abra o arquivo do script de build em um editor de texto
2. Encontre a linha principal de build (por volta da linha 33):

   ```bash
   python3 build_pack.py $apimSerial SyncExtPack/pack_install.bin $magicNum AutoKit MirrorLink_EN_NEW Explorer Reboot
   ```

3. **Descomente** a linha que você quer, ou **crie a sua própria** usando este formato:

   ```bash
   python3 build_pack.py $apimSerial SyncExtPack/pack_install.bin $magicNum {LISTA_DE_APPS_SEPARADOS_POR_ESPAÇO}
   ```

**Apps disponíveis**: AutoKit, MirrorLink_EN_NEW, Explorer, Player_EN, Navitel, DDApp, Reboot

## Passo 4: Construir o Pacote

Execute o script de build com o seu serial APIM:

**Windows**:

```batch
build_pack.bat XV31M13H 0
```

**macOS/Linux**:

```bash
./build_pack.sh XV31M13H 0
```

Isso gerará um arquivo ZIP como: `SyncExtPack_XV31M13H_AutoKit_MirrorLink_EN_NEW_Explorer.zip`

## Passo 5: Preparar o Pen Drive

1. **Formate o pen drive** como partição FAT32 MBR
2. **Extraia o conteúdo do arquivo ZIP** diretamente para a raiz do pen drive
3. **Verifique a estrutura**:

   ```text
   Pen Drive (E:)
   └── SyncExtPack/
       ├── update.bin
       ├── UpdateInstaller.dll
       ├── Installer.jpg
       └── pack_install.bin
   ```

## Passo 6: Instalar no Veículo

1. **Ligue o carro** (recomendado - processo demora e pode descarregar a bateria) e aguarde o SYNC 2 inicializar completamente
2. **Insira o pen drive**
3. **Vá para configurações de papel de parede**: Menu → Configurações → Display → Papel de Parede → Adicionar → usbX
4. **Selecione Installer.jpg** - pressione uma vez e seja paciente
5. **SYNC 2 irá reiniciar** - aguarde até reinicializar completamente

## Passo 7: Completar Instalação

1. **Remova o pen drive** e conecte ao PC
2. **Renomeie o arquivo**: Mude `pack_install.bin` para `install.bin`
3. **Reinsira o pen drive** no veículo
4. **Aguarde alguns segundos** - a instalação começará automaticamente
5. **Seja paciente** - aguarde a instalação completar
6. **SYNC 2 pode reiniciar** quando terminar (se não reiniciar, tudo bem - prossiga para o passo 8)

## Passo 8: Verificar Instalação

1. Aguarde o SYNC 2 inicializar completamente
2. Remova o pen drive
3. Pressione **botão i → Apps**
4. Verifique se os seus novos apps estão lá

## Concluído

Seu Ford SYNC 2 agora tem os apps personalizados instalados.
