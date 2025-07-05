from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Gemini API setup
API_KEY = "AIzaSyCQ4L1M-VfZw3m9itS-XoVieLXLksrXbuI"  # Replace with your Gemini API key
API_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

@app.route('/', methods=['GET', 'POST'])
def index():
    story = ""
    error = ""
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        if prompt:
            try:
                # Enhanced prompt for story generation
                enhanced_prompt = (
                    f"Write a short story (200-300 words) with a clear beginning, middle, and end based on the following prompt: {prompt}. "
                    f"Ensure the story is engaging, creative, and does not repeat the prompt."
                )
                headers = {"Content-Type": "application/json"}
                data = {
                    "contents": [{"parts": [{"text": enhanced_prompt}]}],
                    "generationConfig": {
                        "maxOutputTokens": 500,
                        "temperature": 0.7,
                        "topK": 50,
                        "topP": 0.9
                    }
                }
                response = requests.post(f"{API_ENDPOINT}?key={API_KEY}", json=data, headers=headers)
                response.raise_for_status()
                generated_text = response.json().get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
                
                # Clean up the output to remove prompt or instructions
                story_start = generated_text.find('. ') + 2 if '. ' in generated_text else 0
                story = generated_text[story_start:].strip()
                if not story or len(story.split()) < 50:  # Ensure story is substantial
                    story = generated_text.strip()
            except requests.exceptions.HTTPError as e:
                error = f"Gemini API error: {str(e)}"
            except Exception as e:
                error = f"Error generating story: {str(e)}"
        else:
            error = "Please enter a prompt."
    return render_template('index.html', story=story, error=error)

if __name__ == '__main__':
    app.run(debug=True)