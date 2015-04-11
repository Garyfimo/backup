from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])
    
def g(q):
    q.put([65, None, 'asas'])

if __name__ == '__main__':
    q = Queue()
    q.put([42, None, 'hello'])
    q.put([65, None, 'asas'])
    p = Process(target=f, args=(q,))
    p = Process()
    p.start()
    print q
    print q.get()    # prints "[42, None, 'hello']"
    p.join()