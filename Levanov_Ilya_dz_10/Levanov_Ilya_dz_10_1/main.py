class Matrix:

    def __init__(self, m_list):
        self.m_list = m_list

    def __add__(self, other):
        for i in range(len(self.m_list)):
            for k in range(len(other.m_list[i])):
                self.m_list[i][k] = self.m_list[i][k] + other.m_list[i][k]
        return self.m_list

    def __str__(self):
        str_matrix = ''
        for line in self.m_list:
            str_matrix = str_matrix + f'{line}\n'
        return f'{str_matrix}'


matr_1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(matr_1)

matr_2 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
print(matr_2)

matr_3 = Matrix([[8, 3, 7, 1], [3, 5, 8, 3]])
print(matr_2 + matr_3)
