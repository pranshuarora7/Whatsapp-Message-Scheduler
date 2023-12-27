# app.py
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField
from wtforms.validators import DataRequired
from tasks import send_whatsapp_message

app = Flask(__name__)
app.config.from_pyfile('config.py')

class MessageForm(FlaskForm):
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    message = StringField('Message', validators=[DataRequired()])
    scheduled_time = DateTimeField('Scheduled Time', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MessageForm()
    if form.validate_on_submit():
        send_whatsapp_message.apply_async(args=[form.phone_number.data, form.message.data],
                                          eta=form.scheduled_time.data)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
