# Guia de Instalação de Firmware Ford SYNC 2

Passos para atualizar para 3.10 ou fazer downgrade para 3.08.

## Requisitos

- **Pen Drive**: compatível USB 2.0, máximo 32GB, formatado como partição FAT32 MBR
- **Motor do Carro**: Recomendado ligado (processo demora e pode descarregar a bateria)

## Escolha o Seu Firmware

Download via Mega, [link aqui](https://mega.nz/folder/Bn5F2SYQ#Hy_hkQNVFQeMD1F_CNWZhg).

- **Atualizar para 3.10**: `Gen2v310build16180updatepackageEULangpack5.zip`
- **Downgrade para 3.08**: `Sync2 Downgrade 3.10 16180 to 3.08 15128EU.zip`

*Nota: O processo de instalação é idêntico para atualização e downgrade.*

## Passo 1: Preparar Pen Drive

1. **Formate o pen drive** como partição FAT32 MBR
2. **Extraia o arquivo ZIP do firmware** diretamente para a raiz do pen drive
3. **Verifique a estrutura** - arquivos devem estar na raiz, não em subpasta

## Passo 2: Instalar no Veículo

1. **Ligue o motor** (recomendado - processo demora e pode descarregar a bateria)
2. **Aguarde o SYNC 2** inicializar completamente
3. **Insira o pen drive**
4. **Aguarde a atualização automática** - SYNC 2 deve detectar e iniciar a instalação automaticamente

## Passo 3: Se a Atualização Automática Não Iniciar

Tente a função de atualização integrada do carro:

Vá para: **Menu → Configurações → Geral → Reset Geral → Instalar do Dispositivo**

## Passo 4: Se Ainda Não Funcionar

Use o método do wallpaper hack:

1. **Vá para configurações de papel de parede**: Menu → Configurações → Display → Papel de Parede → Adicionar → usbX
2. **Selecione autoinstall.jpg** (se presente nos arquivos do firmware)
3. **Seja paciente** - a instalação irá iniciar

## Passo 5: Aguardar Conclusão

1. **SYNC 2 pode reiniciar várias vezes** - isso é normal
2. **Seja paciente** - não remova o pen drive durante o processo
3. **Remova o pen drive apenas** quando o SYNC 2 exibir "Atualização concluída com sucesso"
4. **Sistema irá reiniciar** e mostrar a nova versão do firmware

## Passo 6: Verificar Instalação

1. Vá para: **Menu → Configurações → Geral → Sobre o SYNC**
2. Verifique a versão do firmware:
   - **3.10**: Deve mostrar versão 3.10 build 16180
   - **3.08**: Deve mostrar versão 3.08 build 15128

## Notas Importantes

- **Nunca interrompa** o processo de atualização do firmware
- **Mantenha o motor ligado** durante toda a instalação
- **Múltiplas reinicializações são normais** - não entre em pânico
- **Aguarde a mensagem de conclusão** antes de remover o pen drive

## Concluído

Seu Ford SYNC 2 agora está executando a nova versão do firmware.
