from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# 첫 화면: index 페이지 라우트
@app.route('/')
def index():
    return render_template('index.html')  # templates/index.html 파일을 렌더링

# 예약 페이지 라우트
@app.route('/reservation')
def reservation():
    return render_template('reservation.html')  # templates/reservation.html 파일을 렌더링

# 좌석 선택 페이지 라우트
@app.route('/seat_selection')
def seat_selection():
    return render_template('seat_selection.html')  # templates/seat_selection.html 파일을 렌더링

# 예약 페이지 라우트
@app.route('/check_cancel')
def check_cancel():
    return render_template('check_cancel.html')  # templates/reservation.html 파일을 렌더링

# 예약 페이지 라우트
@app.route('/support')
def support():
    return render_template('support.html')  # templates/reservation.html 파일을 렌더링


# 애플리케이션 실행
if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)


