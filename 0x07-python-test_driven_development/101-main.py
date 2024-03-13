#!/usr/bin/python3
""" Doc """
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

m_a = [[1, 2, 3], [3, 4, 5]]
m_b = [[1, 2], [3, 4]]
try:
    print(lazy_matrix_mul(m_a, m_b))
except Exception as e:
    print(e)
