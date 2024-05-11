# credits playwright quick start

from urllib.parse import urlparse
import datetime
import logging
import config

from playwright.async_api import async_playwright
from playwright_stealth import stealth_async

async def screenshot(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        logging.info("browser launched")
        browser = await browser.new_context(
            user_agent=config.user_agent,
            viewport=config.viewport
        )
        page = await browser.new_page()
        await stealth_async(page)
        logging.info(f"url: {url}")
        if url[:4] != 'http':
            logging.info("Appending https to url")
            url = 'https://' + url
        await page.goto(url)
        logging.info("page accessed")
        logging.info("waiting")
        await page.wait_for_timeout(2500)
        await page.evaluate("() => {document.body.style.zoom=0.8;}")
        file_name = f"images/{datetime.datetime.now().strftime("%Y-%m-%d %H %Y")} " \
            + f"{urlparse(page.url).hostname}.png"
        await page.screenshot(path=file_name)
        title = await page.title()
        logging.info("Screenshotted" + title)
        await browser.close()
        return file_name