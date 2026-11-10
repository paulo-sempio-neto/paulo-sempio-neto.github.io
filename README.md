# Portfólio — Paulo Sêmpio Neto

Site estático publicado no GitHub Pages: <https://paulo-sempio-neto.github.io/>

## Conceito: camadas

Cada projeto aparece como três camadas empilhadas em 3D — **interface**, **API** e
**dados** — com os endpoints e as tabelas reais tirados do código de cada repositório.
No topo, as camadas se abrem ao carregar e seguem o mouse; nos estudos de caso, a
tela se desmonta conforme a rolagem. As três cores (roxo, âmbar e verde) significam
sempre a mesma camada no site inteiro.

Projetos: **Ganho Certo**, **Lexin**, **API Sentinel** e **Gôndola**.

## Projetos sempre atualizados

- **Ao vivo:** em telas grandes, a camada de interface do topo carrega o site
  publicado do projeto por cima da captura. Se o site não puder ser exibido dentro
  de outra página (como a Lexin, que bloqueia isso por segurança), a captura fica.
- **Capturas automáticas:** `.github/workflows/refresh-screenshots.yml` abre os sites
  publicados todo dia às 06:17 (Brasília), tira novas capturas e faz commit só se
  alguma tela mudou. Também roda manualmente em **Actions → Atualizar capturas →
  Run workflow**. A lista fica em `scripts/projects.json`.

## Estrutura

- `index.html` — gerado por `scripts/build_index.py`, que concentra os textos e os
  fatos de cada projeto. Edite o script e rode `python3 scripts/build_index.py`.
- `styles.css` — tokens em `:root`, pilha 3D (`.stack`) e responsivo no final.
- `script.js` — menu, troca de projeto, inclinação, rolagem e modo ao vivo.
- `assets/projects/` — capturas em WebP. `assets/fonts/` — Familjen Grotesk e
  JetBrains Mono auto-hospedadas (licença OFL incluída).
- `projetos.html`, `sobre.html`, `contato.html` — redirecionam endereços antigos.

Sem bibliotecas nem etapa de build no site. Todo o conteúdo funciona sem JavaScript;
`prefers-reduced-motion` desliga o movimento e mostra as camadas já abertas.

## Rodar localmente

```sh
python3 -m http.server 8000
```
