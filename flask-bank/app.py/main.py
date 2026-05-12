from flask import Flask

app = Flask(__name__)

balance = 1000


@app.route("/")
def home():
    return f"""
    <h1>🏦 My Bank</h1>
    <h2>Balance: R{balance}</h2>

    <a href="/deposit"><button>Deposit R100</button></a>
    <a href="/withdraw"><button>Withdraw R100</button></a>
    """


@app.route("/deposit")
def deposit():
    global balance
    balance += 100
    return f"Deposited! New balance: R{balance} <br><a href='/'>Back</a>"


@app.route("/withdraw")
def withdraw():
    global balance

    if balance < 100:
        return f"Not enough money. Balance: R{balance} <br><a href='/'>Back</a>"

    balance -= 100
    return f"Withdraw successful! New balance: R{balance} <br><a href='/'>Back</a>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)