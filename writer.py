"""
Agent 2: Writer
- Transforms research notes into a polished report
"""

from llm_config import call_llm


def writer_agent(topic: str, research_notes: str) -> str:
    print("✍️  [Agent 2 - Writer] Writing report...")

    system_prompt = """You are an Expert Technical Writer with years of experience
writing professional reports, white papers, and articles.
You turn research notes into clear, engaging, well-structured Markdown reports."""

    user_message = f"""Using the research notes below, write a professional report on:
**{topic}**

RESEARCH NOTES:
{research_notes}

Your report MUST follow this exact structure:
# [Title]

## Executive Summary
(150 words summary)

## Introduction

## Key Findings
(use subheadings and bullet points)

## Real-World Use Cases

## Challenges & Limitations

## Conclusion & Future Outlook

Format: Markdown
Tone: Professional but easy to read
Length: 800-1200 words"""

    result = call_llm(system_prompt, user_message, temperature=0.7)
    print("✅ [Writer] Done!\n")
    return result
