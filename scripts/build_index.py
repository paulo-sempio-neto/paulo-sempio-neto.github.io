"""Generates index.html for the portfolio from verified project facts.

Every claim below was checked against the project repositories
(routes, tables, test counts, CI configuration) on 2026-11-10.
"""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "index.html"

PROJECTS = [
    {
        "id": "ganho-certo",
        "name": "Ganho Certo",
        "kind": "Fintech para motoristas de aplicativo",
        "accent": "#10b981",
        "problem": "O motorista vê o faturamento do dia, mas não sabe quanto sobra depois de combustível, manutenção e desgaste.",
        "summary": "Um produto completo com contas, planos e cobrança: o motorista lança o dia em segundos e vê o lucro real por hora, por quilômetro e na meta da semana.",
        "built": [
            "Contas com login, redefinição de senha e dados isolados por usuário",
            "Jornadas, despesas, veículos e um perfil de custos por quilômetro",
            "Resumo financeiro, metas com ritmo, histórico e padrões por dia da semana",
            "Importação de CSV com perfis de colunas reaproveitáveis",
            "Planos gratuito e Pro com limites por plano e checkout",
        ],
        "decisions": [
            ("Dinheiro sem float", "Valores monetários trafegam como decimais exatos, nunca como ponto flutuante."),
            ("Usuário vem do token", "O backend deriva o user_id da autenticação; o frontend nunca escolhe de quem são os dados."),
        ],
        "ui": ("Interface", "React · TypeScript"),
        "api": ("API", "FastAPI"),
        "data": ("Dados", "PostgreSQL · SQLAlchemy · Alembic"),
        "routes": [("POST", "/auth/login"), ("POST", "/work-sessions"), ("GET", "/financial-summary"), ("GET", "/financial-goals/{id}/progress")],
        "tables": ["users", "vehicles", "work_sessions", "expenses", "financial_goals", "subscriptions"],
        "stack": ["React", "TypeScript", "Vite", "Tailwind", "Three.js", "Framer Motion", "FastAPI", "SQLAlchemy 2", "Alembic", "PostgreSQL", "Docker", "GitHub Actions"],
        "metrics": [("516", "testes automatizados", "303 no backend, 213 no frontend"), ("4", "checagens no CI", "ruff, mypy, pytest e build")],
        "images": {
            "main": ("ganho-certo-landing", "Página inicial do Ganho Certo: faturar é fácil, lucrar de verdade é o que importa"),
            "detail": ("ganho-certo-painel", "Painel Hoje com a sobra do dia, faturamento, gastos e velocímetro de lucro por hora"),
            "mobile": ("ganho-certo-celular", "Painel do Ganho Certo no celular"),
        },
        "live": None,
        "frame": None,
        "code": "https://github.com/paulo-sempio-neto/ganho-certo",
    },
    {
        "id": "lexin",
        "name": "Lexin",
        "kind": "Curso de inglês para iniciantes",
        "accent": "#a78bfa",
        "problem": "Quem está começando no inglês trava na primeira conversa real, mesmo depois de meses de aplicativo.",
        "summary": "Uma plataforma de curso no ar, com venda, acesso por e-mail e prática guiada: do primeiro “hello” à próxima conversa.",
        "built": [
            "Landing e prática gratuita sem cadastro, para experimentar antes de comprar",
            "14 práticas guiadas, flashcards com repetição espaçada e quizzes",
            "Sessões de escuta com música, comunidade com perfis e notificações, certificado",
            "Acesso por código enviado por e-mail e venda integrada à Cakto por webhook",
            "Painel administrativo com suporte e registro de auditoria",
        ],
        "decisions": [
            ("Revisão no momento certo", "Os flashcards usam o algoritmo FSRS para agendar cada revisão perto do esquecimento."),
            ("Pagamento confiável", "O acesso é liberado pelo webhook do pagamento, não por uma página de obrigado."),
        ],
        "ui": ("Interface", "Next.js · React"),
        "api": ("API", "Route handlers do Next.js"),
        "data": ("Dados", "Supabase · PostgreSQL"),
        "routes": [("POST", "/api/auth/request-link"), ("POST", "/api/webhooks/cakto"), ("GET", "/api/streak"), ("POST", "/api/waitlist")],
        "tables": ["course_activity", "course_certificates", "community_posts", "community_profiles", "checkout_leads", "community_notifications"],
        "stack": ["Next.js 16", "React 19", "TypeScript", "Tailwind 4", "GSAP", "Framer Motion", "Lenis", "Three.js", "Supabase", "Playwright"],
        "metrics": [("500", "casos de teste", "unitários e ponta a ponta com Playwright"), ("14", "práticas guiadas", "no curso Primeiras Conversas")],
        "images": {
            "main": ("lexin-home", "Página inicial da Lexin: do primeiro oi à sua próxima conversa em inglês"),
            "detail": ("lexin-pratica", "Prática gratuita da Lexin com a frase What's your name?"),
            "mobile": ("lexin-celular", "Página inicial da Lexin no celular"),
        },
        "live": "https://lexiningles.com.br",
        "frame": None,
        "code": None,
    },
    {
        "id": "api-sentinel",
        "name": "API Sentinel",
        "kind": "Monitoramento de APIs",
        "accent": "#4fe3c1",
        "problem": "Saber que uma API caiu ou ficou lenta antes de o usuário perceber.",
        "summary": "Um monitor que checa cada endpoint em segundo plano, guarda o histórico e mostra tudo num radar 3D de latência.",
        "built": [
            "Cadastro de endpoints com validação e bloqueio de endereços internos",
            "Checagens automáticas em segundo plano e checagens sob demanda",
            "Histórico com código HTTP, latência e mensagem de erro de cada checagem",
            "Radar 3D: distância do centro é a latência, altura do feixe é o uptime",
            "Faixa de uptime, percentil 95 e gráfico de latência interativo",
        ],
        "decisions": [
            ("Proteção contra SSRF", "URLs que apontam para a rede interna são recusadas antes de qualquer requisição."),
            ("Radar num único shader", "A varredura é um fragment shader e a cena pausa quando sai da tela."),
        ],
        "ui": ("Interface", "React · React Three Fiber"),
        "api": ("API", "FastAPI · HTTPX"),
        "data": ("Dados", "SQLite"),
        "routes": [("POST", "/api/v1/endpoints"), ("POST", "/api/v1/endpoints/{id}/check"), ("GET", "/api/v1/endpoints/{id}/checks"), ("GET", "/health")],
        "tables": ["endpoints", "checks"],
        "stack": ["React", "TypeScript", "Vite", "React Three Fiber", "Motion", "FastAPI", "Pydantic", "HTTPX", "SQLite", "Vercel", "Render", "GitHub Actions"],
        "metrics": [("76", "testes automatizados", "rotas, monitoramento e segurança de URL"), ("60 s", "intervalo padrão", "das checagens em segundo plano")],
        "images": {
            "main": ("api-sentinel-radar", "Visão geral do API Sentinel com o radar 3D de latência e a lista de endpoints"),
            "detail": ("api-sentinel-detalhe", "Detalhe de um endpoint com faixa de disponibilidade e gráfico de tempo de resposta"),
            "mobile": ("api-sentinel-celular", "API Sentinel no celular"),
        },
        "live": "https://api-sentinel-pi.vercel.app",
        "frame": "https://api-sentinel-pi.vercel.app/",
        "code": "https://github.com/paulo-sempio-neto/api-sentinel",
    },
    {
        "id": "gondola",
        "name": "Gôndola",
        "kind": "Gestão de catálogo para pequenos negócios",
        "accent": "#2b4bff",
        "problem": "Pequenos comércios controlam produtos e preços em planilhas que ninguém mantém atualizadas.",
        "summary": "Uma API de catálogo com regras sérias de dados e um painel em que os produtos caem numa prateleira 3D.",
        "built": [
            "API REST com paginação, busca por nome e CRUD completo",
            "Controle de concorrência otimista: edição simultânea responde 409",
            "Preço guardado em centavos inteiros e migrações de esquema versionadas",
            "Interface de terminal e API compartilhando as mesmas regras",
            "Painel com cena 3D, paleta de comandos e desfazer exclusão",
        ],
        "decisions": [
            ("Ninguém sobrescreve ninguém", "Cada produto tem uma versão; salvar com versão antiga devolve conflito em vez de apagar o trabalho de outra pessoa."),
            ("Qualidade com piso", "O CI falha se a cobertura de testes ficar abaixo de 75%."),
        ],
        "ui": ("Interface", "React · React Three Fiber"),
        "api": ("API", "FastAPI · Pydantic"),
        "data": ("Dados", "SQLite · migrações"),
        "routes": [("GET", "/products?page=1&limit=20"), ("POST", "/products"), ("PUT", "/products/{id}"), ("DELETE", "/products/{id}")],
        "tables": ["products", "PRAGMA user_version"],
        "stack": ["React", "TypeScript", "Vite", "React Three Fiber", "Motion", "Python", "FastAPI", "Pydantic", "SQLite", "Pytest", "Docker", "GitHub Actions"],
        "metrics": [("116", "testes automatizados", "API, CLI, migrações e contratos"), ("75%", "cobertura mínima", "exigida pelo CI")],
        "images": {
            "main": ("gondola-cadastro", "Tela de cadastro do Gôndola com produtos caindo numa prateleira 3D"),
            "detail": ("gondola-painel", "Painel de produtos do Gôndola com etiquetas de preço"),
            "mobile": ("gondola-celular", "Painel do Gôndola no celular"),
        },
        "live": "https://product-management-system-beige.vercel.app",
        "frame": "https://product-management-system-beige.vercel.app/cadastro",
        "code": "https://github.com/paulo-sempio-neto/Product-Management-System",
    },
]

e = escape


def route_items(routes):
    return "".join(
        f'<li><b class="m m-{m.lower()}">{m}</b><code>{e(p)}</code></li>' for m, p in routes
    )


def stack_figure(p, *, hero=False, image_key="main"):
    ui_label, ui_tech = p["ui"]
    api_label, api_tech = p["api"]
    data_label, data_tech = p["data"]
    img, alt = p["images"][image_key]
    tables = "".join(f"<li>{e(t)}</li>" for t in p["tables"])
    loading = "eager" if hero else "lazy"
    live_attr = f' data-live-src="{p["frame"]}" data-live-title="{e(p["name"])} ao vivo"' if p.get("frame") and image_key == "main" else ""
    priority = ' fetchpriority="high"' if hero else ""
    return f"""
          <div class="stack-scene">
            <div class="layer layer-data" style="--i:0">
              <span class="layer-tag"><i></i>{data_label} <small>{e(data_tech)}</small></span>
              <ul class="tables">{tables}</ul>
            </div>
            <div class="layer layer-api" style="--i:1">
              <span class="layer-tag"><i></i>{api_label} <small>{e(api_tech)}</small></span>
              <ul class="routes">{route_items(p["routes"])}</ul>
            </div>
            <div class="layer layer-ui" style="--i:2"{live_attr}>
              <img src="assets/projects/{img}.webp" alt="{e(alt)}" width="1200" height="750" loading="{loading}" decoding="async"{priority}>
              <span class="layer-tag"><i></i>{ui_label} <small>{e(ui_tech)}</small></span>
            </div>
          </div>"""


def project_links(p, cls="links"):
    out = []
    if p["live"]:
        host = p["live"].replace("https://", "")
        out.append(f'<a class="link-primary" href="{p["live"]}" target="_blank" rel="noopener">Ver ao vivo<span class="link-host">{e(host)}</span><span aria-hidden="true" class="arrow">↗</span></a>')
    if p["code"]:
        out.append(f'<a class="link-secondary" href="{p["code"]}" target="_blank" rel="noopener">Ver código no GitHub <span aria-hidden="true" class="arrow">↗</span></a>')
    else:
        out.append('<span class="link-note">Código em repositório privado</span>')
    return f'<div class="{cls}">' + "".join(out) + "</div>"


def chapter(p, index):
    built = "".join(f"<li>{e(item)}</li>" for item in p["built"])
    decisions = "".join(f"<div><dt>{e(t)}</dt><dd>{e(d)}</dd></div>" for t, d in p["decisions"])
    stack = "".join(f"<li>{e(t)}</li>" for t in p["stack"])
    metrics = "".join(
        f'<div><dt><span class="metric-value">{e(v)}</span> {e(label)}</dt><dd>{e(note)}</dd></div>' for v, label, note in p["metrics"]
    )
    d_img, d_alt = p["images"]["main"]
    m_img, m_alt = p["images"]["mobile"]
    return f"""
      <article class="chapter" id="{p["id"]}" style="--accent:{p["accent"]}" aria-labelledby="{p["id"]}-title">
        <div class="chapter-media">
          <figure class="stack stack-scroll" data-stack="scroll">
{stack_figure(p, image_key="detail")}
            <figcaption class="stack-legend" aria-hidden="true">
              <span class="legend-ui">Interface</span><span class="legend-api">API</span><span class="legend-data">Dados</span>
            </figcaption>
          </figure>
        </div>
        <div class="chapter-copy">
          <p class="chapter-kind"><span class="chapter-dot" aria-hidden="true"></span>{e(p["kind"])}</p>
          <h3 id="{p["id"]}-title" class="chapter-title">{e(p["name"])}</h3>
          <p class="chapter-problem">{e(p["problem"])}</p>
          <p class="chapter-summary">{e(p["summary"])}</p>
          {project_links(p)}
          <h4 class="chapter-label">O que construí</h4>
          <ul class="built">{built}</ul>
          <h4 class="chapter-label">Decisões que fazem diferença</h4>
          <dl class="decisions">{decisions}</dl>
          <dl class="metrics">{metrics}</dl>
          <h4 class="chapter-label">Tecnologias</h4>
          <ul class="tags" aria-label="Tecnologias do {e(p["name"])}">{stack}</ul>
          <div class="gallery">
            <img class="gallery-desktop" src="assets/projects/{d_img}.webp" alt="{e(d_alt)}" width="1200" height="750" loading="lazy" decoding="async">
            <img class="gallery-mobile" src="assets/projects/{m_img}.webp" alt="{e(m_alt)}" width="600" height="1298" loading="lazy" decoding="async">
          </div>
        </div>
      </article>"""


def hero_tabs():
    buttons = "".join(
        f'<button type="button" class="hero-tab" data-project="{p["id"]}" aria-pressed="{"true" if i == 0 else "false"}" style="--accent:{p["accent"]}"><i aria-hidden="true"></i>{e(p["name"])}</button>'
        for i, p in enumerate(PROJECTS)
    )
    return buttons


def hero_templates():
    out = []
    for p in PROJECTS:
        out.append(f'<template data-stack-template="{p["id"]}" data-name="{e(p["name"])}" data-kind="{e(p["kind"])}">{stack_figure(p)}</template>')
    return "\n    ".join(out)


TOTAL_TESTS = 303 + 213 + 500 + 76 + 116

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
    <meta name="theme-color" content="#eceef2">
    <meta name="description" content="Paulo Sêmpio Neto, desenvolvedor full stack. Quatro produtos completos — da interface à API e ao banco de dados — com mais de 1.200 testes automatizados.">
    <meta property="og:title" content="Paulo Sêmpio Neto · Desenvolvedor full stack">
    <meta property="og:description" content="Ganho Certo, Lexin, API Sentinel e Gôndola: produtos completos, da interface à persistência.">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="pt_BR">
    <meta property="og:url" content="https://paulo-sempio-neto.github.io/">
    <meta property="og:image" content="https://paulo-sempio-neto.github.io/assets/og-image.png">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="canonical" href="https://paulo-sempio-neto.github.io/">
    <link rel="icon" href="favicon.svg" type="image/svg+xml">
    <link rel="preload" href="assets/fonts/familjen-grotesk-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
    <title>Paulo Sêmpio Neto · Desenvolvedor full stack</title>
  </head>
  <body>
    <a class="skip-link" href="#conteudo">Pular para o conteúdo</a>

    <header class="site-header">
      <a class="brand" href="#inicio" aria-label="Paulo Sêmpio Neto, início">
        <span class="brand-mark" aria-hidden="true"><i></i><i></i><i></i></span>
        <span class="brand-name">Paulo Sêmpio</span>
      </a>
      <button class="menu-toggle" type="button" aria-controls="navigation" aria-expanded="false" hidden>
        <span class="menu-label">Menu</span><span class="menu-icon" aria-hidden="true"><i></i><i></i></span>
      </button>
      <nav id="navigation" aria-label="Navegação principal">
        <a href="#projetos">Projetos</a>
        <a href="#competencias">Stack</a>
        <a href="#sobre">Sobre</a>
        <a class="nav-contact" href="#contato">Vamos conversar</a>
      </nav>
    </header>

    <main id="conteudo">
      <section class="hero" id="inicio" aria-labelledby="hero-title">
        <div class="hero-copy">
          <p class="availability"><span aria-hidden="true"></span>Disponível para estágio e vagas júnior full stack</p>
          <h1 id="hero-title" class="hero-title">
            <span class="line"><span>Da interface</span></span>
            <span class="line"><span>à regra de negócio</span></span>
            <span class="line"><span><em>e à persistência.</em></span></span>
          </h1>
          <p class="hero-description">Sou Paulo Sêmpio Neto, estudante de Ciência da Computação. Construo produtos completos — tela, API, banco de dados e testes — e coloco no ar.</p>
          <div class="hero-actions">
            <a class="button button-primary" href="#projetos">Ver os projetos <span aria-hidden="true">↓</span></a>
            <a class="button button-ghost" href="https://github.com/paulo-sempio-neto" target="_blank" rel="noopener">GitHub <span aria-hidden="true">↗</span></a>
          </div>
          <dl class="hero-proof">
            <div><dt>Produtos completos</dt><dd>4</dd></div>
            <div><dt>Testes automatizados</dt><dd>1.200+</dd></div>
            <div><dt>Camadas por produto</dt><dd>3</dd></div>
          </dl>
        </div>

        <div class="hero-stage">
          <figure class="stack stack-hero" data-stack="hero" aria-labelledby="hero-stack-caption">
{stack_figure(PROJECTS[0], hero=True)}
          </figure>
          <div class="hero-switch">
            <p id="hero-stack-caption" class="hero-caption" aria-live="polite"><strong>{e(PROJECTS[0]["name"])}</strong> {e(PROJECTS[0]["kind"])}</p>
            <div class="hero-tabs" role="group" aria-label="Escolha o projeto exibido nas camadas">{hero_tabs()}</div>
          </div>
        </div>
      </section>

      <section class="projects" id="projetos" aria-labelledby="projects-title">
        <div class="section-intro">
          <h2 id="projects-title">Quatro produtos.<br><span>Todas as camadas.</span></h2>
          <p>Role cada projeto e veja a tela se desmontar: por baixo estão os endpoints e as tabelas reais do código. Nada aqui é ilustrativo.</p>
        </div>
{"".join(chapter(p, i) for i, p in enumerate(PROJECTS))}
      </section>

      <section class="capabilities" id="competencias" aria-labelledby="skills-title">
        <div class="section-intro">
          <h2 id="skills-title">Stack organizada<br><span>por camada.</span></h2>
          <p>As mesmas três cores dos projetos: cada ferramenta resolve uma parte clara do produto.</p>
        </div>
        <ol class="layers-list">
          <li class="cap cap-ui"><h3><i aria-hidden="true"></i>Interface</h3><p>Interfaces responsivas e acessíveis, com movimento que explica o que mudou e 3D quando ajuda a entender os dados.</p><ul class="tags"><li>React</li><li>Next.js</li><li>TypeScript</li><li>Tailwind</li><li>Three.js</li><li>React Three Fiber</li><li>GSAP</li><li>Framer Motion</li><li>HTML e CSS</li></ul></li>
          <li class="cap cap-api"><h3><i aria-hidden="true"></i>API</h3><p>APIs REST com validação na entrada, regras de negócio fora das rotas e erros que dizem o que aconteceu.</p><ul class="tags"><li>Python</li><li>FastAPI</li><li>Pydantic</li><li>HTTPX</li><li>Route handlers do Next.js</li><li>Webhooks</li></ul></li>
          <li class="cap cap-data"><h3><i aria-hidden="true"></i>Dados</h3><p>Modelagem, migrações versionadas e consultas seguras, com isolamento de dados por usuário.</p><ul class="tags"><li>PostgreSQL</li><li>SQLAlchemy</li><li>Alembic</li><li>SQLite</li><li>Supabase</li></ul></li>
          <li class="cap cap-quality"><h3><i aria-hidden="true"></i>Qualidade e entrega</h3><p>Testes antes de chamar algo de pronto, CI em todo push e deploy contínuo.</p><ul class="tags"><li>Pytest</li><li>Vitest</li><li>Playwright</li><li>Ruff e mypy</li><li>GitHub Actions</li><li>Docker</li><li>Vercel</li><li>Render</li></ul></li>
        </ol>
      </section>

      <section class="about" id="sobre" aria-labelledby="about-title">
        <div class="about-head">
          <img class="about-photo" src="https://github.com/paulo-sempio-neto.png?size=320" alt="Foto de Paulo Sêmpio Neto" width="160" height="160" loading="lazy" decoding="async">
          <h2 id="about-title">Aprender o sistema inteiro.<br><span>Construir melhor.</span></h2>
        </div>
        <div class="about-copy">
          <p class="about-lead">Sou Paulo Malpice Sêmpio Neto, estudante de Ciência da Computação e desenvolvedor full stack.</p>
          <p>Construo projetos para entender o caminho completo de uma funcionalidade: a interface que orienta a pessoa, a API que aplica as regras e o banco que guarda o estado do produto. Quando um projeto fica pronto, ele vai para o ar e ganha testes.</p>
          <p>Busco estágio ou posição júnior full stack para colaborar com um time, receber feedback e evoluir com código em produção.</p>
          <dl class="principles">
            <div><dt>Clareza</dt><dd>Separar responsabilidades para o código ser fácil de entender e de mudar.</dd></div>
            <div><dt>Evidência</dt><dd>Validar entradas e testar o caminho de erro, não só o caminho feliz.</dd></div>
            <div><dt>Iteração</dt><dd>Começar pequeno, observar os limites e evoluir com propósito.</dd></div>
          </dl>
          <p class="education"><strong>Ciência da Computação, UNIC</strong> Conclusão prevista em dezembro de 2029</p>
        </div>
      </section>

      <section class="contact" id="contato" aria-labelledby="contact-title">
        <h2 id="contact-title" class="contact-title">Vamos construir<br>a próxima camada?</h2>
        <div class="contact-row">
          <a class="contact-email" href="mailto:paulosempio.dev@gmail.com">paulosempio.dev@gmail.com<span aria-hidden="true" class="arrow">↗</span></a>
          <div class="contact-social">
            <a href="https://www.linkedin.com/in/paulo-malpice-sempio-neto/" target="_blank" rel="noopener">LinkedIn <span aria-hidden="true">↗</span></a>
            <a href="https://github.com/paulo-sempio-neto" target="_blank" rel="noopener">GitHub <span aria-hidden="true">↗</span></a>
          </div>
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <p>© <span id="year">2026</span> Paulo Malpice Sêmpio Neto</p>
      <p>Feito à mão com HTML, CSS e JavaScript. Sem bibliotecas.</p>
      <a href="#inicio">Voltar ao início <span aria-hidden="true">↑</span></a>
    </footer>

    {hero_templates()}
  </body>
</html>
"""

OUT.write_text(html, encoding="utf-8")
print("written", OUT, len(html))
