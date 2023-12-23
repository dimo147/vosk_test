import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

question = "رشته تحصیلی من چی باید باشد؟"
answers = ["","","",""]
input_ids = tokenizer.encode(question, return_tensors='pt')

output = model.generate(input_ids, max_length=100, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)
decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)

print(decoded_output)
