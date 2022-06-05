from captcha.image import ImageCaptcha
from random import choice, uniform

def generateCaptcha():
	words = [
		"hi mom",
		"whatsapp",
		"iiHaste",
		"bro"
	]
	for i in range(round(uniform(5, 19))):
		latters = "abcdefghijklmnopqrstuvwxyz0123456789"
		w = ""
		for _ in range(round(uniform(3, 8))):
			if choice([True, False]):
				w += choice(latters.upper())
			else:
				w += choice(latters)
		words.append(w)
		w = None
		
	image = ImageCaptcha(width=300, height=100)
	text = choice(words)
	data = image.generate(text)
	image.write(text, "static/assets/iq_test.png")
	return text

