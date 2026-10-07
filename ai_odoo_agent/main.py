from log_reader import tail_logs
from ai_engine import analyze_error

def run():
    print("🚀 AI Odoo Agent Started...")

    for error in tail_logs():
        print("\n🚨 Error Detected:")
        print(error)

        result = analyze_error(error)
        print("\n🧠 AI Fix:")
        print(result)
        print("=" * 50)


if __name__ == "__main__":
    run()