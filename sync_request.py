from hackernews import HackerNews
hn = HackerNews()


def get_last_n_stories(n=10):
    max_item = hn.get_max_item()
    print(f'max_item no is {max_item}')
    return [hn.get_item(max_item-i) for i in range(n)]

last_n_stories = get_last_n_stories()
print(last_n_stories)
