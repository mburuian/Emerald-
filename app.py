from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/scheduleconsultation')
def schedule_consultation():  # Changed function name here
    return render_template('scheduleconsultation.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Logic to store or send the message (e.g., save to database or send email)
        return redirect('/')
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
