def starter():
    with open('status.txt', 'w') as sts:
        if(sts.write('.')):
            print('stat ready...')

    with open('status.txt', 'r') as sts:
        st = sts.read()
        print (st)

    with open('trendingCount.txt', 'w') as trc:
        if(trc.write('-1')):
            print('count initiated...')
    
    with open('trendingCount.txt', 'r') as trc:
        tr = trc.read()
        print(tr)

    with open("bookStatus.txt", 'w') as status:
        if(status.write("not_book")):
            print('books made...')
    
    with open("bookStatus.txt", 'r') as status:
        st = status.read()
        print(st)

    print("Kickoff...")