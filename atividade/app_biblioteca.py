from aluno import Aluno
from livro import Livro
from emprestimo import Emprestimo
from biblioteca import Biblioteca

# test-drive

# criar biblioteca
bibif = Biblioteca('123', 'Rua A, 123')

# cadastrar alunos
aluno1 = Aluno('123', 'Gustavo Wagner')
aluno2 = Aluno('124', 'Yan Douglas')
aluno3 = Aluno('125', 'Larissa Mendes')
aluno4 = Aluno('126', 'Bruno Oliveira')
aluno5 = Aluno('127', 'Carla Ferreira')
aluno6 = Aluno('128', 'Felipe Andrade')
aluno7 = Aluno('129', 'Natália Souza')

bibif.cadastrar_aluno(aluno1)
bibif.cadastrar_aluno(aluno2)
bibif.cadastrar_aluno(aluno3)
bibif.cadastrar_aluno(aluno4)
bibif.cadastrar_aluno(aluno5)
bibif.cadastrar_aluno(aluno6)
bibif.cadastrar_aluno(aluno7)

print("=== Alunos Cadastrados ===\n")
bibif.imprimir_alunos()

# cadastrar livros

livro1 = Livro('123', 'Aprendendo Python', '978-3-16-148410-0', ['Gustavo Wagner', 'João Silva'], '2023-10-01', 'Tecnologia')
livro2 = Livro('124', 'Aprendendo Java', '978-3-16-148410-1', ['Gustavo Wagner', 'João Silva'], '2023-10-01', 'Tecnologia')
livro3 = Livro('125', 'Aprendendo C++', '978-3-16-148410-2', ['Gustavo Wagner', 'João Silva'], '2023-10-01', 'Tecnologia')
livro4 = Livro('126', 'Aprendendo JavaScript', '978-3-16-148410-3', ['Gustavo Wagner', 'João Silva'], '2023-10-01', 'Tecnologia')
livro5 = Livro('130', '1984', '978-0-452-28423-4', ['George Orwell'], '1949-06-08', 'Ficção Científica')
livro6 = Livro('133', 'Dom Casmurro', '978-85-359-0277-7', ['Machado de Assis'], '1899-01-01', 'Romance')
livro7 = Livro('132', 'O Pequeno Príncipe', '978-3-518-22384-2', ['Antoine de Saint-Exupéry'], '1943-04-06', 'Fábula')
livro8 = Livro('134', 'Orgulho e Preconceito', '978-0-19-283355-2', ['Jane Austen'], '1813-01-28', 'Romance')
livro9 = Livro('135', 'A Divina Comédia', '978-85-325-1163-3', ['Dante Alighieri'], '1320-01-01', 'Poesia Épica')


bibif.cadastrar_livro(livro1)
bibif.cadastrar_livro(livro2)
bibif.cadastrar_livro(livro3)
bibif.cadastrar_livro(livro4)
bibif.cadastrar_livro(livro5)
bibif.cadastrar_livro(livro6)
bibif.cadastrar_livro(livro7)
bibif.cadastrar_livro(livro8)
bibif.cadastrar_livro(livro9)

print("\n=== Livros Cadastrados ===\n")
bibif.imprimir_livros()

# realizar empréstimo
emprestimo1 = Emprestimo(123, '2025-05-07', [livro1], aluno1, '2025-06-15')
emprestimo2 = Emprestimo(124, '2025-05-08', [livro2, livro6], aluno2, '2025-06-10')
emprestimo3 = Emprestimo(125, '2025-05-09', [livro5], aluno3, '2025-06-12')
emprestimo4 = Emprestimo(126, '2025-05-10', [livro9, livro7], aluno4, '2025-06-18')

bibif.realizar_emprestimo(emprestimo1)
bibif.realizar_emprestimo(emprestimo2)
bibif.realizar_emprestimo(emprestimo3)
bibif.realizar_emprestimo(emprestimo4)

print("\n=== Empréstimos Ativos ===")
bibif.imprimir_emprestimos_ativos()
