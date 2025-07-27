# SyncExtPack Builder

Uma ferramenta para construir pacotes de firmware customizados para sistemas de infotainment Ford SYNC 2.

## Suporte de Plataforma

- **Windows**: Plataforma original (use arquivos `.bat`)
- **macOS**: 🤖 **Suporte Gerado por IA** - Compatibilidade completa via integração Docker (use arquivos `.sh`)
- **Linux**: Deve funcionar imediatamente

## Configuração do macOS

Para usuários do macOS, consulte [`README_MACOS_PT-BR.md`](README_MACOS_PT-BR.md) para instruções completas de configuração.

**Nota**: A camada de compatibilidade do macOS foi inteiramente projetada e implementada pelo **Claude 3.5 Sonnet**, demonstrando como a IA pode efetivamente modernizar códigos legados para suporte multiplataforma.

## Início Rápido

### Windows
```batch
build_pack.bat SEU_APIM_SERIAL NUMERO_MAGICO
```

### macOS/Linux
```bash
./setup_macos.sh      # Configuração inicial
./build_pack.sh SEU_APIM_SERIAL NUMERO_MAGICO
```

## Documentação

- **[Guia de Configuração do macOS](README_MACOS_PT-BR.md)** - Instruções completas de configuração para usuários do macOS
- **[Instalação do SyncExtPack](SYNCEXTPACK_INSTALLATION_PT-BR.md)** - Guia completo para instalar o pacote
- **[Instalação Manual de Apps](MANUAL_APP_INSTALLATION_PT-BR.md)** - Guia passo a passo para instalar apps usando Total Commander sem recompilar firmware (usa AutoKit como exemplo)

## Funcionalidades

- **Integração de Apps Customizados** - Adicione CarPlay/Android Auto (AutoKit), VideoPlayer, apps de navegação e mais
- **Suporte Multiplataforma** - Funciona no Windows, macOS e Linux
- **Modo de Instalação Manual** - Instale apps diretamente via Total Commander para atualizações rápidas
- **Criação Automatizada de Plugin DLL** - Script Python para criar automaticamente plugin DLLs para qualquer app
- **Preservação de Firmware** - Mantenha sua configuração SYNC 2 existente enquanto adiciona novas funcionalidades

## AutoKit

- Para funcionar é necessario um adaptador, procure por CarlinKit CCPA, tem no [mercado livre](https://www.mercadolivre.com.br/carlinkit-sem-fio-apple-carplay-android-auto-p-multim-usb/p/MLB23587002?pdp_filters=item_id%3AMLB4074590268&from=gshop&matt_tool=49601181&matt_internal_campaign_id=&matt_word=&matt_source=google&matt_campaign_id=22090354496&matt_ad_group_id=173090612316&matt_match_type=&matt_network=g&matt_device=c&matt_creative=727882733427&matt_keyword=&matt_ad_position=&matt_ad_type=pla&matt_merchant_id=735128188&matt_product_id=MLB23587002-product&matt_product_partition_id=2417612453924&matt_target_id=aud-1966981570049:pla-2417612453924&cq_src=google_ads&cq_cmp=22090354496&cq_net=g&cq_plt=gp&cq_med=pla&gad_source=1&gad_campaignid=22090354496&gbraid=0AAAAAD93qcDs6dy62JgCxUKpAlrZk2eVc&gclid=Cj0KCQjw-ZHEBhCxARIsAGGN96JxOlIbtGDZ4vlAIUDsMywrtKReAsLwE1yq0l0QnJCiXs-3irNG9QYaAvohEALw_wcB) ou vc pode encontrar no aliexpress mais barato
