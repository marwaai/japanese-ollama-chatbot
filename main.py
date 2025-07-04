import requests
import json
import threading
import keyboard  # To capture key presses
import pykakasi

# Global variables
history = []
stop_stream = False
response = None

# 🧵 Monitor pressing "p" to stop the response
def monitor_input():
    global stop_stream, response
    print("\n⏹️ Press [P] to stop the response at any time.")
    while True:
        if keyboard.is_pressed("p"):
            stop_stream = True
            if response:
                try:
                    response.close()
                except:
                    pass
            break

# 🧠 Build prompt
def build_prompt(history, user_input):
    prompt = "/no_thinkあなたの名前はクロです。あなたはとてもカジュアルな友達で、質問に直接的かつ簡潔に答えます。\n\n"
    prompt += "以下は、ユーザーとの会話の履歴です。丁寧かつ親切にご返答ください。わからない場合は「わかりません」とお伝えください。\n\n"
    for pair in history:
        prompt += f"ユーザー：{pair['user']}\nAI：{pair['ai']}\n"
    prompt += f"ユーザー：{user_input}\nAI："
    return prompt

# 📤 Send the request to the model
def ask_model(prompt, model_name="qwen3:1.7b"):
    global stop_stream, response
    stop_stream = False
    final = ""
    
    input_thread = threading.Thread(target=monitor_input, daemon=True)
    input_thread.start()

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model_name,
                "prompt": prompt,
                "stream": True,
                "max_tokens": 500,
                "seed": 42,
                "think":False
                
            },

            stream=True,

        )

        for line in response.iter_lines():
            if stop_stream:
                break
            if line:
                try:
                    data = json.loads(line.decode("utf-8"))
                    if "response" in data:
                        print(data["response"], end="", flush=True)
                        final += data["response"]
                    elif "error" in data:
                        print(f"\n❌ Model Error: {data['error']}")
                        break
                except json.JSONDecodeError:
                    print("\n⚠️ Error decoding response.")
                    break
    except requests.exceptions.RequestException as e:
        print(f"\n🚫 Connection error: {e}")
    finally:
        print()
        return final.strip()

# 🧭 Main menu
def main():
    while True:
        options = ["kanji to hiragana", "normal chat"]
        print("\nPlease choose a number:")
        for idx, item in enumerate(options, 1):
            print(f"{idx}. {item}")
        print("3. Exit")

        try:
            choice = int(input("\nYour choice: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        if choice == 2:
            user_input = input("👤: ")
            if user_input.lower() == "exit":
                break
            full_prompt = build_prompt(history, user_input)
            ai_response = ask_model(full_prompt)
            history.append({"user": user_input, "ai": ai_response})

        elif choice == 1:
            kks = pykakasi.kakasi()
            text = input("🈶 Enter kanji or katakana to convert to hiragana: ")
            result = kks.convert(text)
            for item in result:
                print(f"{item['orig']} → {item['hira']}")

        elif choice == 3:
            print("👋 Goodbye")
            break
        else:
            print("❌ Invalid option.")

# 🚀 Run the program
if __name__ == "__main__":
    main()
