def intersection(x, y):
    return {i for i in x for j in y if i == j}

def statistics(x):
    mean = round(float(sum(x))/float(len(x)),4)
    median = round((float(x[len(x)/2 - 1]) + float(x[len(x)/2]))/2,4) if len(x) % 2 == 0 else x[len(x)//2]
    listRange = x[len(x)-1] - x[0]
    variance = (lambda l: round(sum(l)/len(x),4))(map(float,[(i - mean)**2 for i in x]))

    tscore = (12.706,4.303,3.182,2.776,2.571,2.447,2.365,2.306,2.262,2.228,
              2.201,2.179,2.160,2.145,2.131,2.120,2.110,2.101,2.093,2.086,
              2.080,2.074,2.069,2.064,2.060,2.056,2.052,2.048,2.045,2.042,
              2.040,2.037,2.035,2.032,2.030,2.028,2.026,2.024,2.023,2.021)
    CI = (lambda a, b: [round(a - b,4), round(a + b,4)])(mean, tscore[len(x)-2]*(variance/len(x))**0.5)

    stats = ['mean', 'median', 'range', 'variance', 'standard deviation', '95% CI for mean']
    values = [mean, median, listRange, variance, round(variance**0.5,4), CI]

    return [(stats[i], values [i]) for i in range(len(stats))]

