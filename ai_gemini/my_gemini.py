'''
구글의 Gemini API를 사용하여 텍스트 생성 및 요약을 수행하는 모듈입니다.
이 모듈은 my_perplexity 모듈의 일부로, Perplexity에서 생성한 응답을
Gemini API에게 전달하여 정리된 답변을 생성합니다.
'''
import google.generativeai as genai
from config_reader import ConfigReader

class _Mygemini:
    def __init__(self, api_key=None, model_name=None):
        self.api_key = api_key
        self.model_name = model_name
        if not self.api_key:
            raise ValueError("API key is required for Gemini API.")
        genai.configure(api_key=self.api_key)
        
        
class MyGemini(_Mygemini):
    def __init__(self, api_key=None, model_name=None):
        super().__init__(api_key=api_key, model_name=model_name)
        
        self.model = genai.GenerativeModel(model_name=self.model_name)

    def generate_content(self, question):
        response = self.generate_content_as_response(question)
        if not response or not hasattr(response, 'text'):
            raise ValueError("Invalid response from Gemini API.")
        return response.text
    
    def generate_content_as_response(self, question):
        response = self.model.generate_content(question)
        return response

def make_default_gemini():
    config = ConfigReader()
    gemini_api_key = config.get_value('GEMINI_API_KEY')
    model_name = config.get_value('GEMINI_MODEL_NAME')  # 기본 모델 이름 설정
    return MyGemini(api_key=gemini_api_key, model_name=model_name)

def test():
    gemini = make_default_gemini()
    question = "너는 제미나이 버전이 뭐야? 즉, 모델명 알려줘."
    response = gemini.generate_content(question)
    print(f"Question: {question}")
    print(f"Response: {response}")
    print(f"Model Name: {gemini.model_name}")
    
if __name__ == "__main__":
    test()
    print("Finished testing MyGemini module.")