#P77: Function to calculate the linear correlation
def find_corr_x_y(x,y):    
    n = len(x)
    # find the sum of the products
    prod = []
    for xi,yi in zip(x,y):
        prod.append(xi*yi)
    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x**2
    squared_sum_y = sum_y**2
    x_square = []
    for xi in x:
        x_square.append(xi**2)
    # find the sum
    x_square_sum = sum(x_square)
    y_square=[]
    for yi in y:
        y_square.append(yi**2)
    # find the sum
    y_square_sum = sum(y_square)
    
    # use formula to calculate correlation
    numerator = n*sum_prod_x_y - sum_x*sum_y
    denominator_term1 = n*x_square_sum - squared_sum_x
    denominator_term2 = n*y_square_sum - squared_sum_y
    denominator = (denominator_term1*denominator_term2)**0.5
    correlation = numerator/denominator
    
    return correlation

# Find the correlation for high school math grades and college admission scores
if __name__=='__main__':
    high_school_math = [83, 85, 84, 96, 94, 86, 87, 97, 97, 85]
    college_admission = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]
    corr = find_corr_x_y(high_school_math, college_admission)
    print('Correlation coefficient: {0}'.format(corr))
