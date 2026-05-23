from playwright.async_api import async_playwright


class AmazonBot:
    def __init__(self):
        self.browser = None
        self.context = None
        self.page = None

    # -----------------------
    # START BROWSER
    # -----------------------
    async def start(self):
        if self.browser is None:
            self.p = await async_playwright().start()

            self.context = await self.p.chromium.launch_persistent_context(
                user_data_dir="amazon_profile",
                headless=False,
                args=["--start-maximized"],
                viewport=None
            )

            if self.context.pages:
                self.page = self.context.pages[0]
            else:
                self.page = await self.context.new_page()

            self.browser = self.context

    # -----------------------
    async def open_amazon(self):
        await self.start()
        await self.page.goto("https://www.amazon.in")
        await self.page.wait_for_load_state("domcontentloaded")
        return "Amazon opened"

    # -----------------------
    async def search_item(self, item):
        await self.page.fill("#twotabsearchtextbox", item)
        await self.page.keyboard.press("Enter")
        await self.page.wait_for_timeout(4000)
        return f"Searched {item}"

    # -----------------------
    # -----------------------
# OPEN BEST PRODUCT (ROBUST)
# -----------------------
    # -----------------------
# OPEN PRODUCT FROM SEARCH
# -----------------------
    async def open_best_product(self, keyword=None):
     await self.page.wait_for_timeout(5000)

    # scroll to ensure results load
     for _ in range(6):
        await self.page.mouse.wheel(0, 4000)
        await self.page.wait_for_timeout(1200)

    # get all product result blocks
     cards = await self.page.query_selector_all(
        "div[data-component-type='s-search-result']"
     )

     if not cards:
        return "No products found"

     for card in cards:
        try:
            # find ANY clickable product link
            link = await card.query_selector("a[href*='/dp/'], a[href*='/sspa/']")
            if not link:
                continue

            await link.scroll_into_view_if_needed()
            await self.page.wait_for_timeout(800)

            await link.click()
            await self.page.wait_for_timeout(4000)

            # switch to product tab
            self.page = self.context.pages[-1]
            await self.page.wait_for_load_state("domcontentloaded")

            return "Opened product"

        except:
            continue

     return "Product open failed"
    
    async def open_cheapest_product(self):
     await self.page.wait_for_timeout(5000)

    # scroll to load products
     for _ in range(6):
        await self.page.mouse.wheel(0, 4000)
        await self.page.wait_for_timeout(1000)

     cards = await self.page.query_selector_all(
        "div[data-component-type='s-search-result']"
     )

     cheapest_price = 99999999
     cheapest_link = None

     for card in cards:
        try:
            # get price
            price_el = await card.query_selector(".a-price-whole")
            if not price_el:
                continue

            price_text = await price_el.inner_text()
            price = int(price_text.replace(",", "").strip())

            # get product link
            link = await card.query_selector("h2 a")

            if price < cheapest_price and link:
                cheapest_price = price
                cheapest_link = link

        except:
            continue

     if not cheapest_link:
        return "No product found"

     await cheapest_link.scroll_into_view_if_needed()
     await self.page.wait_for_timeout(1000)

     await cheapest_link.click()
     await self.page.wait_for_timeout(4000)

    # switch to new tab
     self.page = self.context.pages[-1]
     await self.page.wait_for_load_state("domcontentloaded")

     return f"Opened cheapest product ₹{cheapest_price}"

    
    # -----------------------
# FULL AUTONOMOUS AGENT
# -----------------------
    async def autonomous_buy(self, item, mode="cheap"):

     await self.open_amazon()
     await self.search_item(item)

     if mode == "cheap":
        res = await self.open_cheapest_product()
     else:
        res = await self.open_best_product()

     if "Opened" not in res:
        return "Product open failed"

     await self.add_to_cart()
     await self.go_to_checkout()
     await self.go_to_payment()
     await self.payment_cod_and_place(place=False)

     return f"Autonomous shopping completed using mode: {mode}"





    # -----------------------
    # -----------------------
# ADD TO CART (ULTRA STABLE)
# -----------------------
    # -----------------------
# ADD TO CART (PRECISE FIX)
# -----------------------
    # -----------------------
# ADD TO CART (REAL FIX)
# -----------------------
    async def add_to_cart(self):
     await self.page.wait_for_timeout(4000)

     try:
        # CLICK REAL ADD TO CART
        btn = await self.page.wait_for_selector("#add-to-cart-button", timeout=30000)
        await btn.scroll_into_view_if_needed()
        await btn.click()

        await self.page.wait_for_timeout(3000)

        # -----------------------------
        # HANDLE WARRANTY POPUP
        # -----------------------------
        try:
            no_thanks = await self.page.wait_for_selector(
                "input[aria-labelledby='attachSiNoCoverage-announce']",
                timeout=5000
            )
            await no_thanks.click()
            await self.page.wait_for_timeout(3000)
            return "Added to cart → Warranty popup handled"
        except:
            # popup didn't appear
            return "Added to cart"

     except Exception as e:
        return f"Add to cart failed: {e}"





    # -----------------------
    # CHECKOUT
    # -----------------------
    async def go_to_checkout(self):
        await self.page.goto("https://www.amazon.in/gp/cart/view.html")
        await self.page.wait_for_load_state("domcontentloaded")

        try:
            await self.page.wait_for_selector("input[name='proceedToRetailCheckout']", timeout=15000)
            await self.page.click("input[name='proceedToRetailCheckout']")
            await self.page.wait_for_timeout(5000)
            return "Reached checkout page"
        except:
            return "Checkout button not found"

    # -----------------------
    # PAYMENT PAGE
    # -----------------------
    async def go_to_payment(self):
        await self.page.wait_for_timeout(5000)

        try:
            await self.page.wait_for_selector("input[name='shipToThisAddress']", timeout=15000)
            await self.page.click("input[name='shipToThisAddress']")
            await self.page.wait_for_timeout(5000)
        except:
            pass

        return "Reached payment page"

   # ---------------------------
# SELECT COD → USE METHOD → PLACE ORDER
# ---------------------------
    async def payment_cod_and_place(self, place=False):

    # ---------- STEP 1: CLICK COD ----------
     try:
        cod_radio = await self.page.wait_for_selector(
            "input[name='ppw-instrumentRowSelection'][value*='COD']",
            timeout=30000
        )

        await cod_radio.scroll_into_view_if_needed()
        await cod_radio.click()

        # IMPORTANT DELAY (Amazon loads UI)
        await self.page.wait_for_timeout(5000)

     except:
        return "COD radio button not found"


    # ---------- STEP 2: USE PAYMENT METHOD ----------
     try:
        use_btn = await self.page.wait_for_selector(
            "input[data-testid='bottom-continue-button']",
            timeout=30000
        )

        await use_btn.scroll_into_view_if_needed()
        await use_btn.click()

        # wait for final review page
        await self.page.wait_for_timeout(6000)

     except:
        return "Use payment method button not found"


    # ---------- SAFE DEMO STOP ----------
     if not place:
        return "COD selected and confirmed (safe demo stop)"


    # ---------- STEP 3: PLACE ORDER ----------
     try:
        place_btn = await self.page.wait_for_selector(
            "#placeOrder",
            timeout=60000
        )

        await place_btn.scroll_into_view_if_needed()
        await self.page.wait_for_timeout(2000)

        # retry click (Amazon sometimes blocks first click)
        for _ in range(5):
            try:
                await place_btn.click(force=True)
                await self.page.wait_for_timeout(4000)
                return "🎉 ORDER PLACED SUCCESSFULLY"
            except:
                await self.page.wait_for_timeout(2000)

        return "Clicked but Amazon blocked final submit"

     except Exception as e:
        return f"Place order failed: {e}"


bot = AmazonBot()


def get_bot():
    return bot
