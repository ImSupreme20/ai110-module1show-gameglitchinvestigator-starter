from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High" with correct direction
    result = check_guess(60, 50)
    expected = ("Too High", "❄️ Too High! 📉 Go LOWER!")
    assert result == expected

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low" with correct direction
    result = check_guess(40, 50)
    expected = ("Too Low", "❄️ Too Low! 📈 Go HIGHER!")
    assert result == expected

def test_guess_hot_high():
    # If secret is 50 and guess is 52, hint should be hot
    result = check_guess(52, 50)
    expected = ("Too High", "🔥 Too High! 📉 Go LOWER!")
    assert result == expected

def test_guess_hot_low():
    # If secret is 50 and guess is 48, hint should be hot
    result = check_guess(48, 50)
    expected = ("Too Low", "🔥 Too Low! 📈 Go HIGHER!")
    assert result == expected
