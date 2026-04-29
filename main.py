import os
from agents.researcher import researcher_agent
from agents.writer import writer_agent
from agents.reviewer import reviewer_agent


def run(topic: str):
    print("=" * 55)
    print("  🤖 Collaborative Multi-Agent System Starting...")
    print("=" * 55)
    print(f"  📌 Topic: {topic}")
    print("=" * 55)

    # ── Agent 1: Research ──────────────────────────────
    research_notes = researcher_agent(topic)

    # ── Agent 2: Write ─────────────────────────────────
    draft_report = writer_agent(topic, research_notes)

    # ── Agent 3: Review ────────────────────────────────
    final_report = reviewer_agent(draft_report)

    # ── Save Output ────────────────────────────────────
    os.makedirs("output", exist_ok=True)
    output_path = "output/final_report.md"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Topic: {topic}\n\n")
        f.write(final_report)

    print("=" * 55)
    print(f"  🎉 SUCCESS! Report saved to: {output_path}")
    print("=" * 55)

    return final_report


if __name__ == "__main__":
    print("\n🤖 Welcome to the Multi-Agent System!\n")
    topic = input("Enter a topic to research:\n> ").strip()

    if not topic:
        topic = "The impact of Agentic AI on software development in 2026"

    run(topic)
