from transformers import MBartForConditionalGeneration, AutoTokenizer


# 모델 및 토크나이저 불러오기 (many-to-many 모델 예시)
model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
tokenizer = AutoTokenizer.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

# 번역할 문장 설정 (예: 한국어 -> 영어)
text = "버스정류장은 어디에 있나요?" 
tokenizer.src_lang = "ko_KR"
encoded_input = tokenizer(text, return_tensors="pt", padding = True)

# 번역 생성
generated_tokens = model.generate(
    **encoded_input,
    forced_bos_token_id=tokenizer.lang_code_to_id["en_XX"],
    # num_beams=2
)

# 결과 디코딩
print(tokenizer.batch_decode(generated_tokens, skip_special_tokens=True))


  