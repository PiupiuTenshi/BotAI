
# 🎤 Mahiru Voice Assistant

**Mahiru** is a personalized AI voice assistant designed for **Windows**.  
It combines **offline wake-word detection (Picovoice Porcupine)**, **local LLM intelligence (Ollama)**, and **system automation** to help you control your PC and answer queries **hands-free**.

---

## 🇬🇧 English Version

### ✨ Features

- **Hybrid AI**  
  Uses **Ollama (Gemma 2)** for smart conversational responses and Python logic for system control.

- **Wake Word Detection**  
  Always listening for a wake word (default: `google` or custom `Mahiru`) using **Picovoice Porcupine**.

- **Bilingual Support**  
  Automatically detects and speaks in **English or Vietnamese** based on your command.

- **Visual Feedback**  
  Displays an animated **GIF overlay (bottom-right corner)** when the assistant is active.

- **System Commands**
  - Open websites (YouTube, LeetCode, Gmail, Gemini)
  - Open installed applications (e.g. *"Open Excel"*, *"Open Discord"*)
  - Tell the current time
  - Shutdown / Exit the assistant

---

### 🧩 Prerequisites

1. **Python 3.8+**
2. **Ollama installed and running**
   ```bash
   ollama pull gemma2:2b
    ````

3. **Picovoice Account**
   Get a free **Access Key** from the Picovoice Console.

---

### 📦 Installation

1. Clone or download this repository

2. Install required Python libraries:

   ```bash
   pip install pvporcupine pvrecorder speechrecognition pyttsx3 ollama winsound AppOpener langdetect pillow
   ```

   > `winsound` is built-in on Windows
   > `AppOpener` may take a few seconds on first run to scan installed apps

3. Setup the GIF:

   * Place a GIF named **`mahiru_siri.gif`** in the same folder as the script
   * Tip: Use a **black background GIF** for better transparency

---

### ⚙️ Configuration

1. Open `assistant_ver3_update.pyw`

2. **Picovoice API Key**

   ```python
   ACCESS_KEY = "your_picovoice_key_here"
   ```

3. **Wake Word (Important)**

   * Default wake word: `google`

   * To use **"Mahiru"**, generate a `.ppn` file from Picovoice Console

   * If you get **"Not in vocabulary"**:

     * Try phonetic spelling when creating the model:

       * `Ma hee roo`
       * `Ma he rue`

   * Download the file (e.g. `Mahiru_windows.ppn`)

   * Place it in the project folder

   * Update the code:

     ```python
     porcupine = pvporcupine.create(
         access_key=ACCESS_KEY,
         keyword_paths=["Mahiru_windows.ppn"]
     )
     ```

---

### ▶️ Usage

#### I. Run the assistant

```bash
python assistant_ver3_update.pyw
```

* Wait for: **"System started"**
* Say the wake word: **"Google"** or **"Mahiru"**
* GIF appears
* Speak a command:

  * *"Mở Youtube"*
  * *"What time is it?"*

---

### 🧱 Build into EXE (Executable)

#### 1. Install PyInstaller

```bash
pip install pyinstaller
```

#### 2. Build EXE

```bash
pyinstaller --noconsole --onefile \
--add-data "mahiru_siri.gif;." \
--add-data "Mahiru_windows.ppn;." \
assistant_ver3_update.pyw
```

#### 3. Run

* Open the `dist` folder
* Run `assistant_ver3_update.exe`
* The assistant starts silently
  (listen for **"System Started"**)

---

## 🇻🇳 Phiên bản Tiếng Việt

### ✨ Tính năng

* **AI lai (Hybrid)**
  Kết hợp **Ollama (Gemma 2)** để trò chuyện thông minh và Python để điều khiển hệ thống

* **Đánh thức bằng giọng nói**
  Luôn lắng nghe từ khóa (`google` hoặc `Mahiru`) bằng **Picovoice Porcupine**

* **Hỗ trợ song ngữ**
  Tự động nhận diện và trả lời **Tiếng Anh / Tiếng Việt**

* **Giao diện bong bóng GIF**
  Hiển thị ảnh GIF động ở góc phải màn hình khi bot đang nghe

* **Lệnh hệ thống**

  * Mở website (YouTube, Gmail, LeetCode, Gemini)
  * Mở ứng dụng (Zalo, Word, Excel, Discord…)
  * Hỏi giờ
  * Tắt trợ lý

---

### 🧩 Yêu cầu hệ thống

1. Python 3.8+
2. Ollama đang chạy

   ```bash
   ollama pull gemma2:2b
   ```
3. Tài khoản Picovoice (Access Key miễn phí)

---

### 📦 Cài đặt

```bash
pip install pvporcupine pvrecorder speechrecognition pyttsx3 ollama AppOpener langdetect pillow
```

> AppOpener sẽ quét ứng dụng trong lần chạy đầu tiên

---

### ⚙️ Cấu hình

```python
ACCESS_KEY = "dán_key_của_bạn_vào_đây"
```

**Wake Word Mahiru**

* Tạo file `.ppn` trên Picovoice Console
* Nếu lỗi từ vựng: nhập phiên âm
  👉 `Ma hee roo`
* Sửa code:

```python
porcupine = pvporcupine.create(
    access_key=ACCESS_KEY,
    keyword_paths=["Mahiru_windows.ppn"]
)
```

---

### ▶️ Cách sử dụng

```bash
python assistant_ver3_update.pyw
```

* Bot nói: **"System Started"**
* Gọi wake word
* GIF xuất hiện
* Ra lệnh:

  * `"Mở Youtube"`
  * `"Mấy giờ rồi"`
  * `"Open Calculator"`

---

### 🧱 Đóng gói EXE

```bash
pyinstaller --noconsole --onefile \
--add-data "mahiru_siri.gif;." \
--add-data "Mahiru_windows.ppn;." \
assistant_ver3_update.pyw
```

➡️ File `.exe` nằm trong thư mục `dist`
➡️ Chạy được trên máy khác **(có Ollama)**

