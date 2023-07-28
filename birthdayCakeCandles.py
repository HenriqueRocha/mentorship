def birthdayCakeCandles(candles):
    max_height = max(candles)  # Find the maximum height of candles
    count = 0  # Counter to keep track of the number of tallest candles
    
    for height in candles:#loop that iterates through each height in the candles
        if height == max_height:
            count += 1
    
    return count

candles = [4, 3, 4, 1, 4]  # Example input
result = birthdayCakeCandles(candles)
print(result)  # Output: 3




