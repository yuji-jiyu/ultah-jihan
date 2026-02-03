from flask import Flask, render_template, request, redirect, url_for, session
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "supersecretkey")  # bebas, tapi jangan kasih tau orang
app.config["SESSION_TYPE"] = "filesystem"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "pesan_jihan.txt")

PASSWORD = "sayang"  # 🔑 GANTI dengan password yang kamu mau

def kirim_email_ke_yusuf(pesan_dari_jihan):
    import os

    pengirim = os.environ.get("EMAIL_USER1")
    password = os.environ.get("EMAIL_PASS")
    penerima = os.environ.get("EMAIL_USER")
        

    subject = "Pesan Rahasia dari Jihan 🤍"

    isi_email = f"""
    Jihan baru saja menulis pesan untuk kamu...

    ----------------------------

    {pesan_dari_jihan}

    ----------------------------

    Jangan lupa senyum ya Yusuf :)
    """

    msg = MIMEMultipart()
    msg["From"] = pengirim
    msg["To"] = penerima
    msg["Subject"] = subject
    msg.attach(MIMEText(isi_email, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(pengirim, password)
    server.send_message(msg)
    server.quit()


# ================= LOGIN =================
@app.route("/", methods=["GET", "POST"])
def login():
    error = None

    if "tries" not in session:
        session["tries"] = 0

    if request.method == "POST":
        pw = request.form.get("password")

        if pw == PASSWORD:
            session["login"] = True
            session["tries"] = 0  # reset kalau berhasil
            return redirect(url_for("home"))
        else:
            session["tries"] += 1

            if session["tries"] == 1:
                error = "Hehe… salahh jihann..yusuff yakin jihan tau cuman jihan malu ajaa kann"
            elif session["tries"] == 2:
                error = "benerann lupaa yaa jihann.. padahal cuman kita yang tau cluenya 🥺"
            else:
                error = "beneran lupa yaa.. gpp laaa.. seriuss gpp 🥺"

    return render_template("login.html", error=error)




# ================= HALAMAN WEB =================
@app.route("/home")
def home():
    if not session.get("login"):
        return redirect(url_for("login"))
    return render_template("index.html")

@app.route("/page2")
def page2():
    if not session.get("login"):
        return redirect(url_for("login"))
    return render_template("page2.html")

@app.route("/page3")
def page3():
    if not session.get("login"):
        return redirect(url_for("login"))
    return render_template("page3.html")

@app.route("/gallery")
def gallery():
    if not session.get("login"):
        return redirect(url_for("login"))
    return render_template("gallery.html")


@app.route("/penutup")
def penutup():
    if not session.get("login"):
        return redirect(url_for("login"))
    return render_template("penutup.html")

@app.route("/rahasia")
def rahasia():
    if not session.get("login"):
        return redirect(url_for("login"))
    return render_template("rahasia.html")




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

