def score_lead(d):
    score=0
    b=float(d.get("budget",0)); e=int(d.get("engagement",0))
    if b>=5000: score+=35
    elif b>=2000: score+=25
    elif b>0: score+=10
    score+=min(max(e,0),30)
    text=d.get("requirement","").lower()
    score+=min(sum(8 for k in ["urgent","demo","buy","purchase","automation","ai","chatbot"] if k in text),35)
    score=min(score,100)
    return score, ("Hot" if score>=70 else "Warm" if score>=40 else "Cold")

from openai import OpenAI
import os


def score_lead(d):
    score = 0
    b = float(d.get("budget", 0))
    e = int(d.get("engagement", 0))

    if b >= 5000:
        score += 35
    elif b >= 2000:
        score += 25
    elif b > 0:
        score += 10

    score += min(max(e, 0), 30)

    text = d.get("requirement", "").lower()
    keywords = ["urgent", "demo", "buy", "purchase", "automation", "ai", "chatbot"]
    score += min(sum(8 for k in keywords if k in text), 35)

    score = min(score, 100)

    category = "Hot" if score >= 70 else "Warm" if score >= 40 else "Cold"

    return score, category


def generate_message(d):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "OpenAI API key is not configured."

    client = OpenAI(api_key=api_key)

    prompt = f"""
You are an AI sales lead generation assistant.

Create a professional and personalized sales outreach message.

Lead Name: {d.get("name")}
Company: {d.get("company")}
Industry: {d.get("industry")}
Budget: {d.get("budget")}
Requirement: {d.get("requirement")}
Lead Score: {d.get("score")}
Lead Category: {d.get("category")}

Write a short, natural, professional message.
Do not mention the lead score.
End with a clear call to action.
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text