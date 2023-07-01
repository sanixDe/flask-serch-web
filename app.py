from flask import Flask, request, render_template
from web_scraper import search_web, process_question, generate_answer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    topic = request.form['topic']
    question = request.form['question']

    # Search the web for information related to the topic
    search_results = search_web(topic)
    
    # Process the user's question
    processed_question = process_question(question)
    print("--------------------------------------------------------")
    print(processed_question, search_results)
    
    # Generate an answer based on the processed question and search results
    answer = generate_answer(processed_question, search_results)

    return render_template('result.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
