import anthropic  # giao tiep vs AI
client = anthropic.Anthropic(api_key="ANTHROPIC_API_KEY")
message = client.messages.create(  # mesage tin nhan gui den AI
    model="claude-haiku-4-5-20251001", 
    max_tokens=100, # 
    messages=[{
        "role":"user",
        "content":"Xin chào!"
    }]
)
print(message.content[0].text)

# Dùng AI sinh testcase tự động:
api_doc="""
post / register
body:{
    "username": "string",
    "password":"string",
    "email": "string"
    }
"""
message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1000,
    messages=[{
        "role":"user",
        "content": f"Hãy sinh ra 10 testcase cho API này:\n{api_doc}"
    }]
)
print(message.content[0].text)