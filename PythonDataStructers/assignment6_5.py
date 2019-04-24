text = "X-DSPAM-Confidence:    0.8475";

zero = text.find('0')

number = text[zero:]

print(float(number))
