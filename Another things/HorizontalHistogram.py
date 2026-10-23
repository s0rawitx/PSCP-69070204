"""dddddd"""

text = input().strip()

counts = {}
for char in text:
    if char.isalpha():
        counts[char] = counts.get(char, 0) + 1

lowercase_chars = sorted([c for c in counts if c.islower()])
uppercase_chars = sorted([c for c in counts if c.isupper()])

sorted_chars = lowercase_chars + uppercase_chars

for char in sorted_chars:
    freq = counts[char]
    blocks = freq // 5
    remainder = freq % 5

    bar_parts = ['-----'] * blocks
    if remainder > 0:
        bar_parts.append('-' * remainder)

    bar_str = '|'.join(bar_parts)
    print(f"{char} : {bar_str}")
