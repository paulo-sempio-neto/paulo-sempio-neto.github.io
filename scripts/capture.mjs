// Captura as telas publicadas de cada projeto e grava em assets/projects/*.webp.
// Roda no GitHub Actions (ver .github/workflows/refresh-screenshots.yml).
// Movimento reduzido deixa as capturas estáveis, então o arquivo só muda
// quando a tela do projeto realmente mudou.
import { execFileSync } from "node:child_process";
import { readFileSync, rmSync } from "node:fs";
import { chromium } from "playwright";

const config = JSON.parse(readFileSync(new URL("./projects.json", import.meta.url), "utf8"));
const viewports = {
  desktop: { width: 1440, height: 900, deviceScaleFactor: 1, out: 1200 },
  mobile: { width: 390, height: 844, deviceScaleFactor: 2, out: 600 },
};

const browser = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--ignore-gpu-blocklist"] });
let failures = 0;

for (const capture of config.captures) {
  if (!capture.url) {
    console.log(`skip ${capture.file}: sem url`);
    continue;
  }
  const viewport = viewports[capture.viewport];
  const context = await browser.newContext({ ...viewport, reducedMotion: "reduce", locale: "pt-BR" });
  const page = await context.newPage();
  const png = `/tmp/${capture.file}.png`;
  try {
    await page.goto(capture.url, { waitUntil: "domcontentloaded", timeout: 90_000 });
    // Backends em plano gratuito podem levar até um minuto para acordar.
    await page.waitForSelector(capture.waitFor, { timeout: 90_000 });
    await page.waitForTimeout(4000);
    await page.screenshot({ path: png });
    execFileSync("ffmpeg", ["-loglevel", "error", "-y", "-i", png, "-vf", `scale=${viewport.out}:-2`, "-c:v", "libwebp", "-quality", "80", `assets/projects/${capture.file}.webp`]);
    console.log(`ok ${capture.file}`);
  } catch (error) {
    failures += 1;
    console.log(`mantida a captura anterior de ${capture.file}: ${error.message.split("\n")[0]}`);
  } finally {
    rmSync(png, { force: true });
    await context.close();
  }
}

await browser.close();
if (failures === config.captures.filter((c) => c.url).length) process.exitCode = 1;
