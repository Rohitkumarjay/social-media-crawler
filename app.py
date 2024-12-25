from flask import Flask, render_template, request
from backend.crawler import get_social_media_posts

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_posts', methods=['POST'])
def get_posts():
    social_media = request.form.get('social_media', '').strip().lower()
    username = request.form.get('username', '').strip()

    if not social_media or not username:
        return render_template('index.html', error="Please provide both social media type and username.")

    try:
        posts, total_posts = get_social_media_posts(social_media, username)
    except Exception as e:
        return render_template('index.html', error=f"An error occurred: {str(e)}")

    return render_template('index.html', posts=posts, total_posts=total_posts)

if __name__ == '__main__':
    app.run(debug=True)