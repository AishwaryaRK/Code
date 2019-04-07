import collections


def sort_hotels_by_review_words(hotels, user_words):
    hotels_search_count = {}
    for hotel_id, reviews in hotels.items():
        cnt = 0
        for review in reviews:
            review = review.strip()
            review.replace(',', '')
            review.replace('.', '')
            review.replace(':', '')
            word_freq = collections.Counter(review.split(' '))
            for word in user_words:
                if word in word_freq:
                    cnt += word_freq[word]
        hotels_search_count[hotel_id] = cnt

    return sorted(hotels, key=hotels.get, reverse=True)


user_words = input().split()                                       
m = int(input())
hotels = {}
for i in range(0, m):
    hotel_id = input()
    review = input()
    if hotel_id in hotels:
        reviews = hotels[hotel_id]
        reviews.append(review)
        hotels[hotel_id] = reviews
    else:
        hotels[hotel_id] = [review]
    sort_hotels_by_review_words(hotels, user_words)
