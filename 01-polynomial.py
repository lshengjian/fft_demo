class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients    
    
    def __add__(self, other):
        # 补齐系数列表，使两个多项式的长度相等 
        delta_len=len(self.coefficients) - len(other.coefficients)       
        if delta_len>0:
            other.coefficients += [0] *delta_len #合并两个数组
        elif delta_len<0:
            self.coefficients += [0] *abs(delta_len)

        # 执行加法操作
        result = [x + y for x, y in zip(self.coefficients, other.coefficients)]
        return Polynomial(result)

    def __mul__(self, other):
        # 计算乘法结果的系数 
        lengs=[len(self.coefficients),len(other.coefficients)]

        result_degree = sum(lengs) - 1
        result = [0] * result_degree        
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result[i+j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(result)

    def __str__(self):
        # 生成多项式的字符串表示   
        coeffs=self.coefficients     
        terms = [f"{str(coeffs[i])}x^{i}" for i in range(len(coeffs)) if coeffs[i] != 0]
        rt= " + ".join(terms)
        rt=rt.replace('x^0','')
        rt=rt.replace('x^1','x')
        return rt
    
if __name__ == "__main__":
    poly1 = Polynomial([1, 0, 2])
    poly2 = Polynomial([2, 3, 1])
    res=poly1 * poly2
    s1=str(res)
    ss=s1.replace(' ','').split('+')
    ss.reverse()
    s2=' + '.join(ss)
    print(s1)
    print(s2)
    # # 创建两个多项式对象
    # poly1 = Polynomial([1, 2, 3])  # 表示 1 + 2x + 3x^2
    # poly2 = Polynomial([2, 3, 4, 5])  # 表示 2 + 3x + 4x^2 + 5x^3
    # # 测试多项式的加法和乘法
    # print(poly1 + poly2)  # 输出 3 + 5x + 7x^2 + 5x^3
    # print(poly1 * poly2)  # 输出 2 + 7x + 16x^2 + 29x^3 + 26x^4 + 15x^5