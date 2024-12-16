pertanyaan = [
    {
        "soal": "Kota manakah yang dikenal sebagai 'Kota Pahlawan' di Indonesia?",
        "pilihan": ["A. Cianjur", "B. Jakarta", "C. Surabaya", "D. Semarang"],
        "jawaban": "C"
    },
    {
        "soal": "Kota apa yang dikenal dengan sebutan 'Kota Pelajar' di Indonesia?",
        "pilihan": ["A. Yogyakarta", "B. Bandung", "C. Jakarta", "D. Denmark"],
        "jawaban": "A" 
    },
    {
        "soal": "List adalah jenis data yang digunakan untuk menyimpan beberapa item dalam satu variabel.",
        "pilihan": ["A. Benar", "B. Salah", "C. Data tidak menyimpan item", "D. Semua benar"],
        "jawaban": "A"
    },
    {
        "soal": "Dictionary adalah koleksi yang 'berurut' yang berisi pasangan kunci-nilai.",
        "pilihan": ["A. Benar", "B. Salah", "C. Dictionary bukan bagian python", "D. Semua salah"],
        "jawaban": "B"
    },
    {
        "soal": "Ronaldo telah memenangkan penghargaan Ballon d'Or sebanyak .... kali",
        "pilihan": ["A. 3", "B. 5", "C. 1", "D. Semua salah"],
        "jawaban": "B"
    },
    {
        "soal": "Messi atau Ronaldo?",
        "pilihan": ["A. Messi", "B. Ronaldo", "C. Keduanya salah", "D. Mereka layak disebut sebagai yang terbaik"],
        "jawaban": "D"
    }
]

print(f"{"="*50}\n\tJawablah Pertanyaan Dengan Serius\n{"="*50}\n")
def run_quiz(pertanyaan):
    score = 0
    for pertanyaan in pertanyaan:
        print(pertanyaan["soal"])
        for pilihan in pertanyaan["pilihan"]:
            print(pilihan)
        jawab_player = input("Pilih salah satu (A, B, C, D)\n : ").upper()
        if jawab_player == pertanyaan["jawaban"]:
            print("Jawabanmu benar! :)\n")
            score += 1
        else:
            print("Jawabanmu salah :(, jawaban yang benar adalah",pertanyaan["jawaban"], "\n")

    nilai = score / 6 * 100

    print(f"Kamu benar menjawab soal sebanyak {score} dari 6 total pertanyaan")
    print(f"Nilai kamu adalah : {nilai}")
    if nilai >= 80 and nilai < 101:
        print("Nilai kamu sudah lebih dari cukup")
    elif nilai >=75 and nilai < 80:
        print("Nilai kamu sudah di atas rata-rata")
    elif nilai >=1 and nilai < 75:
        print("Tingkatkan lagi belajarnya")


run_quiz(pertanyaan)