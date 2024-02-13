import urllib.request
from time import time

NUM_QUERIES = 10

def test_sends():
    query_strings = ["h", "how", "why", "help"]
    for query_string in query_strings:
        av_time = 0

        for _ in range(0 , NUM_QUERIES, 1):
            start_time = time()
            _ = urllib.request.urlopen("http://127.0.0.1:5000/s?search=" + query_string).read()
            end_time = time()
            
            av_time += end_time - start_time

        av_time /= NUM_QUERIES

        av_time *= 1000

        print("Query: " + query_string + "\nAverage Time (ms): " + str(av_time))

if __name__ == '__main__':
    test_sends()
