import time

def start_pomodoro(minutes, cycles):
    for i in range(cycles):
        seconds = minutes * 60
        print(f"Pomodoro {i + 1} dimulai! Waktu: {minutes} menit.")
        time.sleep(seconds)
        print("Waktu habis! Saatnya istirahat!")
        time.sleep(5 * 60)  # Waktu istirahat selama 5 menit
        print("Istirahat selesai! Siap untuk Pomodoro berikutnya.")

if __name__ == "__main__":
    cycles = 4  # Jumlah siklus Pomodoro
    start_pomodoro(25, cycles)
