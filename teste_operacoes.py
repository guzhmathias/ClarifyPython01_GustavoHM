import unittest
from operacoes import soma, subtra, multip, dividir

# Define uma classe de teste que herda de unittest.testcase
class TesteOperacoes(unittest.TestCase):
    def testar_soma(self):
        self.assertEqual(soma(2, 3), 5) #((Valor de teste 1, Valor de teste 2), resultado esperado)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(-2, -3), -5)

    def testar_subtra(self):
        self.assertEqual(subtra(5, 3), 2)
        self.assertEqual(subtra(-1, 1), -2)
        self.assertEqual(subtra(0, 0), 0)

    def testar_multip(self):
        self.assertEqual(multip(5, 3), 15)
        self.assertEqual(multip(-5, 4), -20)
        self.assertEqual(multip(0, 90000), 0)
        self.assertEqual(multip(-6, -30), 180)
    
    def testar_dividir(self):
        self.assertEqual(dividir(15, 3), 5)
        self.assertEqual(dividir(15, 5), 3)
        self.assertEqual(dividir(5, 1), 5)
        self.assertEqual(dividir(-5, 1), -5)
        self.assertEqual(dividir(-30, -30), 1)
        with self.assertRaises(ValueError):
            dividir(1,0)
        with self.assertRaises(ValueError):
            dividir(-80,0)


if __name__ == "__main__":
    unittest.main()

    

