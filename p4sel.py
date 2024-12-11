def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def display_top_scores(arr, top_n=5):
    print(f"Top {top_n} scores:")
    for score in arr[-top_n:][::-1]:
        print(score)

def main():
    n = int(input("Enter the number of students: "))
    percentages = []

    for i in range(n):
        percentage = float(input(f"Enter percentage for student {i + 1}: "))
        percentages.append(percentage)

    print("\nOriginal Percentages:", percentages)

    # Selection Sort
    sorted_selection = selection_sort(percentages.copy())
    print("\nPercentages sorted using Selection Sort:", sorted_selection)
    display_top_scores(sorted_selection)

    # Bubble Sort
    sorted_bubble = bubble_sort(percentages.copy())
    print("\nPercentages sorted using Bubble Sort:", sorted_bubble)
    display_top_scores(sorted_bubble)

if __name__ == "__main__":
    main()
