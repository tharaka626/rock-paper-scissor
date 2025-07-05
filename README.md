# 🪨 📄 ✂️ Rock Paper Scissors – Python CLI Game

A simple yet fun command-line Rock-Paper-Scissors game built with Python.  
This game supports personalized gameplay, multiple rounds, and tracks wins per session.

---

## 🚀 How to Run

You can run this project in **two ways**:

---

1. **Clone the repository**:

   ```bash
       git clone https://github.com/tharaka626/rock-paper-scissor.git
       cd rock-paper-scissor
   ```

2. **Run the script**:

   ```bash
       python app.py
   ```

   Or, run with your name as a parameter:

   ```bash
       python app.py -n "Your Name"
   ```

   The `-n` or `--name` flag lets you personalize your game experience.

---

## 🧪 How to Test

To test the game, run the following command:

```bash
pytest
```

Make sure `pytest` is installed:

```bash
pip install pytest
```

---

## 🛠️ Tech Stack

- **Python 3**
- `argparse` – For command-line argument parsing
- `random` – To generate computer choices
- `enum` – For move representation (ROCK, PAPER, SCISSORS)
- `pytest` – For unit testing

---

## 📁 Project Structure

```
rock-paper-scissor/
├── app.py           # Main CLI game script
├── tests/
│   └── test_app.py  # Unit test for the game
└── README.md        # Project documentation
```

---

## 📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute it.

---

## 🙌 Contributions

Contributions are welcome! Feel free to:

- Fork the repository
- Submit a pull request
- Report issues

---

✅ Everything is formatted properly in one continuous file without broken spacing or indentation.

Let me know your GitHub username if you'd like me to update the clone URL!
