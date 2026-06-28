import anthropic
import subprocess
import os

client = anthropic.Anthropic(api_key="ANTHROPIC_API_KEY")

def chay_pytest_va_lay_log(file_test):
    ket_qua = subprocess.run(
        ["python", "-m", "pytest", file_test, "-v", "--tb=short"],
        capture_output=True,
        text=True
    )
    return ket_qua.stdout + ket_qua.stderr

def ai_phan_tich_bug(log):
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1000,
        messages=[{
            "role": "user",
            "content": f"""Đây là log test bị lỗi:
{log}
Hãy:
1. Giải thích lỗi là gì
2. Nguyên nhân tại sao
3. Cách fix
Trả lời bằng tiếng Việt, ngắn gọn!"""
        }]
    )
    return message.content[0].text

def test_ai_phan_tich():
    log = chay_pytest_va_lay_log(
        r"c:/Users/sonku/OneDrive/Máy tính/Python/test_co_loi.py"
    )
    print("\n---LOG TEST---")
    print(log)
    phan_tich = ai_phan_tich_bug(log)
    print("\n---AI PHAN TICH---")
    print(phan_tich)
    assert phan_tich is not None
    print("\nPASS - AI phân tích thành công!")

if __name__ == "__main__":
    test_ai_phan_tich()