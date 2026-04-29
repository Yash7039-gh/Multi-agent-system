"""
Agent 3: Reviewer
- Reviews and improves the written report
- Gives a quality score
"""

from llm_config import call_llm


def reviewer_agent(report: str) -> str:
    print("✅ [Agent 3 - Reviewer] Reviewing report...")

    system_prompt = """You are a Senior Editor and Quality Reviewer.
You have reviewed thousands of reports and know exactly what makes
great writing. You are constructive but uncompromising on quality."""

    user_message = f"""Review this report carefully and produce a final improved version.

REPORT TO REVIEW:
{report}

Check for:
1. Factual accuracy and completeness
2. Clarity and readability
3. Structure and logical flow
4. Grammar and professional tone
5. Any missing sections or weak areas

Then output the FINAL improved report with:
- A quality score (e.g ⭐ 9/10) at the very top
- A 2-3 line reviewer note on what was improved
- The complete polished report below

Output in Markdown format."""

    result = call_llm(system_prompt, user_message, temperature=0.3)
    print("✅ [Reviewer] Done!\n")
    return result
