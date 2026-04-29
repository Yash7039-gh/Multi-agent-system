"""
Agent 1: Researcher
- Gathers detailed information on the given topic
"""

from llm_config import call_llm


def researcher_agent(topic: str) -> str:
    print("\n🔍 [Agent 1 - Researcher] Starting research...")

    system_prompt = """You are a Senior Research Analyst with 15 years of experience.
You are known for finding accurate, detailed, and well-organized information.
Your job is to research any topic deeply and return structured research notes."""

    user_message = f"""Research this topic thoroughly: {topic}

Your research notes MUST include:
1. Clear overview / definition of the topic
2. Latest trends and developments (2025-2026)
3. Key statistics or data points
4. Real-world use cases and examples
5. Expert opinions or insights
6. Challenges and limitations

Write at least 500 words. Use clear headings and bullet points."""

    result = call_llm(system_prompt, user_message, temperature=0.5)
    print("✅ [Researcher] Done!\n")
    return result
