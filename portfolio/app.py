from flask import Flask, request, redirect, url_for, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'suhangowda92@gmail.com'  # Your Gmail
app.config['MAIL_PASSWORD'] = 'whsq oeme ovqn bpmk'  # App password (not regular password)
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def index():
    return render_template('contact.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message_content = request.form.get('message')
        
        if not name or not email or not message_content:
            return "All fields are required", 400
        
        # Create the message
        msg = Message(
            subject=f"New Message from {name}",
            sender=app.config['MAIL_USERNAME'], 
            recipients=['suhangowda92@gmail.com'],  
            body=f"Message from {name} ({email}):\n\n{message_content}"
        )
        
        # Send the email
        try:
            mail.send(msg)
            return "Message sent successfully!"
        except Exception as e:
            return f"An error occurred while sending the message: {str(e)}", 500
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
