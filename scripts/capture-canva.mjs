// The Canva connector supplies small previews. Capture the supplied native
// viewer when higher-quality original pages are needed. No design is edited.
// Requires Playwright and a Chromium browser; --browser can select an installed one.
import fs from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)))
let playwright
try { playwright = await import('playwright') }
catch { playwright = await import('../.cache/qa/node_modules/playwright/index.mjs') }
const browserArgument = process.argv.indexOf('--browser')
const executablePath = browserArgument >= 0 ? process.argv[browserArgument + 1] : undefined
const manifestPath = path.join(root, 'sources/canva.json')
const manifest = JSON.parse(await fs.readFile(manifestPath, 'utf8'))
const browser = await playwright.chromium.launch({ executablePath, headless: true })
try {
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 })
  await page.goto(`${manifest.url.replace(/\/edit$/, '/view')}?embed#1`, { waitUntil: 'networkidle' })
  await page.evaluate(() => document.fonts.ready)
  // Hide viewer controls only in this temporary capture browser. The rendered
  // design, including its background and every content element, remains intact.
  const title = page.getByText('LECTURE 9:', { exact: true }).first()
  await title.waitFor()
  const controlSelector = await page.getByRole('button', { name: 'Previous page', exact: true }).evaluate((button) => {
    const title = [...document.querySelectorAll('*')].find(el => el.childElementCount === 0 && el.textContent.trim() === 'LECTURE 9:')
    if (!title) throw new Error('Cannot locate original design content')
    let container = button
    while (container.parentElement && !container.parentElement.contains(title)) container = container.parentElement
    if (container === document.body || container === document.documentElement) throw new Error('Refusing to hide the document')
    container.setAttribute('data-capture-controls', 'true')
    return '[data-capture-controls="true"]'
  })
  await page.addStyleTag({ content: `${controlSelector} { visibility: hidden !important; }` })
  for (const original of manifest.pages) {
    await page.waitForTimeout(1300)
    await page.evaluate(() => document.fonts.ready)
    const filepath = path.join(root, 'public', original.image.replace(/^\//, ''))
    await page.screenshot({ path: filepath, animations: 'disabled' })
    original.connector_width ??= original.width
    original.connector_height ??= original.height
    original.width = 1920
    original.height = 1080
    original.capture = 'native Canva viewer'
    console.log(`Captured Canva Lecture 9 page ${original.number} / ${manifest.pages.length}`)
    if (original.number < manifest.pages.length) {
      const next = page.getByRole('button', { name: 'Next page', exact: true, includeHidden: true })
      await next.evaluate(button => button.click())
    }
  }
  manifest.effects = 'All native page states captured in source order. The native Canva viewer remains available for original animations.'
  await fs.writeFile(manifestPath, JSON.stringify(manifest, null, 2) + '\n')
} finally { await browser.close() }
