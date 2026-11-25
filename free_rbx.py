from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Player Login</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                background: #191b20;
                color: white;
                font-family: Arial;
                text-align: center;
                padding: 40px 15px;
            }

            .box {
                background: #272930;
                padding: 30px;
                border-radius: 12px;
                max-width: 330px;
                margin: auto;
            }

            input, button {
                box-sizing: border-box;
                width: 100%;
                padding: 13px;
                margin: 10px 0;
                border-radius: 6px;
                border: none;
            }

            button {
                background: #00a2ff;
                color: white;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <div class="box" id="login">
            <h1>LOGIN</h1>

            <input placeholder="Username" autocomplete="off">

            <input placeholder="Password"
                   type="password"
                   autocomplete="off">

            <button onclick="finish()">Continue</button>
        </div>

        <script>
            function finish() {
                document.body.innerHTML = `
                    <div style="padding:60px 15px">
                        <h1>NOOB 😂</h1>
                        <h2>Never share your password!</h2>
                    </div>
                `;
            }
        </script>
    </body>
    </html>
    """)

app.run(host="127.0.0.1", port=5000)
if __name__ == "__main__":
    app.run()
