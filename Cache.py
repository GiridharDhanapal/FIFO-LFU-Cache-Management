# Giridhar Dhanapal - 201682772

cache = []      # Global Variable
requests = []   # Global Variable


def fifo():
    for each_request in requests:
        if each_request in cache:
            print('hit')
        else:
            print('miss')
            if not len(cache) < 8:
                cache.pop(0)
            cache.append(each_request)


def lfu():
    unique_requests = ()   # Set contains unique requests
    for each_request in range(len(requests)):
        unique_requests = requests[:each_request]
        cache_list = []    # Contains unique pages with frequency
        min_count_cache = []
        if requests[each_request] in cache:
            print('hit')
        else:
            print('miss')
            if not len(cache) < 8:
                for pages in cache:
                    cache_list.append(unique_requests.count(pages))
                for pages in range(len(cache)):
                    if cache_list[pages] == min(cache_list):
                        min_count_cache.append(cache[pages])
                cache.remove(min(min_count_cache))
            cache.append(requests[each_request])


choose = None


while choose != 'Q':
    requests = []
    while 1:
        user_input = int(input('Give set of requests'))
        if user_input != 0:
            requests.append(user_input)
        else:
            break
    print(requests)
    choose = input('1 for FIFO, 2 for LFU, Q for Quit : ')

    if choose == '1':
        fifo()
    elif choose == '2':
        lfu()
    print(cache)
    cache.clear()
    if choose == 'Q':
        quit()