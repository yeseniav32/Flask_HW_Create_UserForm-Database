from flask import Blueprint, render_template


site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/sell_trade')
def sell_trade():
    return render_template('sell_trade.html')