import os
from flask import Flask, request

def create_app():   
    app = Flask(__name__)

    @app.route("/")
    def index():
        message = os.getenv("MESSAGE", "Hello from Flask on kubenetes")

        return f"""
        <h3>argocd</h3>
        <h1 style="color: red;">{message}</h1>
        """
    return app
app = create_app()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")), debug=True)

