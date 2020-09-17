def nth_lowest_selling(sales, n):

    freq = {}
    for book in sales:
        if (book in freq):
            freq[book] += 1
        else:
            freq[book] = 1

    y = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1])}
    bookSales = list(y)

    print(bookSales)

    return bookSales[n-1]


x = nth_lowest_selling([1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 1], 3)
print(x)