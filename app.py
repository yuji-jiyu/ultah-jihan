from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = "ultahjihanrahasia"  # bebas, tapi jangan kasih tau orang
app.config["SESSION_TYPE"] = "filesystem"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "pesan_jihan.txt")

PASSWORD = "sayang"  # 🔑 GANTI dengan password yang kamu mau

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



@app.route("/page4", methods=["GET", "POST"])
def page4():
    if not session.get("login"):
        return redirect(url_for("login"))

    if request.method == "POST":
        pesan = request.form.get("pesan")
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(pesan + "\n\n")

        return redirect(url_for("penutup"))


    return render_template("page4.html")

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

