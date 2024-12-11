def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def display_top_scores(arr, n=5):
    for score in arr[-n:][::-1]:
        print(score)

def main():
    percentages = [78.5, 92.3, 85.0, 67.4, 90.1, 75.2, 88.8, 82.5, 91.0, 79.5]
    
    # Insertion Sort
    insertion_sorted = percentages.copy()
    insertion_sort(insertion_sorted)
    print("Top 5 Scores (Insertion Sort):")
    display_top_scores(insertion_sorted)
    
    # Shell Sort
    shell_sorted = percentages.copy()
    shell_sort(shell_sorted)
    print("\nTop 5 Scores (Shell Sort):")
    display_top_scores(shell_sorted)

if __name__ == "__main__":
    main()
