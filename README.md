# unfriendr

### Automate Your Instagram Cleanup

**unfriendr** is a Python-based Instagram automation bot designed to help you unfollow accounts you no longer interact with. If your feed has become a cluttered mess from mindless following, this tool will help you curate it back to something meaningful.

> I built this as a fun way to learn web automation and also to solve a personal problem—keeping my Instagram feed relevant and engaging.

---

## 🚀 Features
- Automatically identifies accounts you follow but don’t engage with.
- Unfollows accounts in a safe, controlled manner (default: 25 per run, adjustable to 50 after a week).
- Allows exceptions for accounts you never want to unfollow.
- Uses Selenium and Firefox for web automation.

---

## 🛠 Setup & Usage

### 1️⃣ Download Your Instagram Data
You need an archive of your following/followers list from Instagram:
1. Visit the [Instagram Accounts Center](https://accountscenter.instagram.com/info_and_permissions/dyi/)
2. Request a download of your **following & followers data**
3. Once you receive the archive, extract the `.html` files to the `/data` directory in your cloned repo

### 2️⃣ Clone This Repository
```sh
git clone https://github.com/yourusername/unfriendr.git
cd unfriendr
```

### 3️⃣ Configure Your Settings
Edit `/config.py` to:
- Add your Instagram credentials (username & password)
- Define any exceptions (accounts you never want to unfollow)
- Adjust the unfollow limit if needed

### 4️⃣ Install Dependencies
Ensure you have [Python](https://www.python.org/) installed, then install the required packages:
```sh
pip install selenium
```
You also need [Firefox](https://www.mozilla.org/en-US/firefox/) installed.

### 5️⃣ Run the Bot
```sh
python unfriendr.py
```
- The **first run** will take longer as it builds a list of unfollowers.
- The script will start unfollowing accounts based on the configured settings.

---

## ⚠️ Important Notes
- To stay within Instagram’s automation guidelines, the **default unfollow limit is 25 per run**. After a week, you can increase it to 50.
- Use this tool responsibly. Overuse of automation may lead to action blocks.

---

## 🛠 Built With
- **Python** - The core programming language
- **Selenium** - For browser automation
- **Firefox** - Used as the browser for execution

---

## 📜 Disclaimer
This project is for educational purposes only. Use at your own risk.

---

Happy cleaning! ✨
