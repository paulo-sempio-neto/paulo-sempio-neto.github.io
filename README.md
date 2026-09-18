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
- `script.js`: menu e ano. Nenhum conteúdo depende do JavaScript.
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
