# python3
# 221RDB412 Kārlis Rūdolfs Birznieks

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    threads = [(0, i) for i in range(n)]
    for i in range(m):
        t = data[i]
        time, thread_index = threads.pop(0)
        output.append((thread_index, time))
        threads.append((time + t, thread_index))
        threads.sort()
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))
    
    # TODO: create the function
    result = parallel_processing(n, m, data)
    
    # TODO: print out the results, each pair in it's own line
    for thread_index, start_time in result:
        print(thread_index, start_time)

if __name__ == "__main__":
    main()
