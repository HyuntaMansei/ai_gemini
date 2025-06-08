'''
구글의 Gemini API를 사용하여 텍스트 생성 및 요약을 수행하는 모듈입니다.
이 모듈은 my_perplexity 모듈의 일부로, Perplexity에서 생성한 응답을
Gemini API에게 전달하여 정리된 답변을 생성합니다.
'''
import google.generativeai as genai

from config_reader import ConfigReader

config = ConfigReader()
gemini_api_key = config.get_value('GEMINI_API_KEY')
model_name = config.get_value('GEMINI_MODEL_NAME')  # 기본 모델 이름 설정

print("Gemini API 키:", gemini_api_key)  # 디버깅용 출력

genai.configure(
    api_key=gemini_api_key,
    # api_base=os.getenv("GEMINI_API_BASE", "https://generativeai.googleapis.com")
)
# 기본 모델 설정
model = genai.GenerativeModel(model_name=model_name)

question = "오늘 서울 날씨 어때?"
response = model.generate_content(question,
)
print(response.text)