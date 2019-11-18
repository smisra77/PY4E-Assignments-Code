#Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";

#Find character '0' and it's poistion
start_post = text.find('0')
print(start_post)

#Find character '5' and it's position
#Increment this position value by 1 - to include '5' in string slicing
end_post = text.find('5') + 1
print(end_post)

#Convert to float and print
print(float(text[start_post:end_post]))


