'''dada'''
def decrypt_caesar(ciphertext):
    '''daddadad'''
    # รายการคำศัพท์ภาษาอังกฤษที่พบบ่อยตามที่โจทย์กำหนด
    common_words = {
        'what',
        'when',
        'why',
        'which',
        'this',
        'there',
        'where',
        'the',
        'is',
        'am',
        'are',
        'you',
        'we',
        'they',
        'he',
        'she',
        'it',
    }

    best_decrypted = ciphertext
    max_matches = -1

    # ทดลองเลื่อนตัวอักษรทุกค่าที่เป็นไปได้ตั้งแต่ 1 ถึง 25
    for shift in range(1, 26):
        decrypted_chars = []
        for char in ciphertext:
            if 'a' <= char <= 'z':
                # ถอดรหัสตัวอักษรพิมพ์เล็ก
                new_char = chr(
                    (ord(char) - ord('a') - shift) % 26 + ord('a')
                )
                decrypted_chars.append(new_char)
            elif 'A' <= char <= 'Z':
                # ถอดรหัสตัวอักษรพิมพ์ใหญ่
                new_char = chr(
                    (ord(char) - ord('A') - shift) % 26 + ord('A')
                )
                decrypted_chars.append(new_char)
            else:
                # อักขระอื่นๆ เช่น เว้นวรรค หรือเครื่องหมายวรรคตอน
                decrypted_chars.append(char)

        decrypted_text = ''.join(decrypted_chars)

        # ทำความสะอาดคำและนับจำนวนคำที่ตรงกับ common_words โดยไม่ใช้ re
        matches = 0
        for word in decrypted_text.split():
            cleaned_word = ''.join(
                [c.lower() for c in word if ('a' <= c <= 'z' or 'A' <= c <= 'Z')]
            )
            if cleaned_word in common_words:
                matches += 1

        # เลือกค่าที่ทำให้เจอคำศัพท์พบบ่อยมากที่สุด
        if matches > max_matches:
            max_matches = matches
            best_decrypted = decrypted_text

    return best_decrypted


# สำหรับรับค่าและแสดงผลโดยตรงตามรูปแบบที่โจทย์ต้องการ
try:
    while True:
        input_data = input()
        if not input_data:
            break
        print(decrypt_caesar(input_data))
except EOFError:
    pass
