from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#from .models import UserInput
import json

# Create your views here.
def home(request):
	return render(request, 'index.html', {})


def encrypted(request):
	message = request.POST.get("text")
	key = int(request.POST.get("text2"))
	mode = request.POST.get("mode")
	def getTranslatedMessage(mode, message, key):
		if mode == 'encrypt':
			key = -key
		translated = ''

		for symbol in message:
			if symbol.isalpha():
				num = ord(symbol)
				num += key

				if symbol.isupper():
					if num > ord('z'):
						num -= 26
					elif num < ord('A'):
						num += 26
				elif symbol.islower():
					if num > ord('z'):
						num -= 26
					elif num <ord('a'):
						num += 26
				translated += chr(num)
			else:
				translated +=symbol
		return translated
	json_data = json.dumps(getTranslatedMessage(mode, message, key))
	return HttpResponse(json_data)

alpha_upper = [chr(x) for x in range(ord("A"), ord("Z") + 1)]
alpha_lower = [chr(x) for x in range(ord("a"), ord("z") + 1)]
ALPHA_LENGTH = 26  # Количество англ букв

def diagram(request):
	input_text = request.POST.get("input_value")
	frequency = get_frequency(input_text)
	if frequency.count(0) == len(frequency):  
			data = 0  
			return HttpResponse(json.dumps(data))

	key = get_key(input_text)
	data = json.dumps(key)
	return HttpResponse(data)

def get_frequency(input_text):
			text = input_text.lower() 
			frequency = [0 for x in range(ALPHA_LENGTH)]
			count_en_letters = 0
			for char in text:
				if char in alpha_lower:  
					count_en_letters += 1  
			for char in text:
			    	if char in alpha_lower:
			    		frequency[alpha_lower.index(char)] = text.count(char) / count_en_letters
			return frequency

def get_key(input_text):
		if len(input_text) < 20:  # Не реагировать на текст < 20
			return 0
		average_frequency = [0.0804, 0.0154, 0.0306, 0.0399, 0.1251, 0.0230, 0.0196, 0.0549, 0.0726, 0.0016, 0.0067, 0.0414, 0.0253, 0.0709, 0.0760, 0.0200, 0.0011, 0.0612, 0.0654, 0.0925, 0.0271, 0.0099, 0.0192, 0.0019, 0.0173, 0.0009]
		delta = [0 for x in range(ALPHA_LENGTH)]
		for i in range(0, ALPHA_LENGTH):
			text = encode(input_text, i)
			frequency = get_frequency(text)
			for j in range(0, ALPHA_LENGTH):
				delta[i] += (abs(average_frequency[j] - frequency[j]))
		key = ALPHA_LENGTH - delta.index(min(delta))
		return key


def encode(input_text, text2):
    output_text = ""

    def encode_formula(alphabet):
        code = (alphabet.index(char) + (text2)) % ALPHA_LENGTH
        return alphabet[code]
    for char in input_text:
        if char in alpha_upper:
            output_text += encode_formula(alpha_upper)
        elif char in alpha_lower:
            output_text += encode_formula(alpha_lower)
        else:
            output_text += char
    return output_text
    data = output_text
    return HttpResponse(json.dumps(data))



