def starter():
    with open('status.txt', 'w') as sts:
        sts.write('.')

    with open('trendingCount.txt', 'w') as trc:
        trc.write('-1')

    with open("status.txt", 'w') as status:
        status.write("not_book")
    
    print("Kickoff...")