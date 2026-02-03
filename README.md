# BotAI
I create this bot like Siri by python

Mahiru Voice Assistant 
Mahiru is a personalized AI voice assistant designed for Windows. It combines offline wake-word detection (Porcupine), local LLM intelligence (Ollama), and system automation to help you control your PC and answer queries hands-free.
________________________________________
🇬🇧 English Version
✨ Features
•	Hybrid AI: Uses Ollama (Gemma 2) for smart, conversational responses and Python logic for system control.
•	Wake Word Detection: Always listening for the wake word (default: Google or custom Mahiru) using Picovoice Porcupine.
•	Bilingual Support: Automatically detects and speaks in English or Vietnamese based on your command.
•	Visual Feedback: Displays an animated GIF overlay (bottom right) when the assistant is active.
•	System Commands:
o	Open websites (YouTube, LeetCode, Gmail, Gemini).
o	Open any installed application (e.g., "Open Excel", "Open Discord").
o	Tell the current time.
o	Shutdown/Exit the assistant.
Prerequisites
1.	Python 3.8+ installed.
2.	Ollama installed and running.
o	Pull the model used in the code: ollama pull gemma2:2b
3.	Picovoice Account: You need a free Access Key from Picovoice Console.
Installation
1.	Clone or download this repository.
2.	Install the required Python libraries:
pip install pvporcupine pvrecorder speechrecognition pyttsx3 ollama winsound AppOpener langdetect pillow
(Note: winsound is built-in on Windows. If AppOpener fails on first run, it needs to scan your apps once).
3.	Setup the GIF:
o	Place a GIF file named mahiru_siri.gif in the same folder as the script.
o	Tip: Ensure the GIF has a black background for the transparency effect to work correctly.
⚙️ Configuration
1.	Open assistant_ver3_update.pyw.
2.	API Key: Paste your Picovoice Access Key into the ACCESS_KEY variable:
Python
ACCESS_KEY = "your_picovoice_key_here"
3.	Wake Word (Important):
o	The code currently uses the default keyword 'google'.
o	To use "Mahiru", you must generate a .ppn file from the Picovoice Console.
o	Fixing the "Not in vocabulary" error (from your image): If Picovoice rejects "Mahiru", try typing the phonetic sound: "Ma hee roo" or "Ma he rue" in the console when creating the model.
o	Download the file (e.g., Mahiru_windows.ppn), place it in the folder, and update the code:
Python
# Find the RunProgram function
porcupine = pvporcupine.create(access_key=ACCESS_KEY, keyword_paths=['Mahiru_windows.ppn'])
Usage
I. Run the script:
python assistant_ver3_update.pyw
•	Wait for the prompt: "System started".
•	Say the wake word: "Google" (or your custom word).
•	The GIF appears.
•	Say a command: e.g., "Mở Youtube" or "What time is it?".

II. How to Build into EXE (Executable)
1. Install PyInstaller:
pip install pyinstaller

2. Build the EXE:
Run the following command in your terminal. Crucial: You must use --add-data to include your GIF and PPN (Wake word) files inside the EXE.
pyinstaller --noconsole --onefile --add-data "mahiru_siri.gif;." --add-data "Mahiru_windows.ppn;." assistant_ver3_update.pyw

3. Run:
* Go to the dist folder created in your project directory.
* You will find assistant_ver3_update.exe.
* Double-click to run. The assistant will start silently (listen for "System Started" voice).


🇻🇳 Phiên bản Tiếng Việt
✨ Tính năng
•	AI Lai (Hybrid): Kết hợp Ollama (Gemma 2) để trò chuyện thông minh và Python để điều khiển hệ thống.
•	Đánh thức bằng giọng nói: Luôn lắng nghe từ khóa (mặc định: Google hoặc file riêng Mahiru) sử dụng Picovoice Porcupine.
•	Hỗ trợ song ngữ: Tự động phát hiện và trả lời bằng Tiếng Anh hoặc Tiếng Việt tùy thuộc vào câu lệnh của bạn.
•	Giao diện bong bóng: Hiển thị ảnh GIF động (góc phải màn hình) khi trợ lý đang nghe.
•	Lệnh hệ thống:
o	Mở trang web (YouTube, LeetCode, Gmail, Gemini).
o	Mở ứng dụng cài trên máy (ví dụ: "Mở Zalo", "Open Word").
o	Hỏi giờ.
o	Tắt trợ lý.
Yêu cầu hệ thống
1.	Python 3.8+ đã được cài đặt.
2.	Ollama đã cài đặt và đang chạy.
o	Tải model AI được dùng trong code: ollama pull gemma2:2b
3.	Tài khoản Picovoice: Lấy Access Key miễn phí tại Picovoice Console.
Cài đặt
1.	Tải bộ code về máy.
2.	Cài đặt các thư viện Python cần thiết:
Bash
pip install pvporcupine pvrecorder speechrecognition pyttsx3 ollama AppOpener langdetect pillow
(Lưu ý: AppOpener sẽ mất khoảng vài giây để quét ứng dụng trong lần chạy đầu tiên).
3.	Cài đặt ảnh GIF:
o	Chuẩn bị một file ảnh động tên là mahiru_siri.gif để cùng thư mục với code.
o	Mẹo: Ảnh GIF nên có nền màu đen để code tự động xóa phông nền (làm trong suốt).
⚙️ Cấu hình
1.	Mở file assistant_ver3_update.pyw.
2.	API Key: Dán Access Key của bạn vào dòng ACCESS_KEY:
Python
ACCESS_KEY = "dán_key_của_bạn_vào_đây"
3.	Từ khóa đánh thức (Wake Word):
o	Hiện tại code đang để mặc định là 'google'.
o	Để dùng tên "Mahiru": Bạn cần tải file .ppn từ Picovoice Console.
o	Khắc phục lỗi "Not in vocabulary" (như trong ảnh bạn gửi): Picovoice dùng từ điển tiếng Anh. Nếu nó không hiểu "Mahiru", hãy nhập phiên âm tiếng Anh của nó vào ô tạo model, ví dụ: "Ma hee roo".
o	Tải file về (ví dụ: Mahiru_windows.ppn), để chung thư mục code và sửa dòng này trong hàm RunProgram:
Python
# Sửa keywords=['google'] thành keyword_paths=['tên_file_của_bạn.ppn']
porcupine = pvporcupine.create(access_key=ACCESS_KEY, keyword_paths=['Mahiru_windows.ppn'])
Cách sử dụng
I. Chạy file script:
python assistant_ver3_update.pyw
•	Chờ thông báo: Bot nói "System started".
•	Gọi tên: Nói "Google" (hoặc từ khóa bạn đã cài).
•	GIF hiện lên: Bot bắt đầu nghe.
•	Ra lệnh: Ví dụ "Mở Youtube", "Mấy giờ rồi", hoặc "Open Calculator".

II. Cách đóng gói thành file EXE
1. Cài đặt PyInstaller:
pip install pyinstaller

2. Chạy lệnh đóng gói:
Mở Terminal tại thư mục chứa code và chạy lệnh sau (Chú ý thay tên file .ppn của bạn cho đúng):
pyinstaller --noconsole --onefile --add-data "mahiru_siri.gif;." --add-data "Mahiru_windows.ppn;." assistant_ver3_update.pyw

3. Sử dụng:
* Sau khi chạy xong, vào thư mục dist mới xuất hiện.
* Bạn sẽ thấy file assistant_ver3_update.exe.
* Nhấn đúp chuột để chạy. Bot sẽ khởi động ngầm (bạn sẽ nghe thấy tiếng "System Started").
* Bây giờ bạn có thể mang file .exe này đi máy khác (miễn là máy đó có cài Ollama) để dùng.








