from flask import Flask, render_template, flash
from wtforms import StringField, SelectField, SubmitField, validators
from flask_wtf import FlaskForm, CSRFProtect
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
from bot import XBot
import os

load_dotenv()

app = Flask(__name__)
bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = os.getenv('FLASK_KEY')

HOUR_CHOICES = [(1, '00:00'), (2, '01:00'), (3, '02:00'), (4, '03:00'), (5, '04:00'), (6, '05:00'), (7, '06:00'),
                (8, '07:00'), (9, '08:00'), (10, '09:00'), (11, '10:00'), (12, '11:00'), (13, '12:00'), (14, '13:00'),
                (15, '14:00'), (16, '15:00'), (17, '16:00'), (18, '17:00'), (19, '18:00'), (20, '19:00'), (21, '20:00'),
                (22, '21:00'), (23, '22:00'), (24, '23:00')]

OPTIONS = [(1, "Every 3 hours"), (2, "Every 6 hours"), (3, "Every 12 hours"), (4, "Every day"), (5, "Every 2 days"),
           (6, "Every 3 days"), (7, "Every Monday"), (8, "Every Tuesday"), (9, "Every Wednesday"),
           (10, "Every Thursday"), (11, "Every Friday"), (12, "Every Saturday"),(13, "Every Sunday")]


# AI content manager form:
class AIContentForm(FlaskForm):
    business_name = StringField('Your Business name',
                                [validators.Length(min=8, max=256), validators.InputRequired()],
                                render_kw={"placeholder": "e.g. Jimmy's Cupcakes"})
    business_theme = StringField('Your Business Theme',
                                 [validators.Length(min=8, max=256), validators.InputRequired()],
                                 render_kw={"placeholder": "e.g. We create the tastiest cupcakes"})
    post_frequency = SelectField('How often would you like to post?', [validators.InputRequired()],
                                 choices=OPTIONS)
    post_hour = SelectField('When would you like to post?', [validators.InputRequired()],
                            choices=HOUR_CHOICES)
    submit = SubmitField('Start Automation')


@app.route('/')
def home():
    return render_template('Index.html', title='home page')


@app.route('/ai_content_manager', methods=["POST", "GET"])
def ai_content_manager():
    form = AIContentForm()
    if form.validate_on_submit():
        business = {"name": form.business_theme.data, "theme": form.business_name.data}
        XBot(business)
        flash("Automation save successfully!")
        return render_template('generic.html', form=form)
    return render_template('generic.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
