## 📄 `README.md`

```markdown
# Airline Demand Trends Dashboard

A Python-powered web app that fetches live flight data, analyzes airline market demand, and provides **AI-generated insights** — built for hostel owners monitoring air travel trends in Australia.
---

## Features

✅ **Live Flight Data**  
✅ **Popular Airlines & Routes**  
✅ **Interactive Charts (Plotly)**  
✅ **AI-Powered Summary & Q&A** using OpenAI  
✅ **Streamlit Web App UI**

---

## How It Works

1. **Enter Departure Airport Code** (e.g. `SYD` for Sydney)
2. Fetches real-time flight data using [AviationStack API](https://aviationstack.com/)
3. Cleans and processes data (Pandas)
4. Visualizes insights using **Plotly**
5. Uses **OpenAI GPT-3.5** to:
   - Summarize trends
   - Answer custom user questions

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** | Core programming language |
| **Streamlit** | Web app framework |
| **Pandas** | Data cleaning & transformation |
| **Plotly** | Interactive charts |
| **AviationStack API** | Flight data |
| **OpenAI API** | AI insights & question answering |

---

## Folder Structure

.
├── app.py                 # Main Streamlit app
├── ai\_insights.py         # AI summary + Q\&A logic
├── process\_data.py        # Fetching and cleaning flight data
├── .env                   # API keys (OpenAI, AviationStack)
├── requirements.txt       # Dependencies
└── README.md


---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/airline-demand-dashboard.git
cd airline-demand-dashboard

### 2. Install dependencies

```bash
pip install -r requirements.txt


### 3. Set up environment variables

Create a `.env` file:


OPENAI_API_KEY=your-openai-key
AVIATIONSTACK_API_KEY=your-aviationstack-key


### 4. Run the app

```bash
streamlit run app.py


---

## Example Questions You Can Ask AI

* What’s the best time to fly from Sydney?
* Which routes have the highest demand?
* Which airlines operate the most flights?

---

## Future Improvements

* Filter by airline, time of day, or destination
* Price tracking over time
* Alerts for high-demand periods
* Deploy on Streamlit Cloud or HuggingFace Spaces
