from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 임시 데이터: 출발지와 도착지
locations = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "제주"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/placereservation', methods=['GET', 'POST'])
def placereservation():
    if request.method == 'POST':
        # 사용자가 입력한 출발지와 도착지를 받음
        departure = request.form['departure']
        destination = request.form['destination']
        
        # 출발지와 도착지를 세션이나 데이터베이스에 저장하거나 다음 페이지로 전달할 수 있음
        # 여기서는 간단하게 좌석 선택 페이지로 리다이렉트함
        return redirect(url_for('seat_selection'))

    # GET 요청일 경우, 사용자가 지역 선택 화면을 보도록 함
    return render_template('placereservation.html', locations=locations)

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

@app.route('/operation_info')
def operation_info():
    return render_template('operation_info.html')

@app.route('/check')
def check():
    return render_template('check.html')

@app.route('/cancel')
def cancel():
    return render_template('cancel.html')

# 결제 페이지 라우트 추가
@app.route('/payment')
def payment():
    return render_template('payment.html')



if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
