from flask import Flask, render_template
import markdown
import os

app = Flask(__name__)

@app.route('/')
def index():
    posts = []
    for filename in os.listdir('content'):
        if filename.endswith('.md'):
            with open(os.path.join('content', filename), 'r') as f:
                content = f.read()
                md = markdown.Markdown(extensions=['meta'])
                html = md.convert(content)
                posts.append({
                    'title': md.Meta.get('title', ['Untitled'])[0],
                    'date': md.Meta.get('date', ['Unknown'])[0],
                    'slug': filename[:-3],
                    'content': html
                })
    posts.sort(key=lambda x: x['date'], reverse=True)
    return render_template('index.html', posts=posts)

@app.route('/post/<slug>')
def post(slug):
    with open(os.path.join('content', f'{slug}.md'), 'r') as f:
        content = f.read()
        md = markdown.Markdown(extensions=['meta'])
        html = md.convert(content)
        post = {
            'title': md.Meta.get('title', ['Untitled'])[0],
            'date': md.Meta.get('date', ['Unknown'])[0],
            'content': html
        }
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
