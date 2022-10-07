from collections import Counter
 
honeypot_file = open("honeypot.list", "r")
honeypot_content = honeypot_file.read()
honeypot_list = honeypot_content.split("\n")


Counter = Counter(honeypot_list)
most_seen = Counter.most_common(25)

print(most_seen)
