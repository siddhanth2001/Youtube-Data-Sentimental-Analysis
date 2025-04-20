from flask import Flask, render_template, request, redirect, url_for, flash
from youtube import get_video_comments
from sentiment_analysis import analyze_sentiment

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    video_id = request.form['video_id']
    try:
        video_details, comments = get_video_comments(video_id, max_results=10)  # Fetch video details and up to 10 comments
        sentiment_results = analyze_sentiment(comments)
        return render_template('video.html', video_id=video_id, video_details=video_details, comments=comments, sentiments=sentiment_results)
    except Exception as e:
        print(f"Error: {e}")  # Print the error to the console for debugging
        flash(f"An error occurred: {str(e)}")  # Flash the error message to the home page
        return redirect(url_for('index'))  # Redirect back to the home page

if __name__ == '__main__':
    app.run(debug=True)
