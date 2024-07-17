from flask import Flask, render_template, request, session, redirect
from database import create_akun, validasi, validasi_admin, input_data_krs, data_krs, isi_krs, data_siswa
from database import update_nilai

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/create", methods=['POST'])
def create():
    create_akun()
    return redirect('/')


@app.route("/validation", methods=['POST'])
def validation():
    email = request.form['username']
    if validasi():
        session['username'] = email
        return redirect('/home')
    elif validasi_admin():
        session['username'] = email
        return redirect('/admin')
    else:
        return redirect('/')


@app.route("/home")
def home():
    if 'username' in session:
        return render_template("base.html")


@app.route("/home/isi_krs")
def krs():
    krs = data_krs()
    return render_template("nilai.html", users=krs)


@app.route("/isi_krs", methods=['POST'])
def pilih_krs():
    username = session.get('username')
    isi_krs(username)
    return redirect("/home/isi_krs")


@app.route("/home/lihat_nilai")
def lihat_nilai():
    nilai = data_siswa(session.get('username'))
    return render_template("nilai_siswa.html", users=nilai)


@app.route("/admin")
def admin():
    if 'username' in session:
        return render_template("admin.html")


@app.route("/admin/buat_krs")
def buat_krs():
    return render_template("buat_krs.html")


@app.route("/buat_krs", methods=['POST'])
def input_krs():
    input_data_krs()
    return redirect("/admin/buat_krs")


@app.route("/admin/nilai")
def nilai():
    krs = data_krs()
    return render_template("krs.html", users=krs)


@app.route("/isi_nilai", methods=['POST'])
def isi_nilai():
    update_nilai()
    return redirect("/admin/nilai")


@app.route("/create_account")
def create_account():
    return render_template("create_account.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/logout')
def logout():
    # Clear session data to log the user out
    session.pop('username', None)
    return redirect('/')


@app.route('/tes')
def tes():
    return render_template('TesPostingKKN.html')


if __name__ == '__main__':
    # run the app
    app.run(debug=True)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
