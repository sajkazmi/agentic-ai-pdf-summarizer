import os
import fitz  # PyMuPDF
import openai

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def generate_summary(text, api_key, iterations=3):
    """Autonomous loop to refine the research paper summary."""
    client = openai.Client(api_key=api_key)
    summary = ""

    for _ in range(iterations):
        print("Generating/refining summary...")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI assistant who autonomously summarizes and refines research papers."},
                {"role": "user", "content": f"Summarize the following research paper content:{text}\nCurrent summary: {summary}\nImprove this summary, ensuring clarity and conciseness."}
            ],
            max_tokens=300
        )
        summary = response.choices[0].message.content.strip()
    
    return summary

def validate_summary(summary, api_key):
    """Check if the summary is clear, concise, and accurate."""
    client = openai.Client(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a critical AI reviewer who checks research paper summaries."},
            {"role": "user", "content": f"Review the following summary for clarity, conciseness, and accuracy:\n{summary}\nProvide a brief pass/fail assessment and suggestions for improvement."}
        ],
        max_tokens=150
    )
    return response.choices[0].message.content.strip()

def main():
    api_key = input("Enter your OpenAI API key: ")
    pdf_path = input("Enter the path to the research paper PDF: ")

    if not os.path.exists(pdf_path):
        print("Error: File not found.")
        return

    print("Extracting text from PDF...")
    paper_text = extract_text_from_pdf(pdf_path)

    print("Text extraction complete. Generating agentic AI summary...")
    summary = generate_summary(paper_text, api_key)

    print("Validating summary...")
    review = validate_summary(summary, api_key)

    print("\n--- Final Research Paper Summary ---\n")
    print(summary)
    print("\n--- Summary Review ---\n")
    print(review)

if __name__ == "__main__":
    main()
