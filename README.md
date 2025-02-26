# Agentic AI PDF Summarizer

🚀 Overview

The Agentic AI PDF Summarizer is an autonomous AI tool designed to extract text from PDF research papers and generate concise, accurate summaries using OpenAI's models. It also validates the summaries for clarity and accuracy through an iterative process.

✨ Features

PDF Text Extraction: Reads text from any PDF file.

Autonomous Summarization: Utilizes agentic AI techniques to iteratively improve summaries.

Validation System: Critically reviews summaries to ensure quality.

Customizable Iterations: Users can specify the number of refinement loops.

📦 Installation

Clone the repository:

git clone https://github.com/yourusername/agentic-ai-pdf-summarizer.git
cd agentic-ai-pdf-summarizer

Create a virtual environment (optional but recommended):

# Windows\python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

🔧 Usage

Run the summarizer:

python autoresearcher.py

Input the path to your PDF file when prompted, or update the pdf_path variable directly in the main() function.

⚙️ Environment Variables

To use OpenAI's API, set your API key:

Add your API key directly in the code (not recommended for production):

api_key = "your-openai-api-key"

Or, create a .env file (better practice):

OPENAI_API_KEY=your-openai-api-key

And update your code to load it:

import os
ios.getenv("OPENAI_API_KEY")

📚 File Structure

/agentic-ai-pdf-summarizer
│-- /src
│   │-- autoresearcher.py
│-- /tests
│-- README.md
│-- .gitignore
│-- requirements.txt

🤖 How It Works

Text Extraction: Reads text from the given PDF.

Summarization: Generates an initial summary using OpenAI's GPT models.

Autonomous Iterations: Refines the summary over a set number of loops.

Validation: Checks the final summary for clarity and accuracy.

🛠️ To-Do



📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

🌟 Contributing

Contributions are welcome! If you have ideas for improvements or want to report a bug:

Fork the repo

Create a new branch (feature-xyz)

Commit your changes

Open a pull request

📬 Contact

GitHub: YourUsername

LinkedIn: Your Name

Feel free to reach out if you have any suggestions or feedback!
