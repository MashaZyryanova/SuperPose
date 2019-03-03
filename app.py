from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('page1.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # result1 = match(img_ideal_pose, img1)
    # result2 = match(img_ideal_pose, img2)
    # best_score = max(result1, result2)
    winner = 0          # default value
    # if best_score == result1:
    #     winner = 1
    # else
    #     winner = 2
    return render_template('page2.html', winner=1)