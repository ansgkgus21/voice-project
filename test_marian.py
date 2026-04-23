from transformers import AutoTokenizer, MarianMTModel, AutoModelForSeq2SeqLM

src = "ko"  # source language
trg = "en"  # target language

model_name = f"Helsinki-NLP/opus-mt-{src}-{trg}"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

tokenizer_zh = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-zh")
model_zh = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-zh")

def translate_MT(text) :
 
    batch = tokenizer([text], return_tensors="pt")

    generated_ids = model.generate(**batch, max_length = 40, num_beams = 1)
    res = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return res

print(translate_MT("사이즈는 어떤 걸로 하시겠어요?"))
