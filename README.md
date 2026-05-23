# 🤖 Autonomous AI Shopping Agent

An AI-powered autonomous shopping agent that can:

- Search products on Amazon
- Analyze product listings
- Select cheapest or best products automatically
- Open product pages dynamically
- Add items to cart
- Handle checkout workflows
- Select payment methods automatically
- Navigate until final order page using browser automation

---

# 🚀 Features

## 🔍 Intelligent Product Search
- Search products directly on Amazon
- Dynamic product discovery
- Real-time browser automation

## 🧠 Autonomous Decision Making
- Cheapest product selection
- Best product selection
- Dynamic DOM parsing
- Smart product handling

## 🛒 Automated Shopping Workflow
- Product page navigation
- Add-to-cart automation
- Warranty popup handling
- Checkout automation

## 💳 Payment Automation
- Detect Cash on Delivery (COD)
- Select payment method automatically
- Navigate to final order page

## 🖥 Interactive Frontend
- Streamlit-based frontend
- Real-time autonomous shopping demo
- Strategy-based product selection

## 🔌 MCP Architecture
- FastMCP server-client architecture
- Modular AI-agent workflow
- Scalable automation design

---

# 🏗 Architecture

```text
Streamlit Frontend
        ↓
MCP Client
        ↓
FastMCP Server
        ↓
AmazonBot Agent
        ↓
Playwright Automation
        ↓
Amazon Website
        ↓
Autonomous Shopping Workflow
```

---

# 🧠 Autonomous Workflow

```text
User Input
    ↓
Search Product
    ↓
Analyze Search Results
    ↓
Select Cheapest / Best Product
    ↓
Open Product Page
    ↓
Add To Cart
    ↓
Handle Warranty Popup
    ↓
Proceed To Checkout
    ↓
Select COD Payment
    ↓
Navigate To Final Order Page
```

---

# 🛠 Tech Stack

## Frontend
- Streamlit

## Backend
- Python
- AsyncIO

## Browser Automation
- Playwright

## MCP Framework
- FastMCP

## Concepts Used
- Autonomous AI Agents
- Browser Automation
- Async Programming
- MCP Client-Server Architecture

---

# 📁 Project Structure

```text
MCPpro2/
│
├── frontend.py              # Streamlit frontend
├── mcp_server.py            # MCP server
├── amazon_tools.py          # Autonomous shopping agent
├── test_client.py           # MCP test client
├── requirements.txt
├── README.md
│
├── amazon_profile/          # Persistent browser profile
│
└── venv/
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Autonomous-AI-Shopping-Agent.git

cd Autonomous-AI-Shopping-Agent
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 requirements.txt

```txt
streamlit
playwright
fastmcp
asyncio
```

---

# 🌐 Install Playwright Browsers

```bash
playwright install
```

---

# ▶️ Run MCP Server

```bash
python mcp_server.py
```

---

# ▶️ Run Frontend

```bash
streamlit run frontend.py
```

---

# 🧪 Run Test Client

```bash
python test_client.py
```

---

# 🖥 Frontend Features

- Product search input
- Cheapest / Best strategy selection
- Autonomous browser automation
- Real-time workflow execution

---

# 🧠 MCP Tool Architecture

## MCP Tools

```python
open_amazon()
search_item()
open_cheapest_product()
open_best_product()
add_to_cart()
go_to_checkout()
go_to_payment()
payment_cod_and_place()
buy()
```

---

# 🔥 Product Selection Strategies

## 💰 Cheapest Strategy
- Scans all visible product cards
- Extracts dynamic product prices
- Automatically selects lowest-priced product

## ⭐ Best Strategy
- Opens top valid product from search results
- Uses robust product detection logic

---

# 🛡 Safety Features

✅ Safe demo mode  
✅ Stops before real order placement  
✅ Uses isolated Playwright browser profile  
✅ Does not use personal Chrome profile  

---

# 🚀 Future Enhancements

- Multi-agent workflows
- Voice-controlled shopping
- LLM-powered product recommendations
- Flipkart integration
- Product comparison engine
- Screenshot monitoring
- Real-time AI reasoning dashboard

---

# 💡 Use Cases

- Autonomous browser agents
- AI workflow orchestration
- Browser automation systems
- MCP architecture demos
- AI commerce assistants

---

# 🧠 Key Concepts Demonstrated

- MCP Client/Server Architecture
- Autonomous AI Agents
- Browser Automation
- Dynamic DOM Handling
- Async Programming
- Workflow Orchestration
- AI-driven Automation

---

# 👨‍💻 Author

## Akhilesh Saga

---

# ⭐ If You Like This Project

Give this repository a ⭐ on GitHub

---
