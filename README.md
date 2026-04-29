Project Overview
This project is a Collaborative Multi-Agent System where multiple AI agents work together to research, write, and review a professional report on any given topic. Each agent has a specific role, communicates results to the next agent, and the system produces a final polished Markdown report automatically.
Project Name	Collaborative Multi-Agent System
Topic Number	Topic 1 of 5
Series	Agentic AI Projects 2026
Language	Python 3.14+
AI Model	LLaMA 3.3 70B (via Groq)
API Used	Groq API (Free Tier)
Framework	Pure Python — No CrewAI needed
Output	Markdown Report (.md file)
How It Works
The system runs 3 AI agents sequentially. Each agent completes its task and passes results to the next:

User enters a Topic
↓
🔍 Agent 1: Researcher  →  Gathers facts, trends & data
↓
✍️ Agent 2: Writer  →  Writes a structured report
↓
✅ Agent 3: Reviewer  →  Reviews, scores & polishes
↓
📄 Final Report saved to output/final_report.md

🤖 The 3 Agents

Agent 1 — Researcher
•	Role: Senior Research Analyst
•	Finds key facts, statistics, trends and expert opinions
•	Organizes findings into structured research notes
•	Output: Detailed notes (500+ words)

Agent 2 — Writer
•	Role: Expert Technical Writer
•	Transforms research notes into a professional report
•	Follows a structured format with all sections
•	Output: Full Markdown report (800-1200 words)

Agent 3 — Reviewer
•	Role: Senior Editor & Quality Reviewer
•	Checks accuracy, clarity, structure and grammar
•	Fixes issues and gives a quality score (e.g. 9/10)
•	Output: Final polished Markdown report

📄 Report Output Structure
•	Quality Score (e.g. ⭐ 9/10)
•	Reviewer Notes
•	Title & Executive Summary
•	Introduction
•	Key Findings
•	Real-World Use Cases
•	Challenges & Limitations
•	Conclusion & Future Outlook

🛠️ Tech Stack

Python	3.14+ (Latest — no version conflicts)
Groq API	Free tier — Ultra fast LLaMA 3.3 inference
Model	llama-3.3-70b-versatile
python-dotenv	For secure API key management
requests	HTTP library

📁 Project Structure
•	main.py — Entry point, runs all 3 agents
•	llm_config.py — Groq API connection
•	agents/researcher.py — Agent 1
•	agents/writer.py — Agent 2
•	agents/reviewer.py — Agent 3
•	requirements.txt — Only 3 packages
•	.env — Your secret API keys (never upload this!)
•	output/final_report.md — Generated report

💡 Key Concepts Demonstrated
•	Multi-Agent Collaboration — agents pass results to each other
•	Task Delegation — each agent has one clear responsibility
•	Structured Workflow — sequential pipeline (Research → Write → Review)
•	Role-Based Agents — each agent has a unique role and backstory
•	Autonomous Execution — runs end-to-end with no human input
