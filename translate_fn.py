from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
from opencc import OpenCC
import torch

import naturalize_en
import mappingword

# =========================
# 1. 모델 로드 (1회)
# =========================
model_name = "facebook/m2m100_418M"

tokenizer = M2M100Tokenizer.from_pretrained(model_name)
model = M2M100ForConditionalGeneration.from_pretrained(model_name)

# OpenCC (간체 → 번체)
cc = OpenCC('s2t')

torch.set_num_threads(8)

# =========================
# 2. 자연화 규칙 (영어)
# =========================


# =========================
# 자주 쓰는 단어나 문장은 캐싱
# =========================
# cache = {
#     'order' : 'Are you ready to order?',
#     'calculate' : "I'll get the bill for you",
# }

# def translate_cached(text):
#     if text in cache:
#         return cache[text]

#     result = translate(text)
#     cache[text] = result
#     return result



# =========================
# 3. 번역 함수
# =========================
def translate(text, target="en", use_traditional=False):
    tokenizer.src_lang = "ko"

    inputs = tokenizer(text, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            forced_bos_token_id=tokenizer.get_lang_id(target),
            max_length=40,
            num_beams=1,
            do_sample = False
        )

    result = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # =========================
    # 4. 후처리
    # =========================

    # 영어 자연화
    if target == "en":
        nor_res = mappingword.smarter_template(result)
        result = naturalize_en.naturalize_en(nor_res)

    # 중국어 번체 변환
    if target == "zh" and use_traditional:
        result = cc.convert(result)

    return result


# =========================
# 5. 테스트
# =========================
if __name__ == "__main__":
    print("영어:", translate('더 필요한 거 있으신가요?'))
    print("중국어(간체):", translate("더 필요한 거 있으신가요?", "zh"))
    print("중국어(번체):", translate("더 필요한 거 있으신가요?", "zh", use_traditional=True))
