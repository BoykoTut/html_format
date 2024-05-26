import asyncio
from pyppeteer import launch

async def save_streamlit_html():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://localhost:8501')
    await page.waitForSelector('body')  # Wait until the page is fully loaded
    content = await page.content()
    with open('streamlit_app.html', 'w', encoding='utf-8') as f:
        f.write(content)
    await browser.close()

asyncio.get_event_loop().run_until_complete(save_streamlit_html())
