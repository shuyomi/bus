from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/placereservation')
def placereservation():
    return render_template('placereservation.html')

@app.route('/reservation')
def reservation():
    return render_template('reservation.html')

@app.route('/seat_selection')
def seat_selection():
    return render_template('seat_selection.html')

@app.route('/check_cancel')
def check_cancel():
    return render_template('check_cancel.html')

@app.route('/support')
def support():
    return render_template('support.html')

# 새로 추가된 운행정보 페이지 라우트
@app.route('/operation_info')
def operation_info():
    return render_template('operation_info.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
