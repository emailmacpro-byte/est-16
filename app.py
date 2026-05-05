from flask import Flask, render_template, request, jsonify, session
import json
import os
from questions import SHORT_QUESTIONS, LONG_QUESTIONS
from careers import CAREERS_DB
from riasec_types import RIASEC_TYPES

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test/<test_type>')
def test(test_type):
    if test_type == 'short':
        questions = SHORT_QUESTIONS
        title = "Богино тест"
        subtitle = "30 асуулт · ~10 минут"
    elif test_type == 'long':
        questions = LONG_QUESTIONS
        title = "Дэлгэрэнгүй тест"
        subtitle = "60 асуулт · ~20 минут"
    else:
        return render_template('index.html')
    return render_template('test.html', questions=json.dumps(questions), 
                           title=title, subtitle=subtitle, test_type=test_type)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    answers = data.get('answers', {})
    questions_data = data.get('questions', [])
    
    scores = {'R': 0, 'I': 0, 'A': 0, 'S': 0, 'E': 0, 'C': 0}
    
    for q in questions_data:
        q_id = str(q['id'])
        if q_id in answers:
            riasec_type = q['type']
            score_value = int(answers[q_id])
            scores[riasec_type] += score_value
    
    # Normalize scores to percentage
    max_possible = {}
    for t in 'RIASEC':
        count = sum(1 for q in questions_data if q['type'] == t)
        max_possible[t] = count * 5
    
    percentages = {}
    for t in 'RIASEC':
        if max_possible[t] > 0:
            percentages[t] = round((scores[t] / max_possible[t]) * 100)
        else:
            percentages[t] = 0
    
    # Get top 3 types
    sorted_types = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top3 = [t[0] for t in sorted_types[:3]]
    holland_code = ''.join(top3)
    
    # Find matching careers
    matched_careers = []
    for career in CAREERS_DB:
        career_code = career['code']
        match_score = 0
        for i, t in enumerate(top3):
            if t in career_code:
                match_score += (3 - i) * 2
                if career_code[0] == t:
                    match_score += 3
        if match_score > 0:
            career['match_score'] = match_score
            matched_careers.append(career)
    
    matched_careers.sort(key=lambda x: x['match_score'], reverse=True)
    top_careers = matched_careers[:12]
    
    # Get descriptions for top types
    type_descriptions = {t: RIASEC_TYPES[t] for t in top3}
    
    return jsonify({
        'scores': scores,
        'percentages': percentages,
        'holland_code': holland_code,
        'top3': top3,
        'careers': top_careers,
        'type_descriptions': type_descriptions,
        'all_types': RIASEC_TYPES
    })

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
