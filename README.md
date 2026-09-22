# Portfólio — Paulo Malpice Sêmpio Neto

Site estático em português brasileiro, desenvolvido com HTML, CSS e JavaScript.
Sem instalação de dependências ou build.

## Executar e revisar

Abra `index.html` no navegador, mantendo os arquivos e a pasta `assets` juntos.
Ou, dentro da pasta do projeto, execute:

```sh
python -m http.server 8000
```

Acesse `http://localhost:8000`. No Windows, `py -m http.server 8000` também pode ser usado.

## Publicar no GitHub Pages

1. Faça backup da versão atual ou crie uma branch no seu clone do repositório.
2. Copie os arquivos deste pacote para a raiz de `paulo-sempio-neto.github.io`, preservando a pasta `assets` e a pasta `docs`.
3. Revise o resultado local. Faça commit e envie as alterações para a branch usada pelo Pages.
4. No GitHub, confira **Settings → Pages**. Se usar publicação por branch, selecione a branch de publicação e a pasta `/ (root)`. Se já houver um workflow, mantenha o fluxo existente.
5. Aguarde a publicação e revise o site no endereço habitual. Não há comando de build.

Este pacote não foi enviado ao GitHub e não altera o site publicado.

## Manutenção

- `index.html`: textos, projetos, links e formação. Cada projeto é um `article` dentro de `#projetos`.
- `styles.css`: cores e medidas em `:root`; seções comentadas e regras responsivas no final.
- `script.js`: introdução, menu, ano e revelações ao rolar. Nenhum conteúdo depende do JavaScript.
- `assets/favicon.svg`: monograma vetorial, sem dependências externas.
- `projetos.html`, `sobre.html`, `contato.html`: compatibilidade com endereços antigos.
- `specification.txt`: descrição atual; especificação original preservada em `docs/`.

Para incluir um projeto, duplique um `article`, atualize texto, tecnologias e links,
e remova funcionalidades que ainda não estejam implementadas. Os links técnicos
usam commits específicos para preservar a evidência; atualize o commit e o texto
juntos quando houver uma evolução importante.

A demonstração do sistema de produtos aponta para o GIF existente no repositório.
Não existe uma API em produção vinculada a este site. O quadro da primeira tela
é uma apresentação estática da rota real, não um terminal interativo.

O contato usa e-mail e LinkedIn. `mailto:` abre o aplicativo de e-mail do visitante;
o endereço também fica visível para copiar. Não há formulário sem backend.

## Conteúdo verificado

Leia `docs/analise-e-validacao.md` para fontes, diagnóstico e limitações dos testes.
A formação UNIC e a conclusão prevista em dezembro de 2029 vieram do README do
perfil. A foto não foi incluída porque o download do avatar não estava acessível;
a composição foi planejada para funcionar sem retrato.

## Interações e diagramas técnicos

As seções e os projetos aparecem uma vez ao entrar na tela, com fade de 480 ms,
deslocamento de 14 px e intervalos de 70 ms entre blocos visíveis no mesmo grupo
(máximo de 210 ms). IntersectionObserver e Web Animations são APIs nativas;
não há bibliotecas adicionais, eventos contínuos de scroll ou mudança de layout.
O conteúdo permanece visível se JavaScript ou essas APIs estiverem indisponíveis.

A revelação começa após a introdução. Foco de teclado cancela a animação do
bloco correspondente. `prefers-reduced-motion` desativa os movimentos, inclusive
quando a preferência muda durante a visita. Cartões recebem realce ao passar o
mouse ou focar um link; badges têm feedback discreto sem virar controles falsos.
Movimentos de hover são restritos a dispositivos com ponteiro preciso.

Os diagramas são listas ordenadas com conectores decorativos. No Product
Management System, UI própria e Repository pattern são identificados como
planejados. No API Sentinel, monitoramento, métricas e saúde dos endpoints
também são planejados; `/health` descreve apenas o próprio serviço.

Validação local: Chrome headless, servido por HTTP, em 1440×1000, 1024×768,
768×1024, 390×844 e 320×740. Os diagramas foram revisados visualmente; não houve
transbordamento horizontal. Foram verificados menu mobile, Escape, foco e
âncoras, revelação escalonada, movimento reduzido inicial e alterado durante a
visita, leitura sem JavaScript, introdução e redirecionamentos antigos.
Essas verificações usam viewports emulados; não substituem testes em aparelhos
físicos, outros navegadores ou uma auditoria completa com leitor de tela.
