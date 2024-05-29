# credits playwright quick start

from urllib.parse import urlparse
import datetime
import logging
import config

from pathlib import Path

from playwright.async_api import async_playwright

async def screenshot(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        logging.info("browser launched")
        browser = await browser.new_context(
            user_agent=config.user_agent,
            viewport=config.viewport
        )
        browser.set_default_timeout(config.default_timeout) # 30 seconds by default
        page = await browser.new_page()
        logging.info(f"url: {url}")
        if url[:4] != 'http':
            logging.info("Appending https to url")
            url = 'https://' + url
        await page.goto(url)
        logging.info("page accessed")
        logging.info("waiting")
        await page.evaluate("() => {document.body.style.zoom=0.8;}")
        file_name = f"images/{datetime.datetime.now().strftime("%Y-%m-%d %H %Y")} " \
            + f"{urlparse(page.url).hostname}.png"
        path = Path('image')
        if not Path('image').exists():
            path.mkdir()
        await page.screenshot(path=file_name)
        title = await page.title()
        logging.info("Screenshotted" + title)
        await browser.close()
        return file_name
