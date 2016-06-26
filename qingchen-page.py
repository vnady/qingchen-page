from flask import Flask, url_for, request, render_template

app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/user/<username>')
def show_user_profile(username):
    #show user profile for that user
    return render_template('style.html', name=username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    #show the post with the give id
    return 'Post %d' % post_id

@app.route('/about')
def about():
    #return the about infomation
    return 'The about page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #do_the_login()
        pass
    else:
        #show_the_login_form()
        pass

if __name__ == '__main__':
    app.run(debug=True)
