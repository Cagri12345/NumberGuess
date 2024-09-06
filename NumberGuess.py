import random  # Rastgele sayı üretimi için random modülünü import ediyoruz

# Sayı Tahmin Oyunu fonksiyonu
def number_guessing_game():
    random_number = random.randint(0, 101)  # 0 ile 100 arasında rastgele bir sayı seçiyoruz (101 dahil değil)
    guess_limit = 5  # Kullanıcının tahmin hakkını belirliyoruz, başlangıçta 5 hakkı var
    guesses = []  # Kullanıcının yaptığı tahminleri saklayacağımız bir liste oluşturuyoruz

    print("Welcome to the Number Guessing Game")  # Oyuncuyu karşılayan mesaj
    print("I've picked a number between 0 and 100. Can you guess what it is?")  # Kullanıcıya oyunun kurallarını bildiriyoruz

    # Kullanıcının 5 tahmin hakkı olduğu sürece döngü çalışacak
    while guess_limit > 0:
        try:
            guess = int(input("Enter your guess: "))  # Kullanıcıdan bir tahmin girmesini istiyoruz

        except ValueError:  # Eğer kullanıcı geçersiz bir giriş yaparsa (örneğin sayı yerine harf girerse)
            print("Please enter a valid number!")  # Hata mesajı gösteriyoruz
            continue  # Geçersiz giriş yapılırsa, bu turu atlayıp tekrar tahmin isteme aşamasına geçiyoruz

        guesses.append(guess)  # Yapılan tahmini tahminler listesine ekliyoruz

        # Eğer kullanıcı doğru tahminde bulunursa
        if guess == random_number:
            print(f"Congratulations! You guessed the number with {guess_limit} attempts remaining")  # Tebrik mesajı gösteriyoruz
            break  # Döngüden çıkıyoruz

        # Eğer tahmin edilen sayı rastgele sayıdan küçükse
        elif guess < random_number:
            print("Try a larger number.")  # Daha büyük bir sayı denemesini söylüyoruz

        # Eğer tahmin edilen sayı rastgele sayıdan büyükse
        else:
            print("Try a smaller number.")  # Daha küçük bir sayı denemesini söylüyoruz

        guess_limit -= 1  # Bir tahmin yapıldığı için haklardan birini eksiltiyoruz
        print(f"Remaining guesses: {guess_limit}")  # Kalan tahmin haklarını gösteriyoruz

    # Eğer kullanıcı tahmin hakkını doldurduysa ve doğru tahminde bulunamadıysa
    if guess_limit == 0:
        print(f"Sorry, you're out of guesses. The correct number was {random_number}.")  # Oyunu kaybettiğini ve doğru sayıyı gösteriyoruz

    print("Your guesses were:", guesses)  # Kullanıcının tüm tahminlerini gösteriyoruz

# Oyunu başlat
number_guessing_game()


