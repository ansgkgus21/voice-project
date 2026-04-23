# pip install sectencepiece
# pip install protobuf  필요

from transformers import M2M100ForConditionalGeneration, AutoTokenizer

model_name = "facebook/m2m100_418M"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = M2M100ForConditionalGeneration.from_pretrained(model_name)


def translate(text) :
 
    # text = "주문하시겠어요?"
    # chinese_text = "生活就像一盒巧克力。"

    # translate korean to English
    tokenizer.src_lang = "ko"
    encoded_hi = tokenizer(text, return_tensors="pt")
    generated_tokens = model.generate(**encoded_hi, forced_bos_token_id=tokenizer.get_lang_id("en"))
    return tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

    # 약 20초 걸림

    # # translate Chinese to English
    # tokenizer.src_lang = "zh"
    # encoded_zh = tokenizer(chinese_text, return_tensors="pt")
    # generated_tokens = model.generate(**encoded_zh, forced_bos_token_id=tokenizer.get_lang_id("ko"),do_sample=False)
    # print(tokenizer.batch_decode(generated_tokens, skip_special_tokens=True))


print(translate('주문 도와드리겠습니다'))